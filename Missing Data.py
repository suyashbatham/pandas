import numpy as np
import pandas as pd

d = {'a':[1,2,3,4,5],'b':[6,7,8,9,np.nan],'c':[0,1,2,np.nan,np.nan],'d':[3,4,np.nan,np.nan,np.nan],'e':[5,np.nan,np.nan,np.nan,np.nan]}
df = pd.DataFrame(d)
print(df)
print(df.dropna(axis=0))    # axis = 0 for rows and 1 for columns

print(df.dropna(thresh=3)) # print column at least 3 value

print(df.fillna(1))  # all the nan are replaced by 1.0
print(df['b'].fillna(value=1))
print(df['b'].fillna(value = df['b'].mean())) # mean of all the 4 value except nan


