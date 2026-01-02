import itertools

# Simulated sensor data processing with diagnostic analysis
def collect_samples(base_freq, duration, sample_rate):
    timesteps = [i / sample_rate for i in range(int(duration * sample_rate))]
    raw_signal = [base_freq * (t ** 1.5) for t in timesteps]
    return raw_signal


def filter_noise(signal, threshold=0.75):
    filtered = [s if abs(s) > threshold else 0.0 for s in signal]
    energy = sum(s ** 2 for s in filtered)
    normalized = [s / (energy ** 0.5) if energy > 0 else 0 for s in filtered] if energy != 0 else filtered
    return normalized


def segment_batches(data, batch_size=8):
    batches = []
    for i in range(0, len(data), batch_size):
        batches.append(data[i:i + batch_size])
    padding = [0.0] * (batch_size - len(batches[-1])) if len(batches[-1]) < batch_size else []
    batches[-1].extend(padding)
    return batches


def compute_checksum(batch):
    xor_sum = 0
    for i, val in enumerate(batch):
        shifted = int(abs(val * 100)) ^ (i << 2)
        xor_sum ^= shifted
    return xor_sum % 100


def detect_anomalies(batches):
    anomalies = []
    for i, batch in enumerate(batches):
        mag_avg = sum(abs(x) for x in batch) / len(batch)
        if mag_avg > 0.3:
            anomalies.append(i)
    return anomalies if anomalies else [0]


def transform_coordinates(anomaly_indices, offset=100):
    # Irrelevant geometric mapping - distractor
    coords = []
    for idx in anomaly_indices:
        x = (idx * 31) % 17
        y = (idx * 19) % 23
        coords.append((x + offset, y + offset))
    return coords


def extract_features(signal_batches):
    features = []    
    for batch in signal_batches:
        # Real feature: spectral centroid approximation
        weighted_sum = sum(i * abs(val) for i, val in enumerate(batch))
        total_mag = sum(abs(val) for val in batch)
        centroid = weighted_sum / total_mag if total_mag > 0 else 0
        features.append(round(centroid, 3))
    
    # Distractor: unused frequency sweep
    sweep_pattern = [i * 0.1 for i in range(10)]
    normalization_factor = sum(s**2 for s in sweep_pattern) ** 0.5
    normalized_sweep = [s / normalization_factor for s in sweep_pattern]  # Dead code path
    
    return features


def correlate_patterns(feature_list):
    if len(feature_list) < 2:
        return 0
    diffs = [abs(a - b) for a, b in zip(feature_list, feature_list[1:])]
    return round(sum(diffs) / len(diffs), 4) if diffs else 0.0


def rolling_window_analysis(signal):
    window_size = 5
    if len(signal) < window_size:
        return [0.0]
    windows = [signal[i:i+window_size] for i in range(len(signal) - window_size + 1)]
    entropies = []
    for win in windows:
        norm_win = [abs(x) / sum(abs(w) for w in win) if sum(abs(w) for w in win) > 0 else 0 for x in win]
        entropy = -sum(p * p.bit_length() for p in norm_win if p > 0)  # Simplified entropy analog
        entropies.append(round(entropy, 3))
    return entropies


def analyze_signal(processed_samples):
    # Core pipeline
    batches = segment_batches(processed_samples)
    features = extract_features(batches)
    pattern_drift = correlate_patterns(features)
    
    # Critical computation chain
    window_metrics = rolling_window_analysis(processed_samples)
    avg_window_metric = sum(window_metrics) / len(window_metrics) if window_metrics else 0
    
    # Secondary metrics (some irrelevant)
    checksums = [compute_checksum(b) for b in batches]
    total_checksum = sum(checksums)
    anomaly_list = detect_anomalies(batches)
    coordinate_map = transform_coordinates(anomaly_list)  # Computed but not used
    
    # Final diagnostic calculation (answer depends only on this)
    raw_magnitude = sum(abs(x) for x in processed_samples[:32])  
    scaling_factor = 2.718281  # Approximation of e
    intermediate = (raw_magnitude * pattern_drift * scaling_factor)
    final_diagnostic = int(intermediate - (avg_window_metric * 100))
    
    # Red herring variables
    synthetic_index = sum(itertools.starmap(lambda x, y: x ^ y, enumerate(checksums))) % 500
    dummy_flag = any(len(str(c)) > 2 for c in coordinate_map)  # Always False
    fallback_value = sum(f * (i+1) for i, f in enumerate(features[:3])) * 10
    
    return final_diagnostic

# Entry point
if __name__ == "__main__":
    samples = collect_samples(base_freq=4.2, duration=2.0, sample_rate=16)
    cleaned = filter_noise(samples, threshold=0.68)
    processed_samples = [round(s * 1.05, 4) for s in cleaned]
    final_diagnostic = analyze_signal(processed_samples)
    print(f"Result: {final_diagnostic}")