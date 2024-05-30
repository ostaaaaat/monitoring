import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline
from datetime import datetime, timedelta

# Define the points
points = [(48.7139, 44.5167), (48.7639, 44.5433), (48.6842, 44.4639), (48.7653, 44.5333), (48.7264, 44.5033)]

# Define the period (start and end dates)
start_date = '2022-01-01'
end_date = '2024-12-31'

# Generate dates
dates = pd.date_range(start_date, end_date)

# Create a DataFrame to store the data
df = pd.DataFrame(columns=['date', 'temperature', 'humidity', 'pollution', 'latitude', 'longitude'])

# Define the seasonal components
phase_shift = -90  # shift the temperature pattern by 90 days (approximately 3 months)
seasonal_temp = np.sin(np.linspace(0, 2 * np.pi, 366) + phase_shift * np.pi / 180) * 10 + 10
seasonal_humidity = np.sin(np.linspace(0, 2 * np.pi, 366)) * 20 + 60

# Create a cubic spline interpolation object for temperature and humidity
cs_temp = CubicSpline(np.arange(1, 367), seasonal_temp)
cs_humidity = CubicSpline(np.arange(1, 367), seasonal_humidity)

# Define the noise parameters
temp_noise_std = 3.0
humidity_noise_std = 5.0

# Iterate over the dates and points
for date in dates:
    for point in points:
        # Calculate the day of the year (1-365)
        day_of_year = (date - datetime(date.year, 1, 1)).days + 1

        # Evaluate the seasonal components using the cubic spline interpolation
        temp = cs_temp(day_of_year)
        humidity = cs_humidity(day_of_year)

        # Add noise to the temperature and humidity values
        temp += np.random.normal(0, temp_noise_std)
        humidity += np.random.normal(0, humidity_noise_std)

        # Generate pollution value in ppm
        pollution = np.random.uniform(10, 50)

        # Create a new row
        row = pd.DataFrame({'date': [date], 'temperature': [temp], 'humidity': [humidity], 'pollution': [pollution], 'latitude': [point[0]], 'longitude': [point[1]]})

        # Append the row to the DataFrame
        df = pd.concat([df, row], ignore_index=True)

# Save the data to a CSV file
df.to_csv('data.csv', index=False)