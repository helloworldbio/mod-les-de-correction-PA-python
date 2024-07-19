#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import requests
import os

# Set URL - Update with your API endpoint and parameters
url = 'https://aqs.epa.gov/data/api/sampleData/bySite'
params = {
    'email': 'tjarda.roberts@lmd.ipsl.fr',
    'key': 'rubycat34',
    'param': '88502', #88502=bonne donnée
    'bdate': '20220101',
    'edate': '20221231',
    'state': '02',
    'county': '090',
    'site': '0034'
}

# Fetch JSON data from API
json_data = requests.get(url, params=params).json()

# Normalize JSON data into a DataFrame
df = pd.json_normalize(json_data['Data'])

# Convert date and time columns to datetime
df['datetimegmt'] = pd.to_datetime(df['date_gmt'] + ' ' + df['time_gmt'])

# Select columns for output CSV and rename 'date_local' to 'time_stamp'
output_df = df[['datetimegmt', 'sample_measurement']].copy()
output_df.columns = ['time_stamp', 'PMval']  # Rename 'datetimegmt' to 'time_stamp'

# Set directory to save CSV
output_directory = '/Users/saraguinane/Documents/administratif/stage recherche'

# Save DataFrame to CSV with updated column name and precise datetime format
output_df.to_csv(os.path.join(output_directory, 'datetime_PMval_2022_ref_br.csv'), index=False, date_format='%Y-%m-%d %H:%M:%S')


