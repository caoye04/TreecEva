from itertools import compress

# System status monitoring simulation
cpu_loads = [0.78, 0.85, 0.92, 0.64, 0.71, 0.96, 0.58]
memory_usage = [85, 90, 93, 78, 81, 95, 70]  # in percent
threshold_exceeded = [load > 0.90 for load in cpu_loads]
high_load_zones = list(compress(memory_usage, threshold_exceeded))

# Calculate base metric
average_high_usage = sum(high_load_zones) / len(high_load_zones) if high_load_zones else 0

# Adjustment factor based on system state
multiplier = 1.5 if len(high_load_zones) >= 2 else 1.2

# Apply modular weighting based on peak detection
peak_memory = max(memory_usage) % 7
filtered_sum = sum([x for x in high_load_zones if x > 80])

# Final computation step
data_offset = 3  # unused variable (minimal interference)
result = filtered_sum * multiplier
print(f"Result: {result}")