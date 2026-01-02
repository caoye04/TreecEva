import math

# Simulated sensor data processing system for environmental monitoring

def generate_noise(length, seed=42):
    # Irrelevant utility: generates noise not used in main logic
    result = []
    val = seed
    for i in range(length):
        val = (val * 937) % 101
        result.append((val % 100) / 100)
    return result

def deprecated_filter(data):
    # Dead code path - never called
    return [x for x in data if x > 0.5]

def analyze_pattern(seq):
    # Misleading function: looks important but unused
    total_peaks = 0
    for i in range(1, len(seq)-1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            total_peaks += 1
    return total_peaks

def validate_signal(x):
    # Used in list comprehension; checks signal integrity
    return 0.1 <= x <= 0.9

def compute_magnitude(values):
    # Computes RMS magnitude of valid signals
    clean_vals = [v for v in values if validate_signal(v)]
    squared = sum(v ** 2 for v in clean_vals)
    return math.sqrt(squared / len(clean_vals)) if clean_vals else 0.0

def assess_entropy(data):
    # Unused complex distractor: calculates Shannon entropy
    from collections import Counter
    counts = Counter([round(d, 1) for d in data])
    total = len(data)
    entropy = 0.0
    for c in counts.values():
        p = c / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def extract_features(dataset):
    # Extracts multiple features, some irrelevant
    feature_set = {}
    for key, readings in dataset.items():
        # Valid processing branch
        magnitudes = compute_magnitude(readings)
        reading_count = len([r for r in readings if r > 0.25])  # Filtered count
        
        # Red herring computation
        avg_gap = sum(abs(readings[i+1] - readings[i]) for i in range(len(readings)-1)) / (len(readings)-1) if len(readings) > 1 else 0
        
        feature_set[key] = {
            'power': magnitudes,
            'volume': reading_count,
            'gradient': avg_gap  # Not used later
        }
    return feature_set

def evaluate_stability(features_map):
    # Evaluates system stability based on power/volume ratio
    total_score = 0.0
    for node_id, feats in features_map.items():
        if feats['volume'] == 0:
            continue
        efficiency = feats['power'] / feats['volume']
        # Conditional expression used as per requirement
        penalty = 0.1 if efficiency < 0.5 else (0.05 if efficiency < 0.7 else 0)
        total_score += efficiency - penalty
    return total_score

def process_readings(raw_data, threshold):
    # Core logic with critical execution point
    filtered_data = {}
    for k, v in raw_data.items():
        # Only keep readings above validation floor
        filtered_data[k] = [x for x in v if x >= 0.15]
    
    # Extract meaningful features
    features = extract_features(filtered_data)
    
    # Compute aggregate diagnostic score
    base_metric = evaluate_stability(features)
    
    # Decoy transformation (never used)
    inverted_diagnostic = 1.0 / (base_metric + 0.1) if base_metric > 0 else 10.0
    
    # Final decision logic
    adjustment_factor = 1.25 if base_metric > threshold else 0.8
    final_diagnostic = base_metric * adjustment_factor
    
    # Critical assignment point
    return final_diagnostic

# Simulated input data from sensors
collected_data = {
    'sensor_A1': [0.12, 0.35, 0.67, 0.81, 0.24, 0.93, 0.11],
    'sensor_B2': [0.08, 0.43, 0.51, 0.72, 0.66, 0.88, 0.34, 0.77],
    'sensor_C3': [0.55, 0.61, 0.59, 0.09, 0.63, 0.68],
    'sensor_D4': [0.26, 0.21, 0.19, 0.33, 0.71, 0.82, 0.29]
}

# Irrelevant preprocessing (distractor)
data_buffer = []
for arr in collected_data.values():
    data_buffer.extend(arr)
sorted_buffer = sorted(data_buffer)
median_val = sorted_buffer[len(sorted_buffer)//2]

# Unused statistical summary
summary_stats = {
    'mean': sum(data_buffer)/len(data_buffer),
    'max': max(data_buffer),
    'min': min(data_buffer)
}

# Key statement
final_diagnostic = process_readings(collected_data, threshold=0.75)

# Output result
print(f"Result: {final_diagnostic}")