import itertools

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw_stream = [18, 22, 15, 30, 45, 10, 60, 50]
    offset_correction = 5
    corrected = [x - offset_correction for x in raw_stream]
    return corrected

# Irrelevant helper - dead path
def legacy_calibrate(x):
    return (x * 0.95) + 2

# Unused transformation
transform_weights = [0.1, 0.3, 0.4, 0.2]
scaled_values = [w * 100 for w in transform_weights]  # Distractor list

# Signal filtering function
def filter_noise(data, limit):
    filtered = []
    for val in data:
        if val > limit:
            filtered.append(val)
    padding = [0] * (8 - len(filtered))
    return filtered + padding  # padded to fixed length

# Checksum calculator - looks important but unused
def compute_checksum(seq):
    checksum = 0
    for i, v in enumerate(seq):
        checksum ^= (v + i) * 3
    return checksum

# Data normalization (actually used in chain)
def normalize_sequence(seq):
    mean_val = sum(seq) / len(seq)
    normalized = [(x - mean_val) * 1.5 for x in seq]
    rounded = [round(x, 2) for x in normalized]
    return rounded

# Threshold mapping generator (used later)
def generate_thresholds(base):
    thresholds = {}
    for key in ['T1', 'T2', 'T3', 'T4']:
        thresholds[key] = base * 2 if 'T1' in key else base * 1.5
    thresholds['T2'] = base * 0.8
    thresholds['T5'] = base * 1.1  # extra key
    return thresholds

# Diagnostic analyzer core
# Combines bitwise logic, comparisons, and dictionary lookups
def analyze_signal(signal, config):
    active_peaks = 0
    total_power = 0
    
    for i in range(len(signal)):
        if signal[i] > config['T1']:
            active_peaks += 1
            total_power += signal[i]
    
    # Secondary condition with bit manipulation
    power_flag = total_power & 255
    peak_flag = active_peaks << 2
    combined_flag = power_flag ^ peak_flag
    
    # Tertiary check using itertools to simulate scan
    slices = [signal[i:i+2] for i in range(0, len(signal), 2)]
    valid_windows = 0
    for window in slices:
        if len(window) == 2 and window[0] < window[1]:
            valid_windows += 1
    
    # Decision matrix
    if active_peaks >= 3 and total_power > config['T1']:
        stage_score = 25000
    elif valid_windows >= 2:
        stage_score = 15000
    else:
        stage_score = 5000
    
    # Final computation - only this matters
    adjustment = config['T2'] * 10
    final_score = stage_score + adjustment + combined_flag
    
    # Critical red herring: complex unused calculation
    decoy_entropy = 0
    for pair in itertools.combinations(signal, 2):
        decoy_entropy += abs(pair[0] - pair[1])
    decoy_entropy = round(decoy_entropy / 1000, 3)  # looks important
    
    # Another distraction: unused tuple unpacking
    meta_info = ('diagnostic', 'version_2', 'active')
    status, version, mode = meta_info
    
    # Actual return
    return int(final_score)

# Main execution flow
if __name__ == '__main__':
    readings = collect_readings()  # [13, 17, 10, 25, 40, 5, 55, 45]
    cleaned = filter_noise(readings, 12)
    processed_data = normalize_sequence(cleaned)
    
    # Unused slicing operation
    mid_segment = processed_data[2:6]
    reversed_half = processed_data[::-1]
    
    # Generate configuration map
    threshold_map = generate_thresholds(20)
    
    # Unused set operation
    unique_levels = set(threshold_map.values())
    extended_adjustment = sum(unique_levels) / len(unique_levels)
    
    # Key assignment
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")