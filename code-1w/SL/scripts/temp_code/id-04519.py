from itertools import accumulate

# Simulate daily resource allocation over a workweek with recovery periods
daily_requests = [120, -45, 78, -30, 95]
base_allocation = 50
recovery_rate = 0.8
buffer_zone = 10

# Apply exponential smoothing to requests as preprocessing (distraction)
smoothed_requests = []
alpha = 0.6
prev_smooth = daily_requests[0]
for r in daily_requests:
    prev_smooth = alpha * r + (1 - alpha) * prev_smooth
    smoothed_requests.append(prev_smooth)

# Actual usage model: cumulative usage with partial daily recovery
raw_usage = [base_allocation + req for req in daily_requests]
cumulative_load = list(accumulate(raw_usage))

# Simulate daily reset with recovery rate applied (only 80% of load dissipates)
end_of_day_loads = []
current_load = 0
for load_increment in raw_usage:
    current_load += load_increment
    current_load *= recovery_rate  # 20% recovery each day
    end_of_day_loads.append(current_load)

# Introduce auxiliary computation for peak-to-average ratio (unused)
avg_load = sum(end_of_day_loads) / len(end_of_day_loads)
peak_to_avg_ratio = max(end_of_day_loads) / avg_load if avg_load != 0 else 0

# Compute rolling window averages for stability analysis (distraction)
window_size = 2
rolling_averages = [sum(end_of_day_loads[i:i+window_size]) / window_size 
                       for i in range(len(end_of_day_loads) - window_size + 1)]

# Critical operation: assess usage levels including buffer for safety margin
usage_levels = [load + buffer_zone for load in end_of_day_loads]

# Key statement
peak_capacity = max(usage_levels)

# Irrelevant final transformation (dead code path)
if peak_capacity > 200:
    peak_capacity = round(peak_capacity * 0.95)

print(f"Target result: {peak_capacity}")