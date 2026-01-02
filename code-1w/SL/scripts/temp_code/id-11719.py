from collections import defaultdict, Counter

# Simulated sensor network data with noise and redundant channels
def collect_sensor_data():
    raw_streams = {
        'temp_a': [23.4, 24.1, 25.0, 26.5, 27.3],
        'temp_b': [23.2, 24.3, 24.9, 26.7, 27.1],
        'pressure_x': [101.2, 103.5, 105.1, 106.3, 108.0],
        'humidity_1': [45, 47, 50, 52, 55],
        'flow_rate_z': [1.2, 1.5, 1.3, 1.6, 1.7]
    }

    # Inject meaningless derived values to distract
    temp_deriv = [(raw_streams['temp_a'][i] + raw_streams['temp_b'][i]) / 2 
                  for i in range(len(raw_streams['temp_a']))]
    pressure_deriv = [p * 1000 for p in raw_streams['pressure_x']]

    return raw_streams, temp_deriv, pressure_deriv


def apply_calibration(data_stream, factor=1.02, offset=-0.5):
    # Over-engineered calibration with unused branches
    if isinstance(data_stream, list):
        calibrated = [round(x * factor + offset, 3) for x in data_stream]
        return calibrated
    return []


def analyze_pattern(sequence):
    # Complex but irrelevant pattern analyzer (dead path)
    trends = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trends.append('up')
        elif sequence[i] < sequence[i-1]:
            trends.append('down')
        else:
            trends.append('stable')
    trend_count = Counter(trends)
    return trend_count.get('up', 0) - trend_count.get('down', 0)


def compute_entropy(values):
    # Distractor function: not actually used in final logic
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        prob = count / total
        entropy -= prob * __import__('math').log2(prob)
    return round(entropy, 4)


def filter_outliers(streams, low=20, high=30):
    cleaned = {}
    stats_log = defaultdict(int)
    
    for key, readings in streams.items():
        valid = [r for r in readings if low <= r <= high]
        cleaned[key] = valid
        stats_log[f'{key}_filtered'] = len(readings) - len(valid)
    
    # Attach unrelated metadata
    cleaned['meta_timestamps'] = [1678886400, 1678886460, 1678886520]
    cleaned['meta_version'] = 'v2.3-debug'
    
    return cleaned


def build_threshold_map(sensors, base_offset=5.0):
    # Generate threshold logic with red herring conditions
    thresholds = {}
    for sensor in sensors:
        if 'temp' in sensor:
            thresholds[sensor] = 25.0 + base_offset * 0.1
        elif 'pressure' in sensor:
            thresholds[sensor] = 105.0 + base_offset * 0.2
        elif 'humidity' in sensor:
            thresholds[sensor] = 50.0 + base_offset * 0.3
        else:
            thresholds[sensor] = 1.5 + base_offset * 0.05  # flow_rate
    
    # Add decoy entries
    thresholds['calibration_cycle'] = 999.9
    thresholds['maintenance_flag'] = -1
    
    return thresholds


def evaluate_stability(readings, window=3):
    # Unused stability metric (misleading intermediate)
    if len(readings) < window:
        return 0.0
    variances = []
    for i in range(len(readings) - window + 1):
        window_data = readings[i:i+window]
        mean = sum(window_data) / window
        variance = sum((x - mean) ** 2 for x in window_data) / window
        variances.append(variance)
    return round(sum(variances) / len(variances), 4) if variances else 0.0


def process_readings(cleaned_data, limits):
    diagnostics = []
    
    # Core relevant logic embedded in noise
    for sensor_name, values in cleaned_data.items():
        if not isinstance(values, list) or 'meta_' in sensor_name:
            continue
            
        if values:
            avg = sum(values) / len(values)
            threshold = limits.get(sensor_name, 0)
            
            # Actual decision point
            if avg > threshold:
                diagnostics.append(1)
            else:
                diagnostics.append(0)

    # Secondary transformation
    binary_str = ''.join(map(str, diagnostics))
    if binary_str:
        decimal_equiv = int(binary_str, 2)
    else:
        decimal_equiv = 0

    # Apply fake correction (no effect due to constants)
    adjustment_key = sum([len(v) if isinstance(v, list) else 0 
                          for v in cleaned_data.values()])
    fake_shift = adjustment_key % 4
    masked_result = decimal_equiv ^ ((1 << fake_shift) - 1) if fake_shift else decimal_equiv

    # Final computation: hash of string representation (deterministic)
    str_rep = f"DIAG_{masked_result}_END"
    final_hash = 0
    for c in str_rep:
        final_hash = (final_hash * 31 + ord(c)) % 1000000
    
    return final_hash

# Main execution with red herrings
if __name__ == "__main__":
    # Irrelevant prep
    system_mode = "diagnostic"
    debug_trace = []
    
    data, t_deriv, p_deriv = collect_sensor_data()
    
    # Apply useless transformations
    temp_calibrated = apply_calibration(t_deriv, factor=1.01, offset=-0.3)
    pressure_calibrated = apply_calibration(p_deriv, factor=0.99, offset=10.0)
    
    # Real pipeline starts here
    filtered_data = filter_outliers(data, low=22, high=28)
    
    # Compute meaningless metrics (distraction)
    pattern_score = analyze_pattern(temp_calibrated)
    entropy_val = compute_entropy([item for sublist in data.values() if isinstance(sublist, list) for item in sublist])
    stability_metric = evaluate_stability(temp_calibrated)
    
    # Build actual threshold map
    threshold_map = build_threshold_map(data.keys(), base_offset=7.0)
    
    # Key statement: what is the value of final_diagnostic after this?
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")