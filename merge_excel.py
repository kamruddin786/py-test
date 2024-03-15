import pandas as pd
import os

# directory of your excel files
directory = 'purchase'

# get all excel files
files = [f for f in os.listdir(directory) if f.endswith(".xlsx") or f.endswith(".xls")]

# create a list of dataframes
dfs = [pd.read_excel(os.path.join(directory, f)) for f in files]

# concatenate them together
result = pd.concat(dfs)

# write it out
result.to_excel("all_purchase.xlsx", index=False)