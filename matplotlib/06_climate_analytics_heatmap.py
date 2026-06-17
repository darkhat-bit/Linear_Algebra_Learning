import matplotlib.pyplot as plt
import numpy as np

cities = ["Delhi", "Mumbai", "Shimla", "Chennai"]
months = ["Jan", "Apr", "Jul", "Oct"]

temp_matrix = np.array([
    [14, 38, 32, 25],  # Delhi
    [24, 32, 28, 29],  # Mumbai
    [ 5, 18, 22, 12],  # Shimla
    [26, 35, 31, 28]   # Chennai
#   Jan Apr Jul Oct
])

fig, ax = plt.subplots(figsize=(4,5))

im = ax.imshow(temp_matrix, cmap='coolwarm')
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(months, rotation=45)
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(cities, rotation=45)
fig.colorbar(im, ax=ax, label="Temperature (°C)")

ax.set_title("☀️ Climate Analytics: City vs Month Heatmap ❄️", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
