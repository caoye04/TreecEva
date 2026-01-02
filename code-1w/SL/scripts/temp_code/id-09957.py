from itertools import groupby

# System performance monitoring data
load_readings = [120, 120, 150, 150, 150, 200, 200, 180, 180, 210, 210, 210, 190]

# Filter out noise using lambda to smooth consecutive duplicates above threshold
to_keep = lambda x: x >= 150
filtered_blocks = [list(group) for k, group in groupby(load_readings) if to_keep(k)]

# Reconstruct simplified load sequence
system_loads = [item for block in filtered_blocks for item in block]

# Identify peak operational capacity
peak_capacity = max(system_loads)

# Print final result
print(f"Target result: {peak_capacity}")