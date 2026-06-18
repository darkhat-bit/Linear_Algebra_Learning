import numpy as np

A = np.array([[3, 1], 
              [0, 2]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print(eigenvalues)
print(eigenvectors)