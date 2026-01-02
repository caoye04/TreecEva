def sensor_integrity_check(raw_values):
    checksum = 0
    for i, val in enumerate(raw_values):
        if i % 3 == 0:
            checksum += val * 2
        elif i % 5 == 0:
            checksum -= val
        else:
            checksum += val // (i + 1)
    return checksum

def normalize_signal(signal_data):
    max_val = max(signal_data)
    min_val = min(signal_data)
    range_val = max_val - min_val or 1
    normalized = [(x - min_val) / range_val for x in signal_data]
    return [round(x, 6) for x in normalized]

def generate_frequency_bins(data):
    bins = {'low': 0, 'mid': 0, 'high': 0}
    for x in data:
        if x < 0.3:
            bins['low'] += 1
        elif x < 0.7:
            bins['mid'] += 1
        else:
            bins['high'] += 1
    return bins

def compute_entropy(counts):
    import math
    total = sum(counts.values())
    if total == 0:
        return 0.0
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def decode_calibration_sequence(seq):
    # Irrelevant decoding logic (dead path)
    decoded = []
    for c in seq:
        if c.isalpha():
            decoded.append(ord(c.lower()) - ord('a') + 1)
    return decoded

def evaluate_stability_metrics(norm_data):
    variance_proxy = sum((x - 0.5) ** 2 for x in norm_data) / len(norm_data)
    zero_crossings = 0
    for i in range(1, len(norm_data)):
        if norm_data[i-1] < 0.5 <= norm_data[i] or norm_data[i] < 0.5 <= norm_data[i-1]:
            zero_crossings += 1
    trend_slope = (norm_data[-1] - norm_data[0]) * 100
    return variance_proxy, zero_crossings, trend_slope

def filter_anomalies(data, limits):
    clean = []
    anomalies_detected = 0
    for val in data:
        if limits['min'] <= val <= limits['max']:
            clean.append(val)
        else:
            anomalies_detected += 1
    return clean, anomalies_detected

def temporal_smoothing(values):
    if len(values) < 3:
        return values[:]
    smoothed = [values[0]]
    for i in range(1, len(values)-1):
        smoothed.append((values[i-1] + values[i] + values[i+1]) / 3)
    smoothed.append(values[-1])
    return smoothed

def analyze_readings(data_segments, thresholds):
    results = []
    for label, segment in data_segments.items():
        seg_sum = sum(segment)
        threshold_val = thresholds.get(label, 1e6)
        if seg_sum > threshold_val:
            results.append(1)
        else:
            results.append(0)
    return sum([r * (2**i) for i, r in enumerate(results)])

def main_pipeline(input_stream, config):
    # Step 1: Initial integrity verification
    raw_integrity = sensor_integrity_check(input_stream)
    
    # Step 2: Normalize signal for processing
    normalized_signal = normalize_signal(input_stream)
    
    # Step 3: Apply temporal smoothing (relevant)
    filtered_signal = temporal_smoothing(normalized_signal)
    
    # Step 4: Filter based on dynamic limits (partially relevant)
    bounds = {'min': config['floor'], 'max': config['ceiling']}
    clean_data, _ = filter_anomalies(filtered_signal, bounds)
    
    # Step 5: Generate frequency distribution (distractor)
    freq_bins = generate_frequency_bins(clean_data)
    entropy_score = compute_entropy(freq_bins)  # Distractor
    
    # Step 6: Stability analysis (mixed relevance)
    var_proxy, crossings, slope = evaluate_stability_metrics(clean_data)
    
    # Step 7: Decode fake calibration (red herring)
    calib_seq = "X9K2MnP7"
    calibration_codes = decode_calibration_sequence(calib_seq)
    
    # Step 8: Prepare segmented data using zip and enumerate (critical)
    segments = {}
    chunk_size = 4
    for idx, i in enumerate(range(0, len(clean_data), chunk_size)):
        chunk = clean_data[i:i+chunk_size]
        key = ['alpha', 'beta', 'gamma', 'delta'][idx % 4]
        if len(chunk) == chunk_size:
            segments[key] = [abs(c - 0.5) * 2 for c in chunk]  # Normalize to [0,1] around center
    
    # Step 9: Create threshold map (only 'gamma' and 'delta' thresholds matter)
    base_threshold = var_proxy * 100
    dynamic_offset = abs(slope) / 50
    threshold_map = {
        'alpha': base_threshold + 5,
        'beta': base_threshold + 3,
        'gamma': 1.85,  # Critical threshold
        'delta': 1.92   # Critical threshold
    }
    
    # Step 10: Analyze readings — KEY STATEMENT
    final_diagnostic = analyze_readings(segments, threshold_map)
    
    # Irrelevant print statements and variables (distractions)
    debug_checksum = f"CHK-{raw_integrity:06d}"
    status_flag = debug_checksum.startswith("CHK") and entropy_score > 1.0
    
    # Only this matters:
    return final_diagnostic

# Input data and configuration
input_data = [85, 120, 93, 110, 98, 105, 88, 115, 102, 97, 108, 94, 112, 100, 96, 104]
config_params = {
    'floor': 0.05,
    'ceiling': 0.95
}

# Execute pipeline
final_diagnostic = main_pipeline(input_data, config_params)
print(f"Result: {final_diagnostic}")