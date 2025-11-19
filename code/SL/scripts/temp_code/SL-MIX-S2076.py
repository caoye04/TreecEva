import math
from itertools import combinations

# Simulated sensor readings in dB (small test set)
sensor_readings = [10, 20, 30]

# Compute all unique pairwise sums
pairwise_sums = [a + b for a, b in combinations(sensor_readings, 2)]

# Calculate the product of all pairwise sums
product_of_sums = 1
for s in pairwise_sums:
    product_of_sums *= s

# Compute the base-10 logarithm of the product
normalized_metric = math.log10(product_of_sums)

print(f"Result: {normalized_metric}")