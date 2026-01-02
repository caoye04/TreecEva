from itertools import compress

# Simulate time-series sensor data for system load (in percentage)
timestamps = list(range(100, 200))
system_loads = [abs((t % 23) * (t % 17) - 150) for t in timestamps]

# Apply filtering: only consider loads during active hours (simulated by condition)
active_window = [50 <= t <= 160 for t in timestamps]
system_loads_filtered = list(compress(system_loads, active_window))

# Further process: take every 3rd reading to simulate periodic sampling
system_loads_sliced = system_loads_filtered[::3] if len(system_loads_filtered) > 10 else system_loads_filtered

# Identify peak load from sampled data
peak_load = max(system_loads_sliced)

# Irrelevant auxiliary calculation (minor distraction)
total_samples = len(system_loads_sliced)
avg_load = sum(system_loads_sliced) / total_samples if total_samples else 0

print(f"Result: {peak_load}")