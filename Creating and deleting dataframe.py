import numpy as np
import pandas as pd

A = [1,2,3,4]
B = [5,6,7,8]
C = [9,0,1,2]
D = [3,4,5,6]
E = [7,8,9,0]
df = pd.DataFrame([A,B,C,D,E],['a','b','c','d','e'],['W','X','Y','Z'])
# add column
df['P'] = df['Y'] + df['Z']
print(df)

#remove row
print(df.drop('e'))  # deletion not permanantly
print(df.drop('e',inplace=True))  # deleting permanantly

#remove column
print(df.drop('P',axis=1,inplace=True))