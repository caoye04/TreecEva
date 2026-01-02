import math

# Simulated sensor data acquisition
def acquire_signal():
    raw_samples = [i * 0.5 for i in range(100)]
    noise_floor = sum([math.sin(x / 10) for x in raw_samples])
    return [s + math.cos(s) + noise_floor * 0.1 for s in raw_samples]

# Irrelevant signal transformation (dead path)
def deprecated_filter(data):
    return [x for x in data if x > 1]  # Unused function

# Signal conditioning with distractor logic
def condition_signal(raw):
    clipped = [min(max(x, -5), 5) for x in raw]
    baseline_shift = sum(clipped[:10]) / 10
    shifted = [x - baseline_shift for x in clipped]
    envelope = [abs(x) for x in shifted]
    smoothed = []
    for i in range(len(envelope)):
        window = envelope[max(0, i-2):i+3]
        smoothed.append(sum(window) / len(window))
    return smoothed, baseline_shift  # baseline_shift returned but not used later

# Data segmentation with red herring computation
def segment_data(smoothed_signal):
    segments = []
    for i in range(0, len(smoothed_signal), 10):
        segment = smoothed_signal[i:i+10]
        avg_power = sum([x**2 for x in segment]) / len(segment)
        peak_to_avg_ratio = max(segment) / avg_power if avg_power != 0 else 0
        # Below line computes something misleading but unused
        entropy_approx = -sum([p * math.log(p + 1e-9) for p in segment if p > 0])
        segments.append(segment)
    return segments

# Feature extraction with multiple distractions
def extract_features(segments):
    all_features = []
    total_zero_crossings = 0
    for seg in segments:
        differences = [seg[i+1] - seg[i] for i in range(len(seg)-1)]
        zero_crossings = sum([1 for i in range(len(differences)-1) if differences[i] * differences[i+1] < 0])
        total_zero_crossings += zero_crossings
        rms = math.sqrt(sum([x**2 for x in seg]) / len(seg))
        crest_factor = max(seg) / rms if rms != 0 else 0
        # Decoy statistical measure
        skew_proxy = (sum([x**3 for x in seg]) / len(seg)) / (rms ** 3) if rms != 0 else 0
        all_features.append({'rms': rms, 'crest': crest_factor})
    # Final aggregate features
    aggregated_rms = sum([f['rms'] for f in all_features]) / len(all_features)
    return {'aggregated_rms': aggregated_rms, 'zero_crossings': total_zero_crossings}

# Core analysis logic – relevant path
def analyze_signal(data_features):
    score = 0
    base_metric = data_features['aggregated_rms']
    # Real computation path
    if base_metric > 2.0:
        score += int(base_metric * 10)
    elif base_metric > 1.0:
        score += int(base_metric * 8)
    else:
        score += int(base_metric * 5)
    # Add bonus based on zero crossings (actual key factor)
    zc_bonus = data_features['zero_crossings'] // 5
    score += zc_bonus
    # Distractor: complex trigonometric weighting (unused)
    angle_weight = math.sin(math.pi * data_features['aggregated_rms'] / 4)
    dummy_adjustment = math.floor(angle_weight * 100)
    # Final diagnostic is only based on score and zc_bonus
    final_diagnostic = score * 7 + dummy_adjustment  # dummy_adjustment is noise
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Step 1: Acquire raw signal
    raw_data = acquire_signal()
    
    # Step 2: Condition the signal (real path)
    processed_signal, shift = condition_signal(raw_data)
    
    # Step 3: Segment the data (real, but some outputs ignored)
    signal_segments = segment_data(processed_signal)
    
    # Step 4: Extract meaningful features (some discarded)
    extracted_features = extract_features(signal_segments)
    
    # Step 5: Analyze and produce diagnostic (target point)
    final_diagnostic = analyze_signal(extracted_features)
    
    # Output target result
    print(f"Result: {final_diagnostic}")