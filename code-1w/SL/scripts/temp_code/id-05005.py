def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > 0]
    normalized = [x / max(filtered) for x in filtered]
    return [round(x, 3) for x in normalized]


def compute_entropy(values):
    from math import log2
    frequency = {}
    for v in values:
        frequency[v] = frequency.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in frequency.values():
        prob = count / total
        entropy -= prob * log2(prob)
    return round(entropy, 4)


def generate_checksum(sequence):
    # Irrelevant checksum computation (dead-end)
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= int(val * 100) + i
    return checksum


def evaluate_stability(readings):
    moving_avg = []
    for i in range(2, len(readings)):
        avg = sum(readings[i-2:i+1]) / 3
        moving_avg.append(avg)
    variance = sum((x - sum(moving_avg)/len(moving_avg))**2 for x in moving_avg) / len(moving_avg)
    return variance < 0.05


def extract_features(data_stream):
    # Distractor: complex feature extraction with unused results
    peaks = [i for i in range(1, len(data_stream)-1) if data_stream[i-1] < data_stream[i] > data_stream[i+1]]
    troughs = [i for i in range(1, len(data_stream)-1) if data_stream[i-1] > data_stream[i] < data_stream[i+1]]
    peak_values = [data_stream[i] for i in peaks]
    slope_changes = []
    for i in range(1, len(data_stream)):
        slope_changes.append(data_stream[i] - data_stream[i-1])
    magnitude = sum(abs(x) for x in slope_changes)
    return {'peaks': len(peaks), 'troughs': len(troughs), 'magnitude': magnitude}


def analyze_pattern(sensor_log):
    # Core relevant logic
    base_set = set(range(1, 100))
    observed = set()
    for entry in sensor_log:
        if isinstance(entry, float):
            observed.add(int(entry * 100))
    
    # Critical intersection operation
    detected_anomalies = base_set - observed
    anomaly_score = sum(detected_anomalies) % 97
    
    # Secondary but misleading aggregation
    redundant_sum = sum(len(str(x)) for x in detected_anomalies if x % 2 == 0)
    dummy_flag = redundant_sum > 100
    
    # Final computation path (only this matters)
    critical_entries = [x for x in observed if x in {n*n for n in range(1,10)}]
    final_diagnostic = len(critical_entries) * anomaly_score
    
    # Dead code branches (red herrings)
    if dummy_flag:
        final_diagnostic += redundant_sum
    if len(observed) == 0:
        final_diagnostic = -1
    
    return final_diagnostic

# Simulated input data
raw_input = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10,
             0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.20,
             0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.30]

# Irrelevant preprocessing chain
filtered_signal = preprocess_signal([x*100 for x in raw_input])
entropy_metric = compute_entropy(filtered_signal)
eval_result = evaluate_stability(filtered_signal)
features = extract_features(filtered_signal)
checksum_val = generate_checksum(filtered_signal)

# Collected data used in analysis (critical)
collected_data = [x for x in raw_input]

# Key execution point
final_diagnostic = analyze_pattern(collected_data)
print(f"Result: {final_diagnostic}")