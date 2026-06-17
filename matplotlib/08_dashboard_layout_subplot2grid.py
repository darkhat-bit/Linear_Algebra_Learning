import matplotlib.pyplot as plt
import numpy as np

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Fake Data Generation ---
time = np.linspace(0, 10, 100)
sales = np.sin(time) + 2

ages = np.random.normal(25, 5, 500)

ad_spend = np.random.rand(50) * 100
revenue = ad_spend * 1.5 + np.random.randn(50) * 10

# --- 2. Canvas & Grid Setup ---
fig = plt.figure(figsize=(10, 8))

# Main Big Top Plot
ax_main = plt.subplot2grid(shape=(3, 3), loc=(0, 0), rowspan=2, colspan=3)
ax_main.plot(time, sales, color='blue', lw=2)
ax_main.set_title("📈 Main Trend: Annual Sales Over Time")

# Bottom Left Small Plot (Histogram)
ax_hist = plt.subplot2grid(shape=(3, 3), loc=(2, 0), rowspan=1, colspan=1)
ax_hist.hist(ages, bins=15, color='lightgreen', edgecolor='black')
ax_hist.set_title("👥 Customer Age")

# Bottom Right Medium Plot (Scatter)
# 🔥 TASK FOR YOU: Isko loc=(2, 1) par set karo aur 2 columns ka space do (colspan=2)
# Hint: ax_scatter = plt.subplot2grid(shape=(3, 3), loc=(row, col), rowspan=1, colspan=2)
ax_scatter = plt.subplot2grid(shape=(3, 3), loc=(2, 1), rowspan=1, colspan=2)
ax_scatter.scatter(ad_spend, revenue, color='purple', alpha=0.7)
ax_scatter.set_title("💰 Ad Spend vs Revenue")

# --- 3. Clean up and Show ---
plt.tight_layout()
plt.show()