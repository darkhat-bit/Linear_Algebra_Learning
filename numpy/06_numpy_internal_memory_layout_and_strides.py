import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)

print("Shape:", arr.shape)       # (2, 3)
print("Dtype:", arr.dtype)       # int32
print("Itemsize:", arr.itemsize) # 4 bytes
print("Nbytes:", arr.nbytes)     # 2 * 3 * 4 = 24 bytes
print("Strides:", arr.strides)   # (12, 4) 
# Explanation of Strides (12, 4): 
# To move to the next row, skip 12 bytes (3 elements * 4 bytes).
# To move to the next column, skip 4 bytes (1 element).