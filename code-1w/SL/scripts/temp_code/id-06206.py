from collections import defaultdict

# Simulate hourly system load with baseline and spikes
time_slots = ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00']
base_loads = [120, 135, 240, 450, 670, 520]

# Irrelevant metadata (minimal distraction)
system_info = defaultdict(str)
system_info['region'] = 'west'
system_info['version'] = '2.1'

# Normalization factor (not used in critical path)
normalization = sum(base_loads) / len(base_loads)  # ~355.83

# Overload calculation based on peak detection
overload_threshold = 400
overload_factor = 1.3 if any(load > overload_threshold for load in base_loads) else 1.0

# Apply overload scaling to peak
peak_load = max(base_loads) * overload_factor

# Print result
print(f"Result: {peak_load}")