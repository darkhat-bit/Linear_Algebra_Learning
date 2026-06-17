import numpy as np

dataset = np.array([[1.5, -2.3,  0.0],
                    [-0.5, 4.2, -1.1],
                    [ 3.0, -0.1,  2.2]])

# Using Boolean Masking (Modifies array in-place)
clean_mask = dataset.copy()
clean_mask[clean_mask < 0] = 0
print("Method 1 (Masking):\n", clean_mask)

# Using np.where (Creates a clean, new array copy)
clean_where = np.where(dataset < 0, 0, dataset)
print("\nMethod 2 (np.where):\n", clean_where)

# The High-Performance ML Way (np.maximum)
# This compares element-wise against 0. Fast, vectorised, and clean.
clean_max = np.maximum(0, dataset)
print("\nMethod 3 (np.maximum / ReLU):\n", clean_max)