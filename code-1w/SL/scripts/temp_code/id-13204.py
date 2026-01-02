import math

# Simulated sensor data preprocessing with red herrings
def fetch_raw_sensors():
    return [23.4, -1.2, 56.7, 0.0, 99.9, 120.1, 45.6]

def clean_data(raw):
    cleaned = []
    for val in raw:
        if val < 0:
            val = abs(val)
        if val > 100:
            val = 99.9  # cap extreme values
        cleaned.append(round(val + 0.1, 1))  # minor adjustment
    return cleaned

def generate_lookup():
    # Irrelevant mapping table (decoy)
    return {i: chr(65 + (i % 26)) for i in range(50)}

def compute_checksum(data):
    # Unused function - dead path
    return sum(int(x * 10) for x in data) % 1000

def transform_coordinates(values):
    # Distractor: complex but unused coordinate math
    polar = []
    for v in values:
        r = math.sqrt(v * 2)
        theta = math.atan(v / (v + 1e-5))
        polar.append((r, theta))
    return polar

def encode_sequence(seq):
    # Another decoy transformation
    return [bin(int(s))[2:] for s in seq]

def build_hierarchy(data):
    # Complex nested structure that isn't used
    hierarchy = {}
    for i, d in enumerate(data):
        level = i // 3
        if level not in hierarchy:
            hierarchy[level] = []
        hierarchy[level].append(d * 1.5)
    return hierarchy

def filter_outliers(data, limit=95.0):
    # Relevant filtering step
    return [x for x in data if x <= limit]

def aggregate_peaks(signal):
    # Real computation: find local maxima
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks

def calculate_entropy(values):
    # Misleading advanced math
    total = sum(values)
    probs = [(v / total) for v in values]
    return -sum(p * math.log(p) for p in probs if p > 0)

def normalize_readings(arr):
    # Used in final processing
    min_val, max_val = min(arr), max(arr)
    if max_val == min_val:
        return [0.5] * len(arr)
    return [(x - min_val) / (max_val - min_val) for x in arr]

def derive_weights(length):
    # Red herring weights
    return [math.cos(i * 0.5) ** 2 for i in range(length)]

def map_severity(levels):
    # Unused severity logic
    mapping = {}
    for lvl in levels:
        if lvl < 20:
            mapping[lvl] = 'LOW'
        elif lvl < 50:
            mapping[lvl] = 'MEDIUM'
        else:
            mapping[lvl] = 'HIGH'
    return mapping

def extract_features(dataset):
    # Key feature extraction with distractors
    adjusted = [x * 1.02 for x in dataset]
    smoothed = []
    for i in range(len(adjusted)):
        window = adjusted[max(0, i-1):min(i+2, len(adjusted))]
        smoothed.append(sum(window) / len(window))
    return smoothed

def compute_baseline(peaks):
    # Intermediate calculation
    return sum(peaks) / len(peaks) if peaks else 0.0

def evaluate_stability(metric):
    # Irrelevant stability check
    return math.exp(-abs(metric - 50) / 10)

def analyze_metrics(data, config_map):
    # Core analysis logic
    base_score = compute_baseline(data)
    
    # Apply dynamic thresholds from config
    high_t = config_map['critical_threshold']
    mid_t = config_map['warning_threshold']
    
    count_high = len([x for x in data if x > high_t])
    count_mid = len([x for x in data if x > mid_t and x <= high_t])
    
    penalty = 0
    if count_high > 2:
        penalty += 30
    elif count_mid > 4:
        penalty += 15
    
    # Final diagnostic formula
    raw_diagnostic = base_score * 100 - penalty
    return int(round(raw_diagnostic))

# Main execution flow
if __name__ == '__main__':
    # Step 1: Fetch and clean sensor inputs
    raw_sensor_data = fetch_raw_sensors()
    processed_data = clean_data(raw_sensor_data)
    
    # Use list comprehension – required language feature
    processed_data = [x for x in processed_data if x != 0.0]
    
    # Filter outliers (relevant step)
    filtered_data = filter_outliers(processed_data)
    
    # Extract meaningful features
    engineered_features = extract_features(filtered_data)
    
    # Normalize before peak detection
    normalized_signal = normalize_readings(engineered_features)
    
    # Detect significant peaks
    detected_peaks = aggregate_peaks(normalized_signal)
    
    # Build dummy structures (distractors)
    lookup_table = generate_lookup()
    hierarchy_tree = build_hierarchy(normalized_signal)
    encoded_bins = encode_sequence([10, 20, 30])
    coordinate_system = transform_coordinates([1, 2, 3])
    weight_profile = derive_weights(len(normalized_signal))
    entropy_value = calculate_entropy(detected_peaks) if detected_peaks else 0.0
    
    # Create configuration map (used later)
    threshold_map = {
        'warning_threshold': 0.4,
        'critical_threshold': 0.75,
        'hysteresis_window': 0.1
    }
    
    # Analyze using key function
    final_diagnostic = analyze_metrics(detected_peaks, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")