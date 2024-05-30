from typing import Dict

from fastapi import FastAPI, File, UploadFile, Query
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from sqlalchemy import create_engine
import csv
import pandas as pd
import numpy as np
from sqlalchemy import text

app = FastAPI()

DB_USER = "climate_app"
DB_PASSWORD = "12358"
DB_NAME = "climate_data"
DB_HOST = "localhost"
DB_PORT = 5432

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")


@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    df.to_sql('climate_data', con=engine, if_exists='append', index=False)

    return JSONResponse(content={"message": "CSV file uploaded successfully"}, status_code=201)

@app.get("/graphs")
async def get_graphs(
    parametr: str = Query(..., description="Parameter to filter by (temperature, humidity, pollution)"),
    date_from: str = Query(..., description="Start date (YYYY-MM-DD)"),
    date_to: str = Query(..., description="End date (YYYY-MM-DD)"),
    grouping: str = Query(..., description="Grouping (e.g. hourly, daily)")
):
    query = text("""
                SELECT date as timestamp, {} as value
                FROM climate_data
                WHERE date >= :date_from AND date <= :date_to
            """.format(parametr))
    params = {"date_from": date_from, "date_to": date_to}
    df = pd.read_sql_query(query, engine, params=params)



    if grouping == 'day':
        grouped_df = df
    elif grouping == 'month':
        grouped_df = df.resample('ME', on='timestamp').mean().reset_index()
        grouped_df['timestamp'] = grouped_df['timestamp'] - pd.tseries.offsets.MonthBegin(1)
    elif grouping == 'year':
        grouped_df = df.resample('YE', on='timestamp').mean().reset_index()
        grouped_df['timestamp'] = grouped_df['timestamp'] - pd.tseries.offsets.YearBegin(1)
    else:
        raise ValueError("Invalid grouping parameter")

    mean = grouped_df['value'].mean()
    median = grouped_df['value'].median()
    st_deviation = grouped_df['value'].std()

    # Calculate Z-scores
    z_scores = [(x - mean) / st_deviation for x in grouped_df['value']]

    # Identify abnormal values (e.g., 2 standard deviations away from the mean)
    abnormal_threshold = 1
    abnormal_values = [value for timestamp, value, z_score in zip(grouped_df['timestamp'], grouped_df['value'], z_scores) if abs(z_score) > abnormal_threshold]

    response = {
        "points": [{"timestamp": timestamp, "value": value} for timestamp, value in zip(grouped_df['timestamp'], grouped_df['value'])],
        "mean": mean,
        "median": median,
        "stDeviation": st_deviation,
        "abnormal": abnormal_values
    }
    return response

@app.get("/diagrams")
async def get_diagrams(
    parametr: str = Query(..., description="Parameter to filter by (temperature, humidity, pollution)"),
    date_from: str = Query(..., description="Start date (YYYY-MM-DD)"),
    date_to: str = Query(..., description="End date (YYYY-MM-DD)")
):
    allowed_columns = ["temperature", "humidity", "pollution"]
    if parametr not in allowed_columns:
        return {"error": "Invalid parameter"}

    query = text("""
                SELECT {} as value
                FROM climate_data
                WHERE date >= :date_from AND date <= :date_to
            """.format(parametr))
    params = {"date_from": date_from, "date_to": date_to}
    df = pd.read_sql_query(query, engine, params=params)

    # Round values to the nearest 0.5
    df['value'] = np.round(df['value'] * 2) / 2

    # Group and count
    df = df.groupby('value').size().reset_index(name='frequency')

    response = {
        "points": [{"x": value, "y": frequency} for value, frequency in zip(df['value'], df["frequency"])]
    }
    return response


@app.get("/heatmaps")
async def get_heatmap(
    parametr: str = Query(..., description="Parameter to filter by (temperature, humidity, pollution)"),
    lat_min: float = Query(..., description="Minimum latitude"),
    lat_max: float = Query(..., description="Maximum latitude"),
    lon_min: float = Query(..., description="Minimum longitude"),
    lon_max: float = Query(..., description="Maximum longitude")
):
    allowed_columns = ["temperature", "humidity", "pollution"]
    if parametr not in allowed_columns:
        return {"error": "Invalid parameter"}

    query = text("""
            SELECT latitude as y, longitude as x, {} as value
            FROM climate_data
            WHERE latitude >= :min_lat AND latitude <= :max_lat
            AND longitude >= :min_lon AND longitude <= :max_lon
        """.format(parametr))
    params_dict = {
        "min_lat": lat_min,
        "max_lat": lat_max,
        "min_lon": lon_min,
        "max_lon": lon_max
    }
    df = pd.read_sql_query(query, engine, params=params_dict)

    # Calculate x and y domains
    x_domain = [df["x"].min(), df["x"].max()]
    y_domain = [df["y"].min(), df["y"].max()]

    # Create response
    response = {
        "points": [{"x": x, "y": y, "value": value} for x, y, value in zip(df["x"], df["y"], df["value"])],
        "xDomain": x_domain,
        "yDomain": y_domain
    }
    return response
