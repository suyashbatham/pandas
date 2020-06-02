import numpy as np
import pandas as pd

A = [1,2,3,4]
B = [5,6,7,8]
C = [9,0,1,2]
D = [3,4,5,6]
E = [7,8,9,0]
df = pd.DataFrame([A,B,C,D,E],['a','b','c','d','e'],['W','X','Y','Z'])
# print(df['Y'])  # access column
# print(df.loc['a'])  # access row
# print(df.iloc[1]) # value of the particular row index
print(df.loc['d','Y']) # for accessing the particular value
