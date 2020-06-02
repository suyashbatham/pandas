import numpy as np
import pandas as pd

x1 = {'a':[1,2,3],'b':[5,6,7]}
y1 = {'c':[3,4,5],'d':[2,3,6]}

x = pd.DataFrame(x1,index=['p1','p2','p3'])
y = pd.DataFrame(y1,index=['p4','p5','p6'])
print(x)
print(y)

# join two table
# we join the text in 4 ways left,right,outer,inner
print(x.join(y))
print(x.join(y,how="left"))
print(x.join(y,how="right"))
print(x.join(y,how="outer"))
print(x.join(y,how="inner"))