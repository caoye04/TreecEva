from collections import defaultdict, Counter

# Simulated bio-signal processing pipeline for neural diagnostics
def analyze_waveform(signal_chunk, sample_rate):
    magnitude = sum(abs(x) for x in signal_chunk)
    normalized = magnitude / len(signal_chunk) if signal_chunk else 0
    return round(normalized * sample_rate, 3)

def detect_spikes(amplitudes, threshold=0.75):
    spikes = []
    for i, amp in enumerate(amplitudes):
        if amp > threshold and i > 0 and amplitudes[i-1] < amp:
            spikes.append(i)
    return spikes if len(spikes) > 2 else spikes[:2]

def compute_coherence(left_band, right_band):
    if len(left_band) != len(right_band):
        min_len = min(len(left_band), len(right_band))
        left_band, right_band = left_band[:min_len], right_band[:min_len]
    
    coherence_score = 0
    for a, b in zip(left_band, right_band):
        coherence_score += (a * b) / (abs(a) + abs(b) + 1e-8)
    return round(coherence_score, 4)

def generate_synthetic_control(base_seq, phase_shift):
    # Irrelevant function - decoy for control logic
    rotated = base_seq[-phase_shift:] + base_seq[:-phase_shift]
    inverted = [1 - x for x in rotated]
    return [x ^ 1 for x in inverted][::2]

def evaluate_stability(readings):
    # Dead code path - never actually used in final computation
    moving_avg = []
    window_size = 3
    for i in range(len(readings) - window_size + 1):
        moving_avg.append(sum(readings[i:i+window_size]) / window_size)
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    return variance < 0.05

def filter_artifacts(raw_data, flags):
    clean_sequence = []
    for val, flag in zip(raw_data, flags):
        if flag == 1 and -1.5 <= val <= 1.5:
            clean_sequence.append(val)
    return clean_sequence[::2] + clean_sequence[-5:]  # slicing with overlap

def derive_phase_vector(temporal_trace):
    # Unused transformation - distractor
    transformed = []
    for i, t in enumerate(temporal_trace):
        transformed.append(t * (i % 7 + 1))
    return transformed[::-1]

def process_metrics(signature, baseline):
    # Core logic embedded within noise
    segment_a = signature["alpha"][:12]
    segment_b = signature["beta"][4:16]
    
    # Real computation steps
    alpha_power = analyze_waveform(segment_a, 256)
    beta_power = analyze_waveform(segment_b, 256)
    
    spike_pattern = detect_spikes(signature["gamma"])
    spike_count_metric = len(spike_pattern) * 113
    
    coherence = compute_coherence(signature["delta_left"], signature["delta_right"])
    
    # Distractor variables
    artifact_filtered = filter_artifacts(baseline["noise"], baseline["flags"])
    stability_flag = evaluate_stability(artifact_filtered)  # dead call
    control_sequence = generate_synthetic_control([1,0,1,1,0], 2)  # red herring
    
    # Key intermediate values
    base_score = alpha_power + beta_power
    modulation_index = base_score * coherence
    
    # Final diagnostic calculation
    final_diagnostic = int(modulation_index * 100) + spike_count_metric
    
    # Decoy output variable
    debug_status = {"processed": True, "errors": None, "spikes_detected": spike_pattern}
    
    return final_diagnostic

# Simulated neural sensor data
baseline_readings = {
    "noise": [0.1, 0.3, -0.2, 0.5, 0.7, -1.1, 0.4, 0.2, -0.3, 0.6, 0.8, -0.9],
    "flags": [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    "timestamp": 1684302900
}

health_signature = {
    "alpha": [0.12, 0.33, -0.21, 0.54, 0.27, -0.19, 0.48, 0.32, -0.23, 0.61, 0.18, 0.29, 0.44],
    "beta": [0.61, 0.72, 0.58, 0.83, 0.77, 0.69, 0.81, 0.74, 0.66, 0.79, 0.82, 0.71, 0.68],
    "gamma": [0.15, 0.88, 0.33, 0.91, 0.44, 0.93, 0.55, 0.87, 0.66],
    "delta_left": [0.11, 0.22, 0.19, 0.25, 0.18, 0.21],
    "delta_right": [0.13, 0.20, 0.23, 0.24, 0.17, 0.19]
}

# Execution point
final_diagnostic = process_metrics(health_signature, baseline_readings)
print(f"Result: {final_diagnostic}")