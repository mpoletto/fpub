from google.cloud import bigquery

import pandas as pd
import numpy as np
import openpyxl

client = bigquery.Client()
client.pretty_print = True

query = """
    SELECT region_code, week, rank, percent_gain, refresh_date, country_name, country_code, region_name, term, score  
    FROM `bigquery-public-data.google_trends.international_top_rising_terms` 
    WHERE country_code = 'BR' ORDER BY week 
    LIMIT 10
"""
rows = client.query_and_wait(query)  

lyst = []
lyst.append(['region_code', 'week', 'rank', 'percent_gain', 'refresh_date', 'country_name', 'country_code', 'region_name', 'term', 'score'])
for row in rows:
    lyst.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])
df = pd.DataFrame(lyst)
print(df)
df.to_excel('google-trends.xlsx', index=False)
