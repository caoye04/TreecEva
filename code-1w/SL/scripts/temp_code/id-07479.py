from collections import defaultdict
import math

# Simulated sensor array data (irrelevant for final result but adds distraction)
sensor_readings = [14, 18, 22, 19, 31, 42, 25, 21, 17, 13]
noise_floor = 12
calibration_offset = 3.7

def apply_filter(data, method='moving_avg'):
    # Irrelevant filtering function (dead path)
    return [x + calibration_offset for x in data]

def generate_checksum(sequence):
    # Distractor: used nowhere in critical path
    return sum(x ^ (i * 2) for i, x in enumerate(sequence)) % 100

def extract_peaks(signal, min_magnitude=20):
    # Extracts high values — partially relevant but misleading
    peaks = []
    for i, val in enumerate(signal):
        if val > min_magnitude:
            peaks.append((i, val))
    return peaks

def transform_coordinates(peaks):
    # Dead code path — distracts with coordinate math
    return [(math.sin(i * 0.1), math.log(v + 1)) for i, v in peaks]

def compute_entropy(data):
    # Red herring: entropy sounds important but unused
    freq = defaultdict(int)
    for x in data:
        freq[x // 5] += 1
    total = len(data)
    return -sum((count / total) * math.log(count / total) for count in freq.values())

def preprocess_signal(raw):
    # Main preprocessing — relevant
    shifted = [x - noise_floor for x in raw]
    normalized = [x / 10.0 for x in shifted]
    return [round(x, 2) for x in normalized]

def build_threshold_map(config_level):
    # Creates a nested structure — partially relevant
    base_map = {'low': 0.6, 'mid': 1.2, 'high': config_level * 0.3}
    extended = defaultdict(lambda: 0.0)
    for k, v in base_map.items():
        extended[k] = v + 0.1
    extended['critical'] = base_map['high'] + 0.5
    return extended

def evaluate_stability(measurements):
    # Complex but irrelevant stability analysis
    diffs = [abs(a - b) for a, b in zip(measurements, measurements[1:])]
    return sum(diffs) < 5.0

def analyze_signal(clean_data, thresholds):
    # Critical function: computes final diagnostic score
    score = 0
    for val in clean_data:
        if val > thresholds['high']:
            score += int(val * 10)
        elif val > thresholds['mid']:
            score += int(val * 5)
        elif val > thresholds['low']:
            score += int(val * 2)
    adjustment = len([v for v in clean_data if v > thresholds['low']])
    score -= adjustment * 3
    
    # Decoy logic that looks like it modifies score but doesn't execute
    if score > 1000:
        secondary_analysis = [math.exp(-x) for x in clean_data]
        score = int(sum(secondary_analysis) * 100)
    
    # Final adjustment based on pattern matching (relevant)
    pattern_match = all(clean_data[i] <= clean_data[i+1] for i in range(len(clean_data)-1))
    bonus = 25 if pattern_match else -15
    
    return score + bonus

# Begin main execution flow
raw_sensor_data = [25, 28, 33, 36, 40, 44]  # Input sequence with rising trend

# Irrelevant transformations
filtered_data = apply_filter(raw_sensor_data)
checksum = generate_checksum(filtered_data)
data_entropy = compute_entropy(filtered_data)

# Relevant preprocessing
processed_data = preprocess_signal(raw_sensor_data)

# Build configuration map — relevant
threshold_map = build_threshold_map(config_level=8)

# Evaluate signal stability — distractor call
stability_flag = evaluate_stability(processed_data)

# Extract and transform peaks — dead-end computation
detected_peaks = extract_peaks(raw_sensor_data, min_magnitude=28)
spatial_rep = transform_coordinates(detected_peaks)

# Critical statement: produces the target result
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")