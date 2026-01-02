import itertools

# System telemetry data simulation
time_intervals = list(range(0, 60, 5))
base_loads = [t * 2 + (t**1.5) for t in time_intervals]
noise_offsets = [(i % 3) - 1 for i in range(len(time_intervals))]

# Apply noise to create realistic system load fluctuations
system_loads = [base_loads[i] + noise_offsets[i] for i in range(len(base_loads))]

# Filter out readings below threshold (simulated sensor calibration)
system_loads_filtered = [load for load in system_loads if load >= 30]

# Extract consecutive high-load segments using groupby
grouped_high_loads = [list(group) for k, group in itertools.groupby(system_loads_filtered, key=lambda x: x >= 50)]
valid_segments = [seg for seg in grouped_high_loads if all(load >= 50 for load in seg) and len(seg) >= 3]

# Compute peak capacity from filtered data
peak_capacity = max(system_loads_filtered)

# Irrelevant telemetry stat (minimal distraction)
avg_stability = sum(1 for i in range(1, len(system_loads)) if abs(system_loads[i] - system_loads[i-1]) < 2)

print(f"Target result: {peak_capacity}")