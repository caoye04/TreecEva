from collections import defaultdict

# Simulate sensor range coverage and critical monitoring zones
sensor_coverage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
diagnostic_flags = [True, False, True, True]

temp_offsets = [-2, -1, 0, 1, 2]
base_threshold = 5

# Define valid operational ranges using slicing
valid_ranges = set(sensor_coverage[2:8])  # Covers 3-8

# Define critical zones from patterned data
critical_zones = set()
data_stream = [4, 5, 6, 7]
for val in data_stream:
    if val > base_threshold - 2:
        critical_zones.add(val)

# Irrelevant diagnostic counter (minor distraction)
diag_count = defaultdict(int)
for flag in diagnostic_flags:
    diag_count[flag] += 1

# Key computation step
result = len(valid_ranges & critical_zones)

print(f"Result: {result}")