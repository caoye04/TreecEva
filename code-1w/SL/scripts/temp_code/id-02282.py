import itertools

# Simulated sensor data preprocessing pipeline
raw_readings = [145, 176, 201, 189, 255, 301, 288, 320]
dummy_offsets = [12, -5, 8, 0, -3]
scaling_factor = 0.78
adjustment_map = {i: val * 0.1 for i, val in enumerate([10, 15, 7, 12, 9])}

# Irrelevant transformation chain (dead path)
def deprecated_normalize(x):
    return (x - min(x)) / (max(x) - min(x))

def transform_signal(data, factor):
    return [round(d * factor + 2) for d in data if d > 150]

# Unused helper with misleading purpose
def compute_entropy(seq):
    from math import log
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    return -sum(f * log(f) for f in freq.values())

# Decoy function that looks important but isn't used
def analyze_pattern(sequence):
    trends = []
    for i in range(1, len(sequence)):
        trends.append(1 if sequence[i] > sequence[i-1] else -1)
    return sum(trends)

# Real processing begins here
filtered_readings = [r for r in raw_readings if r < 300]
scaled_values = [v * scaling_factor for v in filtered_readings]

# Generate auxiliary metadata (partially relevant)
index_pairs = list(itertools.combinations(range(len(scaled_values)), 2))
valid_pairs = [(i, j) for i, j in index_pairs if abs(scaled_values[i] - scaled_values[j]) > 20]
pair_count_metric = len(valid_pairs)

# Mock calibration routine (distractor)
calibration_log = []
for i in range(3):
    temp_adj = sum(dummy_offsets[:i+1]) * adjustment_map.get(i, 1)
    calibration_log.append(temp_adj)

def extract_features(signal):
    avg = sum(signal) / len(signal)
    peaks = [s for s in signal if s > avg * 1.2]
    troughs = [s for s in signal if s < avg * 0.8]
    return {
        'mean': avg,
        'peak_count': len(peaks),
        'trough_count': len(troughs),
        'amplitude': max(signal) - min(signal)
    }

def validate_thresholds(metrics, limits):
    issues = 0
    for key, limit in limits.items():
        if key in metrics and metrics[key] > limit:
            issues += 1
    return issues == 0

# Actual core logic hidden among noise
def process_metrics(data, bounds):
    features = extract_features(data)
    
    # Irrelevant intermediate calculation
    dummy_sequence = [features['mean'] * 2, features['amplitude'] / 3]
    shadow_value = sum([int(x) % 7 for x in dummy_sequence])
    
    # Critical computation buried in logic
    base_score = features['mean'] * 10
    penalty = 0
    if features['peak_count'] > 2:
        penalty += features['peak_count'] * 5
    if features['trough_count'] > 1:
        penalty += 10
    
    # Key result computed here
    diagnostic_score = int(base_score - penalty)
    
    # More red herrings
    decoy_map = {k: v * shadow_value for k, v in features.items()}
    fallback = sum(decoy_map.values()) / 100
    
    # Final output determined solely by diagnostic_score
    return diagnostic_score

# Threshold configuration (only partially used)
thresholds = {
    'mean': 150.0,
    'peak_count': 3,
    'amplitude': 120.0
}

# Unused data structures to increase interference
auxiliary_cache = {}
for idx, val in enumerate(scaled_values):
    auxiliary_cache[f"sample_{idx}"] = {
        'raw': raw_readings[idx] if idx < len(raw_readings) else 0,
        'scaled': val,
        'adjusted': val + calibration_log[idx % 3] if calibration_log else 0
    }

# Core execution path
health_data = scaled_values
final_diagnostic = process_metrics(health_data, thresholds)

# Output requirement
print(f"Target result: {final_diagnostic}")