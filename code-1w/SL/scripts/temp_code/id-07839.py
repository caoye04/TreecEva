import math

# Simulated sensor array data processing with diagnostic evaluation
def collect_sensor_readings():
    raw_readings = [23.1, 25.4, 19.5, 27.8, 30.0, 22.3, 24.9, 28.7, 21.0, 26.5]
    calibration_offset = 1.2
    adjusted = [r + calibration_offset for r in raw_readings]  # Adjust all by offset
    return adjusted

# Irrelevant auxiliary function - dead code path (distractor)
def legacy_normalization(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Signal filtering using moving average (relevant)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        end = i + 1
        window_slice = signal[start:end]
        smoothed.append(sum(window_slice) / len(window_slice))
    return smoothed

# Bit manipulation checksum (misleading intermediate result)
def compute_checksum(value_list):
    total = 0
    for v in value_list:
        scaled = int(v * 10)
        total ^= scaled  # XOR into checksum
    return total & 0xFFFF  # Mask to 16 bits

# Data segmentation based on thresholds (partially relevant)
def segment_data(data, low_thresh, high_thresh):
    below = [x for x in data if x < low_thresh]
    above = [x for x in data if x > high_thresh]
    middle = [x for x in data if low_thresh <= x <= high_thresh]
    return {'low': below, 'mid': middle, 'high': above}

# Main analysis function with critical logic
def analyze_readings(processed, thresh):
    # Step 1: Filter out unstable initial samples
    trimmed = processed[2:-2]  # Slice to remove edge noise
    
    # Step 2: Detect anomalies above threshold
    anomalies = [x for x in trimmed if x > thresh]
    anomaly_count = len(anomalies)
    
    # Step 3: Compute base statistic
    avg = sum(trimmed) / len(trimmed)
    deviation_sum = sum(abs(x - avg) for x in trimmed)
    
    # Step 4: Apply correction factor based on checksum (red herring)
    fake_context = [int(x * 2) for x in trimmed[:5]]
    magic_factor = compute_checksum(fake_context) % 7
    corrected_deviation = deviation_sum - magic_factor
    if corrected_deviation < 0:
        corrected_deviation = abs(corrected_deviation)
    
    # Step 5: Use bit shifting to derive diagnostic key (actual contributor)
    diagnostic_key = int(avg) ^ anomaly_count
    diagnostic_key = (diagnostic_key << 2) | (diagnostic_key >> 1)
    
    # Step 6: Final computation chain
    temp_score = corrected_deviation * 100
    normalized_score = temp_score / (anomaly_count + 1)
    final_diagnostic = int(normalized_score) ^ diagnostic_key
    
    # Dead code branches (distractors)
    if final_diagnostic > 10000:
        final_diagnostic = math.sqrt(final_diagnostic)
    elif final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)
    
    # Critical output
    return final_diagnostic

# Unused transformation (distractor)
def frequency_transform(data):
    transformed = []
    for i in range(len(data)):
        angle = data[i] * math.pi / 180.0
        transformed.append(math.sin(angle))
    return transformed

# --- Execution Flow ---
# Collect and process sensor data
raw_data = collect_sensor_readings()
smoothed_data = smooth_signal(raw_data)

# Segment data (irrelevant to final result)
segments = segment_data(smoothed_data, 24.0, 27.0)

# Prepare for analysis
processed_data = smoothed_data
threshold = 26.5

# Checksum for integrity (distractor variable)
integrity_hash = compute_checksum(processed_data)

# Linear search for first over threshold (unused path)
first_alert_index = -1
for i in range(len(processed_data)):
    if processed_data[i] > threshold:
        first_alert_index = i
        break

# Actual critical execution point
final_diagnostic = analyze_readings(processed_data, threshold)

# Output result
print(f"Result: {final_diagnostic}")