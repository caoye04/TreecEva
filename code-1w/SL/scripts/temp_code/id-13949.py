import math

# Simulated sensor array data from environmental monitoring station
def acquire_sensor_data():
    raw_readings = [18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117]
    return raw_readings

# Legacy function - unused but looks relevant
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [x - mean_val for x in data]

# Signal processing pipeline
def filter_noise(signal, threshold=30):
    filtered = []
    for val in signal:
        if abs(val) > threshold:
            filtered.append(val)
    return filtered

# Frequency domain transformation (unused path)
def compute_fft_magnitude(signal):
    N = len(signal)
    fft_result = []
    for k in range(N):
        real = sum(signal[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        imag = -sum(signal[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        fft_result.append(math.sqrt(real**2 + imag**2))
    return [round(x, 3) for x in fft_result]

# Critical data transformation: windowing and scaling
def apply_hamming_window(signal):
    N = len(signal)
    windowed = []
    for i in range(N):
        window_factor = 0.54 - 0.46 * math.cos(2 * math.pi * i / (N - 1))
        windowed.append(signal[i] * window_factor)
    return windowed

# Data segmentation - extract region of interest
def segment_active_zone(data):
    # Middle third of the data contains relevant signal
    start_idx = len(data) // 3
    end_idx = 2 * len(data) // 3
    return data[start_idx:end_idx]

# Advanced feature extraction
def extract_spectral_peaks(windowed_data):
    peak_indices = []
    for i in range(1, len(windowed_data) - 1):
        if windowed_data[i] > windowed_data[i-1] and windowed_data[i] > windowed_data[i+1]:
            peak_indices.append(i)
    return peak_indices

# Secondary diagnostic (red herring)
def calculate_coherence_score(peaks):
    if len(peaks) < 2:
        return 0.0
    differences = [peaks[i+1] - peaks[i] for i in range(len(peaks)-1)]
    avg_diff = sum(differences) / len(differences)
    variance = sum((d - avg_diff)**2 for d in differences) / len(differences)
    return round(1 / (1 + variance), 4)

# Core analysis logic
def analyze_signal(samples):
    # Step 1: Apply non-linear transform
    transformed = [int(math.log(x) * 10) for x in samples if x > 0]
    
    # Step 2: Slice middle section (critical)
    mid_start = len(transformed) // 4
    mid_end = 3 * len(transformed) // 4
    focus_band = transformed[mid_start:mid_end]
    
    # Step 3: Bit manipulation for anomaly detection
    anomalies = 0
    for val in focus_band:
        bit_pattern = (val ^ (val << 1)) & 0xFF
        if bin(bit_pattern).count('1') % 3 == 0:
            anomalies += 1
    
    # Step 4: Conditional amplification
    base_score = sum(focus_band)
    if anomalies > len(focus_band) // 3:
        base_score = base_score * 2 // 3
    
    # Step 5: Final adjustment using index arithmetic
    adjustment = 0
    for i, v in enumerate(focus_band):
        if i % 3 == 0 and v % 4 == 2:
            adjustment += v // 5
    
    final_score = base_score - adjustment
    return final_score

# Unused diagnostic path (decoy)
def legacy_diagnostic_protocol(raw_data):
    cleaned = [x for x in raw_data if x % 9 == 0]
    stats = {}
    for val in cleaned:
        bucket = val // 18
n        if bucket not in stats:
            stats[bucket] = 0
        stats[bucket] += 1
    return sum(stats.values()) * 17

# Main execution flow
if __name__ == "__main__":
    # Acquire raw sensor input
    sensor_feed = acquire_sensor_data()
    
    # Irrelevant preprocessing steps (distractors)
    normalized_legacy = deprecated_normalization(sensor_feed)
    strong_components = filter_noise(sensor_feed, threshold=40)
    spectral_profile = compute_fft_magnitude(strong_components[:8])  # Partial use
    
    # Primary processing chain
    processed_signal = apply_hamming_window(sensor_feed)
    active_segment = segment_active_zone(processed_signal)
    refined_sample = filter_noise(active_segment, threshold=35)
    
    # Feature extraction (partially misleading)
    peaks_list = extract_spectral_peaks(refined_sample)
    coherence_metric = calculate_coherence_score(peaks_list)
    
    # Dead code path - looks important but unused
    dummy_frame = [math.sin(x/10) for x in sensor_feed]
    dummy_frame = [x for x in dummy_frame if x > 0.5]
    
    # Critical computation sequence
    sample_snapshot = refined_sample[::2]  # Every other sample
    processed_samples = [max(1, int(abs(x))) for x in sample_snapshot]
    
    # Key statement
    final_diagnostic = analyze_signal(processed_samples)
    
    # Output result
    print(f"Result: {final_diagnostic}")