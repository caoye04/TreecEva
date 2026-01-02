from collections import defaultdict, Counter

# Simulated sensor data processing with noise filtering and diagnostics
raw_readings = [145, 178, 201, 145, 234, 201, 178, 234, 267, 299, 267, 145]
error_flags = [False, True, False, False, True, False, True, False, False, True, False, False]
timestamp_groups = ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']

# Irrelevant statistical backup (distractor)
meanless_avg = sum([x**2 for x in raw_readings if x < 200]) / len(raw_readings)
useless_variance_proxy = sum([(x - meanless_avg) ** 2 for x in raw_readings]) / len(raw_readings)

# Noise filter: exclude readings marked with error
filtered_data = [reading for i, reading in enumerate(raw_readings) if not error_flags[i]]

# Group valid readings by timestamp category
readings_by_group = defaultdict(list)
for i, group in enumerate(timestamp_groups):
    if not error_flags[i]:
        readings_by_group[group].append(raw_readings[i])

# Compute group peaks (distractor - not used in final result)
group_peaks = {g: max(vals) for g, vals in readings_by_group.items()}

# Count frequency of valid readings
valid_counter = Counter(filtered_data)
dominant_value = valid_counter.most_common(1)[0][0]

# Diagnostic chain: analyze repetition patterns in filtered data
repeat_count = 0
for i in range(1, len(filtered_data)):
    if filtered_data[i] == filtered_data[i-1]:
        repeat_count += 1

# Secondary pattern: rising sequence detection (misleading path)
rising_streaks = 0
for i in range(1, len(filtered_data)):
    if filtered_data[i] > filtered_data[i-1]:
        rising_streaks += 1

# Primary diagnostic logic (obscured by distractors)
base_signature = sum(filtered_data) % 1000
noise_level = len([x for x in raw_readings if x > 250])
correction_factor = (noise_level + 1) * (repeat_count + 1)

# Data slicing to extract key signal window
signal_window = filtered_data[2:-2]
signal_sum = sum(signal_window)

# Hash-like transformation using bitwise and rotation (red herring)
def fake_hash(seq):
    acc = 0
    for val in seq:
        acc = (acc << 3) ^ val ^ (acc >> 5)
    return acc & 0xFFFF

phantom_checksum = fake_hash(filtered_data)  # Unused decoy

# Actual score computation obscured among distractions
aggregate_score = base_signature * 17 + signal_sum

# Final diagnostic depends on non-obvious combination of repeat patterns and noise
final_diagnostic = aggregate_score // correction_factor

# Dead code path (never executed - control flow red herring)
if False:
    temp_buf = [0]*10
    for k in range(len(temp_buf)-1):
        temp_buf[k+1] = temp_buf[k] ^ k
    final_diagnostic -= sum(temp_buf)

# Print target result
print(f"Result: {final_diagnostic}")