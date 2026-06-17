import numpy as np

# Converting a (3,) array to (3, 1) or (1, 3)
weights = np.array([10, 20, 30]) # Shape (3,)
print(weights)
# Make it a column vector
col_vec = weights[:, np.newaxis] # Shape (3, 1)
print(col_vec)

# Make it a row vector
row_vec = weights[np.newaxis, :] # Shape (1, 3)
print(row_vec)