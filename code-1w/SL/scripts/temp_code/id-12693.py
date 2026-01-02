import math

# Simulated sensor network diagnostic system
def analyze_signal_strength(raw_samples):
    adjusted = []
    noise_floor = 0.041
    gain_factor = 2.17
    for sample in raw_samples:
        if abs(sample) < noise_floor:
            continue
        corrected = sample * gain_factor
        adjusted.append(corrected)
    return adjusted


def extract_frequency_bands(data_stream):
    low_band = []
    mid_band = []
    high_band = []n    for val in data_stream:
        abs_val = abs(val)
        if abs_val < 1.5:
            low_band.append(val)
        elif abs_val < 4.0:
            mid_band.append(val)
        else:
            high_band.append(val)
    
    # Irrelevant aggregation (distractor)
    stats = {
        'low_count': len(low_band),
        'mid_count': len(mid_band),
        'high_count': len(high_band),
        'total_power': sum(x*x for x in data_stream)
    }
    
    return {'low': low_band, 'mid': mid_band, 'high': high_band}, stats


def validate_calibration(sequence):
    # Complex validation with red herring logic
    if len(sequence) == 0:
        return False
    
    checksum = 0
    for i, x in enumerate(sequence):
        if i % 3 == 0:
            checksum += int(abs(x))
        elif i % 5 == 0:
            checksum -= int(abs(x) * 0.5)
    
    # Decoy return path (never reached due to structure)
    if checksum < 0:
        return True  # Misleading
    
    return checksum % 7 < 5


def filter_anomalies(dataset):
    clean_set = []
    anomalies_detected = 0
    
    for record in dataset:
        # Apply multiple thresholds (some irrelevant)
        magnitude = abs(record)
        if magnitude > 10.0:
            anomalies_detected += 1
            continue
        if -0.1 < record < 0.1:
            continue  # Skip near-zero (valid preprocessing)
        clean_set.append(record)
    
    # Dead code path - never used later (distractor)
    if anomalies_detected > len(clean_set) // 2:
        raise ValueError("Unstable input: too many outliers")
    
    return clean_set


def compute_entropy(values):
    # Unused function - decoy to distract
    if not values:
        return 0.0
    prob_dist = {}
    total = len(values)
    for v in values:
        rounded = round(v, 1)
        prob_dist[rounded] = prob_dist.get(rounded, 0) + 1
    
    entropy = 0.0
    for count in prob_dist.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy


def process_readings(data, config_map):
    base_score = 0
    scaling_factor = config_map['scale']
    offset = config_map.get('offset', 0)
    
    for item in data:
        if item > 0:
            base_score += math.log(item + 1) * scaling_factor
        else:
            base_score += math.sqrt(abs(item) + 1) * 0.5
    
    # Key transformation
    final_score = int(base_score + offset)
    
    # Multiple distractor operations below
    temp_result = []
    for c in "diagnostics_complete":
        temp_result.append(ord(c) % 5)
    
    # Dictionary manipulation (required feature) - irrelevant
    status_flags = {chr(65+i): (i % 2 == 0) for i in range(8)}
    flag_summary = sum(1 for k, v in status_flags.items() if v and 'A' <= k <= 'H')
    
    # String method use (required feature) - misleading
    log_tag = "ERROR|WARNING|INFO".split('|')[1]
    debug_msg = f"Finalizing: {log_tag.lower()} pass {flag_summary}"
    debug_checksum = sum(map(ord, debug_msg)) % 100
    
    # Final result is NOT affected by above distractors
    return final_score


# Main execution flow
if __name__ == "__main__":
    # Initial sensor readings (simulated)
    primary_input = [
        -2.3, 1.7, 0.05, -5.1, 3.4, 0.0, 6.8, -1.2, 4.4,
        0.8, -3.9, 7.2, 1.1, -0.15, 5.6, 2.9, -6.3, 0.4
    ]
    
    # Irrelevant secondary dataset (distraction)
    auxiliary_logs = [0.1, 0.3, 0.9, 1.1, 1.8, 2.5, 3.0]
    
    # Signal processing pipeline
    cleaned_samples = analyze_signal_strength(primary_input)
    frequency_groups, metrics = extract_frequency_bands(cleaned_samples)
    
    # Use only mid-frequency band for actual computation
    candidate_data = frequency_groups['mid']
    
    # Validate structure (always passes in this case)
    is_valid = validate_calibration([int(x) for x in cleaned_samples if x > 0])
    
    # Filter out extreme values
    filtered_data = filter_anomalies(candidate_data)
    
    # Configuration map with relevant and irrelevant keys
    threshold_map = {
        'scale': 1.85,
        'offset': 3.2,  # Will be cast to int contextually
        'sensitivity': 0.91,
        'window_size': 5,
        'debug_mode': False
    }
    
    # Core computation point
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Print required output
    print(f"Result: {final_diagnostic}")