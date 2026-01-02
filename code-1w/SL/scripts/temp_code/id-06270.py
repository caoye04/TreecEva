from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic logic
def preprocess_sensor_stream(raw):
    normalized = [x * 0.98 + 0.5 for x in raw if x > -100]
    filtered = [x for x in normalized if x % 2 != 0.5]
    return filtered[:len(filtered)//2 + 1]

def generate_frequency_map(seq):
    freq = defaultdict(int)
    for item in seq:
        freq[round(item)] += 1
    return freq

def evaluate_stability_index(data):
    if len(data) < 3:
        return 0
    diffs = [abs(data[i+1] - data[i]) for i in range(len(data)-1)]
    return sum(diffs) / len(diffs)

def extract_peaks(signal):
    if len(signal) < 2:
        return []
    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks or [max(signal)]

def compute_entropy(values):
    count = Counter(values)
    total = len(values)
    entropy = 0
    for c in count.values():
        p = c / total
        entropy -= p * (p ** 0.5)  # simplified pseudo-entropy
    return round(entropy, 4)

def apply_window_filter(dataset, window_size=3):
    smoothed = []
    for i in range(len(dataset)):
        start = max(0, i - window_size + 1)
        end = min(len(dataset), i + 1)
        window_avg = sum(dataset[start:end]) / (end - start)
        smoothed.append(window_avg * 0.95)
    return [round(x, 3) for x in smoothed]

def detect_anomalies(mapped):
    anomalies = []
    for k, v in mapped.items():
        if v > 2 and k % 2 == 1:
            anomalies.append(k * v)
    return sorted(anomalies, reverse=True)[:2]

def derive_checksum(items):
    checksum = 0
    for i, val in enumerate(items):
        checksum ^= int(val) * (i + 1)
    return checksum & 0xFFFF

def analyze_pattern(last_segment):
    segment_sum = sum(last_segment)
    peak_values = extract_peaks(last_segment)
    stability = evaluate_stability_index(last_segment)
    entropy_score = compute_entropy([int(x) for x in last_segment if x > 0])
    
    # Distractor: irrelevant transformation
    temp_encoded = ''.join([chr(int(x) % 26 + 97) for x in last_segment if 0 < x < 100])
    dummy_freq = generate_frequency_map([x*2 for x in last_segment])
    
    # Core logic masked by noise
    base_metric = segment_sum * (1 + stability)
    adjustment = entropy_score * len(peak_values)
    if len(last_segment) > 4:
        adjustment += 0.5
    else:
        adjustment -= 0.2
    
    # Red herring: unused complex structure
    diagnostic_tree = {
        'node_1': {'value': base_metric, 'flags': []},
        'node_2': {'value': adjustment, 'flags': ['A', 'B']}
    }
    
    final_score = base_metric - adjustment
    return int(round(final_score))

# Irrelevant global computations
baseline_readings = [12.3, 15.7, 8.2, 23.1, 19.5, 7.4, 31.6]
dummy_analysis = [x**2 for x in baseline_readings if x < 20]
shadow_map = {i: baseline_readings[i] for i in range(len(baseline_readings))}

# Main data pipeline
raw_sensor_input = [55.6, 43.2, 78.9, 61.3, 47.8, 88.1, 59.4, 72.7, 66.5, 54.3]
processed_batch = preprocess_sensor_stream(raw_sensor_input)
transformed_data = []

for segment in [processed_batch[:4], processed_batch[1:5], processed_batch[2:]]:
    freq_map = generate_frequency_map(segment)
    enhanced = [x + (round(x) % 3) for x in segment]
    smoothed = apply_window_filter(enhanced)
    transformed_data.append(smoothed)

# Secondary distractor: unused anomaly detection
freq_summary = generate_frequency_map(processed_batch)
anomaly_list = detect_anomalies(freq_summary)
checksum_value = derive_checksum(anomaly_list)

# Key execution point
final_diagnostic = analyze_pattern(transformed_data[-1])

# Additional red herring operations
log_snapshot = [{'entry': f'X{x}', 'val': v} for x, v in enumerate(transformed_data[0][:3])]
aggregated_metrics = defaultdict(list)
for t in transformed_data:
    aggregated_metrics['peaks'].append(len(extract_peaks(t)))
    aggregated_metrics['entropy'].append(compute_entropy([int(y) for y in t]))

print(f"Result: {final_diagnostic}")