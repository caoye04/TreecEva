import math

# Simulated sensor data from smart grid zones
time_series_data = [
    [127, 134, 129, 142, 145, 150, 148, 140],
    [95, 98, 102, 105, 110, 112, 108, 104],
    [201, 198, 205, 210, 215, 213, 207, 200],
    [77, 80, 85, 88, 90, 87, 83, 80]
]

# Irrelevant transformation: normalize to percentage (distractor)
normalized_zones = []
for zone in time_series_data:
    min_val, max_val = min(zone), max(zone)
    normalized = [(val - min_val) / (max_val - min_val) * 100 for val in zone]
    normalized_zones.append(normalized)

# Decoy function: appears useful but unused
def calculate_efficiency_rating(data):
    base = sum(data) / len(data)
    variance = sum((x - base) ** 2 for x in data) / len(data)
    return round(base / (1 + math.sqrt(variance)), 2)

# Unused recursive helper (red herring)
def binary_partition_sum(arr, depth=0):
    if len(arr) <= 1 or depth > 3:
        return arr[0] if arr else 0
    mid = len(arr) // 2
    return binary_partition_sum(arr[:mid], depth+1) + binary_partition_sum(arr[mid:], depth+1)

# Simulate voltage fluctuations (irrelevant computation)
voltage_drift = []
for t in range(len(time_series_data[0])):
    drift = 0
    for i, zone in enumerate(time_series_data):
        drift += zone[t] * math.sin(i * 0.5)
    voltage_drift.append(abs(drift % 50))

# Real processing begins here
zone_averages = [sum(zone) / len(zone) for zone in time_series_data]

# Weighted contribution based on infrastructure age
infrastructure_age_weights = [1.2, 0.9, 1.5, 0.8]
weighted_contributions = [
    avg * weight 
    for avg, weight in zip(zone_averages, infrastructure_age_weights)
]

# Simulate load redistribution using slicing and shifting
shifted_loads = weighted_contributions[1:] + [weighted_contributions[0]]  # circular shift
overlap_region = [
    (a + b) / 2 for a, b in zip(weighted_contributions, shifted_loads)
]

# Aggregate loads with overlapping influence zones
aggregate_loads = []
for i, base_load in enumerate(weighted_contributions):
    neighbors = []
    if i > 0: neighbors.append(overlap_region[i-1])
    if i < len(overlap_region): neighbors.append(overlap_region[min(i, len(overlap_region)-1)])
    neighbor_avg = sum(neighbors) / len(neighbors) if neighbors else base_load
    aggregate_loads.append(base_load * 0.7 + neighbor_avg * 0.3)

# Introduce bit manipulation decoy (irrelevant)
final_hash = 0
for val in aggregate_loads:
    shifted = int(val) << 2
    final_hash ^= shifted & 0xFFFF
    final_hash = (final_hash + 17) % 65537

# Critical statement: peak capacity determined by maximum aggregate load
peak_capacity = max(aggregate_loads)

# Print result as required
print(f"Result: {peak_capacity}")