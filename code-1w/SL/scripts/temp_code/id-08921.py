from collections import defaultdict, Counter
import math

# Simulated sensor data acquisition (irrelevant preprocessing)
def acquire_signal(raw=False):
    base_samples = [0.1, 0.3, 0.4, 0.7, 0.9, 1.2, 1.5, 1.8, 2.0]
    if raw:
        return [x * 10 for x in base_samples]
    return [math.sin(x) + 0.1 * x for x in base_samples]

# Irrelevant noise injection function (dead code path)
def inject_noise(signal, level=0.05):
    return [s + random.uniform(-level, level) for s in signal]

# Data normalization (partially relevant but overcomplicated)
def normalize_segment(segment, method='z-score'):
    mean_val = sum(segment) / len(segment)
    if method == 'z-score':
        variance = sum((x - mean_val) ** 2 for x in segment) / len(segment)
        std_dev = math.sqrt(variance)
        return [(x - mean_val) / std_dev for x in segment] if std_dev != 0 else segment
    elif method == 'min-max':
        min_val, max_val = min(segment), max(segment)
        return [(x - min_val) / (max_val - min_val) for x in segment] if max_val != min_val else segment
    return segment

# Feature extraction with red herring features
def extract_features(data):
    features = defaultdict(float)
    n = len(data)
    
    # Relevant feature
    features['peak_count'] = sum(1 for i in range(1, n-1) if data[i-1] < data[i] > data[i+1])
    
    # Distractor features
    features['avg_square'] = sum(x**2 for x in data) / n
    features['skew_proxy'] = (max(data) - min(data)) / (sum(data) / n) if sum(data) != 0 else 0
    features['entropy_like'] = -sum(p * math.log(abs(p)+1e-9) for p in data[:5])  # nonsense
    
    # Another decoy
    counter = Counter([int(abs(x)*10) % 4 for x in data])
    features['mode_freq'] = counter.most_common(1)[0][1] if counter else 0
    
    return features

# Signal conditioning with slicing distraction
def preprocess_signal(raw_signal):
    # Truncate beginning/end (slicing red herring)
    trimmed = raw_signal[2:-2] if len(raw_signal) > 4 else raw_signal
    extended = trimmed + [trimmed[-1]] * (4 - len(trimmed)) if len(trimmed) < 4 else trimmed
    
    # Normalize using irrelevant method
    normalized = normalize_segment(extended, method='z-score')
    
    # More distraction: conditional expression with no real impact
    backup_fill = [0.0] * (5 - len(normalized)) if len(normalized) < 5 else []
    padded = normalized + (backup_fill if len(backup_fill) > 0 else [])
    
    # Final processing that actually matters
    filtered = [x for x in padded if abs(x) > 0.1]  # key filtering
    return filtered if len(filtered) >= 3 else [0.0, 0.0, 0.0]

# Core analysis logic (deceptively simple)
def analyze_signal(processed):
    # Extract meaningful statistics
    length_valid = len(processed)
    sum_positive = sum(x for x in processed if x > 0)
    sum_negative = sum(x for x in processed if x < 0)
    net_bias = sum_positive + sum_negative
    
    # Compute diagnostic score
    peak_focus = length_valid * net_bias
    
    # Hidden key logic: count sign changes (critical step)
    sign_changes = 0
    for i in range(1, len(processed)):
        if (processed[i-1] > 0) != (processed[i] > 0) and processed[i] != 0:
            sign_changes += 1
    
    # Final computation: combines multiple concepts
    diagnostic_raw = (peak_focus * 10) + (sign_changes * 100)
    
    # Distractor: unused complex transformation
    transformed = [math.atan(x) * math.log(abs(x) + 1) for x in processed]
    entropy_metric = -sum(p * math.log(abs(p) + 1e-6) for p in transformed) if transformed else 0
    
    # Actual answer determination
    final_diagnostic = int(diagnostic_raw + 0.5)  # round to nearest integer
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Generate initial signal
    raw_input_data = acquire_signal(raw=False)
    
    # Preprocess (with distractions)
    temp_debug = [x * 2 for x in raw_input_data]  # irrelevant debugging artifact
    processed_data = preprocess_signal(raw_input_data)
    
    # Feature extraction (side computation, not used later)
    extracted_features = extract_features(processed_data)
    feature_dump = dict(extracted_features)  # dead storage
    
    # Critical execution point
    final_diagnostic = analyze_signal(processed_data)
    
    # Output result
    print(f"Result: {final_diagnostic}")