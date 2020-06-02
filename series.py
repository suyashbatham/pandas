import numpy as np
import pandas as pd
x = ['a','b','c','d','e']
x2 = ['a','b','c','d','e']   # if value is different than there will be no error link change e to f and value will change int to float
y = [1,2,3,4,5]
z = {1:'a',2:'b',3:'c',4:'d',5:'e'}
print(pd.Series(x))   # print(pd.Series(z))
print(pd.Series(data=x,index=y))  # print(pd.Series(x,y))
a = pd.Series(y,x)
b = pd.Series(y,x2)
print(a+b)
print(a['c'])  # 3
print(a['c':]) # 3 4 5
print(a[:'e'])