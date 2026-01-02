from itertools import combinations

# System load simulation over time slots
time_slots = list(range(8, 20))  # 8 AM to 8 PM
demand_base = [32, 45, 58, 70, 85, 92, 95, 90, 88, 80, 75, 60, 50]
weather_multiplier = [1.1, 1.0, 0.95, 1.2, 1.3, 1.15, 1.05, 1.0, 0.9, 0.85, 0.95, 1.1, 1.0]

# Apply weather impact on base demand
adjusted_demand = [int(base * mult) for base, mult in zip(demand_base, weather_multiplier)]

# Simulate unexpected spikes during overlapping high-usage windows
spike_zones = []
for i in range(len(adjusted_demand) - 2):
    if adjusted_demand[i] > 70 and adjusted_demand[i+1] > 70:
        spike_zones.append(i)

# Add artificial spikes in overlapping zones
for zone in spike_zones:
    adjusted_demand[zone + 1] += 15

# Compute rolling average for stability analysis (irrelevant to final answer)
stability_window = 3
rolling_stability = []
for i in range(len(adjusted_demand) - stability_window + 1):
    window_avg = sum(adjusted_demand[i:i+stability_window]) / stability_window
    rolling_stability.append(round(window_avg, 2))

# Distractor: simulate maintenance downtimes (not affecting capacity)
maintenance_slots = [x for x in time_slots if x in [10, 14, 18]]
capacity_reduction = {time_slots[idx]: 10 for idx in range(len(time_slots)) if idx % 4 == 0}

# Actual usage levels with redundancy factors
redundancy_factor = 1.4
usage_levels = [int(val * redundancy_factor) for val in adjusted_demand]

# Misleading intermediate calculation
theoretical_max = max(adjusted_demand) * redundancy_factor * 1.1  # Overestimated

# Key statement
peak_capacity = max(usage_levels)

# Irrelevant combinatorial check of load pairings (distractor)
valid_pairs = 0
for pair in combinations(usage_levels, 2):
    if abs(pair[0] - pair[1]) < 50:
        valid_pairs += 1

# Final output
print(f"Result: {peak_capacity}")