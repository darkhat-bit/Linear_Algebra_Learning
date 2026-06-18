import numpy as np

A = np.array([[2,1],
              [1,3]])

b = np.array([5, 10])

D = np.linalg.det(A)

A_x = A.copy()
A_x[:,0] = b
print(A_x)
D_x = np.linalg.det(A_x)

A_y = A.copy()
A_y[:, 1] = b
print(A_y)
D_y = np.linalg.det(A_y)

x = D_x / D
y = D_y / D
print(x, y)