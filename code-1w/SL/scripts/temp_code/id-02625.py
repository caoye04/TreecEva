import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw = [0.7, -1.2, 0.95, 2.3, -0.4, 1.1, 3.0, -2.1, 0.8, 1.5]
    scale_factor = 2.5
    offset = 0.5
    adjusted = [(x * scale_factor) + offset for x in raw]
    return adjusted

# Irrelevant helper: computes entropy (not used in final result)
def compute_entropy(data):
    total = sum(abs(x) for x in data)
    probs = [abs(x)/total for x in data]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 4)

# Distraction function: processes dummy metadata
def extract_metadata():
    meta = {
        'device_id': 'DSV-9X',
        'firmware': 'v2.1.7',
        'calibration': [0.1, 0.05, -0.02],
        'timestamp': 1678886400
    }
    # Dead computation path
    checksum = sum(ord(c) for c in meta['device_id']) * meta['timestamp'] % 1000
    return meta

# Core transformation pipeline
def transform_signal(data, method='quadratic'):
    if method == 'quadratic':
        processed = [x**2 - 2*x + 1 for x in data]  # (x-1)^2
    elif method == 'exponential':
        processed = [math.exp(x/10) for x in data]
    else:
        processed = [abs(x) for x in data]
    
    # Filter outliers above threshold (distraction: not actually used later)
    filtered = [x for x in processed if x < 10]
    normalizer = sum(processed) / len(processed)
    normalized = [x / normalizer for x in processed]
    return normalized

# Bit manipulation red herring
def scramble_index(index):
    temp = (index << 3) & 0xFF
    temp = temp ^ 0b10101010
    temp = (temp >> 2) | (index << 6)
    return temp % len('diagnostic_key')

# Real pattern analyzer (key function)
def analyze_pattern(seq, settings):
    base_weight = settings['threshold']
    factor = settings['gain']
    
    # Key logic chain
    squared_sum = sum(x**2 for x in seq)
    avg = sum(seq) / len(seq)
    fluctuation = sum(abs(seq[i+1] - seq[i]) for i in range(len(seq)-1))
    
    # Critical intermediate values (some are distractions)
    peak = max(seq)
    symmetry_score = abs(avg) / (peak + 1e-8)
    penalty = 0
    
    if symmetry_score < 0.3:
        penalty += 5
    elif symmetry_score > 0.7:
        penalty += 3
    
    # Hidden dependency: count how many values cross zero in original domain
    inverse_transform = [math.sqrt(x) - 1 for x in seq]  # reverse (x-1)^2 approximately
    zero_crossings = 0
    for i in range(1, len(inverse_transform)):
        if inverse_transform[i-1] * inverse_transform[i] < 0:
            zero_crossings += 1
    
    # Main diagnostic formula
    raw_diagnostic = (squared_sum * factor) - (fluctuation * penalty)
    
    # Final adjustment based on zero crossings (crucial but obscured)
    if zero_crossings >= 2:
        raw_diagnostic += base_weight * 2
    else:
        raw_diagnostic -= base_weight
    
    return int(round(raw_diagnostic))

# Unused recursive distraction
def predict_next(values, depth=3):
    if depth == 0 or len(values) < 2:
        return values[-1] if values else 0
    diff = values[-1] - values[-2]
    extended = values + [values[-1] + diff]
    return predict_next(extended, depth - 1)

# Configuration with misleading parameters
config = {
    'threshold': 7.0,
    'gain': 1.8,
    'mode': 'aggressive',
    'filters': ['lowpass', 'notch'],
    'window_size': 5
}

# Execution flow
if __name__ == '__main__':
    # Step 1: Collect data
    readings = collect_sensor_readings()
    
    # Step 2: Extract unused metadata
    metadata = extract_metadata()  # dead end
    
    # Step 3: Transform data using quadratic method
    transformed_data = transform_signal(readings, method='quadratic')
    
    # Step 4: Compute irrelevant entropy
    entropy_value = compute_entropy(transformed_data)  # distraction
    
    # Step 5: Apply bit scrambling on indices (unused)
    scrambled_indices = [scramble_index(i) for i in range(5)]  # red herring
    
    # Step 6: Predict future (unused)
    prediction = predict_next(transformed_data)  # decoy
    
    # Step 7: Analyze pattern - this produces the answer
    final_diagnostic = analyze_pattern(transformed_data, config)
    
    # Output the target result
    print(f"Result: {final_diagnostic}")