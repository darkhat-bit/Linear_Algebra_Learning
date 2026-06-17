import numpy as np
import matplotlib.pyplot as plt

# 1. Core Mathematical Modeling (Pure NumPy)
X = np.random.randn(3, 4)
W = np.random.randn(4, 5)

Z = X @ W # Space Transformation
A = np.where(Z > 0, Z, 0) # ReLU Activation Filter

# 2. Advanced Dashboard Design (Matplotlib)
fig = plt.figure(figsize=(12, 8))

# --- Box 1: Input Matrix ---
ax1 = plt.subplot2grid(shape=(2, 3), loc=(0, 0), rowspan=1, colspan=1)
im1 = ax1.imshow(X, cmap='plasma')
fig.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04) # Clean scale added
ax1.set_title("Input Vectors (X)\nShape: 3x4")

# --- Box 2: Weights Matrix ---
ax2 = plt.subplot2grid(shape=(2, 3), loc=(0, 1), rowspan=1, colspan=1)
im2 = ax2.imshow(W, cmap='plasma')
fig.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04) # Clean scale added
ax2.set_title("Weights Matrix (W)\nShape: 4x5")

# --- Box 3: Linear Product Matrix ---
ax3 = plt.subplot2grid(shape=(2, 3), loc=(0, 2), rowspan=1, colspan=1)
im3 = ax3.imshow(Z, cmap='plasma')
fig.colorbar(im3, ax=ax3, fraction=0.046, pad=0.04) # Clean scale added
ax3.set_title("Linear Transformation (Z = X @ W)\nShape: 3x5")

# --- Box 4: Final Activated Output (Full Bottom Span) ---
ax4 = plt.subplot2grid(shape=(2, 3), loc=(1, 0), rowspan=1, colspan=3)
im4 = ax4.imshow(A, cmap='viridis') # Using beautiful viridis color scale
# fraction aur pad lagane se colorbar box ko squash nahi karega
fig.colorbar(im4, ax=ax4, fraction=0.02, pad=0.02, label='Activation Intensity')
ax4.set_title("🔥 Final Layer Output (After ReLU Activation)\nShape: 3x5", fontsize=12, fontweight='bold')

# Automatically clean overlaps
plt.tight_layout()
plt.show()