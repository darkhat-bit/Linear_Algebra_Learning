import numpy as np

raw_data = np.array([[ 2.0, -1.0,  3.0],
                     [-4.0,  5.0,  0.0],
                     [ 1.0,  1.5, -2.0],
                     [ 3.0, -9.0,  4.0]], dtype=np.float64)

w = np.array([0.5, 1.5, 2.0], dtype=np.float64)

# Task 1: The Filter (ReLU)
raw_data[raw_data<0] = 0

# Task 2: Column-wise Max-Absolute Scaling
col_max = np.max(raw_data, axis=0)
scaled_data = raw_data / col_max

# Task 3: Weight Transformation
output = scaled_data @ w

print("Cleaned & Scaled Data:\n", scaled_data)
print("\nFinal Model Output:\n", output)