import math

# System calibration constants (irrelevant to final result)
CALIBRATION_FACTOR = 0.987
BASELINE_OFFSET = -0.013
REFERENCE_VOLTAGE = 3.3

def generate_checksum(data):
    # Dead function - never used in execution path
    checksum = 0
    for item in data:
        checksum ^= int(item * 100) % 256
    return checksum

def preprocess_signal(raw_samples):
    filtered = []
    noise_floor = 0.05
    amplification = 2.5
    
    for x in raw_samples:
        if abs(x) > noise_floor:
            boosted = x * amplification
            # Apply non-linear compression
            compressed_val = math.copysign(abs(boosted)**0.9, boosted)
            filtered.append(round(compressed_val, 6))
    
    # Irrelevant transformation
    stats = {
        'peak': max(filtered),
        'trough': min(filtered),
        'count': len(filtered)
    }
    
    # Return only the filtered list, stats are unused
    return filtered

def encode_timestamp(event_time):
    # Complex but unused timestamp encoding
    seconds = int(event_time)
    fraction = event_time - seconds
    binary_rep = bin((seconds ^ int(fraction * 1000)) & 0xFFFF)
    return ''.join(reversed(binary_rep))

def build_lookup_table(keys):
    # Distractor: builds a mapping that's never used
    table = {}
    for k in keys:
        table[k] = (k * 113 + 17) % 199
    return table

def transform_coordinates(x, y, z):
    # Unused 3D coordinate rotation
    angle = math.pi / 4
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    
    xr = x * cos_a - y * sin_a
    yr = x * sin_a + y * cos_a
    zr = z * 1.5
    
    return (round(xr, 4), round(yr, 4), round(zr, 4))

def aggregate_metrics(data_stream):
    # Intermediate processing with misleading intermediate values
    magnitude_sum = 0.0
    active_segments = 0
    
    for val in data_stream:
        if val > 0.1:
            magnitude_sum += val ** 2
            active_segments += 1
    
    rms = math.sqrt(magnitude_sum / len(data_stream)) if data_stream else 0
    efficiency = (active_segments / len(data_stream)) * 100 if data_stream else 0
    
    # Return only RMS, efficiency is ignored downstream
    return rms

def analyze_signal(signal_data, thresholds):
    # Core logic embedded within distractions
    decision_weights = []
    
    for i, sample in enumerate(signal_data):
        # Determine impact category using bit manipulation
        category_flag = 0
        if sample > thresholds['high']:
            category_flag = 3  # Critical
        elif sample > thresholds['medium']:
            category_flag = 2  # Elevated
        elif sample > thresholds['low']:
            category_flag = 1  # Normal
        else:
            category_flag = 0  # Suppressed
        
        # Weight calculation using bitwise and arithmetic ops
        weight = (i & 7) + (category_flag << 2)  # Combine index and flag
        decision_weights.append(weight)
    
    # Final diagnostic based on weighted sum
    raw_score = sum(decision_weights)
    
    # Normalize using fixed reference (distractor: complex formula with simple outcome)
    adjustment = (raw_score >> 3) + (raw_score & 0x07)
    final_diagnostic = (raw_score * 3) - adjustment
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    # Raw sensor input
    sensor_readings = [
        0.02, 0.15, 0.08, 0.33, 0.41, 0.04, 0.28,
        0.19, 0.52, 0.07, 0.39, 0.44, 0.11, 0.25
    ]
    
    # Irrelevant spatial coordinates
    location_data = [(1.2, 3.4, 0.5), (2.1, 1.8, 0.7)]
    transformed_coords = [transform_coordinates(x, y, z) for x, y, z in location_data]
    
    # Unused lookup structure
    key_indices = {1, 3, 4, 7, 8, 9, 10, 12}
    lookup = build_lookup_table(key_indices)
    
    # Timestamp generation (dead code)
    timestamps = [encode_timestamp(1678824000 + i*300) for i in range(len(sensor_readings))]
    
    # Signal preprocessing
    processed = preprocess_signal(sensor_readings)
    
    # Aggregate metric (partially used)
    rms_value = aggregate_metrics(processed)
    
    # Threshold configuration (critical)
    threshold_map = {
        'low': 0.10,
        'medium': 0.25,
        'high': 0.40
    }
    
    # Data compression via filtering relevant samples
    compressed_data = [x for x in processed if x > 0.15]
    
    # Final analysis
    final_diagnostic = analyze_signal(compressed_data, threshold_map)
    
    # Output target result
    print(f"Result: {final_diagnostic}")