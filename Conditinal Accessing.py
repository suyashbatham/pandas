import numpy as np
import pandas as pd

A = [1,2,3,4]
B = [5,6,7,8]
C = [9,0,1,2]
D = [3,4,5,6]
E = [7,8,9,0]
df = pd.DataFrame([A,B,C,D,E],['a','b','c','d','e'],['W','X','Y','Z'])

# print value greater than 3
print(df>3)  # print boolean value
print(df[df>3]) # print float value

# not particular column
print(df[df['Y']>3])

# particular column
print(df[df['W']>3][['W']])

# print multiple column
print(df[df['W']>3][['W','X']])

# Multiple Condition
print(df[(df['W']>0) & (df['Z']>2)])
print(df[(df['W']>0) | (df['Z']>2)])