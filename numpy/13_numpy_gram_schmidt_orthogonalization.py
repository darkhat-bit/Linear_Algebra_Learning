import numpy as np

V = np.array([[1.0, 1.0], 
              [0.0, 1.0]])

U = np.zeros_like(V)
print(U)

U[:, 0] = V[:, 0]
print(U)
proj_1 = (np.dot(V[:, 1], U[:, 0]) / np.dot(U[:, 0], U[:, 0])) * U[:, 0]
U[:, 1] = V[:, 1] - proj_1

U[:, 0] = U[:, 0] / np.linalg.norm(U[:, 0])
U[:, 1] = U[:, 1] / np.linalg.norm(U[:, 1])

print(U)