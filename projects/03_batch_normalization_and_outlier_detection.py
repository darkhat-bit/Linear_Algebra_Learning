# Batch Normalization Layer & Outlier Detection

import numpy as np

features = np.array([[ 10.0,  200.0, -0.5,  30.0],
                     [ 12.0,  180.0,  0.2,  32.0],
                     [ 25.0,  210.0,  0.1,  28.0],
                     [  9.0,  190.0, -2.3,  31.0],
                     [ 11.0, 1000.0,  0.0,  29.0]], dtype=np.float64) 

# TASK 1:
# Standardize the Features (Column-wise Normalized): * Calculate the mean and 
# standard deviation (std) of each feature column individually

features_mean = np.mean(features, axis=0)
features_std = np.std(features, axis=0)

mean_sample = np.subtract(features, features_mean)
norm = np.divide(mean_sample, features_std)

print(norm)

# Task 2: Write your boolean condition and use np.nonzero() here
outliers_mask = (norm > 1.5) | (norm < -1.5)
rows, cols = np.nonzero(outliers_mask)

print("Row indices:", rows)
print("Col indices:", cols)