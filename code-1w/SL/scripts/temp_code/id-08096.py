from itertools import compress

# Simulate daily system load profile over a week
hourly_loads = [120, 135, 140, 175, 180, 170, 160, 150, 
                145, 140, 138, 152, 165, 178, 185, 190,
                188, 177, 165, 155, 150, 148, 142, 130]

# Identify peak usage hours (above 90% of maximum observed)
threshold = 0.9 * max(hourly_loads)
peak_hours = list(compress(range(len(hourly_loads)), (x >= threshold for x in hourly_loads)))

# Calculate rolling 3-hour average to smooth transient spikes
smoothed_loads = [sum(hourly_loads[i:i+3]) / 3 for i in range(len(hourly_loads) - 2)]

# Add baseline night-time maintenance load for comparison
baseline_maintenance = 110
adjusted_loads = [load + 5 if 2 <= i <= 6 or 22 <= i <= 23 else load for i, load in enumerate(hourly_loads)]

# Determine effective capacity values excluding short transients
valid_indices = range(1, len(smoothed_loads) - 1)
load_values = [smoothed_loads[i] for i in valid_indices if i % 4 != 0]

# Key assignment: peak operational capacity
peak_capacity = max(load_values)

print(f"Result: {peak_capacity}")