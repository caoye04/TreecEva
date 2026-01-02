import math

# Simulated sensor data processing with embedded diagnostics
def acquire_signal():
    raw_samples = [i * 0.5 + math.sin(i) for i in range(20)]
    offset = 42  # Irrelevant calibration constant (red herring)
    scale_factor = 1.0  # Unused parameter
    return raw_samples

# Noise filtering using moving average (relevant)
def filter_noise(signal, window=3):
    filtered = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        end = i + 1
        window_avg = sum(signal[start:end]) / (end - start)
        filtered.append(window_avg)
    return filtered

# Frequency domain analysis stub (dead code path - misleading)
def compute_fft(samples):
    fft_size = len(samples)
    dummy_result = [0] * fft_size
    for k in range(fft_size):
        real_part = 0
        imag_part = 0
        for n in range(fft_size):
            angle = 2 * math.pi * k * n / fft_size
            real_part += samples[n] * math.cos(angle)
            imag_part -= samples[n] * math.sin(angle)
        dummy_result[k] = complex(real_part, imag_part)
    return dummy_result  # Never used

# Data normalization (relevant)
def normalize(data):
    min_val = min(data)
    max_val = max(data)
    if max_val == min_val:
        return [0.0] * len(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Outlier detection via IQR (partially relevant but results ignored)
def detect_outliers_iqr(values):
    sorted_vals = sorted(values)
    q1_idx = len(sorted_vals) // 4
    q3_idx = 3 * len(sorted_vals) // 4
    q1 = sorted_vals[q1_idx]
    q3 = sorted_vals[q3_idx]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = [v for v in values if v < lower_bound or v > upper_bound]
    return outliers  # Computed but not used

# Signal feature extraction (relevant)
def extract_features(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    peak_to_peak = max(data) - min(data)
    zero_crossings = 0
    for i in range(1, len(data)):
        if (data[i-1] < 0 and data[i] >= 0) or (data[i-1] > 0 and data[i] <= 0):
            zero_crossings += 1
    return {
        'mean': mean_val,
        'variance': variance,
        'peak_to_peak': peak_to_peak,
        'zero_crossings': zero_crossings
    }

# Decoy transformation using lambda and slicing (distractor)
def apply_envelope(signal):
    envelope = list(map(lambda x: x * 0.9 + 0.1, signal[::2]))  # Uses lambda and slicing
    padded = [0.0] * len(signal)
    for i, e in enumerate(envelope):
        padded[i*2] = e
    return padded  # Result discarded later

# Core diagnostic logic (key path)
def analyze_signal(cleaned_data):
    features = extract_features(cleaned_data)
    
    # Secondary processing branch (irrelevant)
    transformed = [math.log(1 + abs(x)) for x in cleaned_data]
    transformed_set = set(transformed)  # Set operation (distractor)
    size_check = len(transformed_set) > 10
    
    # Actual decision logic
    stability_score = features['variance']
    activity_level = features['zero_crossings']
    
    # Diagnostic rule: high variance + low zero crossings = unstable decay
    if stability_score > 0.1 and activity_level < 5:
        diagnosis = 867
    elif stability_score <= 0.05:
        diagnosis = 241
    else:
        diagnosis = 512
    
    # Redundant bit manipulation (misleading)
    mask = 0b1111
    masked_diagnosis = diagnosis & mask
    
    # Final computation
    final_weight = len(cleaned_data) % 7
    weighted_result = masked_diagnosis * final_weight
    
    return weighted_result

# Orchestration function
def main_pipeline():
    # Step 1: Acquire raw data
    signal = acquire_signal()
    
    # Step 2: Filter noise
    denoised = filter_noise(signal)
    
    # Step 3: Normalize amplitude
    normalized = normalize(denoised)
    
    # Step 4: Perform irrelevant outlier check
    anomalies = detect_outliers_iqr(normalized)  # Computed but unused
    
    # Step 5: Apply useless envelope modulation
    enveloped = apply_envelope(normalized)  # Dead end
    
    # Step 6: Extract meaningful features
    processed_data = normalized  # Final input to analyzer
    
    # Step 7: Run frequency analysis (discarded)
    spectrum = compute_fft(signal)  # Distractor computation
    spectral_entropy = sum(abs(s.real) for s in spectrum) / len(spectrum) if spectrum else 0  # Unused
    
    # Step 8: Analyze and generate diagnostic
    final_diagnostic = analyze_signal(processed_data)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")
    
    # Additional decoy output
    debug_flag = True
    if debug_flag:
        extra_diag = sum([len(str(ord(c))) for c in 'diagnostics'])  # Meaningless
        print(f"Debug hash: {extra_diag}")  # Not the answer
    
    return final_diagnostic

# Execute
if __name__ == "__main__":
    main_pipeline()