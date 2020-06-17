import numpy as np
#random.uiniform will generate random float values from 1 -20
x = np.random.uniform(1,high=20, size=20)
#reshape will change the structure of array
a = x.reshape(4, 5)
# np.amax will get the max values of each row,for that we need to give axis=1
row_maxes = np.amax(a, axis=1)
#reshape(-1,1) will arrange the array in undefined row(-1) and one column(1) , and replace with zero
b = np.where(a == row_maxes.reshape(-1,1),0,a)
print("replaced highest row value by zero")
print(b)
"""j=0
#print(max_index_row)
for i in max_index_row:
    a[j][i] = 0
    j+=1
print(a)

#result = np.where(np.amax(a, axis=1),[3])
index = np.max(a, axis=1)
row_maxes = a.max(axis=1)
#np.where(a == row_maxes, 1, 0)
print(np.where(index,0,a))
print(a)"""