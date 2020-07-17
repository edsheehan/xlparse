import numpy as np
import pandas as pd
import re

outs = np.array([])

xlsx = pd.ExcelFile('D:/Users/Ed Sheehan/Documents/Backups.xlsx')
df = pd.read_excel(xlsx, 'Sheet1')
all = np.array(df['App_ID'].dropna())
print(all)

for item in all:
    split = re.split(r'[\,\-\+](?<!APP-)', item)
    for app in split:
        print(app)
        outs = np.append(outs, app)


print(outs)
print(np.unique(outs))