from itertools import groupby

# Simulate sensor data with timestamps and readings
timestamps = [100, 101, 102, 105, 106, 110, 111, 112, 115]
raw_readings = [23.5, 24.1, 23.9, 25.0, 24.8, 26.2, 26.0, 26.1, 27.3]

# Misleading intermediate processing (distractor)
drift_compensation = sum(abs(raw_readings[i] - raw_readings[i-1]) for i in range(1, len(raw_readings))) / len(raw_readings)
baseline_shift = (raw_readings[-1] - raw_readings[0]) / len(raw_readings)

# Group consecutive timestamps (potential gap >1 indicates interruption)
grouped_data = [list(g) for k, g in groupby(zip(timestamps, raw_readings), key=lambda x: x[0] - timestamps.index(x[0]))]

# Extract valid sequences (length >= 3 to filter noise)
valid_sequences = [seq for seq in grouped_data if len(seq) >= 3]

# Flatten back into processed data
processed_data = [item for seq in valid_sequences for item in seq]
count_valid_points = len(processed_data)

event_flags = []
for ts, val in processed_data:
    if val > 25.0:
        event_flags.append((ts, 'HIGH'))
    elif val < 24.0:
        event_flags.append((ts, 'LOW'))
    else:
        event_flags.append((ts, 'NORMAL'))

# Red herring: unused complex lambda transformation
smoothing_kernel = lambda window: [w / sum(window) for w in window] if sum(window) != 0 else [0] * len(window)
weights = smoothing_kernel([1, 2, 1])  # Not actually applied

# Overhead calculation from system metadata (semi-relevant)
system_logs = ['init', 'calib', 'run', 'dump', 'flush']
overhead = len(system_logs) * 0.25 + 1  # Fixed overhead penalty

# Auxiliary function using itertools concept
def calculate_spans(data):
    if not data:
        return 0
    times = [x[0] for x in data]
    return max(times) - min(times)

# Dummy recursive depth counter (not used in final result)
def recursion_probe(n):
    return 1 if n <= 1 else n + recursion_probe(n - 2)

probe_depth = recursion_probe(7)  # Irrelevant computation

# Actual efficiency logic
active_duration = calculate_spans(processed_data)

# Efficiency defined as valid points per unit time, penalized by overhead
def calculate_efficiency(data, overhead_factor):
    if active_duration == 0:
        return 0.0
    base_rate = len(data) / active_duration
    return round(base_rate / (1 + overhead_factor), 4)

# Key statement
efficiency_score = calculate_efficiency(processed_data, overhead)

print(f"Result: {efficiency_score}")