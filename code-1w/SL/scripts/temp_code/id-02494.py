from collections import defaultdict

# Simulate hourly system load over a workday (9 AM - 5 PM)
operational_hours = [9, 10, 11, 12, 13, 14, 15, 16, 17]
base_loads = [45, 60, 75, 80, 70, 75, 65, 60, 50]

# Apply temperature scaling factor: higher temp -> higher cooling load
external_temps = [22, 24, 26, 28, 27, 26, 25, 24, 23]
temp_factor = [1 + (temp - 22) * 0.03 for temp in external_temps]

# Compute actual load with temp adjustment
load_history = [base_loads[i] * temp_factor[i] for i in range(len(base_loads))]

# Track category counts (irrelevant but realistic distractor)
category_tracker = defaultdict(int)
for load in load_history:
    if load < 60:
        category_tracker['low'] += 1
    elif load < 75:
        category_tracker['medium'] += 1
    else:
        category_tracker['high'] += 1

# Key computation step
peak_load = max(load_history)

print(f"Result: {peak_load}")