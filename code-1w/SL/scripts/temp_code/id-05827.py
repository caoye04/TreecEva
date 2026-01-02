from itertools import combinations

# Simulate hourly network load across data centers
center_a_load = [120, 135, 140, 128, 150]
center_b_load = [95, 110, 105, 130, 145]
center_c_load = [80, 90, 100, 95, 85]

# Irrelevant computation: potential future expansion (distractor)
projected_growth_rate = 1.08
expanded_estimates = [x * projected_growth_rate for x in center_a_load]

# Combine loads into time-aligned segments
combined_hourly_loads = []
for i in range(len(center_a_load)):
    combined_hourly_loads.append(center_a_load[i] + center_b_load[i] + center_c_load[i])

# Compute rolling average for smoothing (semi-relevant but not used in final answer)
smoothed_loads = []
window_size = 2
for i in range(len(combined_hourly_loads) - window_size + 1):
    window_avg = sum(combined_hourly_loads[i:i+window_size]) / window_size
    smoothed_loads.append(window_avg)

# Track usage peaks under different failure scenarios
default_capacity = 400
failure_modes = list(combinations(['A', 'B', 'C'], 1))  # Single failures
usage_tracker = []

for mode in failure_modes:
    lost_center = mode[0]
    temp_load = combined_hourly_loads.copy()
    
    # Adjust load if a center fails
    if lost_center == 'A':
        reduction = [x * 0.3 for x in center_a_load]
        temp_load = [temp_load[i] - center_a_load[i] + reduction[i] for i in range(len(temp_load))]
    elif lost_center == 'B':
        reduction = [x * 0.25 for x in center_b_load]
        temp_load = [temp_load[i] - center_b_load[i] + reduction[i] for i in range(len(temp_load))]
    elif lost_center == 'C':
        reduction = [x * 0.2 for x in center_c_load]
        temp_load = [temp_load[i] - center_c_load[i] + reduction[i] for i in range(len(temp_load))]
    
    # Calculate peak usage under this failure mode
    peak_usage = max(temp_load)
    usage_tracker.append(peak_usage)

# Distractor: unused statistical measure
median_peak = sorted(usage_tracker)[len(usage_tracker)//2] if usage_tracker else 0

# Key assignment statement
peak_capacity = max(usage_tracker)

# Final output
print(f"Result: {peak_capacity}")