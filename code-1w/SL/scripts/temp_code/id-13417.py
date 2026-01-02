from collections import defaultdict

# Simulate hourly resource utilization across multiple servers
current_load = [12, 15, 10, 23, 17, 19, 25, 14, 18, 22, 20, 16]
threshold = 18
window_size = 3

# Track rolling average per segment
rolling_averages = []
for i in range(len(current_load) - window_size + 1):
    window_avg = sum(current_load[i:i+window_size]) / window_size
    rolling_averages.append(round(window_avg, 2))

# Misleading: secondary metric not used in final result
stdev_estimation = 0
if len(rolling_averages) > 1:
    mean_ra = sum(rolling_averages) / len(rolling_averages)
    stdev_estimation = (sum((x - mean_ra)**2 for x in rolling_averages) / (len(rolling_averages)-1))**0.5

# Distractor list comprehension with unused outcome
adjusted_loads = [x * 1.1 for x in current_load if x > threshold]

# Core logic: track capacity usage by category
usage_tracker = defaultdict(int)
for hour, load in enumerate(current_load):
    if load < threshold:
        usage_tracker['underused'] += load
    elif load == threshold:
        usage_tracker['balanced'] += load
    else:
        usage_tracker['overused'] += load

# Secondary distractor: irrelevant counter based on rolling average conditions
surge_count = sum(1 for avg in rolling_averages if avg > threshold)

# Additional noise: unused transformation of keys
status_flags = {k: True for k in usage_tracker.keys()}

# Key statement
peak_capacity = max(usage_tracker.values()) if usage_tracker else 0

print(f"Result: {peak_capacity}")