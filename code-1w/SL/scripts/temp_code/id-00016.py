import math
from functools import reduce

device_readings = [1000, 2500, 4000, 8000]
device_ids = ['sensor_a', 'sensor_b', 'sensor_c', 'sensor_d']

# Step 1: Apply logarithmic scaling to readings
scaled_readings = list(map(lambda x: math.log(x, 10), device_readings))

# Step 2: Compute weights from string hashes
hash_weights = list(map(lambda s: hash(s) % 100 + 1, device_ids))

# Step 3: Normalize weights to sum to 1
weight_sum = sum(hash_weights)
normalized_weights = [w / weight_sum for w in hash_weights]

# Step 4: Calculate weighted harmonic mean
harmonic_sum = reduce(lambda acc, pair: acc + pair[1] / pair[0], zip(scaled_readings, normalized_weights), 0)
weighted_harmonic_mean = 1 / harmonic_sum

# Step 5: Apply exponentiation for final normalization
normalized_aggregate = math.exp(weighted_harmonic_mean)

print(f"Result: {normalized_aggregate}")