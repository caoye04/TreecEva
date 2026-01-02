from itertools import combinations

# Simulate sensor readings from three different environmental monitoring stations
sensor_a = {2, 4, 6, 8, 10, 12, 14, 16}
sensor_b = {3, 6, 9, 12, 15, 18}
sensor_c = {4, 8, 12, 16, 20, 24}

# Irrelevant transformation: scale values unnecessarily
scaled_a = {x * 2 for x in sensor_a if x % 4 == 0}
scaled_b = {x + 10 for x in sensor_b}

# Track cumulative sum of all original sensor values (distractor)
total_sum = 0
for val in sensor_a | sensor_b | sensor_c:
    total_sum += val

# Generate all valid pairwise intersections between sensors
intersections = {}
intersections['a_b'] = sensor_a & sensor_b
intersections['b_c'] = sensor_b & sensor_c
intersections['a_c'] = sensor_a & sensor_c

# Compute transient state: maximum in each intersection (semi-relevant)
max_vals = {key: max(val) for key, val in intersections.items()}

# Artificial filtering based on threshold (not used later)
filtered_max = [v for v in max_vals.values() if v > 10]

# Identify elements common to all three sensors
common_elements = sensor_a & sensor_b & sensor_c

# Use of enumerate in a non-critical tracking loop (distractor)
index_map = {}
for idx, elem in enumerate(sorted(common_elements)):
    index_map[elem] = idx * 2  # Arbitrary transformation

# Introduce zip to pair elements with offset indices (irrelevant)
offsets = list(range(len(index_map), 0, -1))
paired_data = list(zip(index_map.keys(), index_map.values(), offsets))

# Final computation: size of full overlap
final_overlap = len(common_elements)

# Print result as required
print(f"Result: {final_overlap}")