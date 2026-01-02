import math

# Simulated sensor array data with calibration offsets
def generate_raw_readings():
    raw = [127, 255, 89, 191, 45]
    calibrated = [x * 0.78 + 3.1 for x in raw]
    return calibrated

# Irrelevant signal processing function (dead code path)
def fft_approx(data):
    result = []
    for i in range(len(data)):
        component = 0
        for j in range(len(data)):
            angle = 2 * math.pi * i * j / len(data)
            component += data[j] * (math.cos(angle) - math.sin(angle))
        result.append(component)
    return result

# Core transformation pipeline
def preprocess_sensor_data(raw_readings, threshold=100.0):
    normalized = []
    outliers = []
    scaling_factor = 1.85
    
    for val in raw_readings:
        adjusted = val / scaling_factor
        if adjusted > threshold:
            outliers.append(adjusted)
        else:
            normalized.append(round(adjusted, 2))
    
    # Distractor: unused statistical computation
    mean_val = sum(normalized) / len(normalized) if normalized else 0
    variance = sum((x - mean_val) ** 2 for x in normalized) / len(normalized) if normalized else 0
    z_scores = [(x - mean_val) / math.sqrt(variance) if variance != 0 else 0 for x in normalized]
    
    return {
        'data': normalized,
        'meta': {
            'outlier_count': len(outliers),
            'valid_count': len(normalized),
            'scaling_used': scaling_factor
        }
    }

# Recursive frequency classification (only some branches are relevant)
def classify_frequency(value, depth=3):
    if depth <= 0:
        return value * 0.92
    if value < 50:
        return classify_frequency(value + 8.5, depth - 1)
    elif value < 80:
        return classify_frequency(value * 1.1, depth - 1)
    else:
        return classify_frequency(value - 12.3, depth - 1)

# Main analysis engine
def analyze_readings(dataset):
    readings = dataset['data']
    meta_info = dataset['meta']
    
    # Initialize various accumulators (some are decoys)
    accumulator_a = 0
    accumulator_b = 1
    diagnostic_score = 0
    entropy_proxy = 0
    temp_shift = 0
    
    # Real logic begins here
    for i, val in enumerate(readings):
        if i % 2 == 0:
            # Even index: apply recursive classification
            processed_val = classify_frequency(val)
            accumulator_a += processed_val
            
            # Decoy operation
            temp_shift = (temp_shift << 2) ^ int(processed_val % 17)
        else:
            # Odd index: direct transformation
            base_contribution = math.log(val + 10) * 1.618
            accumulator_b *= base_contribution
            
            # Another red herring
            entropy_proxy -= base_contribution * math.log(base_contribution + 1e-8)
    
    # Critical calculation hidden among distractors
    intermediate = accumulator_a * meta_info['valid_count']
    adjustment = meta_info['outlier_count'] ** 2 * 3.7
    diagnostic_score = int(intermediate - adjustment)  # Final integer truncation
    
    # Dead branch: never executed due to data constraints
    if meta_info['scaling_used'] < 1.0:
        fallback = 0
        for x in readings:
            fallback += int(math.sqrt(x))
        diagnostic_score = fallback
    
    # Additional irrelevant bit manipulation
    checksum = 0
    for val in readings:
        truncated = int(val)
        checksum ^= (truncated << 1) & 0xFF
        checksum ^= (truncated >> 2) & 0xFF
    
    final_diagnostic = diagnostic_score + checksum // 10
    
    # This print is required for traceability
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Entry point
if __name__ == "__main__":
    raw_data = generate_raw_readings()
    processed_data = preprocess_sensor_data(raw_data)
    final_diagnostic = analyze_readings(processed_data)