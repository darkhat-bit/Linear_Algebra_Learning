# Batch Bounding-Box Cropper & Flattener
import numpy as np

# Represent the Image:
image = np.arange(100).reshape(10, 10)
print("Original Image Matrix: ")
print(image)
print("Crop Box's:")
crop1 = image[1:4, 2:5]
crop2 = image[5:8, 0:3]
crop3 = image[6:9, 6:9]
print(crop1)
print(crop2)
print(crop3)

print("Flatten Images:")
fcrop1 = crop1.flatten()
fcrop2 = crop2.flatten()
fcrop3 = crop3.flatten()
print(fcrop1)
print(fcrop2)
print(fcrop3)

print("Stacked the matrices:")
stacked = np.stack((fcrop1, fcrop2, fcrop3), axis=0)
print(stacked)
