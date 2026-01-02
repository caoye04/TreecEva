import math

# Sensor simulation and diagnostic analysis system
def generate_signals(baseline, count):
    return [baseline + math.sin(i * 0.5) * 3 for i in range(count)]

def filter_noise(signal_list, dampen_factor=0.9):
    # Irrelevant filtering function (not used in final path)
    return [x * dampen_factor for x in signal_list if abs(x) > 1]

def integrate_signal(signal):
    accumulator = 0
    integrated = []
    for val in signal:
        accumulator += val
        integrated.append(accumulator)
    return integrated

def compute_entropy(data):
    # Dead code path — looks important but unused
    total = sum(data)
    probs = [x / total for x in data if x > 0]
    return -sum(p * math.log(p) for p in probs)

def extract_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return sorted(peaks, reverse=True)[:3]

def transform_readings(raw):
    # Applies non-linear transformation to sensor data
    transformed = map(lambda x: round(x ** 2 / 4.5 + 2.1, 2), raw)
    return [t for t in transformed if t > 3]  # list comprehension

def validate_calibration(data):
    # Distractor function with misleading intermediate result
    checksum = sum(int(x) for x in data) % 107
    expected = 89
    status = 'valid' if checksum == expected else 'invalid'
    return status, checksum  # Never actually checked in main flow

def build_threshold_map(config):
    # Creates mapping of thresholds per channel
    base_map = {chr(65+i): 10 + i*2.5 for i in range(8)}  # A-H channels
    for k in config.get('overrides', {}):
        base_map[k] = config['overrides'][k]
    base_map['X'] = 0  # red herring key
    return base_map

def collect_diagnostics(structure):
    # Unused recursive diagnostic tree walker
    def walk(node, path=""):
        if isinstance(node, dict):
            results = {}
            for k, v in node.items():
                results[path + k] = walk(v, path + k + ".")
            return results
        elif isinstance(node, list):
            return sum(walk(item, path) for item in node) if path else 0
        else:
            return 1
    return walk(structure)

def analyze_readings(data_sequence, limits):
    category_scores = {"A": 0, "B": 0, "C": 0, "D": 0}
    temp_log = []
    
    for entry in data_sequence:
        key = entry['channel']
        value = entry['value']
        limit_val = limits.get(key, 15)
        
        if value > limit_val * 0.9:
            category_scores[key] += 3
        elif value > limit_val * 0.7:
            category_scores[key] += 2
        else:
            category_scores[key] += 1
            
        # Capture intermediate state that seems important
        temp_log.append(f"{key}:{value:.1f}")
    
    # Secondary evaluation based on log length (subtle dependency)
    if len(temp_log) > 10:
        adjustment = len([x for x in temp_log if 'C' in x])  # list comprehension
        category_scores['C'] += adjustment // 2
    
    # Final aggregation
    aggregate = 0
    for k, score in category_scores.items():
        if k in ['A','C']:
            aggregate += score * 2
        else:
            aggregate += score
            
    return aggregate

# Main execution workflow
if __name__ == '__main__':
    # Simulated sensor baseline readings
    raw_sensor_data = generate_signals(baseline=7.3, count=15)
    
    # Apply integration (relevant transformation)
    integrated_data = integrate_signal(raw_sensor_data)
    
    # Transform readings using lambda-based mapping
    cleaned_readings = transform_readings(integrated_data)
    
    # Build dummy configuration (contains decoy values)
    config_settings = {
        'mode': 'aggressive',
        'overrides': {'D': 18.0},  # affects threshold
        'calibration_key': 42,
        'debug_trace': True
    }
    
    # Generate threshold map (used later)
    threshold_map = build_threshold_map(config_settings)
    
    # Validate calibration — runs but result ignored (distractor)
    validation_result = validate_calibration(integrated_data)
    
    # Construct processed data entries
    labels = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C']
    processed_data = []
    for i, val in enumerate(cleaned_readings):
        if i >= len(labels): break
        processed_data.append({
            'channel': labels[i],
            'value': val,
            'seq_id': f"S{i:02d}",
            'flagged': False
        })
    
    # Analyze the sequence against thresholds
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print target result
    print(f"Result: {final_diagnostic}")