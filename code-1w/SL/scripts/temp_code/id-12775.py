from collections import defaultdict, Counter
import math

# Simulated patient health monitoring system with diagnostic logic
def preprocess_readings(raw_readings):
    processed = []
    noise_floor = 0.05
    for val in raw_readings:
        if abs(val) > noise_floor:
            processed.append(round(val * 1000))
    return processed

# Irrelevant signal processing decoy
def smooth_signal(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window // 2)
        end = min(len(data), i + window // 2 + 1)
        smoothed.append(sum(data[start:end]) / (end - start))
    return smoothed

# Distractor: unused normalization function
def normalize_range(values, low=-1, high=1):
    min_val, max_val = min(values), max(values)
    if max_val == min_val:
        return [0 for _ in values]
    return [(v - min_val) / (max_val - min_val) * (high - low) + low for v in values]

# Core analysis function with embedded logic chain
def compute_rolling_stat(data, window_size=4):
    if len(data) < window_size:
        return [0]
    stats = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i+window_size]
        mean = sum(window) / len(window)
        variance = sum((x - mean) ** 2 for x in window) / len(window)
        stats.append(round(math.sqrt(variance)))
    return stats

# Secondary metric calculator (partially relevant)
def extract_frequency_patterns(seq):
    freq_map = defaultdict(int)
    for item in seq:
        freq_map[item] += 1
    counter = Counter(freq_map)
    return counter.most_common(3)

# Main diagnostic engine
def analyze_metrics(sensor_stream, limit_config):
    # Step 1: Preprocess raw physiological signals
    cleaned = preprocess_readings(sensor_stream)
    
    # Distractor: irrelevant feature extraction
    spectral_features = []
    for i, x in enumerate(cleaned):
        if i % 5 == 0:
            spectral_features.append(x * math.sin(i + 0.1))
    
    # Step 2: Compute stability metrics (key path)
    variability = compute_rolling_stat(cleaned, 5)
    
    # Step 3: Filter based on dynamic threshold (critical step)
    dynamic_threshold = limit_config.get('baseline') * limit_config.get('multiplier')
    stable_periods = [v for v in variability if v < dynamic_threshold]
    
    # Distractor: unused pattern analysis
    patterns = extract_frequency_patterns(cleaned)
    pattern_score = 0
    for p, count in patterns:
        if count > 1:
            pattern_score += abs(p) // 100
    
    # Step 4: Accumulate diagnostic weight (key logic)
    anomaly_count = 0
    cumulative_drift = 0
    for i, val in enumerate(cleaned):
        if i > 0 and abs(val - cleaned[i-1]) > 200:
            anomaly_count += 1
        if val > 300:
            cumulative_drift += val // 50
    
    # Step 5: Apply multi-factor decision rule
    base_risk = len(stable_periods) * 3
    adjustment = anomaly_count * 2 - cumulative_drift
    
    # Step 6: Final computation with distractor variables
    debug_info = {
        'raw_count': len(sensor_stream),
        'cleaned_len': len(cleaned),
        'peaks': sum(1 for x in cleaned if x > 400),
        'noise_ratio': len(spectral_features) / len(cleaned) if cleaned else 0
    }
    
    # Critical assignment: this is the answer
    final_diagnostic = base_risk + adjustment + pattern_score
    
    # Dead code path (never executed)
    if False:
        fallback = sum(debug_info.values())
        final_diagnostic = fallback if fallback > 0 else 1
    
    return final_diagnostic

# Simulated input data
readings_log = [
    0.012, 0.018, 0.021, 0.019, 0.023, 0.031, 0.042, 0.058, 0.071, 0.083,
    0.092, 0.105, 0.118, 0.132, 0.141, 0.152, 0.168, 0.181, 0.192, 0.205,
    0.218, 0.232, 0.241, 0.258, 0.269, 0.281, 0.292, 0.305, 0.318, 0.332
]

thresholds = {
    'baseline': 15,
    'multiplier': 2.0,
    'emergency': 50
}

# Execute main analysis
final_diagnostic = analyze_metrics(readings_log, thresholds)
print(f"Target result: {final_diagnostic}")