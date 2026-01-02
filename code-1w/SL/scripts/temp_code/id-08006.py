import itertools

# Simulated sensor data and calibration parameters
def generate_signals(baseline, count):
    return [baseline + (i * 0.1) for i in range(count)]

def apply_filter(raw, factor=0.9):
    filtered = []
    acc = 0.0
    for val in raw:
        acc += val * factor
    return acc if acc != 0 else 0.0

def evaluate_stability(signal_list):
    diffs = [abs(a - b) for a, b in zip(signal_list, signal_list[1:])]
    return sum(diffs) / len(diffs) if diffs else 0.0

def normalize_vector(vec):
    norm = sum(x ** 2 for x in vec) ** 0.5
    return [x / norm for x in vec] if norm else vec

def merge_streams(stream_a, stream_b):
    return [a + b for a, b in zip(stream_a, stream_b)]

def calculate_entropy(data):
    from math import log2
    freqs = {}
    for d in data:
        freqs[d] = freqs.get(d, 0) + 1
    total = len(data)
    entropy = -sum((freq / total) * log2(freq / total) for freq in freqs.values())
    return round(entropy, 6)

def detect_outliers(values, threshold=2):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) > threshold * std_dev]

def compute_checksum(sequence):
    # Irrelevant checksum for distraction
    chk = 0
    for item in sequence:
        chk ^= int(item * 100) & 0xFF
    return chk

def extract_features(dataset):
    features = {}
    for key, values in dataset.items():
        if len(values) == 0:
            features[key] = 0.0
            continue
        avg = sum(values) / len(values)
        peak = max(values)
        stability = evaluate_stability(values)
        features[f'{key}_avg'] = avg
        features[f'{key}_peak'] = peak
        features[f'{key}_stable'] = stability
    return features

def adjust_weights(wts, factor=1.1):
    # Distractor: this function is defined but not used
    return [w * factor for w in wts]

def validate_inputs(inp_data, constraints):
    # Dead code path - never actually called
    for k, v in inp_data.items():
        if k in constraints:
            low, high = constraints[k]
            if not (low <= sum(v) <= high):
                return False
    return True

def analyze_correlations(stream_x, stream_y):
    # Complex but irrelevant correlation logic
    n = min(len(stream_x), len(stream_y))
    if n == 0:
        return 0.0
    mx = sum(stream_x[:n]) / n
    my = sum(stream_y[:n]) / n
    num = sum((stream_x[i] - mx) * (stream_y[i] - my) for i in range(n))
    den = (sum((x - mx) ** 2 for x in stream_x[:n]) * sum((y - my) ** 2 for y in stream_y[:n])) ** 0.5
    return num / den if den else 0.0

def process_metrics(sensor_data, importance_weights):
    # Core processing function
    extracted = extract_features(sensor_data)
    
    # Simulated intermediate metrics
    metric_keys = ['temp_avg', 'pressure_peak', 'humidity_stable']
    raw_metrics = [extracted.get(k, 0.0) for k in metric_keys]
    
    # Normalize metrics
    norm_metrics = normalize_vector(raw_metrics)
    
    # Apply weighted scoring using dot product
    weighted_sum = sum(m * w for m, w in zip(norm_metrics, importance_weights))
    
    # Secondary adjustment based on entropy of normalized values
    entropy_norm = calculate_entropy([round(x, 4) for x in norm_metrics])
    adjusted_score = weighted_sum * (1 + entropy_norm)
    
    # Conditional bonus for stability
    humidity_vals = sensor_data.get('humidity', [])
    if len(humidity_vals) > 5:
        stable_region = humidity_vals[2:7]
        if evaluate_stability(stable_region) < 0.15:
            adjusted_score += 5.0  # Bonus point
    
    # Red herring: bitwise manipulation with no real effect
    magic_offset = 0xDEADBEEF
    decoy_value = (int(adjusted_score * 1000) ^ magic_offset) & 0xFFFF
    decoy_shift = (decoy_value >> 4) | (decoy_value << 12)
    
    # Final score computation — this is what matters
    final_score = round(adjusted_score + (decoy_shift & 0) * 1e-6, 6)  # Neutralized decoy impact
    
    # Unused branching — misleading complexity
    if final_score > 100:
        final_score = 100.0
    elif final_score < 0:
        final_score = 0.0
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Real input data
    sensor_readings = {
        'temp': [22.1, 22.3, 22.4, 22.5, 22.6, 22.8, 23.0],
        'pressure': [101.3, 101.5, 101.7, 101.8, 102.0, 102.1, 102.3],
        'humidity': [45.0, 45.2, 45.1, 44.9, 45.0, 45.3, 45.5, 45.6],
        'light': [300, 310, 305, 308, 312, 315, 318]
    }
    
    # Weights for scoring — only first three are used
    weights = [0.4, 0.35, 0.25]
    
    # Irrelevant preprocessing streams
    temp_signal = generate_signals(20.0, 7)
    pressure_filtered = apply_filter(sensor_readings['pressure'])
    combined_stream = merge_streams(temp_signal, sensor_readings['temp'])
    
    # Dummy entropy calculation on unused data
    _ = calculate_entropy([int(x) for x in sensor_readings['temp']])
    
    # Outlier detection (no effect)
    outliers = detect_outliers(sensor_readings['light'])
    
    # Checksum on unrelated sequence
    chk = compute_checksum(itertools.islice(itertools.cycle([1.1, 2.2, 3.3]), 20))
    
    # Set operations for distraction
    unique_lights = set(sensor_readings['light'])
    expected_range = set(range(300, 320))
    common = unique_lights & expected_range  # Intersection
    deviation_set = unique_lights - expected_range
    
    # Correlation analysis — computed but unused
    _ = analyze_correlations(sensor_readings['temp'], sensor_readings['pressure'])
    
    # Actual critical computation
    final_score = process_metrics(sensor_readings, weights)
    
    # Output result as required
    print(f"Target result: {final_score}")