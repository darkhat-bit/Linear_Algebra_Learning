"""
===============================================================================
🌟 THE FOUNDATIONAL AI ENGINEER'S CHEAT SHEET: NUMPY & MATPLOTLIB 🌟
===============================================================================
This single file contains all essential syntax, attributes, and core mechanics
required to build models from scratch and visualize complex data structures.
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# PART 1: NUMPY CORE (Data Structure & Linear Algebra)
# =============================================================================

print("--- 1. ARRAY CREATION & SHAPES ---")
# Creates an array with explicit data type
arr_1d = np.array([1, 2, 3, 4], dtype=np.float32)

# Attributes of an Array (Crucial for debugging matrix shapes in Deep Learning)
print("Shape of Array:", arr_1d.shape)  # Returns a tuple of dimensions
print("Data Type:", arr_1d.dtype)      # Returns memory type (float32, int64 etc)
print("Dimensions:", arr_1d.ndim)      # Number of axes (1D, 2D, 3D)

# Matrix Initializations
zeros_mat = np.zeros((3, 3))       # 3x3 matrix filled with 0.0 (Good for biases)
ones_mat = np.ones((1, 4))         # 1x4 matrix filled with 1.0
identity = np.eye(3, dtype=int)    # 3x3 Identity Matrix (1s on diagonal, 0s elsewhere)
infinite_mat = np.full((5, 5), np.inf) # Fills 5x5 matrix with Infinity (Masking paths)

print("\n--- 2. SEQUENCES & GEOMETRIC GRIDS ---")
# np.arange(start, stop, step): Generates sequences. 'stop' is exclusive.
seq = np.arange(10, 50, 5) # [10, 15, 20, 25, 30, 35, 40, 45]

# np.linspace(start, stop, num): Generates 'num' equally spaced points. 'stop' is inclusive.
space = np.linspace(0, 1, 5) # [0., 0.25, 0.5, 0.75, 1.]

# np.meshgrid(x, y): Stretches arrays to create a 2D coordinate map grid
X_grid, Y_grid = np.meshgrid(space, space)


print("\n--- 3. MATRIX MANIPULATION & MATH ---")
# Reshaping: Changes structure without changing data
mat_3x3 = np.arange(9).reshape(3, 3)

# Transpose: Flips rows into columns (Crucial for backpropagation math)
transposed = mat_3x3.T 

# Matrix Multiplication (Dot Product / Vector Transformation)
# Use '@' or 'np.dot()' for true matrix multiplication, NOT '*' (which is element-wise)
u = np.array([1, 2, 3]).reshape(3, 1)
v = np.ones((1, 3))
matrix_product = u @ v 


print("\n--- 4. ADVANCED LOGIC, FILTERING & STATISTICS ---")
Z = np.array([-1.5, 0.4, 2.3, -3.2, 4.5])

# np.where(condition, action_if_true, action_if_false): Vectorized IF-ELSE
rounded_away_from_zero = np.where(Z > 0, np.ceil(Z), np.floor(Z))

# Statistical Operations
mean_val = np.mean(mat_3x3, axis=1, keepdims=True) # Row-wise mean computation
min_idx = np.argmin(Z) # Returns the index of the minimum value

# Vectorized Operations & Functions
absolute_diff = np.abs(Z - 2.0)
square_root = np.sqrt(np.sum(Z**2))
angles = np.arctan2(1.0, 1.0) # Trigonometric inverse tangent (Quadrant-aware)


# =============================================================================
# PART 2: MATPLOTLIB EXPLICIT INTERFACE (Dashboard & Architecture)
# =============================================================================

# --- 1. System Architecture: Figure vs Axes ---
# fig: The whole window/canvas. ax: The actual plot box container.
fig, ax = plt.subplots(figsize=(8, 6))

# --- 2. Scatter Plots (Data Points & Anchors) ---
# s: Size of dots, zorder: Layer stack level (higher means on top)
ax.scatter([1, 2, 3], [4, 5, 6], color='blue', s=100, zorder=3, label='Data Nodes')

# --- 3. Text & Annotations (Labeling & Directed Vectors) ---
# ax.text: Places plain text on exact coordinates
ax.text(1 + 0.1, 4 + 0.1, "Node A", fontsize=10, fontweight='bold')

# ax.annotate: Creates highly detailed arrows from start to destination coordinates
ax.annotate(
    "", 
    xy=(2, 5),       # Arrow Tip Destination (Target)
    xytext=(1, 4),   # Arrow Base Start (Source)
    arrowprops=dict(
        arrowstyle="->",      # Defines type of head
        color="orange",       # Line color
        lw=2.5,               # Line Width (thickness)
        mutation_scale=15     # Scale size of the arrowhead triangle
    )
)

# --- 4. Custom Grid & Dashboarding Layouts ---
# Creates complex multi-size grids without restrictions of uniform rows/columns
fig_dash = plt.figure(figsize=(10, 4))
# shape=(total_rows, total_cols), loc=(start_row, start_col)
ax_main = plt.subplot2grid(shape=(1, 3), loc=(0, 0), rowspan=1, colspan=2) # Spans 2 columns
ax_side = plt.subplot2grid(shape=(1, 3), loc=(0, 2), rowspan=1, colspan=1) # Spans 1 column

# --- 5. Images & Heatmaps ---
# Imshow maps 2D data arrays directly to visual pixel color matrices
# cmap: Color mapping style ('viridis', 'coolwarm', 'plasma', 'hot')
matrix_data = np.random.rand(4, 4)
im = ax_side.imshow(matrix_data, cmap='coolwarm')
# Colorbar adds a reference scale window to decode colors back to numbers
fig_dash.colorbar(im, ax=ax_side, label='Scale Metric')

# --- 6. Aesthetic Customization ---
ax.set_title("Aesthetic Plot Title", fontsize=12, fontweight='bold')
ax.set_xlabel("X Label Axis")
ax.set_ylabel("Y Label Axis")
ax.grid(True, linestyle='--', alpha=0.6) # Dotted grid lines with 60% opacity
ax.legend() # Displays labels registered inside plots

plt.tight_layout() # Optimizes spacing so text doesn't clip boundaries
# plt.show() # Uncomment to deploy windows to monitor screen
print("\n[SUCCESS] Cheat sheet syntax completely mapped in memory!")
plt.show()