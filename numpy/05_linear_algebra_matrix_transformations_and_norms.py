import numpy as np

# A mock dataset matrix (e.g., 3 samples, 3 features)
A = np.array([[2, 1, 1],
              [1, 3, 2],
              [1, 0, 4]], dtype=np.float64)

# 1. Standard Matrix Multiplication (@ operator)
vector = np.array([1, 2, 3], dtype=np.float64)
a = np.matmul(A, vector)
transformed = A @ vector

# 2. Matrix Inverse and Determinant
A_inv = np.linalg.inv(A)
determinant = np.linalg.det(A)

# 3. L2 Norm (Euclidean Distance of the matrix)
matrix_norm = np.linalg.norm(A)

# 4. Singular Value Decomposition (SVD)
# U: Left singular vectors, S: Singular values (1D array), Vt: Right singular vectors
U, S, Vt = np.linalg.svd(A)

print("--- Matrix Properties ---")
print(f"Determinant: {determinant:.4f}")
print(f"L2 Norm: {matrix_norm:.4f}\n")

print("--- SVD Factorization Components ---")
print("U Matrix (Rotation):\n", U)
print("\nSingular Values (S - Scale factors):\n", S)
print("\nVt Matrix (Rotation):\n", Vt)
# print(transformed)
# print(a)