import itertools

# Simulated sensor data processing pipeline for aerospace telemetry
raw_readings = [0.78, 0.63, 0.81, 0.75, 0.69, 0.83, 0.77, 0.71]
baseline_offset = 0.74
noise_threshold = 0.05

def apply_calibration(data, offset):
    """Apply baseline calibration to sensor readings."""
    calibrated = []
    for x in data:
        adjusted = x - offset
        if abs(adjusted) < noise_threshold:
            calibrated.append(0.0)
        else:
            calibrated.append(round(adjusted, 2))
    return calibrated

def generate_combinations(values):
    # Distractor function: generates unused combinations
    return list(itertools.combinations(values, 3))

def detect_anomalies(stream):
    # Heavily nested logic with red herrings
    anomalies = []
    window_size = 3
    for i in range(len(stream) - window_size + 1):
        window = stream[i:i+window_size]
        avg = sum(window) / len(window)
        if avg > 0.1:
            anomalies.append((i, avg))
    # Dead code path - never used
    if len(anomalies) > 10:
        return [x for x in anomalies if x[1] > 0.15]
    return anomalies

def compress_data(packets):
    # Irrelevant compression routine
    encoded = ''
    for p in packets:
        if p > 0:
            encoded += '1'
        elif p < 0:
            encoded += '0'
        else:
            encoded += 'X'
    return encoded.replace('X', '')

def filter_outliers(sequence):
    """Remove extreme values using interquartile range (distraction variant)"""
    sorted_seq = sorted(sequence)
    q1 = sorted_seq[len(sorted_seq)//4]
    q3 = sorted_seq[3*len(sorted_seq)//4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    filtered = [x for x in sequence if lower_bound <= x <= upper_bound]
    return filtered if filtered else [0]  # Fallback

def integrate_frames(frames):
    """Accumulate frame contributions with decay factor"""
    total = 0.0
    decay = 0.9
    for i, f in enumerate(frames):
        total += f * (decay ** i)
    return round(total, 4)

def validate_checksum(payload):
    # Complex but irrelevant checksum validation
    chk = 0
    for c in str(payload):
        if c.isdigit():
            chk ^= int(c)
        elif c.isalpha():
            chk += ord(c.lower()) % 10
    return chk % 7 == 0

def reconstruct_signal(snippets):
    # Signal reconstruction with decoy transformations
    reversed_parts = [snippet[::-1] for snippet in snippets]
    flattened = list(itertools.chain.from_iterable(reversed_parts))
    normalized = [round(x * 1.05, 3) for x in flattened]
    return normalized

def analyze_signal(signal):
    """Final analysis combining multiple metrics"""
    if not signal:
        return -1
    
    # Key computation steps
    abs_values = [abs(x) for x in signal]
    peak = max(abs_values)
    avg_mag = sum(abs_values) / len(abs_values)
    zero_crossings = 0
    for i in range(1, len(signal)):
        if signal[i-1] * signal[i] < 0:
            zero_crossings += 1
    
    # Critical formula: combines peak, average, and oscillation count
    diagnostic_score = int((peak * 400) + (avg_mag * 200) + (zero_crossings * 50))
    
    # Red herring: complex conditional that doesn't affect result
    if diagnostic_score > 300:
        temp_adjustment = 0
        for val in signal[:5]:
            if val > 0.05:
                temp_adjustment += 10
            elif val < -0.05:
                temp_adjustment -= 5
        # This adjustment is calculated but NOT applied
        final_value = diagnostic_score  # Actual assignment
    else:
        final_value = diagnostic_score + 100
        
    return final_value

# Main execution flow
# Step 1: Calibrate raw sensor data
calibrated_readings = apply_calibration(raw_readings, baseline_offset)

# Step 2: Filter spurious readings (this alters length)
filtered_readings = filter_outliers(calibrated_readings)

# Step 3: Create time-shifted frames for signal processing
frame_length = 3
overlapping_frames = []
for i in range(len(filtered_readings) - frame_length + 1):
    frame = filtered_readings[i:i+frame_length]
    integrated_value = integrate_frames(frame)
    overlapping_frames.append(integrated_value)

# Step 4: Reconstruct full signal from processed frames
reconstructed_snippets = [[val * 0.9] for val in overlapping_frames]
processed_signal = reconstruct_signal(reconstructed_snippets)

# Step 5: Detect anomalies in the processed signal (unused result)
anomaly_list = detect_anomalies(processed_signal)

# Step 6: Generate irrelevant combinations as distraction
dummy_combinations = generate_combinations([1, 2, 3, 4, 5])

# Step 7: Compress the signal data into bitstream (unused)
compressed_bits = compress_data(processed_signal)

# Step 8: Validate checksum on a string representation (red herring)
signal_string = ''.join(f'{x:.3f}' for x in processed_signal)
checksum_valid = validate_checksum(signal_string)

# Step 9: Final diagnostic analysis
final_diagnostic = analyze_signal(processed_signal)

print(f"Result: {final_diagnostic}")