import numpy as np


# PRACTICE 1
# imagine we have a matrix[[1,0],[0,1]] so the size of / det of a is 1
# now we will check if we multiply the matrix with scalar how much times the det / size changes
A = np.array([[2, 0],
              [0, 2]])

# Calculate determinant using NumPy syntax
det_A = np.linalg.det(A)
print(f"Determinant of A: {det_A:.1f}")  # Outputs: 4.0


# PRACTICE 2
# if the points or vector is on same line then it will be not give a new vector
# hence it is linearly independent
B = np.array([[1,2],
              [2,4]])
det_B = np.linalg.det(B)
print(f"Determinant of B: {det_B:.1f}") 

# PRACTICE 3
# SVD

# 1. Define Matrix C
C = np.array([[3.0, 0.0],
              [0.0, -2.0]])
print(C)

# 2. Compute SVD
U, S, Vt = np.linalg.svd(C)

print("U (Left Singular Vectors):\n", U)
print("\nS (Singular Values 1D Array):", S) # NumPy returns diagonal as 1D array to save space
print("\nVt (Right Singular Vectors Transpose):\n", Vt)

# 3. Reconstruct back to A
# S ko 1D se 2D diagonal matrix banaya
S_matrix = np.diag(S) 
A_reconstructed = U @ S_matrix @ Vt

print("\nReconstructed Matrix A:\n", A_reconstructed)
