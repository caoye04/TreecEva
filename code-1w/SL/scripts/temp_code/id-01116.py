from collections import defaultdict

# Simulate hourly system load over a day with occasional spikes
time_slots = [f"{hour:02d}:00" for hour in range(24)]
base_loads = [120, 110, 105, 95, 90, 130, 200, 350, 600, 750, 820, 800, 790, 810, 830, 780, 740, 700, 680, 670, 650, 600, 500, 400]

# Apply conditional spike at midday due to batch job
if base_loads[12] > 750:
    base_loads[12] += 150

# Track load per time category using defaultdict
load_by_period = defaultdict(list)
for i, load in enumerate(base_loads):
    if i < 6:
        load_by_period['night'].append(load)
    elif i < 12:
        load_by_period['morning'].append(load)
    elif i < 18:
        load_by_period['afternoon'].append(load)
    else:
        load_by_period['evening'].append(load)

# Compile historical load values above threshold
threshold = 700
load_history = [load for load in base_loads if load >= threshold]

# Determine peak observed load
peak_load = max(load_history, default=0)

# Print final result
print(f"Result: {peak_load}")