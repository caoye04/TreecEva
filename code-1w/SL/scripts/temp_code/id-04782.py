import itertools

# Simulate sensor data preprocessing with noise filtering and feature extraction
def acquire_sensor_stream():
    raw_samples = [18, 22, 19, 25, 30, 28, 20, 17]
    noise_floor = 15
    filtered = [x for x in raw_samples if x > noise_floor]
    return filtered

# Misleading auxiliary function - never called
def deprecated_normalization(data):
    max_val = max(data)
    return [round(x / max_val, 3) for x in data]

# Unused transformation path (dead code path)
def legacy_transform(seq):
    shifted = [(x << 1) for x in seq]  # Bit shift red herring
    return [y % 25 for y in shifted]

# Signal processing core
def extract_features(signal):
    avg = sum(signal) / len(signal)
    deviations = [abs(x - avg) for x in signal]
    significant = [d for d in deviations if d > 3.0]
    return round(sum(significant), 2)

# Complex conditional logic with distractor variables
def classify_regime(value):
    regime_code = None
    temp_offset = 0  # Irrelevant variable
    calibration_flag = True  # Distractor flag

    if value < 10:
        regime_code = 1
    elif value < 20:
        regime_code = 2
        temp_offset = -2  # Unused assignment
    else:
        regime_code = 3
        temp_offset = 5  # Dead assignment
    
    # Decoy computation
    decoy_score = (regime_code * 17) % 11
    return regime_code

# Data windowing using itertools
def slide_windows(data, size=3):
    it = iter(data)
    window = tuple(itertools.islice(it, size))
    if len(window) == size:
        yield window
    for next_val in it:
        window = window[1:] + (next_val,)
        yield window

# Primary transformation pipeline
def transform_signal(raw):
    # Apply moving average via windowing
    windows = list(slide_windows(raw))
    smoothed = [sum(w) // len(w) for w in windows]  # Integer division
    
    # Introduce irrelevant intermediate
    dummy_stats = {
        'peak': max(smoothed),
        'baseline': min(smoothed),
        'delta': abs(max(smoothed) - min(smoothed))
    }
    
    # Add dummy offset (never used)
    adjusted = [x + 2 for x in smoothed if x % 2 == 0] or [0]
    
    # Final processed form
    return smoothed + [len(smoothed)]  # Include length as feature

# Core processing with logical branching
def process_signal(data, limit):
    size = len(data)
    cap = data[-1]  # Last element
    
    # Conditional expression with boolean logic
    mode_flag = 'high' if cap > limit else 'low'
    
    # Multiple assignments (some irrelevant)
    weight_a, weight_b = 0.6, 0.4
    debug_trace = []  # Unused tracing list
    
    # Nested logic with distractors
    if mode_flag == 'high' and size >= 4:
        base_metric = data[0] * weight_a
        adjustment = 0
        for i in range(1, min(size, 5)):
            if i % 2 == 0:
                adjustment += data[i] // 3
            else:
                adjustment -= data[i] % 4
        
        # Decoy calculation
        phantom_value = (base_metric ^ adjustment) & 0xFF  # Bitwise red herring
        
        result = base_metric - adjustment
    else:
        result = sum(data) // size
    
    # Extra logical check (always false in this case)
    override = False
    if all(x < 0 for x in data) and not override:  # Short-circuit red herring
        result = -1
        
    return int(round(result))

# Orphaned utility function (unused)
def checksum_sequence(seq):
    acc = 0
    for i, val in enumerate(seq):
        acc ^= (val + i) % 16
    return acc

# Main execution flow
if __name__ == '__main__':
    # Initial acquisition
    sensor_data = acquire_sensor_stream()
    
    # Feature extraction (used)
    feature_score = extract_features(sensor_data)
    
    # Regime classification (used for threshold only)
    regime = classify_regime(feature_score)
    threshold = 25 if regime == 3 else 20
    
    # Irrelevant string manipulation (distractor)
    log_tag = "SYS_" + "_".join(str(regime))
    log_tag = log_tag[::-1]  # Reversed but unused
    
    # Signal transformation
    transformed_data = transform_signal(sensor_data)
    
    # Final processing
    final_output = process_signal(transformed_data, threshold)
    
    # Output result
    print(f"Result: {final_output}")