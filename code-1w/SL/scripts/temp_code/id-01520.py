import math

# Simulated sensor array data from environmental monitoring system
def acquire_sensor_data():
    raw_values = [127, 255, 18, 92, 64, 203, 45, 150]
    timestamps = [1634567890 + i * 30 for i in range(8)]
    metadata = {'location': 'Zone B7', 'version': '2.1'}
    return list(zip(timestamps, raw_values))

# Signal processing pipeline
def filter_noise(data_pairs):
    filtered = []
    noise_floor = 20
    for ts, val in data_pairs:
        if val > noise_floor:
            corrected = val * 0.87 + 5  # empirical calibration
            filtered.append((ts, int(corrected)))
        else:
            filtered.append((ts, 0))
    return filtered

# Legacy compatibility shim (unused but looks relevant)
def legacy_transform(sequence):
    """Outdated transformation, no longer used in pipeline."""
    return [x ^ 0xFF for x in sequence]

# Core signal processor
def extract_magnitude(signal_list):
    magnitudes = [val for ts, val in signal_list if val > 0]
    if not magnitudes:
        return [0]
    avg = sum(magnitudes) / len(magnitudes)
    deviation = [abs(x - avg) for x in magnitudes]
    consistency_score = sum(1 for d in deviation if d < 30)
    threshold = 2 if consistency_score > 4 else 3
    
    # Apply adaptive windowing
    windows = [magnitudes[i:i+threshold] for i in range(0, len(magnitudes), threshold)]
    processed = []
    for window in windows:
        if len(window) == threshold:
            processed.append(int(sum(window) / len(window)))
    return processed if processed else [avg]

# Checksum validation (distractor function - appears important)
def validate_checksum(arr):
    checksum = 0
    for i, x in enumerate(arr):
        checksum ^= (x + i) * 3
    return format(checksum % 256, '02X')

# Secondary analysis with red herring output
def compute_oscillation_index(peaks):
    if len(peaks) < 2:
        return 0.0
    diffs = [peaks[i+1] - peaks[i] for i in range(len(peaks)-1)]
    mean_diff = sum(diffs) / len(diffs)
    variance = sum((d - mean_diff) ** 2 for d in diffs) / len(diffs)
    fake_stability_metric = math.exp(-variance / 100)  # looks sophisticated
    return round(fake_stability_metric * 100, 3)

# Main diagnostic engine
def analyze_readings(amplitudes):
    base_score = sum(amplitudes) * 1.75
    
    # Complexity through conditional weighting
    if len(amplitudes) >= 4:
        weight = 1.2
        adjustment = sum(1 for x in amplitudes if x > 100)
        if adjustment > 2:
            weight += 0.3
            temp_array = [x * 2 for x in amplitudes if x > 90]  # unused computation
            temp_sum = sum(temp_array) % 1000  # misleading intermediate
        else:
            weight += 0.1
    else:
        weight = 0.8
    
    refined_score = base_score * weight
    
    # Additional logic layer
    peak_count = len([x for x in amplitudes if x > 110])
    if peak_count >= 3:
        refined_score += 25.5
        # Decoy block: looks like it affects result but doesn't change core path
        decoy_factor = 0
        for i in range(3):
            decoy_factor += math.sin(refined_score / (i + 1))
        final_adjustment = abs(decoy_factor) % 10
        refined_score += final_adjustment  # actually contributes
    
    # Final non-linear transformation
    final_diagnostic = int(refined_score + 0.5)  # round to nearest integer
    return final_diagnostic

# Orchestration function
def run_diagnostics():
    # Step 1: Acquire raw data
    sensor_data = acquire_sensor_data()
    
    # Step 2: Filter out noise
    cleaned_signals = filter_noise(sensor_data)
    
    # Step 3: Extract meaningful magnitudes
    extracted_peaks = extract_magnitude(cleaned_signals)
    
    # Irrelevant transformation (distractor)
    transformed_legacy = legacy_transform(extracted_peaks)
    legacy_checksum = validate_checksum(transformed_legacy)
    
    # Step 4: Run primary analysis
    oscillation_index = compute_oscillation_index(extracted_peaks)
    
    # Step 5: Critical diagnostic computation
    final_diagnostic = analyze_readings(extracted_peaks)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")
    
    # Unused debugging artifacts
    debug_snapshot = {
        'raw_length': len(sensor_data),
        'filtered_nonzero': len([v for _, v in cleaned_signals if v > 0]),
        'peak_variability': max(extracted_peaks) - min(extracted_peaks),
        'dummy_flag': False
    }
    
    return final_diagnostic

# Execute main process
result = run_diagnostics()