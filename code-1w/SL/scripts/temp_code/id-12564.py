import math

def analyze_phase_shift(signal, baseline):
    # Irrelevant signal processing function (dead code path)
    magnitude = sum([abs(s - baseline) for s in signal])
    normalized = magnitude / len(signal) if signal else 0
    return math.sin(normalized)  # Unused result

def validate_sequence(seq):
    # Misleading validation with side computation
    if not seq:
        return False
    checksum = 0
    for i, val in enumerate(seq):
        checksum ^= (val + i) * 3
    return checksum % 7 == 0  # Not actually used in main logic

def compute_entropy(values):
    # Distractor: computes information-theoretic entropy (not used)
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def extract_features(dataset):
    # Real but obfuscated feature extraction
    temp_data = [x for x in dataset if x > 0]  # Filter positives
    shift = len(temp_data) // 2
    adjusted = [temp_data[i] - temp_data[i - shift] for i in range(shift, len(temp_data))]
    return adjusted

def evaluate_stability(readings):
    # Computes stability index using variance-like measure
    if len(readings) < 2:
        return 0.0
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    return round(math.sqrt(variance), 5)

def process_metrics(log, thresh):
    # Core logic embedded in noise
    
    # Irrelevant preprocessing
    filtered_log = [x for x in log if x % 2 == 1]  # Keep only odds (unused later)
    offset = sum(filtered_log[:3]) if len(filtered_log) >= 3 else 0
    
    # Real data pipeline starts here
    primary_stream = [x for x in log if x > thresh]
    derived_values = extract_features(primary_stream)
    
    # Conditional expression (required Python feature)
    scaling_factor = 1.75 if len(derived_values) > 5 else 2.25
    
    # Actual efficiency calculation
    raw_sum = sum(derived_values)
    penalty = len([v for v in derived_values if v < 0]) * 0.5
    efficiency_score = (raw_sum - penalty) * scaling_factor
    
    # Dead code: fake aggregation
    summary_stats = {
        'peak': max(primary_stream, default=0),
        'base': min(primary_stream, default=0),
        'count': len(primary_stream)
    }
    
    # Unused intermediate
    _ = evaluate_stability(primary_stream)
    
    # Final assignment
    final_output = efficiency_score  # This captures the real answer
    
    # Print required output format
    print(f"Result: {final_output}")
    return final_output

# Simulated sensor data log (real input)
data_log = [12, -5, 8, 23, 17, 4, 19, 21, 34, 27, 11, 6, 38, 33, 29, 14, 22, 16, 10, 3]
threshold = 15

# Call that triggers the key statement
final_output = process_metrics(data_log, threshold)