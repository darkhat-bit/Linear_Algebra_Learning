import numpy as np

# dot product and duality results
v = np.array([1,2,3])
w = np.array([4,5,6])

dot_prod = np.dot(v,w)
print(dot_prod)

projection_matrix = np.array([[4, 5, 6]])
v_column = np.array([[1], 
                     [2], 
                     [3]])

duality_result = np.dot(projection_matrix, v_column)
print(duality_result)

# cross product results
v_3d = np.array([1, 0, 0])
w_3d = np.array([0, 1, 0])

cross_product = np.cross(v_3d, w_3d)
print(cross_product)
