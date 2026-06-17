import numpy as np

# ============================================
# Q1: Input matrix and convert to NumPy array
# ============================================
n, m = map(int, input().split())
matrix_list = [list(map(int, input().split())) for _ in range(n)]
array = np.array(matrix_list)
print(array)


# ============================================
# Q2: Create array from 10 to 50 and reverse
# ============================================
a = np.arange(10, 50, dtype=int)
print(a[::-1])


# ============================================
# Q3: Reshape 1D to 2D (3x3)
# ============================================
a = np.arange(9, dtype=int)
b = a.reshape(3, 3)
print(b)


# ============================================
# Q4: Find non-zero elements
# ============================================
Z = np.array([1, 2, 0, 0, 4, 0])
print(np.nonzero(Z))


# ============================================
# Q5: Replace even numbers with 0
# ============================================
a = np.arange(1, 10).reshape(3, 3)
b = np.where(a % 2 == 0, 0, a)
print(b)


# ============================================
# Q6: Matrix multiplication (broadcasting)
# ============================================
u = np.array([1, 2, 3])
x = u.reshape(3, 1)
a = np.ones((1, 4), dtype=int)
new_matrix = x @ a
print(new_matrix)


# ============================================
# Q7: Subtract row mean from each row
# ============================================
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])
row_mean = np.mean(matrix, axis=1, keepdims=True)
result = matrix - row_mean
print(result)


# ============================================
# Q8: Find index of element closest to target
# ============================================
Z = np.array([10, 22, 38, 47, 55])
target = 30
x = np.abs(Z - target)
print(np.argmin(x))


# ============================================
# Q9: Find value closest to target (detailed)
# ============================================
Z = np.array([10, 22, 38, 47, 55])
target = 30
x = np.abs(Z - target)
y = np.min(x)
mask = (x == y)
index = np.nonzero(mask)[0]
print(Z[index])


# ============================================
# Q10: Top 3 movies by score
# ============================================
scores = np.array([0.15, 0.85, 0.34, 0.92, 0.55])
sorted_index = np.argsort(scores)
reverse_index = sorted_index[::-1]
print("Top 3 Movies:")
print(scores[reverse_index[0:3]])


# ============================================
# Q11: Stack arrays (IDs and Age)
# ============================================
ids = np.array([101, 102, 103])
age = np.array([25, 30, 22])
stacked_array = np.stack((ids, age), axis=1)
print(stacked_array)


# ============================================
# Q12: Identity matrix with values replaced
# ============================================
identity_matrix = np.eye(3, dtype=int)
identity_matrix[identity_matrix == 1] = 5
print(identity_matrix)


# ============================================
# Q13: Random 3D arrays
# ============================================
a = np.arange(27).reshape(3, 3, 3)
b = np.random.rand(27).reshape(3, 3, 3)
c = np.random.rand(3, 3, 3)
print(a)


# ============================================
# Q14: Min and max of random array
# ============================================
a = np.random.rand(10, 10)
print(a.min())
print(a.max())


# ============================================
# Q15: Create ones matrix with center zeros
# ============================================
a = np.ones((5, 5), dtype=int)
a[1:4, 1:4] = 0
print(a)


# ============================================
# Q16: Pad matrix with zeros
# ============================================
a = np.ones((3, 3), dtype=int)
padded = np.pad(a, pad_width=((1, 1), (1, 1)), mode='constant', constant_values=0)
print(padded)


# ============================================
# Q17: Diagonal matrix with offset
# ============================================
a = np.diag((1, 2, 3, 4), k=-1)
print(a)


# ============================================
# Q18: Checkerboard pattern (8x8)
# ============================================
a = np.zeros((8, 8), dtype=int)
a[::2, 1::2] = 1
a[1::2, ::2] = 1
print(a)


# ============================================
# Q19: Checkerboard using indices
# ============================================
a = np.zeros((8, 8), dtype=int)
x, y = np.indices((8, 8))
a[(x + y) % 2 == 1] = 1
print(a)


# ============================================
# Q20: Matrix multiplication (5x3 @ 3x2)
# ============================================
a = np.random.randn(5, 3).astype(np.float32)
b = np.random.randn(3, 2).astype(np.float32)
result = np.dot(a, b)
print(result)


# ============================================
# Q21: In-place operations
# ============================================
A = np.array([1.0, 2.0, 3.0])
B = np.array([4.0, 5.0, 6.0])
np.add(B, A, out=B)
np.multiply(B, -A/2, out=A)
print(A)
print(B)


# ============================================
# Q22: Ceil for positive, floor for negative
# ============================================
Z = np.array([-1.5, 0.4, 1.6, -2.3, 3.5])
a = np.where(Z > 0, np.ceil(Z), np.floor(Z))
print(a)


# ============================================
# Q23: Find intersection of two arrays
# ============================================
Z1 = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
Z2 = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print(np.intersect1d(Z1, Z2))


# ============================================
# Q24: Date range (July 2026)
# ============================================
date_series = np.arange('2026-07-01', '2026-08-01', dtype='datetime64[D]')
print(date_series)

day_numbers = date_series.astype(int)
even_dates = date_series[day_numbers % 2 == 0]
odd_dates = date_series[day_numbers % 2 != 0]
print(even_dates)
print(odd_dates)


# ============================================
# Q25: Convert Cartesian to Polar coordinates
# ============================================
Z = np.random.random((10, 2))
X, Y = Z[:, 0], Z[:, 1]
R = np.sqrt(X**2 + Y**2)
O = np.arctan2(Y, X)
print(R)
print(O)


# ============================================
# Q26: Create grid (linspace + meshgrid)
# ============================================
a = np.linspace(0, 1, 5)
X, Y = np.meshgrid(a, a)
print("X Grid:\n", X)
print("\nY Grid:\n", Y)


# ============================================
# Q27: Digitize - bin elements
# ============================================
X = np.array([0.5, 1.3, 2.7, 1.1, 0.8, 3.2])
bins = np.array([0, 1, 2, 3, 4])
bins_indices = np.digitize(X, bins)
print(bins_indices)