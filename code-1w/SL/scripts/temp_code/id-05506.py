import math

# Simulated sensor data preprocessing with red herrings
def collect_samples(raw_data, offset=0.0):
    calibrated = []
    noise_floor = 0.023
    gain_factor = 1.87
    temp_buffer = []  # Unused decoy structure

    for val in raw_data:
        if abs(val) < 0.1:  # Filter negligible readings
            continue
        adjusted = (val + offset) * gain_factor
        calibrated.append(adjusted)
    
    # Irrelevant transformation (dead code path)
    inverted = [math.cos(x) for x in calibrated if x < 0]
    magnitude_sum = sum(abs(x) for x in calibrated)
    
    # Actual return value
    return calibrated

# Signal feature extraction with misleading intermediate steps
def extract_features(signal):
    features = {}
    n = len(signal)
    
    # Real computation: spectral centroid approximation
    weighted_sum = sum(i * abs(signal[i]) for i in range(n))
    total_energy = sum(abs(x) for x in signal)
    centroid = weighted_sum / total_energy if total_energy != 0 else 0
    features['centroid'] = centroid

    # Distractor: irrelevant peak detection
    peaks = [i for i in range(1, n-1) if signal[i] > signal[i-1] and signal[i] > signal[i+1]]
    avg_peak_height = sum(signal[i] for i in peaks) / len(peaks) if peaks else 0
    
    # Decoy statistics
    rolling_avg = [sum(signal[i:i+3])/3 for i in range(n-2)] if n >= 3 else []
    fluctuation_index = len([x for x in rolling_avg if abs(x) > 0.5])
    
    # Unused but plausible feature
    entropy_approx = -sum((abs(x)/total_energy)*math.log(abs(x)/total_energy) for x in signal if x != 0) if total_energy > 0 else 0
    
    # Real feature: signal stability ratio
    diffs = [abs(signal[i+1] - signal[i]) for i in range(n-1)]
    stability = (sum(1 for d in diffs if d < 0.3) / len(diffs)) if diffs else 0
    features['stability'] = stability
    
    return features

# Data windowing with slicing operations (required Python feature)
def segment_signal(data, window_size=5):
    segments = []
    step = window_size // 2
    
    # Use slicing to create overlapping windows
    for i in range(0, len(data) - window_size + 1, step):
        segment = data[i:i + window_size]  # Core slicing operation
        segments.append(segment)
    
    # Distractor: reverse analysis on odd indices
    reversed_segments = [seg[::-1] for idx, seg in enumerate(segments) if idx % 2 == 1]
    
    # Return only original segments
    return segments[:len(segments)//2 + 1]  # Further slicing distraction

# Primary processing function with red herring branches
def process_noise_artifacts(cleaned):
    artifact_count = 0
    critical_levels = []
    
    for sample in cleaned:
        # Fake anomaly detection logic
        if len(str(sample)) > 5 and math.isclose(sample % 1, 0.77, abs_tol=1e-2):
            artifact_count += 1  # Never actually triggered
        
        # Real filtering criterion (obscured)
        if abs(sample) > 1.5 and sample not in critical_levels:
            critical_levels.append(sample)
    
    # Irrelevant statistical moment calculation
    if critical_levels:
        mean_critical = sum(critical_levels) / len(critical_levels)
        variance = sum((x - mean_critical)**2 for x in critical_levels) / len(critical_levels)
        kurtosis = sum(((x - mean_critical)/variance)**4 for x in critical_levels) / len(critical_levels) if variance > 0 else 0
    
    # Actual output used downstream
    return len(critical_levels)

# Final diagnostic engine with complex control flow
def analyze_signal(samples):
    if not samples:
        return -999
    
    # Step 1: Extract core features
    feats = extract_features(samples)
    stability_score = feats.get('stability', 0)
    centroid_val = feats.get('centroid', 0)
    
    # Step 2: Segment data (uses slicing)
    segments = segment_signal(samples)
    
    # Misleading complexity: harmonic resonance check (unused)
    resonant_bands = 0
    for seg in segments:
        transformed = [math.sin(x * math.pi / 2) for x in seg]
        if any(abs(t) > 0.9 for t in transformed):
            resonant_bands += 1
    
    # Critical path: instability multiplier
    instability_factor = (1 - stability_score) * 100
    
    # Hidden accumulator: sum of positive centroids across all segments
    segment_centroids = []
    for seg in segments:
        if len(seg) == 0:
            continue
        seg_weighted = sum(i * abs(seg[i]) for i in range(len(seg)))
        seg_energy = sum(abs(x) for x in seg)
        if seg_energy > 0:
            segment_centroids.append(seg_weighted / seg_energy)
    
    average_segment_centroid = sum(segment_centroids) / len(segment_centroids) if segment_centroids else 0
    
    # Final computation chain
    base_rating = abs(centroid_val) * 10
    adjustment = average_segment_centroid * instability_factor
    final_score = base_rating + adjustment
    
    # Key decision point obscured by distractions
    threshold = 45.0
    tolerance = 5.0
    
    # Distractor: unused classification tree
    classification = ""
    if final_score < threshold - tolerance:
        classification = "LOW"
    elif final_score > threshold + tolerance:
        classification = "HIGH"
    else:
        classification = "MEDIUM"
    
    # The real answer derivation (non-obvious due to context)
    critical_count = process_noise_artifacts(samples)
    final_diagnostic = int(final_score) + critical_count * 100
    
    return final_diagnostic

# Main execution sequence
if __name__ == "__main__":
    # Input data with meaningful structure
    raw_input_stream = [
        0.05, -0.12, 0.33, 0.67, -1.08, 2.15, -0.03, 0.44, 
        1.88, -2.01, 0.76, 0.29, -0.88, 1.95, 3.12, -1.11
    ]
    
    # Initiate processing pipeline
    processed_samples = collect_samples(raw_input_stream, offset=0.05)
    
    # Introduce decoy function calls with side-effect-like appearance
    dummy_copy = processed_samples.copy()
    dummy_copy.sort(reverse=True)
    median_like = dummy_copy[len(dummy_copy)//2] if dummy_copy else 0
    
    # Core analysis call - target intervention point
    final_diagnostic = analyze_signal(processed_samples)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")