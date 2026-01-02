import itertools

# Simulated biomedical signal processing pipeline
def analyze_waveform(signal, sample_rate):
    n = len(signal)
    freqs = [i * sample_rate / n for i in range(n // 2)]
    spectrum = [abs((signal[i] + signal[n-1-i]) / 2) for i in range(n // 2)]
    dominant_freq = freqs[spectrum.index(max(spectrum))] if spectrum else 0

    # Irrelevant transformation (distractor)
    normalized = [x / max(signal) if max(signal) != 0 else 0 for x in signal]
    derivative = [normalized[i+1] - normalized[i] for i in range(len(normalized)-1)]
    zero_crossings = sum(1 for i in range(len(derivative)-1) if derivative[i]*derivative[i+1] < 0)

    return dominant_freq

# Data quality assessment (mostly dead code path)
def assess_quality(timestamps):
    intervals = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    stability = sum(1 for x in intervals if 0.95 < x < 1.05) / len(intervals) if intervals else 0
    
    # This function is never called but looks important
    def advanced_jitter_analysis(seq):
        from collections import deque
        window = deque(maxlen=5)
        peaks = 0
        for val in seq:
            window.append(val)
            if len(window) == 5 and window[2] > max([window[0], window[1], window[3], window[4]]):
                peaks += 1
        return peaks
    
    return stability

# Core diagnostic logic
thresholds = {
    'hrv_sdp': 50,
    'respiration_rate': 18,
    'spectral_entropy': 0.7
}

health_data = {
    'raw_ecg': [60, 65, 70, 68, 72, 75, 66, 69, 71, 73],
    'timestamps': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'breathing_wave': [0.5, 1.2, 0.8, -0.3, -1.0, -0.7, 0.2, 1.1, 0.9, -0.5],
    'aux_sensors': {'temp': 36.7, 'spo2': 98}
}

# Complex multi-step processing with red herrings
def extract_features(data):
    ecg = data['raw_ecg']
    wave = data['breathing_wave']
    
    # Real computation: Heart rate variability (SDP)
    hrv_sdp = sum((ecg[i+1] - ecg[i])**2 for i in range(len(ecg)-1))
    
    # Real computation: Respiration rate via frequency analysis
    resp_rate = analyze_waveform(wave, 10)
    
    # Distractor: meaningless entropy on small sequence
    probs = [abs(x)/sum(abs(y) for y in wave) for x in wave if x != 0]
    spectral_entropy = -sum(p * __import__('math').log(p) for p in probs if p > 0)
    
    # Dead branch that looks relevant
    if len(wave) > 20:  # Never true
        moving_avg = [sum(wave[i:i+3])/3 for i in range(len(wave)-2)]
        smoothed_entropy = sum(x*x for x in moving_avg)

    # Another decoy using itertools
    paired_diffs = list(itertools.starmap(lambda a,b: abs(a-b), zip(wave, wave[1:])))
    cycle_consistency = sum(1 for x in paired_diffs if x > 0.5)
    
    # Only these three are actually used later
    features = {
        'hrv_sdp': hrv_sdp,
        'respiration_rate': int(round(resp_rate)),
        'spectral_entropy': round(spectral_entropy, 3)
    }
    
    # Fake feature injection (never used)
    features['synthetic_index'] = (features['hrv_sdp'] * features['respiration_rate']) % 100
    
    return features

# Decision engine with early returns
def evaluate_risk(features, limits):
    critical_count = 0
    
    # Check each threshold (order matters)
    if 'hrv_sdp' in features:
        if features['hrv_sdp'] > limits['hrv_sdp']:
            critical_count += 1
    
    if 'respiration_rate' in features:
        if features['respiration_rate'] > limits['respiration_rate']:
            critical_count += 1
    
    if 'spectral_entropy' in features:
        if features['spectral_entropy'] > limits['spectral_entropy']:
            critical_count += 1
    
    # Early return red herring (looks like it might be primary logic)
    if critical_count == 0:
        return 0  # Low risk
    
    # More complex evaluation (actual path)
    composite_score = (
        (features.get('hrv_sdp', 0) / limits['hrv_sdp']) * 0.4 +
        (features.get('respiration_rate', 0) / limits['respiration_rate']) * 0.3 +
        (features.get('spectral_entropy', 0) / limits['spectral_entropy']) * 0.3
    )
    
    # Final categorization
    if composite_score >= 2.0:
        return 3
    elif composite_score >= 1.5:
        return 2
    elif composite_score >= 1.0:
        return 1
    else:
        return 0

# Main processing chain
def process_metrics(data, config):
    extracted = extract_features(data)
    
    # Spurious dictionary transformation
    transformed = {k.upper(): v for k, v in extracted.items()}
    inverted = {v: k for k, v in extracted.items() if isinstance(v, (int, float)) and v > 0}
    
    # Slice manipulation that goes nowhere
    values = list(extracted.values())
    mid_slice = values[1:3] if len(values) > 2 else values
    shifted = mid_slice[-1:] + mid_slice[:-1]  # Rotation
    
    # Actual decision logic
    risk_level = evaluate_risk(extracted, config)
    
    # Final diagnostic calculation (depends on prior steps)
    baseline = 100
    adjustment = {
        0: -10,
        1: 5,
        2: 25,
        3: 60
    }[risk_level]
    
    # Add secondary effect based on respiration rate
    resp_val = extracted['respiration_rate']
    if resp_val > 20:
        adjustment += 15
    elif resp_val > 15:
        adjustment += 5
    
    final_diagnostic = baseline + adjustment
    
    # Dead code path with misleading name
    def calculate_optimal_threshold():
        # This is never executed
        return sum(inverted.keys()) / len(inverted) if inverted else 0
    
    return final_diagnostic

# Execute main logic
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Target result: {final_diagnostic}")