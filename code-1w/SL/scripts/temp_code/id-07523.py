import math

# Simulated sensor data processing with noise filtering and signal extraction
def collect_sensor_data():
    raw_data = [i * 0.5 + (i % 7) for i in range(30)]
    noise_mask = [math.sin(i * 0.3) for i in range(30)]
    return [raw_data[i] + noise_mask[i] for i in range(30)]

def apply_calibration(signal):
    calibrated = []
    offset = 2.3
    gain = 1.8
    for val in signal:
        corrected = (val + offset) * gain
        calibrated.append(round(corrected, 6))
    # Distractor: unused transformation path
    inverted = [1.0 / (x + 1e-5) for x in calibrated]
    normalized = [x / max(calibrated) for x in calibrated]  # Not used
    return calibrated

def identify_peaks(data):
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append((i, data[i]))
    return peaks

def compute_entropy(values):
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 6)

def roughness_metric(seq):
    diffs = [abs(seq[i+1] - seq[i]) for i in range(len(seq)-1)]
    return sum(diffs) / len(diffs)

def filter_outliers(data, threshold=1.5):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val)**2 for x in data) / len(data))**0.5
    return [x for x in data if abs(x - mean_val) <= threshold * std_dev], std_dev

# Irrelevant helper function (dead code path)
def deprecated_smoothing(arr):
    smoothed = [arr[0]]
    for i in range(1, len(arr)-1):
        avg = (arr[i-1] + arr[i] + arr[i+1]) / 3
        smoothed.append(avg)
    smoothed.append(arr[-1])
    return smoothed

def analyze_pattern(sequence):
    pattern_score = 0
    for i, val in enumerate(sequence):
        if i % 3 == 0 and val > 5:
            pattern_score += 1.5
        elif i % 4 == 0 and val < 3:
            pattern_score -= 0.7
    # Decoy computation
    dummy_sum = sum(math.cos(i * 0.1) for i in range(len(sequence)))
    return round(pattern_score, 6)

def extract_features(dataset):
    feature_set = {}
    feature_set['count'] = len(dataset)
    feature_set['average'] = sum(dataset) / len(dataset)
    feature_set['max_val'] = max(dataset)
    feature_set['min_val'] = min(dataset)
    feature_set['range'] = feature_set['max_val'] - feature_set['min_val']
    
    # Real feature used later
    feature_set['midpoint'] = (feature_set['max_val'] + feature_set['min_val']) / 2
    
    # Distractor features
    feature_set['skew_hint'] = (feature_set['average'] > feature_set['midpoint'])
    feature_set['peak_density'] = len([x for x in dataset if x > feature_set['average']]) / len(dataset)
    
    return feature_set

def process_signals(data_list):
    # Main logic chain begins here
    features = extract_features(data_list)
    base_reference = features['midpoint']
    
    # Secondary transformation
    adjusted = [x - base_reference for x in data_list]
    
    # Use enumerate and zip as required
    indexed = list(enumerate(adjusted))
    shifted = [x[1] * 0.9 for x in indexed]
    paired = list(zip(adjusted, shifted))
    
    # Core calculation
    cumulative = 0
    for orig, adj in paired:
        if orig > 0:
            cumulative += math.sqrt(abs(orig * adj))

    # Tertiary adjustment based on entropy
    valid_vals = [x for x in data_list if x > 0]
    entropy = compute_entropy(valid_vals)
    cumulative = cumulative * (1 + entropy * 0.1)

    # Final manipulation
    final_result = int(cumulative + 0.5)  # Round to nearest integer
    
    # Dead branch - misleading
    if len(data_list) > 100:
        final_result *= 2
    
    return final_result

# Irrelevant global computation
aux_data = [i**2 for i in range(10)]
shadow_copy = aux_data[:]
processed_aux = [math.sqrt(x) for x in shadow_copy if x > 0]

# Main execution flow
sensor_stream = collect_sensor_data()
calibrated_signal = apply_calibration(sensor_stream)
filtered_data, dev_info = filter_outliers(calibrated_signal, threshold=1.8)

# Additional distractions
peak_locations = identify_peaks(filtered_data)
analysis_score = analyze_pattern(filtered_data)
roughness = roughness_metric(filtered_data)

# Key statement
final_output = process_signals(filtered_data)

# Print result as required
print(f"Result: {final_output}")