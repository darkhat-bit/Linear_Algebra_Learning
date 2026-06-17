import numpy as np
import matplotlib.pyplot as plt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def scale(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    
    def magnitude(self):
        return np.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        mag = self.magnitude()
        return Vector(self.x / mag, self.y / mag)
        
    def plot(self, color='blue', label=''):
        plt.arrow(0, 0, self.x, self.y, 
                 head_width=0.2, head_length=0.2, 
                 fc=color, ec=color, label=label)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

print("=== VECTOR OPERATIONS ===")

# Create vectors
v1 = Vector(3, 2)
v2 = Vector(1, 4)

print(f"v1 = {v1}")
print(f"v2 = {v2}")

# Addition
v_sum = v1.add(v2)
print(f"\nv1 + v2 = {v_sum}")

# Scaling
v_scaled = v1.scale(2)
print(f"2 * v1 = {v_scaled}")

# Dot product
dot_product = v1.dot(v2)
print(f"v1 · v2 = {dot_product}")  # 3*1 + 2*4 = 11

# Magnitude
print(f"\n||v1|| = {v1.magnitude()}")  # sqrt(9 + 4) = sqrt(13)

# Normalize
v_normalized = v1.normalize()
print(f"v1 normalized = {v_normalized}")
print(f"Its magnitude = {v_normalized.magnitude()}")  # Should be 1.0

# Visualize
plt.figure(figsize=(8, 8))
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

v1.plot(color='blue', label='v1')
v2.plot(color='red', label='v2')
v_sum.plot(color='green', label='v1+v2')

plt.legend()
plt.title("Vector Addition")
plt.show()