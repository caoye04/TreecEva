from collections import defaultdict

# Sensor readings: list of lists where each sublist represents readings from one sensor
sensor_readings = [
    [12, 28, 35],
    [15, 22, 40],
    [10, 30, 33]
]

# Threshold definitions
low_threshold = 5
high_threshold = 15

# Initialize data structures
pairwise_diff_counts = defaultdict(int)
transform_cache = {}

# Lambda for computing absolute difference
abs_diff = lambda x, y: abs(x - y)

# Nested loops to compute pairwise differences between all readings of different sensors
for i in range(len(sensor_readings)):
    for j in range(i + 1, len(sensor_readings)):
        for reading_a in sensor_readings[i]:
            for reading_b in sensor_readings[j]:
                diff = abs_diff(reading_a, reading_b)
                if low_threshold <= diff <= high_threshold:
                    pairwise_diff_counts[(i, j)] += 1

# Transformation function using a cache
def transform_count(count):
    if count in transform_cache:
        return transform_cache[count]
    # A simple quadratic transformation
    result = count * count + 2 * count + 1
    transform_cache[count] = result
    return result

# Compute the final coherence index
coherence_index = 0
for (sensor_i, sensor_j), count in pairwise_diff_counts.items():
    transformed_value = transform_count(count)
    coherence_index += transformed_value

print(f"Result: {coherence_index}")