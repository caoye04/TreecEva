from collections import defaultdict

# Simulate hourly server load over a week
daily_loads = defaultdict(float)
base_load = [120, 135, 160, 180, 175, 140, 130]
fluctuation = [0.9, 1.1, 1.05, 1.2, 0.95, 0.85, 1.0]

for i in range(7):
    daily_loads[i] = base_load[i] * fluctuation[i]

# Normalize weekend loads slightly upward
if daily_loads[5] < 135:
    daily_loads[5] += 10
if daily_loads[6] < 135:
    daily_loads[6] += 8

# Identify peak usage capacity
peak_capacity = max(daily_loads)

# Additional metric: average weekday load (not used in peak)
weekday_avg = sum(daily_loads[i] for i in range(5)) / 5

# Output target result
print(f"Target result: {peak_capacity}")