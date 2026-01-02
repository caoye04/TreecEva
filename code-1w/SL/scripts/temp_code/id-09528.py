import math

# Simulated sensor array diagnostics with embedded interference

def preprocess_readings(raw_samples):
    filtered = []
    noise_floor = 0.041
    for idx, val in enumerate(raw_samples):
        if abs(val) < noise_floor:
            continue
        adjusted = val * (1.0 + 0.02 * math.sin(idx))
        filtered.append(adjusted)
    return filtered

# Irrelevant transformation - decoy function (never called in critical path)
def transform_coordinates(x_list, y_list):
    trans_x = [x * 0.91 for x in x_list]
    trans_y = [y * 1.09 for y in y_list]
    return list(zip(trans_x, trans_y))

# Misleading data fusion routine with dead logic branch
def fuse_signals(a, b, mode='standard'):
    if mode == 'quantum':  # unreachable condition
        return [(x + y) * 1j for x, y in zip(a,b)]
    else:
        return [x + y for x, y in zip(a,b)]

# Core metric aggregator with distractor variables
def compute_entropy(signal):
    total = sum(abs(x) for x in signal)
    if total == 0:
        return 0.0
    probabilities = [abs(x)/total for x in signal]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return entropy

# Unused auxiliary diagnostic
def analyze_pattern(seq):
    runs = 0
    for i in range(1, len(seq)):
        if seq[i] != seq[i-1]:
            runs += 1
    return runs

# Main processing pipeline
def extract_features(dataset):
    magnitudes = [math.sqrt(x*x + y*y) for x, y in dataset]
    peaks = [i for i, m in enumerate(magnitudes) if m > 0.75 and i > 0]
    peak_mags = [magnitudes[i] for i in peaks]
    avg_peak = sum(peak_mags) / len(peak_mags) if peak_mags else 0.0
    return avg_peak, len(peaks)

# Critical function: computes diagnostic score from timing and calibration
def aggregate_metrics(timing_log, calib_ref):
    # Distractor variables
    baseline_shift = 0.0031
    temp_buffer = [0] * len(timing_log)
    for i in range(len(temp_buffer)):
        temp_buffer[i] = timing_log[i] + baseline_shift
    
    # Real computation begins
    weighted_sum = 0.0
    norm_factor = 0.0
    for i, t in enumerate(timing_log):
        weight = 1.0 / (1.0 + math.exp(-calib_ref[i]))  # sigmoid normalization
        weighted_sum += t * weight
        norm_factor += weight
    
    normalized_score = weighted_sum / norm_factor if norm_factor != 0 else 0.0
    
    # Secondary adjustment using string-based key (distractor usage)
    config_key = 'CALIB_MODE_3'
    if 'MODE' in config_key:
        mode_digit = int(config_key[-1])
        normalized_score *= (1.0 + 0.1 * mode_digit)
    
    # Tertiary adjustment via dictionary mapping (actual impact)
    adjustment_map = {1: 0.85, 2: 0.92, 3: 1.05, 4: 1.15}
    adjustment = adjustment_map.get(3, 1.0)  # uses key 3
    final_adjusted = normalized_score * adjustment
    
    return final_adjusted

# Simulated input data
raw_timings = [0.12, 0.33, 0.21, 0.88, 0.47, 0.63, 0.55, 0.71]
timing_data = preprocess_readings([t * 1.02 for t in raw_timings])

# Calibration matrix with meaningful structure
calibration_indices = list(range(len(timing_data)))
calibration_values = [math.cos(i * 0.4) for i in calibration_indices]
calibration_matrix = [max(0.1, abs(cv)) for cv in calibration_values]

# Dead code path - creates irrelevant data structure
dummy_grid = [[i*j for j in range(5)] for i in range(5)]

# Auxiliary unused statistics
decoy_mean = sum(timing_data) / len(timing_data)
decoy_variance = sum((x - decoy_mean)**2 for x in timing_data) / len(timing_data)

# Key statement
final_diagnostic = aggregate_metrics(timing_data, calibration_matrix)

# Print result
print(f"Result: {final_diagnostic}")