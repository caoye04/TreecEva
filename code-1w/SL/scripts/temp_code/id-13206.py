from itertools import compress

# System monitoring simulation data
base_loads = [120, 150, 135, 160, 145, 170, 130, 165]
threshold = 140

# Generate status flags for overloaded components
over_threshold = [load > threshold for load in base_loads]

# Filter loads using boolean mask
critical_loads = list(compress(base_loads, over_threshold))

# Apply efficiency decay on critical loads (simulated correction)
system_loads_filtered = [load * 0.9 for load in critical_loads]

# Identify peak operational capacity
peak_capacity = max(system_loads_filtered)

print(f"Result: {peak_capacity}")