import math

# Sensor calibration data (partially irrelevant)
calibration_factors = {'sensor_a': 1.02, 'sensor_b': 0.98, 'sensor_c': 1.01}
offset_values = [0.1, -0.05, 0.03]

def preprocess_signal(raw_signal, gain=1.0, filter_noise=True):
    # Apply gain and basic noise suppression (only partially used)
    signal = [x * gain for x in raw_signal]
    if filter_noise:
        smoothed = []
        for i in range(len(signal)):
            neighbors = signal[max(0, i-1):min(i+2, len(signal))]
            smoothed.append(sum(neighbors) / len(neighbors))
        return smoothed
    return signal

def transform_coordinates(x_vals, y_vals):
    # Unused geometric transformation (red herring)
    polar_r = []
    polar_theta = []
    for i in range(len(x_vals)):
        r = math.sqrt(x_vals[i]**2 + y_vals[i]**2)
        theta = math.atan2(y_vals[i], x_vals[i])
        polar_r.append(r)
        polar_theta.append(theta)
    return polar_r, polar_theta

def compute_entropy(data):
    # Irrelevant statistical measure (distractor function)
    total = sum(data)
    probabilities = [x / total for x in data if x > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 4)

def recursive_window_sum(values, window_size, index=None):
    # Recursively computes overlapping window sums (misleading complexity)
    if index is None:
        index = len(values) - 1
    if index < 0:
        return []
    start = max(0, index - window_size + 1)
    current_sum = sum(values[start:index+1])
    result = recursive_window_sum(values, window_size, index - 1)
    result.append(current_sum)
    return result

def extract_peaks(signal, min_gap=3):
    # Detect peaks with minimum separation (unused path)
    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            if not peaks or i - peaks[-1] >= min_gap:
                peaks.append(i)
    return peaks

def accumulate_with_decay(values, decay_factor=0.9):
    # Accumulate with exponential decay (dead code path)
    acc = 0
    series = []
    for v in values:
        acc = acc * decay_factor + v
        series.append(acc)
    return series

def validate_checksum(data_chunk):
    # Dummy checksum validation (irrelevant security check)
    checksum = 0
    for val in data_chunk:
        checksum ^= int(val * 100) % 256
    return checksum == 0

def normalize_dataset(dataset):
    # Normalize each list in dataset (unused preprocessing)
    normalized = []
    for seq in dataset:
        mean_val = sum(seq) / len(seq)
        std_val = math.sqrt(sum((x - mean_val)**2 for x in seq) / len(seq))
        norm_seq = [(x - mean_val) / std_val for x in seq]
        normalized.append(norm_seq)
    return normalized

def sort_by_magnitude(data_dict):
    # Sort dictionary by absolute value of entries (decoy operation)
    return dict(sorted(data_dict.items(), key=lambda x: abs(x[1]), reverse=True))

def shift_register_update(current_state, input_val, mode='left'):
    # Simulate register shift (irrelevant hardware mimicry)
    new_state = current_state[1:] + [input_val]
    if mode == 'right':
        new_state = [input_val] + current_state[:-1]
    return new_state

def modular_average(values, modulus=7):
    # Compute average under modular arithmetic (distractor calc)
    total_mod = sum(v % modulus for v in values)
    return total_mod / len(values)

def decode_bit_pattern(pattern_list):
    # Convert list of bits to integer (unused decoding)
    binary_str = ''.join(str(int(p % 2)) for p in pattern_list)
    if not binary_str:
        return 0
    return int(binary_str, 2)

def analyze_readings(data_sequence, thresholds):
    # Core analysis logic: count how many readings exceed dynamic thresholds
    count = 0
    for i, val in enumerate(data_sequence):
        # Use modular arithmetic to select threshold dynamically
        selector = i % len(thresholds)
        threshold_key = list(thresholds.keys())[selector]
        if val > thresholds[threshold_key]:
            count += 1
    return count

def main():
    # Raw sensor inputs
    raw_readings = [0.45, 0.67, 0.33, 0.89, 0.56, 0.78, 0.21, 0.91, 0.12, 0.64]
    
    # Preprocess signal with default parameters
    processed_signal = preprocess_signal(raw_readings, gain=1.1)
    
    # Define threshold map for dynamic comparison (critical)
    threshold_map = {
        't_urgent': 0.75,
        't_high': 0.6,
        't_medium': 0.4,
        't_low': 0.2
    }
    
    # Perform entropy analysis (distraction)
    _ = compute_entropy(processed_signal)
    
    # Recursive window sum on processed signal (misleading intermediate)
    _ = recursive_window_sum(processed_signal, window_size=3)
    
    # Simulate multiple irrelevant operations
    _ = sort_by_magnitude(calibration_factors)
    _ = modular_average(raw_readings, modulus=5)
    
    # Actual key processing: apply final analysis
    processed_data = [round(x, 2) for x in processed_signal]
    
    # Key statement: analyze readings against threshold map
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")

if __name__ == "__main__":
    main()