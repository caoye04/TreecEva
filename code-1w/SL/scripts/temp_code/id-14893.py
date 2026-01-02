import itertools

# Simulated sensor fusion system for environmental monitoring
def collect_raw_readings():
    return [18, 22, 19, 25, 30, 28, 21]

def calibrate_sensor(input_stream, factor=1.03):
    # Irrelevant calibration function (not used in final path)
    return [round(x * factor, 2) for x in input_stream]

def compute_rolling_average(data, window=3):
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages

def generate_frequency_map(values):
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    return freq_map

def filter_anomalies(stream):
    mean_val = sum(stream) / len(stream)
    return [x for x in stream if abs(x - mean_val) < 10]

def accumulate_checksum(sequence):
    # Distractor function: looks important but unused
    checksum = 0
    for idx, val in enumerate(sequence):
        checksum ^= (val + idx) % 256
    return checksum

def derive_entropy_index(items):
    # Another red herring - not part of main logic
    unique_count = len(set(items))
    return round(unique_count / len(items), 3) if items else 0

def transform_magnitude(x):
    return (x ** 2 + 3 * x + 7) % 89

def enrich_dataset(basic_data):
    # Apply meaningful transformation
    processed = [transform_magnitude(x) for x in basic_data]
    
    # Dead code branch - misleading control flow
    if len(processed) > 100:
        return [p * 2 for p in processed]
    elif len(set(processed)) == 1:
        return [0] * len(processed)
    
    # Actual relevant path
    return [p + 5 for p in processed]

def detect_outlier_pairs(values):
    # Unused complex logic with nested loops
    pairs = set()
    for a, b in itertools.combinations(values, 2):
        if abs(a - b) > 40:
            pairs.add((a, b))
    return pairs

def merge_and_sort_segments(A, B):
    # Decoy data structure manipulation
    merged = sorted(set(A) | set(B))
    partitioned = {"low": [], "high": []}
    for m in merged:
        partitioned["low" if m < 50 else "high"].append(m)
    return partitioned

def analyze_readings(metrics):
    # Core logic hidden among distractions
    base_sum = sum(metrics)
    adjustment = len(metrics) * 3
    
    # Critical calculation buried in noise
    temp_result = base_sum - adjustment
    
    # Multiple irrelevant operations before final step
    dummy_dict = {i: i*2 for i in range(10)}
    _ = [dummy_dict.update({k: v+1}) for k, v in dummy_dict.items() if k % 3 == 0]
    
    # Final computation
    final_score = temp_result + 17
    return final_score

# Main execution sequence
raw_readings = collect_raw_readings()

# Several irrelevant intermediate variables
calibrated = calibrate_sensor(raw_readings)
drift_corrected = [x - 0.5 for x in calibrated]  # Unused
averages = compute_rolling_average(raw_readings)
frequencies = generate_frequency_map(raw_readings)
anomaly_filtered = filter_anomalies(raw_readings)

# Seemingly important but actually peripheral transformations
paired_deltas = []
for i in range(len(anomaly_filtered) - 1):
    paired_deltas.append(abs(anomaly_filtered[i+1] - anomaly_filtered[i]))

entropy_index = derive_entropy_index(paired_deltas)
checksum_value = accumulate_checksum(anomaly_filtered)  # Computed but unused

# Key data pipeline
processed_batch = enrich_dataset(anomaly_filtered)

# More distraction: unused set and dict operations
unique_batch_set = set(processed_batch)
batch_stats = {
    'count': len(processed_batch),
    'range': max(processed_batch) - min(processed_batch),
    'mode': max(set(processed_batch), key=processed_batch.count)
}

# Spurious call to decoy function
outlier_combinations = detect_outlier_pairs(processed_batch)
segment_groups = merge_and_sort_segments(processed_batch, raw_readings)

# Central assignment - this produces the answer
final_diagnostic = analyze_readings(processed_batch)

# Output result as required
print(f"Target result: {final_diagnostic}")