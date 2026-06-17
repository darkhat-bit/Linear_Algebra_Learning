import matplotlib.pyplot as plt
import numpy as np

movies = ['Intersteller', 'Inception', 'Dark']
scores = [8.5, 9.2, 7.8]

x_random = np.random.rand(50)
y_random = np.random.rand(50)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].bar(movies, scores, color='skyblue')
ax[0].set_title("Movie Ratings")

ax[1].scatter(x_random, y_random, color='purple', marker='o')
ax[1].set_title("Random Data Distribution")

plt.tight_layout()
plt.show()