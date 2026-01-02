from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic analysis
def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

def generate_checksum(sequence):
    # Irrelevant checksum for distraction
    return sum((i + val) * 2 for i, val in enumerate(sequence)) % 1000

def evaluate_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(i)
    return len(peaks) > 3

def build_threshold_map(config_level):
    # Creates mapping of thresholds across frequency bands
    base_map = defaultdict(float)
    for band in ['low', 'mid', 'high']:
        base_map[band] = config_level * (0.5 if band == 'low' else 0.8 if band == 'mid' else 1.2)
    return base_map

def extract_moment_features(data):
    # Statistical moments (distraction: not used in final result)
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val)**2 for x in data) / len(data)
    skewness = sum((x - mean_val)**3 for x in data) / (len(data) * variance**1.5)
    return {'mean': mean_val, 'variance': variance, 'skew': round(skewness, 4)}

def slice_and_aggregate(temporal_data, window_size=4):
    # Overlapping window slicing
    slices = [temporal_data[i:i+window_size] for i in range(0, len(temporal_data)-2, 2)]
    aggregated = [round(sum(window)/len(window), 3) for window in slices]
    return aggregated

def analyze_signal(cleaned_signal, thresholds):
    # Core logic hidden among distractions
    segment_sums = [sum(cleaned_signal[i:i+3]) for i in range(0, len(cleaned_signal), 3)]
    
    # Distractor: unused conditional branch
    if len(segment_sums) < 5:
        fallback = 0
        for x in cleaned_signal:
            if x > thresholds['mid']:
                fallback += int(x * 10)
        return fallback
    
    # Real computation path
    high_activity = [s for s in segment_sums if s > thresholds['high']]
    mid_activity = [s for s in segment_sums if thresholds['mid'] < s <= thresholds['high']]
    
    score_map = Counter({'high': len(high_activity), 'mid': len(mid_activity)})
    
    # Critical computation: weighted diagnostic score
    diagnostic_score = 0
    diagnostic_score += score_map['high'] * 17
    diagnostic_score += score_map['mid'] * 7
    diagnostic_score -= len([x for x in cleaned_signal if x < -0.6]) * 5
    
    # Dead code path (never reached due to above logic)
    redundant_check = None
    if diagnostic_score > 100:
        temp_state = [int(s*10) for s in cleaned_signal if s > 0]
        redundant_check = sum((s % 3) for s in temp_state)
    
    return diagnostic_score

# --- Main execution with red herrings ---
raw_sensor_data = [
    0.05, -0.12, 0.34, 0.67, 0.23, -0.45, 0.89, 0.12, -0.08, 0.56,
    0.78, -0.21, 0.91, 0.33, 0.64, -0.52, 0.77, 0.88, 0.41, -0.19
]

# Irrelevant preprocessing steps
checksum_value = generate_checksum(raw_sensor_data)  # distractor
feature_stats = extract_moment_features(raw_sensor_data)  # unused stats

# Actual relevant pipeline
processed_data = preprocess_signal(raw_sensor_data)
sliced_segments = slice_and_aggregate(processed_data)  # computed but not used later

config_level = 0.65
threshold_map = build_threshold_map(config_level)

# Key statement containing the target variable
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Secondary distractor function call
peak_analysis_result = evaluate_peaks(processed_data)

# Print required output
print(f"Result: {final_diagnostic}")