import numpy as np
import pandas as pd

df1 = pd.DataFrame({'key0':[1,2,3],'a':[2,3,4],'b':[5,6,7]})
df2 = pd.DataFrame({'key1':[1,2,3],'a':[2,3,4],'b':[5,6,7]})
print(df1)
print(df2)
print(pd.merge(df1,df2,how='right',on='key0'))