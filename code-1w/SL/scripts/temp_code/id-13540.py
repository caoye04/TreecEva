from itertools import combinations

# Simulate hourly energy consumption patterns across zones
zone_a = [18, 22, 25, 30, 28, 24, 20]
zone_b = [15, 19, 23, 27, 30, 26, 20]
zone_c = [10, 14, 18, 22, 25, 24, 20]

# Misleading: unused zone data (distractor)
zone_d = [8, 12, 15, 17, 19, 18, 14]  
zone_e = [5, 9, 11, 13, 15, 14, 12]

# Generate all possible two-zone pairings for redundancy analysis (semi-relevant)
pairwise_combinations = list(combinations([zone_a, zone_b, zone_c], 2))
overlap_hours = []
for pair in pairwise_combinations:
    hours_in_sync = 0
    for hr in range(len(pair[0])):
        if pair[0][hr] > 20 and pair[1][hr] > 20:
            hours_in_sync += 1
    overlap_hours.append(hours_in_sync)

# Compute joint load profiles for reliability assessment (irrelevant computation)
total_redundancy_load = 0
for idx, pair in enumerate(pairwise_combinations):
    combined = [a + b for a, b in zip(pair[0], pair[1])]
    total_redundancy_load += sum(combined) // len(combined)

# Core calculation: system-wide aggregate loads by hour
aggregate_loads = []
for i in range(len(zone_a)):
    aggregate_loads.append(zone_a[i] + zone_b[i] + zone_c[i])

# Normalize aggregate loads to efficiency-adjusted capacity units
normalized_loads = [round(load * 0.95, 2) for load in aggregate_loads]

# Introduce irrelevant transformation (dead path)
sorted_normalized = sorted(normalized_loads, reverse=True)
decay_factor = 0.9
adjusted_decay = [val * (decay_factor ** i) for i, val in enumerate(sorted_normalized)]

# Key assignment point
peak_capacity = max(aggregate_loads)

# Print final result as required
print(f"Result: {peak_capacity}")