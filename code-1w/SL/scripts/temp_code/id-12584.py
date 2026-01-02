from itertools import combinations

# Simulate hourly energy consumption readings (in kW) over a day
electric_loads = [3.2, 4.1, 5.6, 7.3, 8.4, 9.1, 8.9, 8.0, 7.2, 6.3, 5.1, 4.4,
                4.3, 5.0, 6.2, 7.8, 8.6, 9.4, 9.2, 8.7, 7.5, 6.4, 5.3, 4.2]

# Misleading: calculate average temperature (irrelevant to load capacity)
temperatures = [18, 19, 21, 23, 25, 26, 27, 28, 27, 26, 25, 24, 23, 23, 24, 25, 27, 28, 29, 28, 27, 25, 23, 21]
avg_temp = sum(temperatures) / len(temperatures)

# Apply time-based efficiency factor (reduces load during off-peak)
efficiency_factor = [0.95] * 6 + [0.88] * 12 + [0.90] * 6
adjusted_loads = [load * factor for load, factor in zip(electric_loads, efficiency_factor)]

# Simulate redundant peak detection using sliding window (not used in final result)
window_peaks = []
for i in range(len(adjusted_loads) - 2):
    window_peaks.append(max(adjusted_loads[i:i+3]))

# Identify high-consumption periods for potential redistribution
candidate_periods = []
for hour, load in enumerate(adjusted_loads):
    if load > 7.0:
        candidate_periods.append(hour)

# Attempt load balancing by shifting 10% from peak hours to adjacent low-use hours
optimized_loads = adjusted_loads.copy()
for period in candidate_periods:
    shift_amount = optimized_loads[period] * 0.1
    # Distribute to previous and next hour if within bounds and not already high
    if period > 0 and optimized_loads[period-1] < 6.0:
        optimized_loads[period-1] += shift_amount * 0.6
        optimized_loads[period] -= shift_amount
    if period < len(optimized_loads)-1 and optimized_loads[period+1] < 6.0:
        optimized_loads[period+1] += shift_amount * 0.4
        optimized_loads[period] -= shift_amount

# Secondary irrelevant calculation: find most stable temperature interval
max_stability = 0
for i in range(len(temperatures)):
    for j in range(i+1, len(temperatures)+1):
        if len(set(temperatures[i:j])) <= 2:
            max_stability = max(max_stability, j - i)

# Key computation step: determine maximum optimized capacity
peak_capacity = max(optimized_loads)

print(f"Result: {peak_capacity}")