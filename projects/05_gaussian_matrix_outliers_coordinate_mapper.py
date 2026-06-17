import numpy as np

A = np.random.randn(5, 5)
print("--- Original 5x5 Matrix ---")
print(A)

outlier_mask = (A > 1.0) | (A < -1.0)
rows, cols = np.nonzero(outlier_mask)

print("\n--- Outliers Ke Exact Coordinates ---")
print("Row indices:", rows)
print("Col indices:", cols)

print("\n--- Detected Outlier Values ---")
for r, c in zip(rows, cols):
    print(f"Position ({r}, {c}) par value hai: {A[r, c]:.4f}")