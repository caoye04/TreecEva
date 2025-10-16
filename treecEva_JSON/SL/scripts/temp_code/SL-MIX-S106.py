import math
from functools import reduce

temperatures = [23.5, 25.1, 22.8, 26.3, 24.7, 27.2, 21.9, 25.8, 23.9, 26.7]

# Step 1: Calculate mean
mean_temp = reduce(lambda a, b: a + b, temperatures) / len(temperatures)

# Step 2: Calculate variance and standard deviation
variance = reduce(lambda a, b: a + b, [(t - mean_temp) ** 2 for t in temperatures]) / len(temperatures)
std_dev = math.sqrt(variance)

# Step 3: Calculate z-scores
z_scores = [(t - mean_temp) / std_dev for t in temperatures]

# Step 4: Apply sigmoid transformation using lambda
sigmoid = lambda x: 1 / (1 + math.exp(-x))
transformed_scores = list(map(sigmoid, z_scores))

# Step 5: Calculate mean of transformed scores
final_mean = reduce(lambda a, b: a + b, transformed_scores) / len(transformed_scores)

print(f"Result: {final_mean}")