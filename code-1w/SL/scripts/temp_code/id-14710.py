import itertools

# Sensor calibration and diagnostic system for environmental monitoring
base_offset = 17
scaling_factor = 3
redundant_flag = False
temp_buffer = [0] * 12
diagnostic_log = []

# Simulated raw sensor readings (after noise injection)
raw_readings = [84, 23, 56, 77, 192, 44, 68, 91, 33, 155, 50, 74]

# Irrelevant helper that logs to unused buffer
def update_buffer(value):
    if len(temp_buffer) > 5:
        temp_buffer.pop(0)
    temp_buffer.append(value % 256)
    return value + 1  # Misleading side effect

# Unused diagnostic flagger
def mark_anomaly(x):
    diagnostic_log.append(f'Anomaly marked: {x}')
    return True

# Real processing chain begins here

def apply_calibration(raw):
    calibrated = []
    for val in raw:
        adjusted = (val * scaling_factor) // 2
        corrected = adjusted - base_offset
        calibrated.append(corrected)
    return calibrated

filter_threshold = 85
exclusion_list = set()

# This function appears complex with red herrings but has a clear core
def filter_anomalies(data):
    global exclusion_list
    valid_data = []
    anomaly_count = 0

    # Distractor: complex-looking but unused filtering condition
    high_freq_peaks = list(itertools.compress(data, (x > 90 for x in data)))
    running_avg = sum(data) / len(data) if data else 0

    # Real filtering logic (decoy above)
    for reading in data:
        if reading <= filter_threshold:  # Only this matters
            valid_data.append(reading)
        else:
            anomaly_count += 1
            exclusion_list.add(reading)
            update_buffer(reading)  # Side effect distractor

    # Another decoy operation
    if anomaly_count > 3:
        mark_anomaly(anomaly_count)

    return valid_data

# Critical analysis function
checksum_seed = 2


def analyze_readings(cleaned):
    result_set = set()
    total = 0
    cycle_marker = 0

    # Meaningful computation buried in abstraction
    for idx, val in enumerate(cleaned):
        if idx % 2 == 0:
            transformed = (val ^ checksum_seed) % 100
        else:
            transformed = (val + checksum_seed) % 100

        result_set.add(transformed)
        total += transformed

        # Complex-looking but irrelevant cycling logic
        cycle_marker = (cycle_marker + val) % 7
        if cycle_marker == 0:
            result_set.discard(min(result_set)) if result_set else None

    # The actual answer comes from set cardinality and total
    set_influence = len(result_set) * 13
    final_score = total - set_influence

    # Dead code path - never reached due to positive numbers
    if final_score < 0 and redundant_flag:
        fallback = sum(itertools.accumulate(result_set))
        return fallback

    return final_score

# Execution flow with misleading intermediate steps
calibrated_samples = apply_calibration(raw_readings)

# Fake usage to suggest importance
running_diagnostic = sum(1 for x in calibrated_samples if x > 100)
diagnostic_log.append(f'Pre-filter count: {running_diagnostic}')

# Key statement
final_diagnostic = analyze_readings(filter_anomalies(calibrated_samples))

# Final output
print(f"Result: {final_diagnostic}")