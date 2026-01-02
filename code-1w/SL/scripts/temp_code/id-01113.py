from collections import defaultdict

# Simulate hourly system load over a day with some fluctuations
time_slots = range(24)
baseline_load = 40
load_fluctuations = [1, -2, 3, -1, 5, 8, 12, 15, 14, 10, 7, 5, 6, 5, 9, 13, 16, 18, 17, 14, 11, 8, 5, 2]

load_history = [(t + 1) * (baseline_load + fluctuation) // 10 for t, fluctuation in enumerate(load_fluctuations)]

capacity_map = defaultdict(int)
for hour, load in enumerate(load_history):
    capacity_map[hour] = load * 1.1  # projected future capacity

# Identify peak observed load
temp_avg = sum(load_history) / len(load_history)
above_avg_count = len([x for x in load_history if x > temp_avg])

peak_capacity = 0
if above_avg_count > 0:
    peak_capacity = max(load_history)

Result: peak_capacity