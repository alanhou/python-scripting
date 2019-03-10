import pandas as panda

excel_file = 'Sample - Superstore.xls'
cols = [1, 2, 3]
df = panda.read_excel(excel_file, sheet_names='Orders', usecols=cols)

print(df.head())
