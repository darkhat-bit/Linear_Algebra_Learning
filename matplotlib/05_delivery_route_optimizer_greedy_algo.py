import matplotlib.pyplot as plt
import numpy as np

# 1. Initial Data Setup
cities_names = ["Beawar", "Ajmer", "Jaipur", "Bhilwara", "Udaipur"]

cities_coord = np.array(
    [[0, 0], 
     [200, 150], 
     [400, 100], 
     [100, 300], 
     [350, 250]]
)

# 2. Distance Matrix Calculation using NumPy
dist_f = np.full((5, 5), np.inf)

for i in range(5):
    for j in range(5):
        if i != j:
            diff = cities_coord[i] - cities_coord[j]
            dist_f[i][j] = np.round(np.sqrt(np.sum(diff**2)))

print()
print("===== DELIVERY ROUTE OPTIMIZER =====")
print()
print("Starting City: Beawar")
print()
print("--- Distance Matrix (km) ---")
print(
    "Cities   |   Beawar   |    Ajmer   |     Jaipur   |    Bhilwara   |  Udaipur"
)
for i in range(5):
    length = len(cities_names[i])
    n = 13 - length
    spacing = " "
    print(cities_names[i], end=spacing * n)
    for j in range(5):
        if j < 4:
            if dist_f[i][j] == np.inf:
                print(dist_f[i][j], end=spacing * 11)
            else:
                print(dist_f[i][j], end=spacing * 9)
        else:
            print(dist_f[i][j])

# 3. Matplotlib Canvas Setup (Before the Routing Loop)
fig, ax = plt.subplots(figsize=(8, 6))

# Plot all cities as dots
ax.scatter(cities_coord[:, 0], cities_coord[:, 1], color="blue", s=100, zorder=3)

# Highlight Beawar (Starting point) as a green dot
ax.scatter(
    cities_coord[0, 0],
    cities_coord[0, 1],
    color="green",
    s=150,
    zorder=4,
    label="Start (Beawar)",
)
ax.scatter(
    cities_coord[2, 0],
    cities_coord[2, 1],
    color="red",
    s=150,
    zorder=4,
    label="End (Jaipur)",
)

# Label names for each city
for i, name in enumerate(cities_names):
    ax.text(
        cities_coord[i, 0] + 10,
        cities_coord[i, 1] + 10,
        name,
        fontsize=10,
        fontweight="bold",
    )

print()
print("--- Optimal Route ---")
current_city = 0
total_dist = 0
visited = [True, False, False, False, False]

# 4. Greedy Loop with Dynamic Matplotlib Plotting
for i in range(4):
    row = dist_f[current_city].copy()
    for v in range(5):
        if visited[v]:
            row[v] = np.inf
    next_city = np.argmin(row)

    print(
        f"{cities_names[current_city]}      -->   {cities_names[next_city]}      |  {dist_f[current_city][next_city]} km"
    )

    # Dynamic Arrow Plotting: Coordinates are grabbed directly from NumPy array
    x_start, y_start = cities_coord[current_city]
    x_end, y_end = cities_coord[next_city]

    ax.annotate(
        "",
        xy=(x_end, y_end),
        xytext=(x_start, y_start),
        arrowprops=dict(
            arrowstyle="->", color="orange", lw=2.5, mutation_scale=15
        ),
    )

    total_dist += dist_f[current_city][next_city]
    visited[next_city] = True
    current_city = next_city

print(f"{cities_names[current_city]}      (Destination)")
print()
print(f"Total Distance: {total_dist} km")

# 5. Graph Aesthetics and Customization
ax.set_title(
    "🏆 Optimized Delivery Route Map", fontsize=14, fontweight="bold"
)
ax.set_xlabel("Distance X (km)")
ax.set_ylabel("Distance Y (km)")
ax.grid(True, linestyle="--", alpha=0.6)
ax.legend()

# 1. Ek naya figure banao
fig, ax = plt.subplots(figsize=(8, 6))

# 2. Distance Matrix ko image ki tarah dikhao
# 'imshow' NumPy array ko colors mein map kar dega
im = ax.imshow(dist_f, cmap='viridis')

# 3. Side mein color bar lagao (Scale)
plt.colorbar(im, label='Distance in km')

# 4. Axes par cities ke naam likho
ax.set_xticks(np.arange(5))
ax.set_yticks(np.arange(5))
ax.set_xticklabels(cities_names)
ax.set_yticklabels(cities_names)

ax.set_title("Distance Matrix Heatmap (Visual Insight)")
plt.show()
plt.tight_layout()
# plt.show()