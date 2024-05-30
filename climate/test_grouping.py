import pandas as pd
import numpy as np

# Create some sample data
date_range = pd.date_range('2020-01-01', '2022-12-31', freq='D')
values = np.random.rand(len(date_range))
df = pd.DataFrame({'timestamp': date_range, 'value': values})

# Define the grouping function
def group_data(df, grouping):
    if grouping == 'day':
        # no grouping needed, return the original data
        grouped_df = df
    elif grouping == 'month':
        # group by month and calculate the mean value
        grouped_df = df.resample('M', on='timestamp').mean().reset_index()
        grouped_df['timestamp'] = grouped_df['timestamp'] - pd.tseries.offsets.MonthBegin(1)
    elif grouping == 'year':
        # group by year and calculate the mean value
        grouped_df = df.resample('Y', on='timestamp').mean().reset_index()
        grouped_df['timestamp'] = grouped_df['timestamp'] - pd.tseries.offsets.YearBegin(1)
    else:
        raise ValueError("Invalid grouping parameter")
    return grouped_df

# Test the grouping function with different grouping parameters
grouping_params = ['day', 'month', 'year']

for grouping in grouping_params:
    print(f"Grouping by {grouping}:")
    grouped_df = group_data(df, grouping)
    print(grouped_df.head())
    print()