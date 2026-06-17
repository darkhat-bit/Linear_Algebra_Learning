import numpy as np

data = np.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])
#Basix Slicing
print(data[:2, 0:2]) # [[10 20] [40 50]]
print()
#Fancy Indexing
print(data[[2,0,1]]) # [[70 80 90] [10 20 30] [40 50 60]] (fetching multiple element at once)
print(data[[2,0,1][2]]) # [40 50 60] (fetching from newly fetched element)
print(data[1][2]) # 60 (fetching one element at once)
print()
#Boolean Indexing
print(data[data>=50]) # [50 60 70 80 90]