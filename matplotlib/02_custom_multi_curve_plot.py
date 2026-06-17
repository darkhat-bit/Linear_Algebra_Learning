import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)


plt.plot(x, y1, "r--", linewidth=2, label="Sine Wave")
plt.plot(x, y2, color="blue", linestyle="-.", linewidth=2, label="Cosine Wave")
plt.plot(x, y1, 'g-o')

plt.xlabel("X Axis (Time)")
plt.ylabel("Y Axis (Amplitude)")
plt.title("My Custom Waveform Plot")

plt.legend()

print(x)
print(y1)
print(y2)
plt.show()