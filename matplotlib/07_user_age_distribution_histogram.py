import numpy as np
import matplotlib.pyplot as plt

# 1. NumPy se 1000 logon ka random age data generate karo (Mean=25, StdDev=5)
np.random.seed(42) # Taaki har baar same random numbers aayein
user_ages = np.random.normal(loc=25, scale=5, size=1000)

# 2. Canvas ready karo
fig, ax = plt.subplots(figsize=(8, 5))

# 3. Histogram plot karo
# Hint: ax.hist(data_variable, bins=number, color='rang', edgecolor='rang')
# Aap color ko 'lightgreen' aur edgecolor ko 'black' rakh sakte ho
ax.hist(user_ages, bins=20, color='lightgreen', edgecolor='black')

# 4. Graph ko label karo
ax.set_title("👥 Website User Age Distribution", fontsize=14, fontweight='bold')
ax.set_xlabel("Age Groups (Years)")
ax.set_ylabel("Number Of Peoples")


plt.tight_layout()
plt.show()