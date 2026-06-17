import numpy as np

# --where--
three_d = np.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])

print("--3D Array--")
print(np.where(three_d>=50, 'Yes', 'No'))
print()

print("--3D Array--")
print(np.where(three_d>=50, ['A', 'B', 'C'], ['X', 'Y', 'Z']))


# --argmax/argmin--

t3mx = np.argmax(three_d)
t3mn = np.argmin(three_d)

# flat use to convert a matrix into a 1d list so it can fetch the data according to the list by indexing
max_value = three_d.flat[t3mx]
min_value = three_d.flat[t3mn]

print(f"Max Index: {t3mx} | Max Value: {max_value}")
print(f"Min Index: {t3mn} | Min Value: {min_value}")
print()


# to fetch the value normally via matrix[row, col], It converts the flat index into a proper 2D/3D coordinate tuple.
# Convert flat index 8 into (row, col) based on the shape of three_d
coords = np.unravel_index(t3mx, three_d.shape)
print(f"Actual Grid Coordinates: {coords}") # Outputs: (2, 2)

# Fetch the value using normal indexing
max_value = three_d[coords]
print(f"Value at {coords}: {max_value}")    # Outputs: 90


# two_d = np.array([[10,20,30],
#                   [40,50,60]])

# print("--2D Array--")
# print(np.where(two_d>=50, 'Yes', 'No'))
# print()
# print("--2D Array--")
# print(np.where(two_d>=50, ['A', 'B', 'C'], ['X', 'Y', 'Z']))
# print()
# t2mx = np.argmax(two_d)
# t2mn = np.argmin(two_d)
# min2_value = two_d.flat[t2mn]
# max2_value = two_d.flat[t2mx]

# print(f"Max Index: {t2mx} | Max Value: {max2_value}")
# print(f"Min Index: {t2mn} | Min Value: {min2_value}")
# print()

