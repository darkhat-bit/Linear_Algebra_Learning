import numpy as np

P = np.array([[2, 1], 
              [1, 2]])

v_jenny = np.array([3, -1])

v_me = np.dot(P, v_jenny)
print(v_me)

P_inv = np.linalg.inv(P)
v_jenny_back = np.dot(P_inv, v_me)
print(v_jenny_back)

M_me = np.array([[0, -1], 
                 [1,  0]])

M_jenny = np.dot(np.dot(P_inv, M_me), P)
print(M_jenny)