import numpy as np
import pandas as pd

p ={'item':['apple','apple','orange','orange','annas','annas'],'days':['mon','tues','wed','thres','fri','sat'],'sales':[100,80,200,100,5,10]}
df = pd.DataFrame(p)
print(df)

x = df.groupby('item')
print(x.mean())
print(x.sum())
print(x.std())
print(x.count())  # print days and sales
print(x.max())
print(x.min())
print(x.describe())    # print result in vertical
print(x.describe().transpose())  # print result in horizontal