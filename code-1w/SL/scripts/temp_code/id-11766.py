from itertools import combinations

# Simulate hourly network node utilization across a distributed system
node_loads = [12, 15, 22, 18, 25, 30, 28, 24, 20, 19]
drift_compensation = 0.98
calibration_offset = 3

# Apply non-uniform compensation factor (simulated sensor drift correction)
adjusted_loads = [round(load * drift_compensation + calibration_offset) for load in node_loads]

# Generate synthetic secondary metrics for redundancy validation (not used in final result)
signal_quality = [abs(100 - (load % 100)) for load in adjusted_loads]
redundancy_score = sum([len(pair) for pair in combinations(signal_quality, 2) if pair[0] > pair[1]]) % 50

# Filter out hours with sub-threshold activity (preprocessing step)
active_periods = [load for load in adjusted_loads if load > 18]

# Compute rolling 3-hour average to smooth fluctuations
smoothed = []
for i in range(2, len(active_periods)):
    window_avg = (active_periods[i-2] + active_periods[i-1] + active_periods[i]) / 3
    smoothed.append(round(window_avg, 2))

# Simulate diagnostic checksum (dead computation - does not affect result)
diagnostic_checksum = 0
for i, val in enumerate(smoothed):
    diagnostic_checksum += int(val) * (i + 1)
diagnostic_checksum = diagnostic_checksum % 97

# Normalize data for cross-system comparison
scaling_factor = 1.05
normalized_fluctuations = [x * scaling_factor for x in smoothed if x > 20]

# Identify anomalous spikes using simple threshold
spike_flags = [1 if x > 26 else 0 for x in normalized_fluctuations]
anomaly_count = sum(spike_flags)

# Final usage levels before peak detection
usage_levels = [int(x) for x in normalized_fluctuations]
peak_capacity = max(usage_levels)

# Irrelevant trailing operations (distractor code)
consistency_check = all([usage_levels[i] <= usage_levels[i+1] for i in range(len(usage_levels)-1)])
baseline_deviation = abs(usage_levels[0] - adjusted_loads[0])

print(f"Result: {peak_capacity}")