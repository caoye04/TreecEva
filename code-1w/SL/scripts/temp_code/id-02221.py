import math

def preprocess_signal(raw_data):
    filtered = [x for x in raw_data if x > -50 and x < 50]
    baseline = sum(filtered) / len(filtered)
    normalized = [x - baseline for x in filtered]
    return normalized

def compute_entropy(values):
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 6)

def validate_checksum(data, expected):
    actual = sum(data) % 1000
    return actual == expected

def generate_frequency_profile(readings):
    profile = {}
    for i, val in enumerate(readings):
        bucket = i % 7
        profile[bucket] = profile.get(bucket, 0) + abs(val)
    return profile

def extract_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks[:5] if peaks else [0]

def merge_calibration_data(primary, secondary):
    merged = primary.copy()
    for key, value in secondary.items():
        if key in merged:
            merged[key] = (merged[key] + value) / 2
        else:
            merged[key] = value
    return merged

def calculate_phase_shift(sequence):
    shifted = [(x * 1.5) + 2 for x in sequence]
    return [int(x) for x in shifted]

def analyze_system_state(readings, calib_map):
    # Step 1: Preprocess signal
    processed = preprocess_signal(readings)
    
    # Irrelevant transformation (distractor)
    dummy_transform = [math.sin(x / 10) for x in readings[:10]]
    average_dummy = sum(dummy_transform) / len(dummy_transform)
    
    # Step 2: Extract key features
    peaks = extract_peaks(processed)
    peak_count = len(peaks)
    
    # Step 3: Compute entropy of processed signal
    signal_entropy = compute_entropy(processed)
    
    # Dead code path - never used (red herring)
    if peak_count > 10:
        fallback = [x for x in processed if x % 2 == 0]
        fallback_result = sum(fallback)

    # Step 4: Use calibration map to adjust entropy
    adjustment_factor = 0
    for key in calib_map:
        if isinstance(key, int) and key % 3 == 0:
            adjustment_factor += calib_map[key]
    adjusted_entropy = signal_entropy * (1 + adjustment_factor / 10)
    
    # Step 5: Generate frequency profile (partially irrelevant)
    freq_profile = generate_frequency_profile(processed)
    max_freq_contribution = max(freq_profile.values()) if freq_profile else 0
    
    # Step 6: Simulate phase correction on peaks
    corrected_peaks = calculate_phase_shift(peaks)
    peak_sum = sum(corrected_peaks)
    
    # Step 7: Determine system mode based on entropy threshold (misleading intermediate)
    mode_flag = "STABLE" if adjusted_entropy > 2.0 else "FLUCTUATING"
    mode_score = 100 if mode_flag == "STABLE" else 50
    
    # Step 8: Final diagnostic calculation (critical)
    # Only peak_sum and adjusted_entropy are actually used in final result
    final_diagnostic = int(peak_sum + adjusted_entropy * 1000)
    
    # Unused complex structure (distractor)
    diagnostics_log = {
        'raw_peak_count': peak_count,
        'entropy_raw': signal_entropy,
        'adjustment_applied': adjustment_factor,
        'frequency_energy': max_freq_contribution,
        'mode': mode_flag,
        'timestamp': '2023-12-05',
        'checksum_valid': validate_checksum(processed, 456)
    }
    
    # Another decoy computation
    outlier_set = {x for x in processed if abs(x) > 20}
    if len(outlier_set) > 5:
        closure_value = sum(outlier_set) / len(outlier_set)
    else:
        closure_value = 0
    
    return final_diagnostic

# Main execution block
quantum_readings = [42, -18, 73, 15, -44, 89, 6, -27, 91, 33, 58, -61, 4, 77, -35, 82, 19, -50, 64, 26]
calibration_map = {2: 0.4, 3: 0.7, 6: 0.5, 9: 0.8, 'offset_x': 1.1, 'offset_y': 0.9}

# Execute analysis
final_diagnostic = analyze_system_state(quantum_readings, calibration_map)
print(f"Result: {final_diagnostic}")