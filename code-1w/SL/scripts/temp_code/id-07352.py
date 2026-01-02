import math

def preprocess_readings(readings):
    # Irrelevant preprocessing: normalizes values but not used in final path
    return [round((x - min(readings)) / (max(readings) - min(readings)) * 100, 2) for x in readings]

def compute_entropy(data):
    # Distractor function: computes entropy but unused
    total = sum(data)
    entropy = 0
    for x in data:
        p = x / total if total else 0
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 4)

def filter_outliers(seq, limit=3):
    # Dead code path: never called with meaningful data
    mean = sum(seq) / len(seq)
    return [x for x in seq if abs(x - mean) <= limit]

def validate_signal_integrity(signal):
    # Misleading intermediate: looks important but irrelevant
    checksum = 0
    for i, val in enumerate(signal):
        checksum ^= int(val) ^ i
    return checksum % 17 == 0

def rolling_window_avg(values, w=3):
    # Unused transformation
    if len(values) < w:
        return []
    return [sum(values[i:i+w]) / w for i in range(len(values) - w + 1)]

def analyze_metrics(data, config):
    # Core logic hidden among distractions
    
    # Irrelevant block: creates decoy variables
    temp_snapshot = [x * 1.05 for x in data['temperatures']]
    baseline_shift = max(temp_snapshot) - min(temp_snapshot)
    adjusted_phase = math.sin(baseline_shift) * 100
    
    # Real computation begins
    raw_values = data['metrics']['primary']
    scaling_factor = config['scale']
    offset = config.get('offset', 0)
    
    # Actual transformation chain
    scaled = [x * scaling_factor for x in raw_values]
    shifted = [x + offset for x in scaled]
    squared = [x ** 2 for x in shifted if x > -50]  # Conditional filtering matters
    
    # Critical aggregation
    cumulative_score = 0
    for i, val in enumerate(squared):
        if i % 2 == 0:
            cumulative_score += val // (i + 1)
        else:
            cumulative_score -= val % 7
    
    # Decoy intermediate that looks like final result
    preliminary_diag = int(cumulative_score * 0.95)
    
    # Additional red herring: bit manipulation not affecting output
    packed = 0
    for x in squared[-3:]:
        packed = (packed << 5) ^ int(x)
    masked_result = packed & 0xFFFFF
    
    # Final relevant operation
    final_diagnostic = abs(cumulative_score) + 17
    
    # Output required format
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated health monitoring data (realistic domain context)
health_data = {
    'device': 'sensor_v4',
    'timestamp': 1735692000,
    'temperatures': [36.5, 37.1, 38.2, 37.8, 36.9],
    'metrics': {
        'primary': [4.3, -2.1, 8.7, 5.5, -1.3, 9.9, 6.4],  # core input
        'secondary': [0.8, 0.92, 0.88]
    },
    'aux_data': [[1,2],[3,4],[5,6]]
}

# Configuration with misleading keys
thresholds = {
    'scale': 3,
    'offset': -4,
    'critical': 9.5,
    'tolerance_window': [0.1, 0.3, 0.4],
    'mode': 'aggressive'
}

# Trigger execution
final_diagnostic = analyze_metrics(health_data, thresholds)