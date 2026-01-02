import math

# Simulated sensor fusion system for environmental monitoring
base_frequency = 50.0
sampling_rate = 1024
harmonic_series = [base_frequency * (i + 1) for i in range(8)]
noise_floor = 0.042

# Irrelevant signal synthesis (distractor)
def generate_pseudo_noise(length, seed=1):
    result = []
    x = seed
    for _ in range(length):
        x = (x * 997 + 661) % 10000
        result.append((x % 100) / 100.0)
    return result

# Unused modulation function (dead code path)
def apply_amplitude_modulation(signal, carrier_freq, sample_rate):
    modulated = []
    for i, s in enumerate(signal):
        carrier = math.sin(2 * math.pi * carrier_freq * i / sample_rate)
        modulated.append(s * carrier)
    return modulated

# Signal preprocessing with bit manipulation red herring
def preprocess_signal(raw_data):
    processed = []
    shift_key = 0b1010  # Distractor: bitwise operation not used in critical path
    
    for val in raw_data:
        if abs(val) < noise_floor:
            continue  # Skip noise
        amplified = val * 3.5
        # Bit-twiddling distraction
        amplified_int = int(abs(amplified) * 100)
        masked = amplified_int ^ shift_key & 0xFF
        restored = masked / 100.0
        processed.append(restored if val > 0 else -restored)
    
    # Sorting (relevant only for median extraction)
    processed.sort()
    return processed

# Set-based anomaly filtering (core concept)
def filter_anomalies(data_points, threshold_percentile=95):
    if len(data_points) == 0:
        return []
    
    # Compute threshold using percentile (simulated)
    sorted_vals = sorted(data_points)
    threshold_idx = int(len(sorted_vals) * threshold_percentile / 100)
    safe_set = set(sorted_vals[:threshold_idx])  # Use set for fast lookup
    
    # Distractor: unused complement set
    outlier_set = set(sorted_vals[threshold_idx:])
    
    filtered = [x for x in data_points if x in safe_set]
    return filtered

# Redundant transform chain (misleading intermediate results)
def time_domain_transform(signal):
    transformed = []
    for x in signal:
        y = x ** 2 + 0.1 * x - 0.002
        transformed.append(y)
    return transformed

# Frequency domain approximation (decoy computation)
def estimate_spectral_peaks(signal, rate):
    peak_candidates = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peak_candidates.append(i)
    return len(peak_candidates)  # Unused metric

# Main analysis pipeline
def analyze_readings(cleaned_signal):
    if not cleaned_signal:
        return 0.0
    
    # Compute moving averages (nested list comprehension)
    window_size = 3
    smoothed = [
        sum(cleaned_signal[i:i+window_size]) / window_size
        for i in range(len(cleaned_signal) - window_size + 1)
    ]
    
    # Extract statistical features
    mean_val = sum(smoothed) / len(smoothed)
    squared_diffs = [(x - mean_val) ** 2 for x in smoothed]
    variance = sum(squared_diffs) / len(squared_diffs)
    std_dev = math.sqrt(variance)
    
    # Apply safety thresholds
    warning_threshold = mean_val + 1.8 * std_dev
    critical_threshold = mean_val + 2.5 * std_dev
    
    # Count exceedances using linear search (relevant)
    critical_count = 0
    for val in cleaned_signal:
        if val > critical_threshold:
            critical_count += 1
    
    # Combinatorics distractor: pair counting (irrelevant)
    pair_count = 0
    for i in range(len(cleaned_signal)):
        for j in range(i + 1, len(cleaned_signal)):
            if abs(cleaned_signal[i] - cleaned_signal[j]) < 0.05:
                pair_count += 1
    
    # Final diagnostic score based on critical factors
    stability_index = 1.0 / (std_dev + 0.1)  # Prevent division by zero
    risk_factor = critical_count * 100.0 / len(cleaned_signal)
    final_diagnostic = (stability_index * 70.0) - (risk_factor * 1.5) + (mean_val * 2.0)
    
    return final_diagnostic

# Generate synthetic input (deterministic)
raw_sensor_data = [
    0.012, -0.031, 0.055, 0.124, 0.089, 0.301, 0.433, 0.251,
    0.187, 0.521, 0.613, 0.582, 0.654, 0.701, 0.041, -0.028
]

# Processing pipeline execution
processed_signals = preprocess_signal(raw_sensor_data)
refined_readings = filter_anomalies(processed_signals, 90)
decoy_transform = time_domain_transform(refined_readings)
spectral_analysis_result = estimate_spectral_peaks(decoy_transform, sampling_rate)  # Unused

# Critical execution point
final_diagnostic = analyze_readings(refined_readings)
print(f"Result: {final_diagnostic}")