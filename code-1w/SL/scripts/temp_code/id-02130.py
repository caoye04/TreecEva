import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_data():
    raw_samples = [i * 0.01 for i in range(500)]
    noise_floor = 0.02
    signal_data = []
    for t in raw_samples:
        # Real signal component
        clean_signal = math.sin(40 * t) * math.exp(-t * 0.5)
        # Add controlled noise
        noisy_sample = clean_signal + noise_floor * (hash(str(t)) % 1000) / 1000.0
        signal_data.append(noisy_sample)
    return signal_data

# Irrelevant helper - dead code path
def deprecated_filter(x):
    return [val for val in x if abs(val) > 0.1]  # Unused

# Legacy normalization function (distractor)
def normalize_legacy(data):
    max_val = max(data, key=abs)
    return [x / max_val for x in data]

# Actual preprocessing pipeline
def preprocess_signal(raw_signal):
    # Slice relevant time window: mid-segment only
    trimmed = raw_signal[100:400]
    
    # Apply envelope detection via rectification and smoothing
    envelope = [abs(x) for x in trimmed]
    smoothed = []
    window_size = 5
    for i in range(len(envelope) - window_size + 1):
        segment_avg = sum(envelope[i:i+window_size]) / window_size
        smoothed.append(segment_avg)
    
    # Resample to fixed output size
    resampled = smoothed[::3][:80]
    
    # Inject distractor variables
    baseline_offset = sum(resampled) / len(resampled)
    fluctuation_energy = sum(x**2 for x in resampled) / len(resampled)
    entropy_proxy = -sum(x * math.log(abs(x) + 1e-8) for x in resampled)  # unused
    
    # Return structured block
    return {
        'readings': resampled,
        'stats': {
            'mean': baseline_offset,
            'rms': math.sqrt(fluctuation_energy),
            'peak': max(resampled),
            'valid_count': len(resampled)
        }
    }

# Segment into analysis windows
def segment_data(envelope_block):
    readings = envelope_block['readings']
    segments = []
    for i in range(0, len(readings) - 16 + 1, 8):
        window = readings[i:i+16]
        segments.append(window)
    
    # Decoy transformation
    inverted_segments = [[1.0 - x for x in s] for s in segments]  # never used
    
    # Metadata generation (distraction)
    meta_tags = [{'id': idx, 'length': len(s), 'active': True} for idx, s in enumerate(segments)]
    
    return segments

# Advanced pattern analyzer
def detect_anomaly_pattern(segment):
    # Compute spectral centroid approximation
    weighted_sum = sum(i * x for i, x in enumerate(segment))
    total_power = sum(segment)
    if total_power == 0:
        centroid = 0
    else:
        centroid = weighted_sum / total_power
    
    # Spectral spread
    variance = sum(((i - centroid) ** 2) * x for i, x in enumerate(segment)) / (total_power + 1e-8)
    
    # Distractor metrics
    skewness = sum(((i - centroid) ** 3) * x for i, x in enumerate(segment))  # not used
    kurtosis_proxy = sum(((i - centroid) ** 4) * x for i, x in enumerate(segment))  # not used
    
    # Decision logic
    if variance > 25.0:
        return 3
    elif variance > 15.0:
        return 2
    elif variance > 5.0:
        return 1
    else:
        return 0

# Main analysis engine
def analyze_signal(segment_list):
    pattern_scores = []
    for seg in segment_list:
        score = detect_anomaly_pattern(seg)
        pattern_scores.append(score)
    
    # Aggregate diagnostics
    score_freq = {}
    for s in pattern_scores:
        score_freq[s] = score_freq.get(s, 0) + 1
    
    # Compute final index using combinatorial weighting
    weights = {0: 1, 1: 3, 2: 7, 3: 15}
    weighted_index = 0
    for key in sorted(weights.keys()):
        freq = score_freq.get(key, 0)
        weighted_index += weights[key] * freq * (freq % 2)  # Only odd frequencies contribute
    
    # Secondary adjustment based on sequence properties
    transitions = 0
    for i in range(len(pattern_scores) - 1):
        if pattern_scores[i] != pattern_scores[i+1]:
            transitions += 1
    
    # Obfuscation through bit manipulation
    transition_flag = (transitions << 2) & 0xFF
    final_diagnostic = weighted_index ^ transition_flag
    
    # Dead code branch - misleading
    if final_diagnostic < 0:
        final_diagnostic = int(math.sqrt(abs(final_diagnostic)))
    
    # Critical print statement
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Orchestration
if __name__ == "__main__":
    # Collect raw input
    raw_signal = collect_sensor_data()
    
    # Preprocess stream
    processed_block = preprocess_signal(raw_signal)
    
    # Break into analyzable chunks
    processed_segments = segment_data(processed_block)
    
    # Core diagnostic computation
    final_diagnostic = analyze_signal(processed_segments)