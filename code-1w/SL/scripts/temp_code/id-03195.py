import math

# Simulated sensor array data from environmental monitoring station
def acquire_sensor_data():
    raw_values = [127, 255, 192, 64, 224, 32, 160, 96]
    noise_floor = 15
    adjusted = [x - noise_floor for x in raw_values if x > noise_floor]
    return adjusted

# Legacy function - unused but looks relevant
def deprecated_normalization(data):
    max_val = max(data)
    return [round(x / max_val, 3) for x in data]

# Signal conditioning with red herring operations
def preprocess_signal(raw_signal):
    amplified = [x * 1.8 for x in raw_signal]
    filtered = [x for x in amplified if x > 100 and x < 400]
    
    # Distractor: irrelevant frequency analysis
    sample_rate = 44100
    nyquist = sample_rate // 2
    frequencies = [abs(math.sin(i * 0.1)) * nyquist for i in range(len(filtered))]
    avg_frequency = sum(frequencies) / len(frequencies) if frequencies else 0
    
    # Real transformation: apply logarithmic compression
    compressed = [math.log(x) if x > 1 else 0 for x in filtered]
    return compressed

# Secondary processing path - dead code branch
def alternative_processing(chain):
    if len(chain) == 0:
        return [0]
    result = []
    for i in range(len(chain)-1):
        diff = chain[i+1] - chain[i]
        result.append(diff ** 2)
    return result

# Core diagnostic logic
def extract_features(signal_segments):
    means = [sum(segment) / len(segment) for segment in signal_segments if len(segment) > 0]
    variances = []
    for m, seg in zip(means, signal_segments):
        variance = sum((x - m) ** 2 for x in seg) / len(seg)
        variances.append(variance)
    
    # Distractor: unused spatial correlation matrix
    spatial_matrix = [[i * j + 0.1 for j in range(3)] for i in range(3)]
    eigen_approx = sum(spatial_matrix[i][i] for i in range(3))
    
    # Only return meaningful aggregated metrics
    return {
        'avg_mean': sum(means) / len(means),
        'avg_variance': sum(variances) / len(variances)
    }

# Main analysis pipeline
def analyze_readings(clean_signal):
    # Break signal into overlapping windows
    window_size = 3
    step = 1
    segments = []
    for i in range(0, len(clean_signal) - window_size + 1, step):
        segment = clean_signal[i:i+window_size]
        segments.append(segment)
    
    # Extract statistical features
    features = extract_features(segments)
    
    # Distractor: power spectral density estimation (unused)
    psd_estimates = []    
    for seg in segments:
        psd_bin = sum(math.cos(x * 0.5) ** 2 for x in seg)
        psd_estimates.append(psd_bin)
    
    # Red herring: entropy calculation with no impact
    def shannon_entropy(data):
        from collections import Counter
        counts = Counter([round(x, 1) for x in data])
        total = sum(counts.values())
        probs = [c/total for c in counts.values()]
        return -sum(p * math.log2(p) for p in probs if p > 0)
    
    entropy_value = shannon_entropy(clean_signal)
    
    # Critical computation: diagnostic score based on feature thresholds
    mean_score = features['avg_mean'] * 1.5
    variance_penalty = features['avg_variance'] * 0.7
    diagnostic_score = mean_score - variance_penalty
    
    # Final adjustment using bitwise manipulation (actual key step)
    int_component = int(diagnostic_score)
    fractional = diagnostic_score - int_component
    final_score = int_component ^ 255  # Bitwise XOR with magic number
    final_score += fractional
    
    return final_score

# Orchestration function with misleading branches
def system_diagnostics(run_full_analysis=True, debug_mode=False):
    # Primary execution path
    raw_data = acquire_sensor_data()
    processed_signals = preprocess_signal(raw_data)
    
    # Dead branch: never executed due to flag
    calibration_sequence = []
    if debug_mode:
        for i in range(5):
            temp_cal = (i * 17) % 255
n            calibration_sequence.append(temp_cal)
    
    # Another distractor: historical baseline comparison
    historical_avg = 4.872
    current_avg = sum(processed_signals) / len(processed_signals) if processed_signals else 0
    deviation = abs(current_avg - historical_avg)
    compliance_flag = deviation < 1.0
    
    # Actual critical computation
    final_diagnostic = analyze_readings(processed_signals)
    
    # Unused health indicators
    system_health = {
        'stability': compliance_flag,
        'calibration_valid': len(calibration_sequence) > 0,
        'entropy_metric': 0.82
    }
    
    # Output target result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute main process
if __name__ == "__main__":
    system_diagnostics(run_full_analysis=True, debug_mode=False)