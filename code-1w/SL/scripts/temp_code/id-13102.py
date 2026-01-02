from collections import defaultdict, Counter

# Simulated sensor fusion and diagnostic system
def analyze_pattern(seq):
    if len(seq) < 3:
        return 0
    count = 0
    for i in range(len(seq) - 2):
        if seq[i] < seq[i+1] > seq[i+2]:  # Peak detection
            count += 1
    return count

def normalize(value, min_val, max_val):
    # Irrelevant normalization function (not used in final path)
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0

def calculate_entropy(data):
    # Dead code path — looks important but unused
    freqs = Counter(data)
    total = len(data)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, just decoy
    return round(entropy, 4)

def filter_outliers(values, limit=3):
    # Distractor: modifies list but result not used
    upper = sum(values) / len(values) + limit
    filtered = [v for v in values if v <= upper]
    return filtered

def accumulate_diagnostics(logs):
    # Complex-looking but ultimately irrelevant accumulation
    stats = defaultdict(int)
    for entry in logs:
        stats['total'] += 1
        if entry % 7 == 0:
            stats['special'] += 1
        elif entry > 50:
            stats['high'] += 1
    return dict(stats)

def evaluate_stability(ratio):
    # Unused evaluation branch
    if ratio < 0.1:
        return 'UNSTABLE'
    elif ratio < 0.5:
        return 'CAUTION'
    else:
        return 'STABLE'

def process_readings(data, config):
    # Core logic buried under distractions
    baseline = config.get('base', 10)
    factor = config.get('multiplier', 3)
    offset = 0
    temp_result = []
    
    for val in data:
        adjusted = val - baseline
        if adjusted > 5:
            offset += 1
            adjusted = adjusted // 2  # Integer division
        temp_result.append(adjusted)
    
    # Key transformation
    transformed = [t ** 2 for t in temp_result if t > 0]
    
    # Real usage of Counter
    freq_map = Counter(transformed)
    mode_value = max(freq_map, key=freq_map.get)
    
    # Actual answer derivation
    checksum = 0
    for k, v in freq_map.items():
        checksum += k % 7 * (v % 3)
    
    # Critical intermediate state
    threshold_met = [k for k, v in freq_map.items() if v >= 2 and k > 5]
    if threshold_met:
        checksum *= 2
    
    # Final computation
    adjustment_factor = len(threshold_met) + config.get('offset', 1)
    final_score = checksum * adjustment_factor
    
    # Red herring: complex string operation with no effect
    status_str = ''.join([chr(97 + (final_score % 26)) for _ in range(3)])
    
    # This is the actual target variable
    final_diagnostic = final_score + analyze_pattern(temp_result)
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Input data
    sensor_data = [12, 15, 13, 22, 11, 25, 22, 18, 15, 28]
    
    # Configuration map with decoy keys
    thresholds = {
        'base': 10,
        'multiplier': 3,
        'offset': 2,
        'sensitivity': 0.85,
        'calibration': [1, 1, 2],
        'window_size': 5
    }
    
    # Unused variables to increase interference
    diagnostics_log = [201, 103, 405, 201, 103, 607, 201]
    outlier_set = filter_outliers(sensor_data, limit=5)
    entropy_value = calculate_entropy(sensor_data)
    pattern_count = accumulate_diagnostics(diagnostics_log)
    
    # Execution point of interest
    final_diagnostic = process_readings(sensor_data, thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")