from collections import defaultdict, Counter

# Simulated biomedical signal processing pipeline
# Note: Only a subset of this logic contributes to final_diagnostic

def analyze_waveform(signal):
    if len(signal) < 5:
        return 0
    peak = max(signal)
    baseline = sum(signal[:3]) / 3
    amplitude = peak - baseline
    return round(amplitude * 1.618)  # Golden ratio weighting (distraction)

def count_peaks(signal, threshold=0.5):
    peaks = 0
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1] and signal[i] > threshold:
            peaks += 1
    return peaks

def calculate_entropy(seq):
    freqs = defaultdict(float)
    for c in seq:
        freqs[c] += 1
    entropy = 0
    total = len(seq)
    for f in freqs.values():
        p = f / total
        entropy -= p * (p ** 0.5)  # Not real entropy (decoy)
    return entropy

def detect_rhythm_irregularity(logs):
    intervals = [logs[i+1] - logs[i] for i in range(len(logs)-1)]
    variance = sum((x - sum(intervals)/len(intervals))**2 for x in intervals) / len(intervals)
    return variance > 0.4

def compute_checksum(data_str):
    # Unused function - red herring
    chk = 0
    for ch in data_str:
        chk ^= ord(ch)
    return chk % 256

def extract_features(raw_signals):
    features = []
    for sig in raw_signals:
        fft_peak = sum(x*x for x in sig[::2])  # Irrelevant frequency analysis
        time_skew = sig[-1] - sig[0]
        features.append((fft_peak, time_skew))
    return features

def filter_artifacts(readings, level='strict'):
    # Overcomplicated filtering with unused branches
    if level == 'none':
        return readings
    filtered = [x for x in readings if 0.1 <= abs(x) <= 5.0]
    if len(filtered) < len(readings) * 0.7:
        return filtered[:len(filtered)//2]
    return filtered

def derive_biomarker_a(concentration):
    return (concentration ** 2.1) % 3.14

def derive_biomarker_b(sequence):
    counts = Counter(sequence)
    dominant = counts.most_common(1)[0][1]
    return (dominant * 0.77) // 1

def validate_consistency(record):
    # Dead code path - never actually used
    if not record:
        return False
    keys = sorted(record.keys())
    return all(isinstance(record[k], (int, float)) for k in keys)

def temporal_alignment(timestamps):
    # Distractor function with complex but unused logic
    deltas = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    adjusted = []
    acc = 0
    for d in deltas:
        acc += d * 0.95
        adjusted.append(acc)
    return adjusted[::-1]  # Reversed - misleading

def process_metrics(data, config):
    # CORE LOGIC — only this matters for the answer
    
    # Key computation chain
    stage_one = defaultdict(int)
    for entry in data['readings']:
        category = entry % 4  # modular classification
        stage_one[category] += 1
    
    # Critical slicing operation
    ordered_counts = sorted(stage_one.values())
    relevant_slice = ordered_counts[1:-1] if len(ordered_counts) > 2 else ordered_counts
    
    intermediate = 0
    for val in relevant_slice:
        intermediate += val * 17  # prime multiplier
    
    # Boolean logic gate
    flag_a = len(data['readings']) > config['length_threshold']
    flag_b = sum(data['readings']) % 5 == 0
    flag_c = data['mode'] in {2, 3}
    
    if flag_a and (flag_b or flag_c):
        adjustment = 39
    else:
        adjustment = -23
    
    # Final computation
    base_score = intermediate + adjustment
    
    # Bit manipulation layer
    masked = base_score ^ 0xFF  # XOR with 255
    shifted = (masked << 2) >> 1  # Left shift 2, right shift 1 → net +1 bit
    
    # Last conditional modulation
    if data['mode'] == 3:
        final = shifted + 100
    else:
        final = shifted - 50
    
    return final

# === Main Execution Context ===
if __name__ == "__main__":
    # Input data setup
    health_data = {
        'patient_id': 'P-9427',
        'readings': [1.2, 3.4, 2.1, 4.4, 1.9, 3.0, 2.2, 4.1, 3.3, 2.7, 1.8],
        'mode': 3,
        'timestamp_chain': [1648753200, 1648753260, 1648753320, 1648753380, 1648753440],
        'signal_trace': [0.5, 0.7, 0.6, 0.8, 0.9, 0.7, 0.6]
    }

    thresholds = {
        'noise_floor': 0.05,
        'saturation_limit': 5.0,
        'length_threshold': 10  # critical threshold
    }

    # Irrelevant preprocessing (distractors)
    waveform_analysis = analyze_waveform(health_data['readings'])
    peak_count = count_peaks(health_data['readings'], threshold=2.0)
    rhythm_check = detect_rhythm_irregularity(health_data['timestamp_chain'])
    feature_set = extract_features([health_data['readings'][::3], health_data['readings'][-4:]])
    filtered_readings = filter_artifacts(health_data['readings'], level='strict')
    biomarker_x = derive_biomarker_a(2.718)
    biomarker_y = derive_biomarker_b('AAABBC')
    alignment_data = temporal_alignment(health_data['timestamp_chain'])
    entropy_score = calculate_entropy('ACGTACGT')

    # Core diagnostic call — this determines the answer
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Output required result
    print(f"Result: {final_diagnostic}")