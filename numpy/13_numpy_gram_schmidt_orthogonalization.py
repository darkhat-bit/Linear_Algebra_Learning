import numpy as np

V = np.array([[1.0, 1.0], 
              [0.0, 1.0]])

U = np.zeros_like(V)

U[:, 0] = V[:, 0]
proj_1 = (np.dot(V[:, 1], U[:, 0]) / np.dot(U[:, 0], U[:, 0])) * U[:, 0]
U[:, 1] = V[:, 1] - proj_1
U[:, 0] = U[:, 0] / np.linalg.norm(U[:, 0])
U[:, 1] = U[:, 1] / np.linalg.norm(U[:, 1])

print(U)



# print("U 1:",U)
# print("U 2:",U)
# print("proj1:",proj_1)
# print("U 3:",U)