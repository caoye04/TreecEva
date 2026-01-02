from collections import defaultdict

# Simulate sensor readings over time with some noise
timestamps = [100, 101, 102, 103, 104, 105, 106]
raw_readings = [23.1, 24.5, 22.8, 25.6, 26.2, 21.9, 27.3]
noise_flags = ['low', 'high', 'low', 'med', 'med', 'high', 'low']

delta_map = defaultdict(float)
for i in range(1, len(raw_readings)):
    delta_map[timestamps[i]] = round(raw_readings[i] - raw_readings[i-1], 2)

deltas = list(delta_map.values())

# Misleading intermediate processing: temperature compensation (not actually used)
temp_compensation = 0.0
for reading in raw_readings:
    if reading > 25.0:
        temp_compensation += 0.15
    elif reading < 23.0:
        temp_compensation -= 0.10

# Apply arbitrary filtering based on synthetic condition (simulates data cleaning)
valid_conditions = [True if flag in ['low', 'med'] else False for flag in noise_flags[1:]]
filtered_deltas = [deltas[i] for i in range(len(deltas)) if valid_conditions[i]]

# Red herring: unused peak detection
peak_count = 0
for i in range(1, len(filtered_deltas)-1):
    if filtered_deltas[i-1] < filtered_deltas[i] > filtered_deltas[i+1]:
        peak_count += 1

# Baseline adjustment computed from initial stable period
baseline_window = raw_readings[:3]
baseline_adjustment = sum(baseline_window) / len(baseline_window) - min(baseline_window)

# Key computation step
net_flux = sum(filtered_deltas) - baseline_adjustment

# Irrelevant formatting task (string method distractor)
data_summary = " | ".join([f"T{t}: {v}" for t, v in zip(timestamps[1:], raw_readings[1:])])
summary_length = len(data_summary.split(" | "))

# Print final result as required
print(f"Result: {net_flux}")