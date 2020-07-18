import numpy as np
import pandas as pd
import re

out = np.array([])

xlsx = pd.ExcelFile('D:/Users/Ed Sheehan/Documents/Backups.xlsx')
df = pd.read_excel(xlsx, 'Sheet1')
all = np.array(df['App_ID'].dropna())
print(all)

for item in all:
    split = re.split(r'[\,\-\+](?<!APP-)', item)
    for app in split:
        print(app)
        out = np.append(out, app)

print(out)
print(np.unique(out))

results = pd.DataFrame(np.unique(out))
results.columns = ['App_ID']
print(results)

results.to_excel('D:/Users/Ed Sheehan/Documents/Output.xlsx', index=False)