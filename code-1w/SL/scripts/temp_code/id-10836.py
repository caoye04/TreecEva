from collections import defaultdict

# Simulate hourly resource usage across servers
capacity_log = [
    [120, 135, 140, 160],
    [155, 160, 150, 170],
    [180, 190, 185, 175],
    [160, 150, 145, 140]
]

hourly_stats = defaultdict(float)
peak_capacity = 0
total_hours = 0

for i, readings in enumerate(capacity_log):
    hourly_avg = sum(readings) / len(readings)
    hourly_stats[i] = round(hourly_avg, 2)
    
    if hourly_avg > 170:
        peak_capacity = max(readings)
        total_hours = i + 1
        break

    if i == 1:
        dummy_var = [x * 0.9 for x in readings]  # Irrelevant adjustment (distractor)

Result: {peak_capacity}