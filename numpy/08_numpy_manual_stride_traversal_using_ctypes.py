import numpy as np
import ctypes
a = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]], dtype=np.int64)

base_address = a.ctypes.data
row_s, col_s = a.strides
rows, cols = a.shape
print(a.strides)
print(u"➔ Starting Manual Stride Traversal:")

for r in range(rows):
    for c in range(cols):
        byte_offset = (r*row_s)+(c*col_s)
        target_address = base_address + byte_offset
        value = ctypes.c_int64.from_address(target_address).value
        print(f"Pos ({r},{c}) | Offset: {byte_offset} bytes | Value: {value}")

