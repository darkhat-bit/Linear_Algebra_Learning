import matplotlib.pyplot as plt
import numpy as np

# Ek 1 x 2 grid (1 row, 2 columns) ka layout banao. 
# Pehle box mein Sine wave plot karo (Green color mein) aur 
# doosre box mein Cosine wave plot karo (Orange color mein).

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# plt.plot(a, x, "g-", linewidth=2, label='Sine Wave')
# plt.plot(a, y, color="orange", linstyle="-", linewidth=2, label="Cosine Wave")

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(x, y1, color="green")
ax[0].set_title("Sine Wave")
ax[0].set_xlabel("X")
ax[0].set_ylabel("Y")

ax[1].plot(x, y2, color="orange")
ax[1].set_title("Cosine Wave")
ax[1].set_xlabel("X")
ax[1].set_ylabel("Y")

print(x)
print(y1)
print(y2)
plt.tight_layout()
plt.show()