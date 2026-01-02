import math

# Simulated sensor data preprocessing with red herrings
def collect_signals(raw_readings):
    processed = []
    noise_floor = 0.041
    calibration_offset = -0.017
    temp_buffer = []

    for val in raw_readings:
        if abs(val) < noise_floor:
            continue
        corrected = val + calibration_offset
        if corrected > 0:
            normalized = math.log(1 + corrected)
        else:
            normalized = -math.log(1 - corrected)
        processed.append(round(normalized * 1000))
        temp_buffer.append(normalized ** 2)  # unused distraction

    spike_count = 0
    for i in range(1, len(processed)):
        if abs(processed[i] - processed[i-1]) > 500:
            spike_count += 1
    # spike_count is never used again — red herring

    return processed

# Irrelevant transformation chain
def legacy_filter(sequence):
    filtered = []
    for x in sequence:
        if x % 2 == 0 and x > 100:
            filtered.append(x // 2)
    return [y - 50 for y in filtered if y > 150]  # dead-end path

# Core logic obscured by decoys
def transform_sequence(data_stream):
    shifted = [(x >> 2) for x in data_stream if x > 0]
    masked = [x ^ 0b1101 for x in shifted if x % 3 == 1]  # selective bit manipulation
    grouped = {}
    for num in masked:
        key = num // 10
        grouped[key] = grouped.get(key, 0) + 1

    frequencies = sorted(grouped.items())
    result = []
    for k, v in frequencies:
        if v >= 2:
            result.append(k * 10 + v)
    return result  # some are used, many paths ignored

# Decoy function — looks important but unused
def compute_rolling_stat(arr, window=3):
    stats = []n    for i in range(len(arr) - window + 1):
        window_avg = sum(arr[i:i+window]) / window
        stats.append(math.sin(window_avg / 100))
    return [round(s, 3) for s in stats]

# Real threshold logic hidden among distractions
def evaluate_anomalies(dataset):
    anomalies = 0
    baseline = sum(dataset) / len(dataset)
    variance_sum = 0

    for val in dataset:
        deviation = (val - baseline) ** 2
        variance_sum += deviation
        if deviation > 60000:  # high threshold
            anomalies += 1

    variance = variance_sum / len(dataset)
    std_dev = math.sqrt(variance)
    score = int(baseline + std_dev)
    return score  # this gets used later

# Another irrelevant utility
def generate_checksum(values):
    checksum = 0
    for v in values:
        checksum = (checksum + v) * 11 % 97
    return checksum  # never integrated

# Real processing begins here
raw_input = [0.12, -0.05, 0.83, 0.44, -0.67, 0.91, 0.25, -0.18, 0.77]
acquired_signals = collect_signals(raw_input)

# Distractor: applying legacy filter to something it can't use
decoy_output = legacy_filter(acquired_signals)
checksum_probe = generate_checksum(acquired_signals)  # computed but unused

# Main transformation
transformed_data = transform_sequence(acquired_signals)

# Hidden dependency: threshold function defined via lambda
threshold_func = lambda x: x > 55 and (x % 7 != 0)

# Evaluation function that combines results
# Note: evaluate_anomalies returns score used in next step
temp_diagnostic = evaluate_anomalies(acquired_signals)

# Final integration of relevant components
# Only transformed_data and threshold_func matter; others are distractions
def process_metrics(data_list, predicate):
    count = 0
    total = 0
    for item in data_list:
        if predicate(item):
            count += 1
            total += item
    aggregation_key = (total // (count or 1)) + temp_diagnostic  # uses outer-scope temp_diagnostic
    return aggregation_key

# Critical execution point
final_diagnostic = process_metrics(transformed_data, threshold_func)

print(f"Result: {final_diagnostic}")