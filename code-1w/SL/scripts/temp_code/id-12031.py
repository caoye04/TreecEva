import math

# Sensor simulation and diagnostic analysis system
def generate_signals(baseline, noise_factor, count):
    return [baseline + math.sin(i) * noise_factor for i in range(count)]

# Irrelevant helper: spectrogram placeholder
def compute_spectrogram(signal):
    magnitude = sum([abs(x) for x in signal[::2]])
    norm = len(signal) or 1
    return magnitude / norm

# Core processing pipeline
def filter_outliers(data, threshold=2.5):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    filtered = [x for x in data if abs(x - mean_val) <= threshold * std_dev]
    return filtered if filtered else [mean_val]

# Redundant transformation chain
def enhance_resolution(dataset, factor=2):
    expanded = []
    for val in dataset:
        expanded.extend([val] * factor)
    return [sum(expanded[i:i+factor]) / factor for i in range(0, len(expanded), factor)]

# Unused auxiliary function (decoy)
def validate_calibration(sequence):
    checksum = 0
    for item in sequence:
        if item > 0:
            checksum += int(math.log(abs(item) + 1, 2))
        else:
            checksum -= item % 7
    return checksum % 11 == 0

# Key analysis logic
def analyze_readings(readings):
    # Step 1: Normalize around median-like behavior
    sorted_vals = sorted(readings)
    mid = len(sorted_vals) // 2
    pivot = (sorted_vals[mid] + sorted_vals[~mid]) / 2
    
    # Step 2: Compute deviation signature
    deviations = [abs(x - pivot) for x in readings]
    dev_mean = sum(deviations) / len(deviations)
    
    # Step 3: Apply weighted impact model
    weights = [math.exp(-d / (dev_mean + 1e-6)) for d in deviations]
    weighted_sum = sum(d * w for d, w in zip(deviations, weights))
    total_weight = sum(weights)
    
    # Step 4: Transform through diagnostic curve
    response_curve = math.tanh(weighted_sum / (total_weight + 1e-6))
    
    # Step 5: Discrete state mapping
    state_code = int(response_curve * 100) % 97
    
    # Step 6: Final integration with environmental offset
    offset = 17
    final_score = state_code + offset
    
    # Distractor: unused branching
    if final_score < 50:
        adjustment = math.ceil(math.sqrt(50 - final_score))
        final_score += adjustment  # This path not taken
    elif final_score > 80:
        decay = final_score * 0.1
        final_score -= int(decay)  # Also not triggered
    
    return final_score

# Irrelevant telemetry tracking
telemetry_log = []
system_health = {'sensors': 5, 'status': 'nominal', 'uptime': 1274}

def log_event(event_type, timestamp):
    telemetry_log.append(f'{event_type}:{timestamp}')

# Main execution block
if __name__ == '__main__':
    # Generate raw sensor input
    raw_sensor_data = generate_signals(baseline=12.8, noise_factor=4.3, count=64)
    
    # Dead code path: calibration check (never actually used in flow)
    test_sequence = [16, 8, 4, 2]
    if validate_calibration(test_sequence):
        system_health['status'] = 'calibrated'
    else:
        system_health['status'] = 'needs_attention'
    
    # Actual processing path
    cleaned_data = filter_outliers(raw_sensor_data, threshold=2.1)
    enhanced_data = enhance_resolution(cleaned_data, factor=2)
    processed_data = [x * 0.87 for x in enhanced_data if x > 5]  # Final preprocessing
    
    # Introduce misleading intermediate
    temp_diagnostic = compute_spectrogram(processed_data)
    reference_baseline = temp_diagnostic * 1.5  # Looks important but unused
    
    # Critical statement
    final_diagnostic = analyze_readings(processed_data)
    
    # Logging side effects (irrelevant to result)
    log_event('DIAG_START', 1000)
    log_event('DIAG_COMPLETE', 1003)
    
    # Output target result
    print(f"Result: {final_diagnostic}")