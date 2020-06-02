import pandas as pd
import numpy as np

#1.Index
x = pd.DataFrame({'a':[1,2,3,4,5,3],'b':[23,20,31,28,74,450]})
print(x)
print(x.index)

#2.Columns
print(x.columns)

#3.sum()
print(x['b'].sum())

#4.apply(fun)
def inc(x):
    x = x + 100
    return x
print(x['b'].apply(inc))

#5.sort_values()
print(x.sort_values('b'))

#6.unique()
print(x['b'].unique())

#7.nunique()
print(x['b'].nunique())

#8.value_counts()
print(x['b'].value_counts())

#9.isnull()
print(x.isnull())