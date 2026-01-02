from itertools import combinations

# System load simulation across time windows
time_slots = list(range(8, 20))
equipment_count = [3, 5, 4, 2, 6, 7, 3, 4, 5, 6, 8, 4, 3]

# Simulate fluctuating demand based on operational cycles
demand_factor = [((t ** 2) * 0.1 + t * 0.5) % 4 for t in time_slots]
base_load = sum(equipment_count) * 0.6

# Compute dynamic usage per hour
hourly_usage = []
for i, t in enumerate(time_slots):
    spike = 0
    # Artificial complexity: simulate equipment interaction pairs
    for pair in combinations(equipment_count[:5], 2):
        if (pair[0] + pair[1] + t) % 7 == 0:
            spike += 0.8
    adjusted_demand = base_load * demand_factor[i] + spike
    hourly_usage.append(round(adjusted_demand, 2))

# Misleading intermediate calculation - not used in final result
avg_usage = sum(hourly_usage) / len(hourly_usage)
std_deviation = (sum((x - avg_usage) ** 2 for x in hourly_usage) / len(hourly_usage)) ** 0.5

# Normalize usage with offset (semi-relevant transformation)
normalized_loads = [max(0, (u - avg_usage) * 1.2 + 3) for u in hourly_usage]

# Apply safety threshold filtering
filtered_levels = []
for val in normalized_loads:
    if val > 2.5:
        filtered_levels.append(val * 1.1)
    else:
        filtered_levels.append(val * 0.9)

# Round again to simulate measurement precision
usage_levels = [round(x, 2) for x in filtered_levels]

# Critical statement
peak_capacity = max(usage_levels)

# Print result as required
print(f"Result: {peak_capacity}")