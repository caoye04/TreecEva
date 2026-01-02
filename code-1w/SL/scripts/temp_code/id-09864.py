import math

# Simulated sensor data processing pipeline for aerospace telemetry
def acquire_signal(raw_id, duration):
    base_wave = [math.sin(2 * math.pi * t / 50) for t in range(duration)]
    noise_floor = [0.1 * math.cos(t / 7) for t in range(duration)]
    return [base_wave[i] + noise_floor[i] for i in range(duration)]


def filter_outliers(data, threshold=0.1):
    mean_val = sum(data) / len(data)
    deviations = [(x - mean_val) ** 2 for x in data]
    variance = sum(deviations) / len(deviations)
    std_dev = math.sqrt(variance)
    return [x for x in data if abs(x - mean_val) <= threshold * std_dev], std_dev


def compute_entropy(values):
    # Irrelevant function - mimics signal complexity analysis but unused in final path
    probs = [values.count(v) / len(values) for v in set(values)]
    return -sum(p * math.log2(p) for p in probs)


def segment_signal(signal, window_size=10):
    segments = []
    for i in range(0, len(signal), window_size):
        segment = signal[i:i + window_size]
        if len(segment) == window_size:
            segments.append(segment)
    return segments


def extract_features(seg_list):
    features = []
    for idx, seg in enumerate(seg_list):
        rms = math.sqrt(sum(x**2 for x in seg) / len(seg))
        peak = max(abs(x) for x in seg)
        zero_crossings = sum(1 for i in range(1, len(seg)) if seg[i]*seg[i-1] < 0)
        # Distractor computation - looks important but not used later
        spectral_centroid = sum(i * abs(seg[i]) for i in range(len(seg))) / sum(abs(x) for x in seg)
        features.append({'id': idx, 'rms': rms, 'peak': peak, 'zero_crossings': zero_crossings})
    return features


def correlate_segments(features_a, features_b):
    # Dead function - appears to compare segments but never called
    correlations = []
    for a, b in zip(features_a, features_b):
        diff = abs(a['rms'] - b['rms'])
        correlations.append(diff < 0.05)
    return correlations


def reconstruct_phase(segments):
    # Another decoy function - complex-looking but irrelevant
    phase_shifts = []
    for s in segments:
        fft_vals = [complex(math.cos(x), math.sin(x)) for x in s]
        magnitude = sum(abs(z) for z in fft_vals) / len(fft_vals)
        phase_shifts.append(magnitude * 0.1)
    return phase_shifts


def detect_anomalies(feature_set):
    anomalies = []
    for f in feature_set:
        # Real logic: anomaly if RMS > 0.85 and high zero crossing
        if f['rms'] > 0.85 and f['zero_crossings'] > 3:
            anomalies.append(f['id'])
    return anomalies if anomalies else [0]


def integrate_diagnostics(anomaly_list, weight_map):
    total_score = 0
    for aid in anomaly_list:
        if aid in weight_map:
            total_score += weight_map[aid]
    return total_score * 1.75


def analyze_signal(clean_data):
    segmented = segment_signal(clean_data)
    characterized = extract_features(segmented)
    
    # Critical distraction: multiple intermediate variables with plausible names
    baseline_metrics = {i: {'threshold': 0.7 + i*0.01, 'tolerance': 0.05} for i in range(len(characterized))}
    
    # Unused transformation chain
    normalized_segs = [[x * 0.98 for x in s] for s in segmented]
    resegmented = segment_signal([x for sub in normalized_segs for x in sub], window_size=10)
    
    # Real path resumes here
    detected = detect_anomalies(characterized)
    
    # Weight map based on segment position (even indices weighted more)
    weights = {i: 1.5 if i % 2 == 0 else 0.8 for i in range(20)}
    
    # Final integration
    integrated = integrate_diagnostics(detected, weights)
    
    # Red herring: entropy-based confidence (never actually affects result)
    fake_confidence = compute_entropy([integrated] + [1.0] * 9)
    adjusted_result = integrated + fake_confidence * 0.0  # No effect due to multiplication
    
    # Final diagnostic score
    final_diagnostic = round(adjusted_result, 4)
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    # Acquire simulated telemetry signal
    raw_telemetry = acquire_signal(raw_id=1024, duration=128)
    
    # Filter signal - returns clean signal and computed std_dev (unused later)
    filtered_signal, noise_level = filter_outliers(raw_telemetry, threshold=0.12)
    
    # Apply secondary smoothing (distractor - not actually changing anything critical)
    smoothed = [x * (0.99 + 0.02 * math.sin(i/10)) for i, x in enumerate(filtered_signal)]
    
    # Normalize amplitude (real preprocessing step)
    max_amp = max(abs(x) for x in smoothed)
    processed_segments = [x / max_amp for x in smoothed] if max_amp > 0 else smoothed
    
    # Introduce dead branch with misleading calculations
    if len(processed_segments) > 200:  # Never true
        dummy_analysis = reconstruct_phase(segment_signal(processed_segments, 8))
        backup_score = sum(dummy_analysis) * 100
    else:
        placeholder = [0] * 5  # Dead code path
        derived_offset = sum(placeholder)
    
    # Key execution point
    final_diagnostic = analyze_signal(processed_segments)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")