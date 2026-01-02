import itertools

# Simulated sensor data with noise and calibration offsets
data_stream = [102, 98, -999, 105, -999, 100, 103, 99, 101, -999, 104, 102]

calibration_factor = 0.98
drift_compensation = 2
offset_table = {100: 1, 102: 2, 104: 1, 98: -1}

# Irrelevant transformation: time-based dummy weights
time_weights = [1.0, 0.95, 0.9, 0.85, 0.8]
weighted_contributions = []
for i in range(len(time_weights)):
    weighted_contributions.append(time_weights[i] * (i + 1) ** 2)

# Misleading intermediate: frequency analysis of invalid markers
invalid_marker_count = 0
marker_positions = []
for idx, val in enumerate(data_stream):
    if val == -999:
        invalid_marker_count += 1
        marker_positions.append(idx)

# Decoy function: never actually used but looks important
def analyze_signal_integrity(raw_data, threshold=100):
    peak_count = 0
    for x in raw_data:
        if x > threshold and x != -999:
            peak_count += 1
    return peak_count / len(raw_data) if raw_data else 0

# Simulated redundant checksum (unused)
checksum = 0
for x in data_stream:
    if x != -999:
        checksum ^= x  # Bitwise XOR for integrity (distractor)

# Real processing begins: clean data and apply compensation
raw_readings = [x for x in data_stream if x != -999]
adjusted_readings = []
for val in raw_readings:
    adjusted = val * calibration_factor + drift_compensation
    if val in offset_table:
        adjusted += offset_table[val]
    adjusted_readings.append(adjusted)

# Further filtering: only trust readings within expected physical range
valid_entries = []
for adj in adjusted_readings:
    if 95 <= adj <= 108:
        valid_entries.append(adj)

# Use slicing to discard last two entries due to known instability in final measurements
stable_entries = valid_entries[:-2] if len(valid_entries) > 2 else valid_entries

# Red herring: group consecutive similar values (never used)
grouped_by_proximity = [list(group) for k, group in itertools.groupby(stable_entries, key=lambda x: round(x))]

# Key computation obscured by prior noise
filtered_sum = sum(stable_entries)

# Another dead-end: hypothetical prediction model
if len(stable_entries) > 3:
    trend_estimate = stable_entries[-1] - stable_entries[0]
    projected_next = stable_entries[-1] + (trend_estimate / len(stable_entries))

print(f"Result: {filtered_sum}")