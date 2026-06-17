import numpy as np

cities_names = ["Beawar", "Ajmer", "Jaipur", "Bhilwara", "Udaipur"]

cities_coord = np.array([
    [0,   0],  
    [200, 150],
    [400, 100],
    [100, 300],
    [350, 250] 
])

dist_f = np.full((5,5), np.inf)

for i in range(5):
    for j in range(5):
        if i != j:
            diff = cities_coord[i] - cities_coord[j]
            dist_f[i][j] = np.round(np.sqrt(np.sum(diff**2)))
print(dist_f)
print()
print("===== DELIVERY ROUTE OPTIMIZER =====")
print()
print("Starting City: Beawar")
print()
print("--- Distance Matrix (km) ---")
print("Cities   |   Beawar   |    Ajmer   |     Jaipur   |    Bhilwara   |  Udaipur")
for i in range(5):
    length = len(cities_names[i])
    n = 13 - length
    spacing = " "
    print(cities_names[i], end=spacing*n)
    for j in range(5):
        if j < 4:
            if dist_f[i][j] == np.inf:
                print(dist_f[i][j], end=spacing*11)
            else:
                print(dist_f[i][j], end=spacing*9)
        else:
            print(dist_f[i][j])

print()
print("--- Optimal Route ---")
current_city = 0
total_dist = 0
visited = [True, False, False, False, False]

for i in range(4):
    row = dist_f[current_city].copy()
    for v in range(5):
        if visited[v]:
            row[v] = np.inf
    next_city = np.argmin(row)
    print(f"{cities_names[current_city]}      -->   {cities_names[next_city]}      |  {dist_f[current_city][next_city]} km")
    total_dist += dist_f[current_city][next_city]
    visited[next_city] = True
    current_city = next_city

print(f"{cities_names[current_city]}      (Destination)")
print()
print(f"Total Distance: {total_dist} km")