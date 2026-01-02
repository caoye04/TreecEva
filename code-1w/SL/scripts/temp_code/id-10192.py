import math

# Simulated sensor data processing with diagnostic analysis
raw_readings = [3.2, 4.1, 2.8, 5.6, 3.9, 4.4, 2.1, 5.0]
offset_calibration = 0.37
noise_floor = 0.88
temp_correction = -0.12

# Irrelevant calibration constants (distractors)
calibration_key = 'X9ZT'
version_stamp = 'v2.1'
max_threshold = 6.0
min_threshold = 1.0

# Signal mapping dictionary for non-linear correction (relevant)
signal_map = {
    2.1: 0.45,
    2.8: 0.62,
    3.2: 0.71,
    3.9: 0.83,
    4.1: 0.86,
    4.4: 0.89,
    5.0: 0.94,
    5.6: 1.0
}

# Decoy dictionary - never used (distractor)
diagnostic_codes = {
    'ERR_1': 'Sensor overload',
    'ERR_2': 'Calibration drift',
    'WARN_1': 'High variance',
    'INFO_1': 'Normal fluctuation'
}

# Apply base calibration and generate intermediate forms (some irrelevant)
calibrated = [x + offset_calibration for x in raw_readings]
filtered = [x for x in calibrated if x > noise_floor]
denoised = [x + temp_correction for x in filtered]  # Minor temp adjustment

# Compute statistical features (some will be unused)
mean_val = sum(denoised) / len(denoised)
variance = sum((x - mean_val) ** 2 for x in denoised) / len(denoised)
std_dev = math.sqrt(variance)
skewness = sum((x - mean_val) ** 3 for x in denoised) / (len(denoised) * std_dev ** 3)

# Bit manipulation red herring (distractor block - not connected to result)
status_flag = 0xAE5D
status_flag ^= 0x8000
status_flag &= ~0x000F
status_flag |= (len(raw_readings) << 2)

# String-based identifier generation (irrelevant to final result)
sensor_id = "SNSR-TRX9"
encoded_tag = ''.join([chr(ord(c) ^ 0x3) for c in sensor_id])
serial_version = f"{sensor_id[:4]}_{calibration_key}_{version_stamp}"

# Primary signal transformation using dictionary lookup
mapped_signals = [signal_map[round(x - temp_correction, 1)] for x in denoised]

# Frequency analysis decoy (dead code path)
frequency_count = {}
for val in raw_readings:
    rounded = round(val, 1)
    frequency_count[rounded] = frequency_count.get(rounded, 0) + 1

# Construct composite index with logical conditions and set operations
valid_indices = {i for i, v in enumerate(denoised) if v > mean_val}
anomalous_indices = {i for i, v in enumerate(denoised) if abs(v - mean_val) > std_dev}
overlap_check = valid_indices & anomalous_indices  # Non-empty set, misleading

# Secondary transformation chain
weighted_sum = 0.0
for i, val in enumerate(mapped_signals):
    if i % 2 == 0:
        weighted_sum += val * 1.1
    else:
        weighted_sum += val * 0.9

# Normalize and prepare processed data structure (key output)
scaling_factor = 2.5
processed_data = {
    'samples': len(mapped_signals),
    'amplitude': weighted_sum * scaling_factor,
    'consistency': 1.0 - (variance / 10.0),
    'flags': list(valid_indices)
}

# Decoy function - never called (distractor)
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Auxiliary function with misleading complexity
def detect_pattern(sequence):
    if len(sequence) < 3:
        return False
    for i in range(len(sequence) - 2):
        if sequence[i] + sequence[i+2] == 2 * sequence[i+1]:
            return True
    return False

# Core analysis function that computes final result
def analyze_signal(data_dict):
    sample_count = data_dict['samples']
    amplitude = data_dict['amplitude']
    consistency = data_dict['consistency']
    
    # Complex conditional logic with nested expressions
    if sample_count >= 6:
        base_score = amplitude * consistency
        if amplitude > 20.0:
            adjustment = math.log(amplitude) * 0.8
        else:
            adjustment = math.sqrt(amplitude) * 0.5
        
        # Additional condition based on set property (uses overlap_check from outer scope)
        if len(overlap_check) > 0 and 'flags' in data_dict:
            adjustment *= 1.15
        
        # Final composition with trigonometric weighting (relevant)
        angle = math.pi * (consistency / 2)
        weight = math.sin(angle) if consistency < 1.5 else 1.0
        
        diagnostic_value = base_score + adjustment * weight
    else:
        diagnostic_value = amplitude * 0.6
    
    # Final nonlinear transformation
    return int(diagnostic_value * 1.07) if diagnostic_value > 0 else 0

# Execute main analysis
final_diagnostic = analyze_signal(processed_data)

# Print result as required
print(f"Result: {final_diagnostic}")