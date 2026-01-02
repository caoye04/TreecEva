from collections import Counter

# Simulate sensor readings over time with some noise
timestamps = list(range(10))
sensor_data = [98, 102, 110, 108, 115, 112, 118, 116, 109, 104]

# Filter out edge spikes using slicing and compute derived load values
voltage_offset = 0.5
load_values = [(val * 0.75) + voltage_offset for val in sensor_data]

# Exclude first and last segments due to unstable conditions
load_samples = [round(x, 2) for x in load_values]

# Critical evaluation point: determine peak operational load from core segment
peak_load = max(load_samples[1:-1])

# Irrelevant counter for frequency tracking (minor distraction)
reading_counter = Counter(sensor_data)

dummy_flag = any(x > 115 for x in sensor_data)

Result: peak_load