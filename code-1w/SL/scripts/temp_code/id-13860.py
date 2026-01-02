import itertools

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_samples = [0.88, 0.76, 0.91, 0.45, 0.23, 0.67, 0.78, 0.34]
    sample_weights = [1, 2, 1, 3, 2, 1, 2, 1]
    weighted_sum = sum(s * w for s, w in zip(raw_samples, sample_weights))
    normalization_factor = sum(sample_weights)
    normalized_score = weighted_sum / normalization_factor
    return raw_samples, normalized_score

# Irrelevant auxiliary function (dead path)
def calculate_redundant_metric(data):
    cumulative = 0
    for i in range(len(data)):
        if i % 2 == 0:
            cumulative += data[i] ** 2
    return cumulative * 1.5  # Not used in main logic

# Signal conditioning with multiple distractions
def preprocess_signal(samples):
    offset_compensation = 0.1
    adjusted = [max(0, s - offset_compensation) for s in samples]
    
    # Distractor: complex smoothing with unused variants
    smoothed_v1 = [sum(adjusted[i:i+3]) / 3 for i in range(len(adjusted)-2)]
    smoothed_v2 = list(itertools.accumulate(adjusted))
    active_segments = [val for val in adjusted if val > 0.5]
    
    # Actual relevant transformation
    amplified = [val ** 1.5 for val in active_segments]
    return amplified

# Misleading intermediate analysis (unused)
def evaluate_stability(signal):
    diffs = [abs(signal[i] - signal[i-1]) for i in range(1, len(signal))]
    return sum(diffs) / len(diffs) < 0.3

# Core diagnostic logic
def generate_threshold_map(config_level=3):
    base_map = {'low': 0.4, 'medium': 0.65, 'high': 0.8}
    scaling_factors = [1.1, 1.2, 1.3]
    
    # Complex but irrelevant expansion
    expanded = {}
    for key in base_map:
        for i, factor in enumerate(scaling_factors):
            expanded[f'{key}_tier{i+1}'] = base_map[key] * factor
    
    # Relevant simplified map actually used
    used_map = {
        'crit': base_map['high'] * scaling_factors[config_level-1],
        'warn': base_map['medium'],
        'info': base_map['low']
    }
    
    # Dead code: unused statistics
    avg_threshold = sum(used_map.values()) / len(used_map)
    threshold_variance = sum((v - avg_threshold) ** 2 for v in used_map.values())
    
    return used_map

# Main analysis with red herrings
def analyze_signal(amplified_signal, thresholds):
    critical_level = thresholds['crit']
    warning_level = thresholds['warn']
    
    # Multiple counting mechanisms - only one matters
    count_critical = 0
    count_warning = 0
    total_energy = 0
    peak_magnitude = 0
    
    for val in amplified_signal:
        total_energy += val
        if val > peak_magnitude:
            peak_magnitude = val
        if val >= critical_level:
            count_critical += 1
        elif val >= warning_level:
            count_warning += 1
    
    # Distractor: entropy-like calculation (unused)
    probabilities = [val / total_energy for val in amplified_signal if total_energy > 0]
    import math
    shannon_entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    
    # Another dead path: pattern matching
    pattern_matches = 0
    for a, b in itertools.pairwise(amplified_signal):
        if a > b and a > critical_level:
            pattern_matches += 1
    
    # The real decision logic (non-obvious due to noise)
    if count_critical >= 2:
        diagnostic_code = 900 + int(total_energy)
    elif count_warning >= 3:
        diagnostic_code = 700 + int(peak_magnitude * 10)
    else:
        diagnostic_code = 500 + len(amplified_signal)
    
    # Final red herring: bitwise manipulation (unused)
    debug_flag = (count_critical << 3) | (pattern_matches & 7)
    final_checksum = (diagnostic_code ^ debug_flag) & 0xFFFF
    
    return diagnostic_code  # Only this matters

# Orchestration with misleading flow
if __name__ == '__main__':
    readings, score = collect_sensor_readings()
    processed_data = preprocess_signal(readings)
    
    # Unused alternative processing path
    alt_path = False
    if score > 1.0:
        processed_data = [x * 2 for x in processed_data]
        alt_path = True
    
    # This function call contains the key execution point
    threshold_map = generate_threshold_map(config_level=3)
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Print required result
    print(f"Result: {final_diagnostic}")