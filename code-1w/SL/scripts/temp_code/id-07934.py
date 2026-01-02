import math

def generate_noise(length):
    return [((i * 7 + 13) % 101) / 10.0 for i in range(length)]

def apply_filter(signal, kernel_size=3):
    smoothed = []
    padding = kernel_size // 2
    padded_signal = [signal[0]] * padding + signal + [signal[-1]] * padding
    for i in range(len(signal)):
        window = padded_signal[i:i + kernel_size]
        smoothed.append(sum(window) / len(window))
    return smoothed

def calculate_entropy(data):
    freq_map = {}
    for x in data:
        rounded = round(x, 1)
        freq_map[rounded] = freq_map.get(rounded, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def segment_data():
    raw_stream = [i * 0.5 + ((i * i) % 8) for i in range(64)]
    outliers = [x for x in raw_stream if x > 30]
    filtered = [x for x in raw_stream if x <= 30]
    noise_pad = generate_noise(5)
    extended = filtered + noise_pad
    return {'data': extended, 'outlier_count': len(outliers), 'timestamp': 1294875}

def process_sequence(dataset):
    data = dataset['data']
    
    # Irrelevant transformation chain (distractor)
    temp_a = [math.sin(x / 10.0) for x in data]
    temp_b = [abs(y) ** 0.5 for y in temp_a if y != 0]
    summary_stats = {
        'max_val': max(data),
        'min_val': min(data),
        'range': max(data) - min(data),
        'midpoint_hint': (max(data) + min(data)) / 2
    }
    
    # Core processing path
    cleaned = apply_filter(data, kernel_size=3)
    normalized = [(x - summary_stats['min_val']) / (summary_stats['range'] + 1e-8) for x in cleaned]
    discretized = [int(x * 100) % 64 for x in normalized]
    
    # Dead code path - never used (red herring)
    def deprecated_transform(seq):
        return [seq[i] ^ seq[(i+1)%len(seq)] for i in range(len(seq))]
    
    # More distractions
    checksum = sum(discretized[i] * (i % 7 + 1) for i in range(0, len(discretized), 4)) % 97
    anomaly_flag = False
    for val in discretized:
        if val in [0, 1, 62, 63]:
            anomaly_flag = True
            break
    
    return {
        'discrete_values': discretized,
        'size': len(discretized),
        'checksum': checksum,
        'anomaly_detected': anomaly_flag,
        'auxiliary': temp_b  # Unused but looks important
    }

def validate_purity(processing_result):
    values = processing_result['discrete_values']
    size = processing_result['size']
    
    # Distractor logic: complex but unused metric
    unique_set = set(values)
    diversity_index = len(unique_set) / size
    critical_threshold = 0.7
    meets_diversity = diversity_index >= critical_threshold
    
    # Decoy statistical check
    mean_val = sum(values) / size
    variance = sum((x - mean_val) ** 2 for x in values) / size
    stability_score = 1 / (1 + variance)
    
    # Real decision path
    high_freq_count = sum(1 for v in values if v > 40)
    ratio_above_threshold = high_freq_count / size
    
    # Secondary filter based on modular clustering
    mod_clusters = [0]*8
    for v in values:
        mod_clusters[v % 8] += 1
    dominant_mod = max(mod_clusters)
    uniformity_penalty = (dominant_mod / size) * 0.3
    
    # Final score calculation
    base_score = ratio_above_threshold * 1000
    adjusted_score = base_score - (uniformity_penalty * 1000)
    
    # Red herring: a function that looks like it affects result but doesn't
    def compute_legacy_metric(arr):
        acc = 0
        for i, x in enumerate(arr):
            if i % 5 == 0 and x % 2 == 1:
                acc += x * 3
        return acc % 100
    
    return int(round(adjusted_score))

# Main execution flow
if __name__ == '__main__':
    dataset_snapshot = segment_data()
    processed_output = process_sequence(dataset_snapshot)
    filtration_score = validate_purity(process_sequence(segment_data()))
    print(f"Result: {filtration_score}")