import numpy as np

a=np.array([
    [1,2,3],
    [4,5,6]
])

b=np.array([
    [10,20,30],
    [40,50,60]
])
# Addition

for i in range(0,len(a)):
    for j in range(0, a[i].size):
        result= (a[i][j] + b[i][j])
        print(result, end="  ")
    print()