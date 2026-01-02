import math

# Simulated sensor array data from environmental monitoring station
def fetch_sensor_data():
    raw_readings = [23.4, 19.8, 20.1, 25.3, 18.7, 22.0, 20.5, 19.3, 21.8, 24.6]
    calibration_offset = 1.2
    adjusted = [r + calibration_offset for r in raw_readings]
    return adjusted

# Legacy function - unused but looks relevant
def legacy_normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Signal processing pipeline
def filter_outliers(readings, threshold=2.0):
    mean = sum(readings) / len(readings)
    std_dev = (sum((x - mean) ** 2 for x in readings) / len(readings)) ** 0.5
    filtered = [x for x in readings if abs(x - mean) <= threshold * std_dev]
    return filtered

# Frequency domain transformation (distraction)
def compute_fft_magnitude(signal):
    N = len(signal)
    fft_real = [sum(signal[k] * math.cos(2 * math.pi * k * n / N) for k in range(N)) for n in range(N)]
    fft_imag = [sum(-signal[k] * math.sin(2 * math.pi * k * n / N) for k in range(N)) for n in range(N)]
    magnitudes = [math.sqrt(r*r + i*i) for r, i in zip(fft_real, fft_imag)]
    return magnitudes  # Never used

# Main processing with multiple distractions
def process_signal_chain(raw_data):
    # Initial filtering
    cleaned = filter_outliers(raw_data)
    
    # Red herring: frequency analysis
    spectral = compute_fft_magnitude(cleaned)
    dominant_freq_index = spectral.index(max(spectral)) if spectral else 0
    
    # Real processing begins
    window_size = 3
    smoothed = []
    for i in range(len(cleaned) - window_size + 1):
        window_avg = sum(cleaned[i:i+window_size]) / window_size
        smoothed.append(round(window_avg, 2))
    
    # Distractor: string-based status tracking
    status_log = "Processing completed at level {}"
    levels = ['LOW', 'MEDIUM', 'HIGH']
    for lvl in levels:
        status_log.format(lvl)  # Useless formatting
    
    # Set operation to track unique rounded values (partially relevant)
    unique_bases = set(int(x) for x in cleaned)
    base_count = len(unique_bases)
    
    # Slicing to extract mid-range segment
    mid_segment = smoothed[len(smoothed)//4 : len(smoothed)*3//4]
    
    # Decoy statistical measures
    pseudo_entropy = 0.0
    if mid_segment:
        for x in mid_segment:
            if x > 0:
                pseudo_entropy -= x * math.log(x)
    
    # Key transformation
    processed = [x * 1.08 for x in mid_segment]  # Climate adjustment factor
    
    # Dead code path - never executed due to logic
    extreme_values = []
    if False and len(processed) > 100:
        extreme_values = [x for x in processed if x > 30.0]
    
    return processed

# Diagnostic engine with conditional logic
def analyze_readings(signals):
    if not signals:
        return -999
    
    # Determine operational mode based on signal length
    mode_flag = 'A' if len(signals) % 2 == 0 else 'B'
    
    # Initialize multiple accumulators (some irrelevant)
    total_power = 0.0
    diagnostic_score = 0
    harmonic_weight = 0
    temporal_drift = 0.0
    
    # Primary diagnostic calculation
    for i, val in enumerate(signals):
        total_power += val ** 2
        
        # Conditional update - only even indices contribute
        if i % 2 == 0:
            diagnostic_score += int(val)
        
        # Red herring accumulation
        if val > 20.0:
            temporal_drift += val - 20.0
        
        # Bit manipulation distraction
        bit_shifted = int(val) ^ 0b1010
        bit_shifted = bit_shifted << 1 & 0b1111
        harmonic_weight += bit_shifted  # Accumulates but unused
    
    # Secondary validation chain
    reference_set = {18, 19, 20, 21, 22}
    signal_bases = set(int(s) for s in signals)
    overlap = reference_set & signal_bases
    coverage_ratio = len(overlap) / len(reference_set)
    
    # Final fusion logic (determines answer)
    if coverage_ratio >= 0.6:
        final_diagnostic = diagnostic_score * 2 + int(total_power // 10)
    else:
        final_diagnostic = int(temporal_drift * 10)
    
    # Dead assignment - doesn't affect result
    final_diagnostic = final_diagnostic | 0b1000 if len(signals) > 5 else final_diagnostic
    
    return final_diagnostic

# Orchestration with decoy control flow
def main_pipeline():
    # Fetch and preprocess
    raw = fetch_sensor_data()
    
    # Unused alternative processing path
    if sum(raw) / len(raw) < 20:
        pass  # Placeholder for alternate logic (never reached in practice)
    
    # Critical processing chain
    processed_signals = process_signal_chain(raw)
    
    # Final diagnostic computation
    final_diagnostic = analyze_readings(processed_signals)
    
    # Irrelevant post-processing
    report_summary = "Diagnostics: {}".format(final_diagnostic)
    summary_length = len(report_summary)
    
    # Output required result
    print(f"Result: {final_diagnostic}")

# Execute
main_pipeline()