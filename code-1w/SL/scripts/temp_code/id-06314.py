from collections import defaultdict, Counter

# Sensor calibration and diagnostic system for environmental monitoring

def calibrate_sensor(raw_data, offset=0.05, gain=1.02):
    """Apply calibration transform (distraction: not actually used in final path)"""
    return [(x + offset) * gain for x in raw_data]

def normalize_readings(readings):
    mean_val = sum(readings) / len(readings)
    return [r - mean_val for r in readings]

def detect_spikes(signal, threshold=2.5):
    """Detect abnormal spikes (red herring function - unused)"""
    return [i for i, s in enumerate(signal) if abs(s) > threshold]

def filter_anomalies(samples):
    # Real processing step disguised among distractions
    filtered = []
    history = defaultdict(int)
    for idx, val in enumerate(samples):
        hex_code = f'{idx ^ int(val * 10) & 0xFF:02x}'  # Bitwise XOR and masking
        checksum = sum(int(c) for c in str(idx) + str(int(val))) % 7
        history[hex_code] += 1
        if val < 90 or val > 110:
            continue  # Filter out-of-range values
        if checksum in {0, 3, 4}:
            filtered.append(val + 0.5)
        else:
            filtered.append(val - 0.25)
    return filtered

def compute_entropy(data_list):
    """Entropy calculation (decoy - looks important but unused)"""
    count_map = Counter(data_list)
    total = len(data_list)
    entropy = 0.0
    for count in count_map.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, just mimicry
    return round(entropy, 4)

def rolling_average(values, window=3):
    """Unused helper - creates false trail"""
    if len(values) < window:
        return [0.0]
    avgs = []
    for i in range(len(values) - window + 1):
        avgs.append(sum(values[i:i+window]) / window)
    return avgs

def analyze_readings(validated):
    analysis = {}
    temp_buckets = defaultdict(list)
    for v in validated:
        bucket_key = int(v // 5) * 5
        temp_buckets[bucket_key].append(v)
    
    # Core logic hidden in complex structure
    result_stack = []
    for key in sorted(temp_buckets.keys()):
        group = temp_buckets[key]
        count = len(group)
        base = key + 2.5
        adjustment = (count * 0.7) if count % 2 == 0 else -(count * 0.3)
        computed = base + adjustment
        result_stack.append(computed)
    
    # Final transformation chain
    transformed = [abs(x) * 1.1 for x in result_stack if x > 0]
    if len(transformed) > 1:
        product = 1.0
        for t in transformed:
            product *= t
        magnitude = len(transformed) ** 2
        final_score = (product / magnitude) * 0.85
    else:
        final_score = transformed[0] if transformed else 0.0
    
    # Secondary metrics (distractions)
    stats = {
        'peak': max(validated) if validated else 0,
        'stability': len([v for v in validated if 95 <= v <= 105]),
        'jitter': sum(abs(a - b) for a, b in zip(validated, validated[1:]))
    }
    
    # The actual answer is embedded here
    diagnostics = {
        'baseline': sum(temp_buckets.keys()) / len(temp_buckets) if temp_buckets else 0,
        'complexity_index': len(result_stack) + len(str(int(final_score))),
        'final_diagnostic': int(round(final_score + 50))
    }
    return diagnostics['final_diagnostic']

# Main execution with red herrings
if __name__ == '__main__':
    # Raw sensor inputs (simulated)
    raw_samples = [102, 107, 88, 112, 97, 103, 95, 109, 111, 89, 93, 106]
    
    # Irrelevant preprocessing paths
    normalized_data = normalize_readings(raw_samples)
    spike_indices = detect_spikes(normalized_data)
    rolled_data = rolling_average(raw_samples, window=2)
    
    # Critical distraction: fake calibration path
    dummy_calibrated = [round((x * 1.01) + 0.03, 2) for x in raw_samples]
    entropy_metric = compute_entropy(dummy_calibrated)
    
    # Actual signal path starts here
    calibrated_samples = [x * 1.005 for x in raw_samples]  # Subtle correction
    
    # Key computation with heavy interference
    intermediate_stats = {
        'size': len(raw_samples),
        'mode_approx': Counter([int(x) for x in raw_samples]).most_common(1)[0][1],
        'checksum_total': sum(int(str(idx)+str(int(v))[-1]) for idx, v in enumerate(raw_samples))
    }
    
    # This is the critical execution point
    final_diagnostic = analyze_readings(filter_anomalies(calibrated_samples))
    
    # Print required output
    print(f"Result: {final_diagnostic}")