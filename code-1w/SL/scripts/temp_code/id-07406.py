import math

def analyze_phase(signal):
    # Irrelevant helper function (dead code path)
    return sum(abs(s) for s in signal) / len(signal)

def compute_entropy(data):
    # Distractor function: looks important but unused in critical path
    total = sum(data)
    entropy = 0
    for x in data:
        p = x / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

def shift_window(sequence, offset=1):
    # Unused slicing operation — red herring
    return sequence[offset:] + sequence[:offset]

def validate_checksum(record):
    # Decoy validation logic that seems critical but isn't used
    chk = 0
    for i, val in enumerate(record):
        chk ^= (val + i) % 256
    return chk == record[-1]

def extract_features(dataset):
    # Complex-looking transformation with irrelevant operations
    features = {}
    for key, values in dataset.items():
        if len(values) < 3:
            continue
        smoothed = [round((a + b + c)/3, 2) for a, b, c in zip(values, values[1:], values[2:])]
        features[f'{key}_peak'] = max(smoothed)
        features[f'{key}_trend'] = smoothed[-1] - smoothed[0]
    return features  # Never used later

def process_readings(data, config):
    # Core logic buried among distractions
    result = 0
    temp_log = []
    
    for sensor, readings in data.items():
        # Extract only sensors present in config
        if sensor not in config:
            continue
            
        threshold = config[sensor]
        count_above = 0
        cumulative = 0
        
        for val in readings:
            cumulative += val
            if val > threshold:
                count_above += 1
            
        # Only this line contributes to final answer
        if sensor == 'S3':
            intermediate = cumulative * count_above
            temp_log.append(intermediate)
    
    # Actual computation for answer
    final_value = int(sum(temp_log))
    
    # Multiple misleading variables
    stats_summary = {
        'total_sensors': len(data),
        'valid_sensors': len([s for s in data if s in config]),
        'diagnostics': [cumulative, count_above],  # Captures last loop values, misleading
        'debug_code': 0xDEADBEF
    }
    
    # Final assignment (answer depends only on S3 processing)
    final_diagnostic = final_value + 100  # Add constant bias
    
    # Dead branch — never executes due to hard-coded condition
    if len(temp_log) > 100:
        fallback = compute_entropy([len(d) for d in data.values()])
        final_diagnostic = int(fallback)
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Real input data
    sensor_data = {
        'S1': [12, 15, 10, 18],
        'S2': [88, 92, 85],
        'S3': [45, 48, 55, 60],      # Only this affects answer
        'S4': [101, 99, 103, 110, 95]
    }
    
    thresholds = {
        'S1': 14,
        'S2': 90,
        'S3': 50,
        'S4': 100
    }
    
    # Extraneous data structures — red herrings
    historical_meta = {
        'calibration': {
            'version': '2.1',
            'shifts': [-0.5, 0.0, 0.3],
            'window_size': 3
        },
        'flags': [0, 1, 1, 0],
        'checksum': 42
    }
    
    feature_set = extract_features(sensor_data)  # Called but unused
    
    # Simulated pre-processing with slicing distraction
    flat_data = [val for readings in sensor_data.values() for val in readings]
    window_sample = flat_data[::2]  # Every other value — irrelevant
    
    # Key execution point
    final_diagnostic = process_readings(sensor_data, thresholds)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")