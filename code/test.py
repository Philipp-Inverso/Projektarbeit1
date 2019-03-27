import math
from functools import reduce
data = [[0,0,0,1,0,0,0,0],[0,1,1,1,1,1,1,1]]
#print(list(x for i,x in enumerate(data)))
for c in data:
    print(reduce((lambda x,y: x+y), list(math.pow(2,i)  if x == 1 else 0 for i, x in enumerate(c))))
