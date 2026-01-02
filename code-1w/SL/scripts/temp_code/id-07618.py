def analyze_pattern(sequence):
    # Irrelevant helper function (dead code path)
    return sum(x ** 2 for x in sequence if x % 3 == 0)


def validate_checksum(data):
    # Distractor function: looks important but unused
    return sum(data) % 7 == 0

# Simulated sensor readings (some relevant, some red herrings)
sensor_ids = ['S1', 'S2', 'S3', 'S4']
raw_readings = [12, 15, 8, 23, 7, 19, 4, 11]

timestamps = [1623456000, 1623456060, 1623456120, 1623456180]

# Misleading aggregation (not used in final result)
aggregate_stats = {
    'peak': max(raw_readings),
    'baseline': min(raw_readings),
    'delta': max(raw_readings) - min(raw_readings)
}

# Real data processing begins here
paired_data = list(zip(sensor_ids, raw_readings[::2]))  # Only even-indexed readings matter

# Threshold logic with decoy entries
threshold_map = {
    'S1': 10, 'S2': 14, 'S3': 6, 'S4': 20,  # S4 threshold too high — never triggered
    'dummy1': 100, 'dummy2': -5  # Decoy keys to mislead
}

status_flags = []
for sid, value in paired_data:
    if sid in threshold_map:
        if value > threshold_map[sid]:
            status_flags.append(1)
        else:
            status_flags.append(0)

# Complex conditional with red herring variables
adjustment_factor = 0
if len(status_flags) > 2:
    adjustment_factor += 2
if sum(raw_readings) > 50:  # True, but irrelevant
    adjustment_factor += 1  # This doesn't affect anything

# Core logic: counting valid high-readings with offset
high_count = sum(status_flags)
offset_correction = len(paired_data) - high_count

calibration_sequence = [i * 2 + offset_correction for i, _ in enumerate(paired_data)]

# Final processing with tuple unpacking and real dependency
def process_readings(data_pairs, thresholds):
    temp_sum = 0
    for idx, (sensor, reading) in enumerate(data_pairs):
        if sensor in thresholds and reading > thresholds[sensor]:
            temp_sum += reading * (idx + 1)  # Weight by position
    temp_sum -= offset_correction * adjustment_factor  # Uses misleading factor (but harmless)
    anomaly_score = temp_sum % 17
    diagnostic_code = temp_sum + anomaly_score
    return diagnostic_code

# Key assignment statement
final_diagnostic = process_readings(paired_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")