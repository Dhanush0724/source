import numpy as np
import random

# Define the number of cities and ants
num_cities = 5
num_ants = 10

# Create a distance matrix representing the distances between cities
# You can replace this with your own city distances
distance_matrix = np.array([[0, 29, 20, 21, 16],
                            [29, 0, 15, 18, 12],
                            [20, 15, 0, 28, 4],
                            [21, 18, 28, 0, 31],
                            [16, 12, 4, 31, 0]])

# Initialize pheromone levels on paths
pheromone_matrix = np.ones((num_cities, num_cities)) #create array of spaces filled with ones as ants explore value will be updated

# Define parameters for the ACO algorithm
alpha = 1.0  # Pheromone influence decision making process
beta = 2.0   # Distance influence distance b/w cities
evaporation_rate = 0.5 #evaporate overtime
Q = 100       # Pheromone deposit amount

# Main ACO loop
num_iterations = 100
for iteration in range(num_iterations):
    ant_paths = []

    # Generate solutions for each ant
    for ant in range(num_ants):
        current_city = random.randint(0, num_cities - 1)
        unvisited_cities = set(range(num_cities))
        unvisited_cities.remove(current_city)
        path = [current_city]

        while unvisited_cities:
            probabilities = []

            # Calculate the probabilities for the next city
            for city in unvisited_cities:
                pheromone = pheromone_matrix[current_city][city]
                distance = distance_matrix[current_city][city]
                probability = (pheromone * alpha) * ((1.0 / distance) * beta)
                probabilities.append((city, probability))

            # Choose the next city based on probabilities
            total_probability = sum(prob for _, prob in probabilities)
            probabilities = [(city, prob / total_probability) for city, prob in probabilities]
            next_city = random.choices(range(len(probabilities)), weights=[prob for _, prob in probabilities])[0]
            next_city = probabilities[next_city][0]

            # Move to the next city
            path.append(next_city)
            unvisited_cities.remove(next_city)
            current_city = next_city

        ant_paths.append(path)

    # Update pheromone levels
    pheromone_matrix *= (1 - evaporation_rate)

    for ant_path in ant_paths:
        for i in range(num_cities - 1):
            pheromone_matrix[ant_path[i]][ant_path[i + 1]] += Q

# Find the best path
best_path = ant_paths[np.argmin([sum(distance_matrix[i][j] for i, j in zip(path, path[1:] + [path[0]])) for path in ant_paths])]
best_distance = sum(distance_matrix[i][j] for i, j in zip(best_path, best_path[1:] + [best_path[0]]))

print("Best Path:", best_path)
print("Best Distance:", best_distance)
