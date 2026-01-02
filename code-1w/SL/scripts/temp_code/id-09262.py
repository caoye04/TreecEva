from collections import defaultdict

# Simulate hourly energy consumption for a microgrid over a day
hours = list(range(24))
temperature_factor = [1.0 + (temp - 12) * 0.03 for temp in [15,16,18,20,22,25,27,29,30,29,27,25,24,23,22,21,22,23,25,26,27,26,24,20]]

# Energy demand baseline with occupancy patterns (work hours vs night)
owner_occupancy = [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
base_load = 2.5

# Compute dynamic load based on temperature and usage
capacity_tracker = defaultdict(float)
for hour in hours:
    thermal_load = base_load * temperature_factor[hour]
    occupancy_multiplier = 1.8 if owner_occupancy[hour] else 0.9
    total_load = thermal_load * occupancy_multiplier
    capacity_tracker[hour] = round(total_load, 3)

# Identify peak capacity required in a single hour
peak_capacity = max(capacity_tracker.values())
print(f"Result: {peak_capacity}")