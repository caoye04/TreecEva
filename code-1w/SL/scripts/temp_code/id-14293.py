import itertools

def analyze_readings(readings):
    # Irrelevant transformation: normalize readings (not used in final path)
    normalized = [r / max(readings) for r in readings]
    smoothed = list(map(lambda x: round(x, 2), normalized))

    # Distractor: frequency analysis with no impact
    freq_count = {}
    for val in readings:
        freq_count[val] = freq_count.get(val, 0) + 1

    # Real computation: compute weighted trend (used later)
    weights = [0.1, 0.2, 0.3, 0.4]
    trend = sum(readings[i] * weights[i] for i in range(len(weights)))
    return trend

def validate_signal(data):
    # Decoy function: processes signal but is never called
    if not data:
        return False
    checksum = 0
    for d in data:
        checksum ^= d
    return checksum % 2 == 0

def decode_pattern(seq):
    # Dead code path: string manipulation red herring
    seq_str = ''.join(map(str, seq))
    flipped = seq_str.translate(str.maketrans('01', '10'))
    chunks = [flipped[i:i+3] for i in range(0, len(flipped), 3)]
    filtered = [c for c in chunks if '1' in c]
    return len(filtered)

def evaluate_stability(metrics):
    # Complex distractor: nested loops and early returns
    baseline = metrics.get('base', 0)
    samples = metrics.get('values', [])
    
    if len(samples) < 5:
        return -999

    adjustments = []
    for i, val in enumerate(samples):
        diff = val - baseline
n        if diff > 10:
            adjustments.append((i, diff * 0.8))
        elif diff < -10:
            adjustments.append((i, diff * 1.2))
    
    # Misleading intermediate result
    total_adjustment = sum(a[1] for a in adjustments) if adjustments else 0.0

    # Actual logic buried here: peak deviation
    peak_dev = max(abs(s - baseline) for s in samples)
    return peak_dev

def process_metrics(data, limits):
    # Key logic hidden among distractions
    
    # Irrelevant unpacking and reassignment
    temp_data, pressure_data, heart_data = [], [], []
    for k, v in data.items():
        if 'temp' in k:
            temp_data.extend(v)
        elif 'pressure' in k:
            pressure_data.extend(v)
        elif 'heart' in k:
            heart_data.extend(v)
    
    # Distractor: unused itertools combinations
    pairs = list(itertools.combinations([1, 2, 3], 2))
    pair_sums = [sum(p) for p in pairs]

    # Real processing begins
    rhythm_trend = analyze_readings(heart_data)  # uses lambda and map indirectly
    
    # Simulated diagnostic score
    metric_summary = {
        'base': 72,
        'values': heart_data
    }
    
    stability_score = evaluate_stability(metric_summary)
    
    # Conditional override red herring
    if stability_score > 15:
        adjustment_factor = 0.9
    else:
        adjustment_factor = 1.1  # This branch taken
    
    # Core calculation (answer derived here)
    raw_index = rhythm_trend * 2.5
    adjusted_index = raw_index * adjustment_factor
    
    # Final mapping using threshold
    threshold = limits['critical']
    if adjusted_index > threshold:
        risk_level = 3
    elif adjusted_index > threshold * 0.7:
        risk_level = 2
    else:
        risk_level = 1
    
    # Critical answer variable
    final_diagnostic = int(adjusted_index) + risk_level
    
    # Never reached code (dead path)
    if False:
        fallback = decode_pattern([1,0,1,1])
        final_diagnostic -= fallback
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Input data
    health_data = {
        'temp_sensor_a': [36.5, 36.7, 36.6],
        'temp_sensor_b': [36.8, 36.9],
        'pressure_sys': [120, 118, 122],
        'pressure_dia': [80, 78, 82],
        'heart_rate_primary': [72, 75, 78, 85],
        'heart_rate_backup': [73, 74, 77, 86]
    }
    
    thresholds = {
        'warning': 180,
        'critical': 190
    }
    
    # Key execution point
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Output result
    print(f"Target result: {final_diagnostic}")