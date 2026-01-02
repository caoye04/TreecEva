import math

# Simulated biomedical signal processing pipeline
def preprocess_signals(raw_readings):
    filtered = []
    noise_floor = 0.041
    for idx, val in enumerate(raw_readings):
        if idx % 3 == 0:
            adjusted = val * 0.89 + noise_floor
        elif idx % 5 == 0:
            adjusted = val * 0.92 - noise_floor
        else:
            adjusted = val * 0.95
        filtered.append(round(adjusted, 6))
    return filtered

# Irrelevant helper: spectral baseline correction (unused)
def correct_baseline(signal, factor=1.03):
    return [s * factor for s in signal]

# Data fusion from multiple sensors
def fuse_modalities(eeg_data, emg_data):
    fused = []
    for eeg, emg in zip(eeg_data, emg_data):
        combined = math.sqrt(eeg**2 + emg**2) * 0.75
        fused.append(round(combined, 6))
    return fused

# Secondary metric: rhythm coherence index (distractor)
def compute_coherence(signal):
    coherence = 0
    for i in range(1, len(signal)):
        coherence += abs(signal[i] - signal[i-1])
    return round(coherence / len(signal), 6)

# Primary analysis: anomaly scoring with thresholds
def score_anomalies(fused_signal, config):
    scores = []
    for val in fused_signal:
        severity = 0
        if val > config['critical']:
            severity = 4
        elif val > config['elevated']:
            severity = 3
        elif val > config['warning']:
            severity = 2
        elif val > config['normal']:
            severity = 1
        else:
            severity = 0
        scores.append(severity)
    return scores

# Red herring function: entropy calculation (not used in main path)
def shannon_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

# Core diagnostic engine
def analyze_metrics(metrics, thresholds):
    # Apply dynamic gain based on patient profile
    amplified = [m * thresholds['gain'] for m in metrics]
    
    # Calculate moving average over 3-point window (with wraparound)
    smoothed = []
    n = len(amplified)
    for i in range(n):
        prev = amplified[(i-1) % n]
        curr = amplified[i]
        next_val = amplified[(i+1) % n]
        avg = (prev + curr + next_val) / 3
        smoothed.append(avg)
    
    # Determine dominant trend
    increasing = 0
    for i in range(1, len(smoothed)):
        if smoothed[i] > smoothed[i-1]:
            increasing += 1
    
    trend_bias = increasing / (len(smoothed) - 1) if len(smoothed) > 1 else 0
    
    # Compute final diagnostic index
    base_index = sum(smoothed) / len(smoothed)
    adjustment = (trend_bias * thresholds['trend_factor'])
    final_score = base_index + adjustment
    
    # Normalize to diagnostic scale (0-100)
    normalized = (final_score / thresholds['normalizer']) * 100
    
    # Dead code branch: hypothetical mode (never triggered)
    debug_mode = False
    if debug_mode and normalized > 75:
        return round(normalized * 1.25, 6)
    
    return round(normalized, 6)

# Unused recursive combinatorics function (decoy)
def combinations(n, r):
    if r == 0 or r == n:
        return 1
    return combinations(n-1, r-1) + combinations(n-1, r)

# Main execution
if __name__ == '__main__':
    # Simulated raw physiological readings
    eeg_input = [0.67, 0.72, 0.63, 0.81, 0.55, 0.91, 0.44, 0.76]
    emg_input = [0.33, 0.41, 0.52, 0.29, 0.68, 0.37, 0.59, 0.48]
    
    # Preprocess individual signals
    cleaned_eeg = preprocess_signals(eeg_input)
    cleaned_emg = preprocess_signals(emg_input)
    
    # Fused modality signal
    neuro_fusion = fuse_modalities(cleaned_eeg, cleaned_emg)
    
    # Compute irrelevant secondary metrics
    rhythm_index = compute_coherence(neuro_fusion)  # Distractor
    entropy_value = shannon_entropy([int(x*100) for x in neuro_fusion])  # Misleading
    
    # Generate anomaly severity scores
    threshold_settings = {
        'warning': 0.45,
        'elevated': 0.58,
        'critical': 0.75,
        'normal': 0.30,
        'gain': 1.85,
        'trend_factor': 12.5,
        'normalizer': 2.15
    }
    anomaly_ranks = score_anomalies(neuro_fusion, threshold_settings)
    
    # Final diagnostic computation
    final_diagnostic = analyze_metrics(neuro_fusion, threshold_settings)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")