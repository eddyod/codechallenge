"""
dosing.py file to generate:
    1.  csv file of filtered results
    2. pie chart that renders in a browser

Libraries used: 
    1. pandas
    2. pytest
    3. plotly
Created on Nov 16, 2019
@author: Edward O'Donnell eodonnell@ucsd.edu
"""

import pandas as pd

file1 = './data/t2_ec_20190619.csv'
file2 = './data/t2_registry_20190619.csv'

df_ec = pd.read_csv(file1)
df_registry = pd.read_csv(file2)
print(df_ec.head())
print("\n\n")
print(df_registry.head())
