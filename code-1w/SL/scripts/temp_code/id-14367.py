from collections import Counter

# Simulate server load readings over time
timestamps = [100, 101, 102, 103, 104, 105, 106]
raw_loads = [15, 23, 18, 47, 32, 29, 41]
server_loads = []

for load in raw_loads:
    adjusted = load + (load * 0.1 if load > 40 else 0)
    server_loads.append(int(adjusted))

# Identify active period starting from threshold crossing
threshold_index = -1
for i, val in enumerate(server_loads):
    if val >= 40:
        threshold_index = i
        break

active_index = threshold_index if threshold_index != -1 else len(server_loads)//2

# Critical computation point
peak_load = max(server_loads[active_index:])

# Irrelevant metric for minor distraction
total_observations = len(server_loads)
load_freq = Counter(server_loads)

# Output result
print(f"Result: {peak_load}")