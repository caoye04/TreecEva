import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_signal(raw_samples):
    filtered = []
    noise_floor = 0.05
    gain_compensation = 1.87
    temp_accum = 0.0

    for sample in raw_samples:
        if abs(sample) < noise_floor:
            continue
        compensated = sample * gain_compensation
        temp_accum += abs(compensated)
        if len(filtered) % 3 == 0:
            temp_accum *= 0.9
        filtered.append(compensated)

    # Irrelevant transformation (distractor)
    spectral_trend = [math.sin(x * 0.1) for x in range(len(filtered))]
    normalization_factor = sum([x**2 for x in spectral_trend]) if spectral_trend else 1

    return filtered, temp_accum, normalization_factor

def extract_features(signal_part):
    mean_val = sum(signal_part) / len(signal_part) if signal_part else 0
    variance = sum((x - mean_val) ** 2 for x in signal_part) / len(signal_part) if signal_part else 0
    peak_amplitude = max(abs(x) for x in signal_part) if signal_part else 0

    # Dead code path - never used (red herring)
    if variance > 100:
        anomaly_score = 999
    else:
        anomaly_score = -1  # Unused

    # Bit manipulation distractor
    bit_analysis = 0
    for i in range(len(signal_part)):
        bit_analysis ^= int(abs(signal_part[i])) & 7

    # Tuple unpacking and irrelevant stats
    stats_bundle = (mean_val, variance, peak_amplitude, bit_analysis)
    m, v, p, b = stats_bundle

    # Early return not taken (misleading control flow)
    if p < 0.1:
        return (0, 0, 0)

    return stats_bundle

def recursive_smooth(data, depth=0):
    if depth >= 3 or len(data) < 2:
        return data
    smoothed = [(data[i] + data[i+1]) / 2 for i in range(len(data)-1)]
    return recursive_smooth(smoothed, depth + 1)

def analyze_signal(data_chunk, sensitivity):
    feature_set = extract_features(data_chunk)
    base_metric = feature_set[0] * 2.3 + feature_set[2] * 1.7
    adjustment = math.log(sensitivity + 1) if sensitivity > 0 else 0

    # Complex conditional with short-circuit (irrelevant branch)
    override_flag = (len(data_chunk) > 100) and (feature_set[1] < 0.01) and (False or False)
    if override_flag:
        return -999.0  # Dead path

    # Modular arithmetic decoy
    checksum = 0
    for val in data_chunk[:10]:
        checksum = (checksum + int(abs(val) * 100)) % 97

    # Final computation - only this matters
    diagnostic_score = (base_metric - adjustment) * (1 + feature_set[3] * 0.05)
    return round(diagnostic_score, 6)

# Main execution flow
raw_sensor_data = [0.01, -0.03, 0.12, 0.45, -0.23, 0.67, 0.89, -0.11, 0.34, 0.78, 0.22, 0.61]

# Preprocessing stage
processed_data, accumulator, norm_factor = preprocess_signal(raw_sensor_data)

# Signal transformation chain
intermediate_result = recursive_smooth(processed_data)
if len(intermediate_result) < 5:
    transformed_data = processed_data
else:
    transformed_data = intermediate_result

# Threshold calculation with string distraction
config_param = 'threshold_boost=high'
boost_level = config_param.split('=')[1] if '=' in config_param else 'low'
temp_threshold = 0.5
if boost_level in ['high', 'critical']:
    temp_threshold *= 1.4

# Unused variable - misleading
validation_log = f"Final validation passed: {len(transformed_data)} samples at {boost_level} boost"

threshold = temp_threshold * (1 + norm_factor * 0.1)  # Slight influence from distractor

# Critical statement
final_diagnostic = analyze_signal(transformed_data, threshold)

print(f"Result: {final_diagnostic}")