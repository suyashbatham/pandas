import numpy as np
import pandas as pd

x1 = {'a':[1,1,1,1,1],'b':[1,1,1,1,1],'c':[1,1,1,1,1],'d':[1,1,1,1,1],'e':[1,1,1,1,1]}
x2 = {'e':[2,2,2,2,2],'f':[2,2,2,2,2],'g':[2,2,2,2,2],'h':[2,2,2,2,2],'i':[2,2,2,2,2]}
x3 = {'a':[3,3,3,3,3],'b':[3,3,3,3,3],'c':[3,3,3,3,3],'d':[3,3,3,3,3],'e':[3,3,3,3,3]}
df1 = pd.DataFrame(x1,index=[1,2,3,4,5])
df2 = pd.DataFrame(x2,index=[1,2,3,4,5])
df3 = pd.DataFrame(x3,index=[5,6,7,8,9])
print(df1)
print(df2)
print(df3)
print(pd.concat([df1,df2],axis=1))
print(pd.concat([df1,df3],axis=0))
print(pd.concat([df1,df2,df3],axis=0))
