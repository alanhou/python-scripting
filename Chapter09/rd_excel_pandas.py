import pandas as pd

excel_file = 'Sample - Superstore.xls'
df = pd.read_excel(excel_file)
print(df.head())
