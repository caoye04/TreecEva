import math

# Simulated sensor data acquisition and analysis system
def acquire_signal():
    raw_samples = [i * 0.01 for i in range(1000)]
    noise_floor = sum([math.sin(x * 0.5) * 2.3 for x in raw_samples[:100]])
    signal_power = sum([abs(math.cos(x) * 1.7) for x in raw_samples[::10]])
    return raw_samples, noise_floor, signal_power

# Irrelevant helper: calculates dummy entropy (not used in final result)
def compute_entropy(data):
    if not data:
        return 0.0
    hist = {}
    for d in data:
        hist[d] = hist.get(d, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in hist.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

# Signal preprocessing with distractor operations
def preprocess(signal_list, threshold=0.5):
    # Real processing steps
    filtered = [x for x in signal_list if abs(math.sin(x)) > threshold]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-8) for x in filtered]
    
    # Distractor: slicing and string conversion (irrelevant)
    sample_slice = signal_list[100:150:2]
    slice_as_str = ''.join([str(int(abs(x)*10)) for x in sample_slice[:5]])
    checksum = sum([int(c) for c in slice_as_str if c.isdigit()])
    
    # More red herring: unused transformation chain
    temp_transform = [math.tan(x) for x in normalized if x < 0.9]
    if len(temp_transform) > 10:
        inverted = [1.0 / (1 + x) for x in temp_transform]
        reshaped = [[inverted[i], inverted[i+1]] for i in range(0, len(inverted)-1, 2)][:10]
    else:
        reshaped = []
    
    # Actual output used downstream
    compressed = [normalized[i] for i in range(0, len(normalized), 3)]
    return compressed

# Recursive frequency analysis (only partially relevant)
def recursive_peak_detect(data, depth=0, max_depth=3):
    if depth >= max_depth or len(data) < 2:
        return [data[0]] if data else []
    mid = len(data) // 2
    left_peaks = recursive_peak_detect(data[:mid], depth + 1, max_depth)
    right_peaks = recursive_peak_detect(data[mid:], depth + 1, max_depth)
    local_max = max(data)
    return left_peaks + [local_max] + right_peaks

# Main analysis function with decoy logic
def analyze_signal(data_segment):
    # Real computation branch
    avg_val = sum(data_segment) / len(data_segment)
    squared_devs = [(x - avg_val) ** 2 for x in data_segment]
    variance = sum(squared_devs) / len(squared_devs)
    std_dev = math.sqrt(variance)
    z_scores = [abs(x - avg_val) / std_dev for x in data_segment]
    outliers = [z for z in z_scores if z > 2.0]
    
    # Decoy control flow with misleading intermediate
    if len(outliers) > 5:
        adjustment_factor = 0.85
    elif len(outliers) > 0:
        adjustment_factor = 1.12
    else:
        adjustment_factor = 1.0
    
    # Dead code path - never executed due to logic
    if False and adjustment_factor < 0.9:
        correction_map = {i: math.log(i+1) for i in range(len(data_segment))}
        data_segment = [data_segment[i] * correction_map[i] for i in range(len(data_segment))]
    
    # String-based distractor using method calls
    label_template = "DIAG_{}"
    labels = [label_template.format(i) for i in range(len(data_segment))]
    label_concat = ''.join(labels)
    label_checksum = sum([ord(c) for c in label_concat[::10]]) % 1000
    
    # Final calculation - only this matters
    peak_values = recursive_peak_detect(data_segment)
    if peak_values:
        primary_peak = max(peak_values)
        secondary_effect = math.log(len(data_segment) + 1)
        diagnostic_score = int((primary_peak * 1500) + secondary_effect * 10 - label_checksum)
    else:
        diagnostic_score = 0
    
    return diagnostic_score

# Orchestration with irrelevant setup
if __name__ == "__main__":
    # Acquire real data
    samples, floor, power = acquire_signal()
    
    # Compute irrelevant entropy
    dummy_entropy = compute_entropy(samples[::50])
    
    # Process the signal (core relevant step)
    processed_data = preprocess(samples)
    
    # Additional distraction: simulate calibration
    calibration_sequence = "CALIBRATE_XYZ"
    calib_shift = sum([calibration_sequence.index(c) for c in "CAB" if c in calibration_sequence])
    
    # Critical execution point
    final_diagnostic = analyze_signal(processed_data)
    
    # Print required output
    print(f"Result: {final_diagnostic}")