import math

# Simulated sensor data processing with embedded logic chain
def preprocess_readings(raw): 
    filtered = [x for x in raw if x > 0]
    adjusted = [math.log(x) * 2 for x in filtered]
    return adjusted

# Irrelevant helper - decoy function (never called in execution path)
def deprecated_normalization(arr):
    mean_val = sum(arr) / len(arr)
    return [x / mean_val for x in arr]

# Central transformation with red herring computations
def transform_signal(seq):
    # Distractor: unused intermediate forms
    squared_seq = [x**2 for x in seq]
    shifted_seq = [x + 1.5 for x in seq]
    masked_seq = [x for i, x in enumerate(seq) if i % 2 == 0]

    # Actual relevant transformation
    processed = []
    for idx, val in enumerate(seq):
        if idx == 0:
            processed.append(val)
        else:
            delta = seq[idx] - seq[idx-1]
            if delta > 1:
                processed.append(val * 0.9)
            else:
                processed.append(val * 1.1)
    return processed

# Set-based feature extraction (key concept)
def extract_features(data):
    unique_vals = set(round(x, 1) for x in data)
    high_threshold = {x for x in unique_vals if x > 3.0}
    low_threshold = {x for x in unique_vals if x < 1.5}
    
    # Distractor: complex but unused set operations
    overlap_check = high_threshold & low_threshold
    symmetric_diff = high_threshold ^ {x+0.5 for x in low_threshold}
    
    # Only this value is used later
    feature_metric = len(high_threshold) * 100 + len(low_threshold) * 10
    return feature_metric

# String-based diagnostic tagger - irrelevant but plausible
def generate_diagnostics(count):
    status_map = {0: 'NULL', 1: 'LOW', 2: 'MID', 3: 'HIGH'}
    code_tag = ''.join([status_map.get(min(count // 1000, 3), 'NULL'), str(count % 100)])
    checksum = sum(ord(c) for c in code_tag) % 7
    return code_tag + '-' + str(checksum)

# Core analysis function with conditional nesting
def analyze_sequence(cleaned):
    baseline = sum(cleaned) / len(cleaned)
    variance = sum((x - baseline) ** 2 for x in cleaned) / len(cleaned)
    std_dev = math.sqrt(variance)
    
    category_flags = []
    
    if std_dev > 2.0:
        category_flags.append('VOLATILE')
        adjustment_factor = 0.8
        secondary_check = True
        
        if baseline < 5.0:
            category_flags.append('UNSTABLE')
            adjustment_factor *= 0.9
            
            for item in cleaned:
                if item > baseline * 2:
                    category_flags.append('SPIKE_FOUND')
                    break
            
    elif std_dev > 1.0:
        category_flags.append('MODERATE')
        adjustment_factor = 1.1
    else:
        category_flags.append('STABLE')
        adjustment_factor = 1.25

    # Tuple unpacking - actual use
    meta = (len(category_flags), baseline, std_dev)
    flag_count, avg_val, spread = meta
    
    # Key logic step: combinatoric adjustment
    impact_score = int((avg_val * 100) + (spread * 10) - (flag_count * 5))
    
    # Distractor: dead code path
    if False:
        fallback = (impact_score + 500) // 2
        impact_score = max(impact_score, fallback)
    
    # Final computation using string method (irrelevant to result but adds noise)
    log_id = f"DIAG-{impact_score}".replace('I', '1')
    
    return impact_score * adjustment_factor

# Unused global variables - red herrings
MAX_BUFFER_SIZE = 1024
CALIBRATION_OFFSET = -0.05
TEMPORAL_WEIGHTS = (0.1, 0.3, 0.6)

# Main execution flow
if __name__ == '__main__':
    # Initial input data
    sensor_input = [1.2, 0.8, 3.4, 5.6, 2.1, 8.9, 0.5, 7.2]
    
    # Step 1: Preprocess readings
    calibrated = preprocess_readings(sensor_input)
    
    # Step 2: Transform signal (core modification)
    transformed_data = transform_signal(calibrated)
    
    # Dead code: unused assignment
    summary_stats = {
        'count': len(transformed_data),
        'peak': max(transformed_data),
        'trough': min(transformed_data)
    }
    
    # Step 3: Extract features (called but only one part matters)
    feature_code = extract_features(transformed_data)
    
    # Step 4: Generate diagnostic tag (irrelevant output)
    diag_label = generate_diagnostics(feature_code)
    
    # Critical statement: final_diagnostic = analyze_sequence(transformed_data)
    final_diagnostic = analyze_sequence(transformed_data)
    
    # Output target result
    print(f"Result: {final_diagnostic}")