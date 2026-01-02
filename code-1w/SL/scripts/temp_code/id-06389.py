import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [0.88, -0.32, 1.44, 0.12, -0.91]
    scale_factor = 3.5
    offset = 1.2
    calibrated = []
    for x in raw_samples:
        adjusted = (x * scale_factor) + offset
        calibrated.append(round(adjusted, 3))
    return calibrated

# Irrelevant auxiliary function – dead code path (distractor)
def legacy_compatibility_mode(data):
    if len(data) > 10:
        return sum([d ** 2 for d in data]) / len(data)
    else:
        temp_sum = 0
        for d in data:
            temp_sum += math.sqrt(abs(d) + 0.1)
        return temp_sum * 0.75

# Signal windowing – relevant preprocessing step
def apply_hamming_window(signal):
    N = len(signal)
    windowed = []
    for i in range(N):
        window_value = 0.54 - 0.46 * math.cos((2 * math.pi * i) / (N - 1))
        windowed.append(signal[i] * window_value)
    return windowed

# Checksum verification – misleading intermediate result (distractor)
def compute_checksum(data_list):
    checksum = 0
    for item in data_list:
        truncated = int(abs(item) * 100) % 256
        checksum ^= truncated
    return checksum  # Used nowhere – red herring

# Data smoothing via exponential moving average – actually used
def smooth_signal(signal, alpha=0.3):
    smoothed = [signal[0]]
    for i in range(1, len(signal)):
        new_val = alpha * signal[i] + (1 - alpha) * smoothed[-1]
        smoothed.append(round(new_val, 4))
    return smoothed

# Recursive frequency classification – key logic component
def classify_band(freq):
    if freq < 0.5:
        return 1
    elif freq < 1.5:
        return 2
    else:
        return 3 + classify_band(freq - 1.0)  # Simple recursion

# Main analysis pipeline – combines multiple concepts
def analyze_spectrum(magnitude_array):
    total_power = sum([m ** 2 for m in magnitude_array])
    avg_power = total_power / len(magnitude_array)
    band_counters = {1: 0, 2: 0, 3: 0}
    
    for mag in magnitude_array:
        norm_freq = mag / (avg_power + 1e-8)
        band = classify_band(norm_freq)
        if band <= 3:
            band_counters[band] += 1
        else:
            band_counters[3] += 1  # cap higher bands
    
    diversity_score = len(set(magnitude_array))
    return band_counters, diversity_score, avg_power

# Final diagnostic engine – computes target answer
def analyze_signal(input_data):
    # Step 1: Smooth and prepare
    filtered = smooth_signal(input_data)
    
    # Step 2: Apply window (relevant)
    processed_frame = apply_hamming_window(filtered)
    
    # Step 3: Analyze spectral characteristics
    bands, diversity, power_level = analyze_spectrum(processed_frame)
    
    # Step 4: Compute secondary metrics (some irrelevant)
    peak = max(processed_frame)
    entropy_proxy = 0
    for x in processed_frame:
        if x != 0:
            entropy_proxy -= x * math.log(abs(x))
    
    # Distractor variables (not used in final result)
    system_flag = "NORMAL"
    calibration_log = "CAL-OK"
    debug_trace = [len(input_data), len(set(input_data)), round(power_level, 2)]
    
    # Actual formula for final_diagnostic
    # Uses band distribution and diversity only
    b1, b2, b3 = bands[1], bands[2], bands[3]
    base_score = (b1 * 1.1) + (b2 * 2.3) + (b3 * 3.7)
    diversity_factor = math.sqrt(diversity)
    final_diagnostic = int(round(base_score * diversity_factor + 0.5))
    
    # Critical output point
    return final_diagnostic

# Unused function – decoy for configuration (distractor)
def get_system_defaults():
    defaults = {
        'gain': 2.0,
        'filter_type': 'butterworth',
        'version': '2.1a',
        'max_iter': 50
    }
    return defaults

# String-based metadata handler – uses string methods (required feature)
def parse_device_id(serial_tag):
    tag = serial_tag.strip().upper()
    if tag.startswith("DEV"):
        num_part = tag[3:].rstrip("X")
        if num_part.isdigit():
            return int(num_part)
    return -1

# Orchestration block
if __name__ == "__main__":
    # Real data flow
    raw_data = collect_readings()  # [3.88, 0.08, 6.24, 1.62, 0.015]
    
    # Irrelevant string operation (distractor)
    device_code = "  Dev982XX  "
    unit_id = parse_device_id(device_code)
    
    # Actual processing chain
    processed_data = smooth_signal(raw_data, alpha=0.35)
    processed_data = [round(x, 4) for x in processed_data]
    
    # Checksum computed but not used (misleading intermediate)
    chk = compute_checksum(processed_data)
    
    # Execute key statement
    final_diagnostic = analyze_signal(processed_data)
    
    # Output result
    print(f"Result: {final_diagnostic}")