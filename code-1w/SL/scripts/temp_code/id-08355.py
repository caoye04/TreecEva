import math

# Simulated sensor data processing system
def collect_sensor_readings():
    raw_values = [3, 5, 7, 9, 12, 15, 18, 21, 24, 27, 30]
    offset = 0.5
    adjusted = [x + offset for x in raw_values]
    return adjusted

def apply_noise_filter(data):
    # Irrelevant filtering method (not actually used)
    filtered = [x for x in data if x > 10]
    temp_result = sum([x ** 0.5 for x in filtered])  # Distractor computation
    normalization_factor = 1.0
    scaled = [x / normalization_factor for x in filtered]
    return scaled

def extract_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(signal[i])
    if not peaks:
        peaks = [max(signal)]
    reduction = 0.9
    decayed = [p * reduction for p in peaks]  # Red herring transformation
    return peaks  # Actual return ignores decay

def transform_coordinates(peaks):
    # Meaningless coordinate mapping (unused path)
    angles = [math.atan(p / (i+1)) for i, p in enumerate(peaks)]
    polar_sum = sum(angles)
    dummy_shift = polar_sum * 0.1
    cartesian = [(p * math.cos(dummy_shift), p * math.sin(dummy_shift)) for p in peaks]
    flattened = [val for pair in cartesian for val in pair]
    return flattened

def aggregate_metrics(flattened_data):
    # Dead code branch - never executed due to prior logic
    if len(flattened_data) == 0:
        return 0
    total = sum(flattened_data)
    count = len(flattened_data)
    avg = total / count if count else 0
    variance = sum((x - avg) ** 2 for x in flattened_data) / count if count else 0
    return avg + variance

def validate_integrity(checksum):
    # Decoy validation function with no real impact
    test_str = "validation_check_123"
    if test_str.startswith("valid") and test_str.endswith("3"):
        digit_sum = sum(int(c) for c in test_str if c.isdigit())
        return digit_sum == 6
    return False

def process_signals(data):
    # Core relevant logic begins here
    threshold = 14.5
    filtered = [x for x in data if x >= threshold]  # Key filtering step
    
    # Bit manipulation red herring
    bit_mask = 0b1111
    masked_values = [int(x) & bit_mask for x in filtered]  # Computation with no use
    
    # Real processing chain
    squared = [x ** 2 for x in filtered]
    shifted = [s - 200 for s in squared]  # Shift to create negative values
    abs_vals = [abs(sv) for sv in shifted]
    
    # String-based distractor
    status_log = "processing_complete_status_ok"
    log_parts = status_log.split('_')
    completion_flag = len(log_parts) > 3 and log_parts[-1] == 'ok'
    
    # Critical accumulation
    running_total = 0
    multiplier = 1
    for val in abs_vals:
        if val % 2 == 0:
            running_total += val * multiplier
            multiplier += 1  # Increases only on even values
    
    # Final adjustment using string length as obfuscation
    adjustment_key = "key_adjust_4"
    adj_factor = int(adjustment_key[-1])  # Extract '4' from string
    final_output = running_total + adj_factor
    
    # Unused complex structure
    metadata_bundle = {
        'version': 'v1.7a',
        'checksum': sum(masked_values) * 3,
        'active': completion_flag
    }
    
    return final_output

# Orchestration sequence
readings = collect_sensor_readings()
noise_filtered = apply_noise_filter(readings)
peak_list = extract_peaks(noise_filtered)
coordinates = transform_coordinates(peak_list)
metric_score = aggregate_metrics(coordinates)  # Never used
is_valid = validate_integrity(metric_score)  # Always True but irrelevant

filtered_data = noise_filtered  # Assign to meaningful variable
final_output = process_signals(filtered_data)
print(f"Result: {final_output}")