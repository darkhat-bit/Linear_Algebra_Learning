import numpy as np
import matplotlib.pyplot as plt

# matrix a input
print("Enter your matrix A numbers by separating them by space:-")
input_string1 = list(map(int, input().split()))
a_1d = np.array(input_string1)

print("Enter your matrix A shape separating by space (Rows Cols):- ")
n, m = map(int, input().split())
a_2d = a_1d.reshape(n, m)

# matrix b input
print("\nEnter your matrix B numbers by separating them by space:-")
input_string2 = list(map(int, input().split()))
b_1d = np.array(input_string2)

print("Enter your matrix B shape separating by space (Rows Cols):- ")
q, r = map(int, input().split())
b_2d = b_1d.reshape(q, r)


# --- AUXILIARY FUNCTION TO ADD TEXT ON HEATMAPS ---
def annotate_heatmap(ax, matrix):
    """Loops through the matrix and draws numbers on top of the pixels."""
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            ax.text(j, i, f"{np.round(matrix[i, j], 1)}", 
                    ha="center", va="center", 
                    color="white" if abs(matrix[i, j]) > (matrix.max()/2) else "black",
                    fontweight='bold')

# operation menu
print('''
    Enter the Operation you want to perform:-
    1. Multiplication -->  M
    2. Transpose      -->  T
    3. Determinant    -->  D
    4. Inverse        -->  I
''')
x = input().strip().upper()

# logical operation dashboard
if x == "M":
    if m == q:
        print("\nThe multiplication of matrix A with matrix B is:-")
        result = a_2d @ b_2d
        print(result)

        # dashboard-1
        fig = plt.figure(figsize=(11, 8))
        fig.suptitle("Matrix Multiplication Dashboard", fontsize=16, fontweight='bold')

       
        ax1 = plt.subplot2grid((2, 2), (0, 0))
        im1 = ax1.imshow(a_2d, cmap='plasma')
        ax1.set_title(f"Matrix A ({n}x{m})")
        annotate_heatmap(ax1, a_2d)

        ax2 = plt.subplot2grid((2, 2), (0, 1))
        im2 = ax2.imshow(b_2d, cmap='plasma')
        ax2.set_title(f"Matrix B ({q}x{r})")
        annotate_heatmap(ax2, b_2d)

        ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
        im3 = ax3.imshow(result, cmap='viridis')
        ax3.set_title(f"Result Matrix A@B ({n}x{r})", fontweight='bold', color='darkgreen')
        annotate_heatmap(ax3, result)
        fig.colorbar(im3, ax=ax3, orientation='horizontal', pad=0.15)

        plt.tight_layout()
        plt.show()
    else:
        print(f"\n[ERROR] Cannot multiply matrices! Matrix A Columns ({m}) must match Matrix B Rows ({q}).")

elif x == "T":
    a_t, b_t = a_2d.T, b_2d.T
    print("\nThe Transpose of matrix A is:\n", a_t)
    print("\nThe Transpose of matrix B is:\n", b_t)

    # dashboard-2
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    fig.suptitle("Matrix Transpose Dashboard", fontsize=16, fontweight='bold')

    axes[0, 0].imshow(a_2d, cmap='coolwarm')
    axes[0, 0].set_title("Original Matrix A")
    annotate_heatmap(axes[0, 0], a_2d)

    axes[0, 1].imshow(b_2d, cmap='coolwarm')
    axes[0, 1].set_title("Original Matrix B")
    annotate_heatmap(axes[0, 1], b_2d)

    axes[1, 0].imshow(a_t, cmap='inferno')
    axes[1, 0].set_title("Transposed Matrix A (A.T)")
    annotate_heatmap(axes[1, 0], a_t)

    axes[1, 1].imshow(b_t, cmap='inferno')
    axes[1, 1].set_title("Transposed Matrix B (B.T)")
    annotate_heatmap(axes[1, 1], b_t)

    plt.tight_layout()
    plt.show()

elif x == "D":
    is_A_square = (n == m)
    is_B_square = (q == r)
    
    det_A = np.round(np.linalg.det(a_2d), 2) if is_A_square else "N/A (Not Square)"
    det_B = np.round(np.linalg.det(b_2d), 2) if is_B_square else "N/A (Not Square)"

    print(f"\nThe determinant of matrix A is: {det_A}")
    print(f"The determinant of matrix B is: {det_B}")

    # dashboard-3
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("Matrix Determinant Analysis", fontsize=16, fontweight='bold')

    axes[0].imshow(a_2d, cmap='magma')
    axes[0].set_title(f"Matrix A\nDeterminant = {det_A}", fontsize=12, color='red' if det_A == 0 else 'black')
    annotate_heatmap(axes[0], a_2d)

    axes[1].imshow(b_2d, cmap='magma')
    axes[1].set_title(f"Matrix B\nDeterminant = {det_B}", fontsize=12, color='red' if det_B == 0 else 'black')
    annotate_heatmap(axes[1], b_2d)

    plt.tight_layout()
    plt.show()

elif x == "I":
    is_A_invertible = (n == m and np.linalg.det(a_2d) != 0)
    is_B_invertible = (q == r and np.linalg.det(b_2d) != 0)

    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    fig.suptitle("Matrix Inverse Dashboard", fontsize=16, fontweight='bold')

    axes[0, 0].imshow(a_2d, cmap='cividis')
    axes[0, 0].set_title("Original Matrix A")
    annotate_heatmap(axes[0, 0], a_2d)

    axes[0, 1].imshow(b_2d, cmap='cividis')
    axes[0, 1].set_title("Original Matrix B")
    annotate_heatmap(axes[0, 1], b_2d)

    if is_A_invertible:
        a_inv = np.linalg.inv(a_2d)
        print("\nThe Inverse of matrix A is:\n", a_inv)
        axes[1, 0].imshow(a_inv, cmap='cubehelix')
        axes[1, 0].set_title("Inverse Matrix A^-1")
        annotate_heatmap(axes[1, 0], a_inv)
    else:
        print("\n[ERROR] Matrix A Inverse does not exist.")
        axes[1, 0].text(0.5, 0.5, "Inverse Not\nPossible", ha="center", va="center", color="red", fontsize=14, fontweight='bold')
        axes[1, 0].set_title("Matrix A (Non-Invertible)")

    if is_B_invertible:
        b_inv = np.linalg.inv(b_2d)
        print("The Inverse of matrix B is:\n", b_inv)
        axes[1, 1].imshow(b_inv, cmap='cubehelix')
        axes[1, 1].set_title("Inverse Matrix B^-1")
        annotate_heatmap(axes[1, 1], b_inv)
    else:
        print("[ERROR] Matrix B Inverse does not exist.")
        axes[1, 1].text(0.5, 0.5, "Inverse Not\nPossible", ha="center", va="center", color="red", fontsize=14, fontweight='bold')
        axes[1, 1].set_title("Matrix B (Non-Invertible)")

    plt.tight_layout()
    plt.show()

else:
    print("\nInvalid Input. Try Again!")