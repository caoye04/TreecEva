import math

# Simulated sensor data processing pipeline for environmental monitoring
def acquire_signals():
    raw_signals = [i * 0.5 + (i % 7) * 0.1 for i in range(100)]
    noise_floor = sum([math.sin(x / 10) for x in raw_signals]) / len(raw_signals)
    cleaned = [sig - noise_floor + math.cos(sig / 5) for sig in raw_signals]
    return cleaned

# Irrelevant helper: signal smoothing (unused in final path)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window // 2)
        end = min(len(signal), i + window // 2 + 1)
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed

# Frequency domain analysis (distractor function)
def analyze_frequency(signal):
    fft_magnitude = 0
    for i in range(len(signal)):
        fft_magnitude += math.sin(signal[i] * 2 * math.pi / 10) * math.cos(signal[i] / 5)
    spectral_entropy = abs(fft_magnitude) / len(signal)
    return spectral_entropy

# Core preprocessing with red herring operations
def preprocess_batch(data_chunk):
    shifted_chunk = [(x * 1.05) % 100 for x in data_chunk]
    
    # Distractor variables
    temp_checksum = sum([int(x) ^ 255 for x in shifted_chunk if x > 10]) & 0xFFFF
    anomaly_flags = [x for x in shifted_chunk if x > 80 and x < 90]
    
    # Real transformation
    transformed = [math.log(abs(x) + 1) * 1.75 for x in shifted_chunk]
    normalized = [(x - min(transformed)) / (max(transformed) - min(transformed) + 1e-8) for x in transformed]
    
    # More decoys
    peak_count = len([x for x in normalized if x > 0.95])
    avg_gradient = sum(abs(normalized[i+1] - normalized[i]) for i in range(len(normalized)-1)) / (len(normalized) - 1)
    
    return normalized

# Threshold engine with fake and real logic branches
def evaluate_thresholds(metrics):
    base_levels = {"low": 0.2, "medium": 0.45, "high": 0.7}
    
    # Fake threshold scoring
    fake_score = 0
    for m in metrics:
        if m > 0.8:
            fake_score += 0.1
        elif m < 0.1:
            fake_score -= 0.05
    
    # Real dynamic thresholds
    q1 = sorted(metrics)[len(metrics)//4]
    q3 = sorted(metrics)[3*len(metrics)//4]
    iqr = q3 - q1
    dynamic_high = q3 + 1.5 * iqr
    dynamic_low = q1 - 1.5 * iqr
    
    # Misleading intermediate
    outlier_ratio = len([m for m in metrics if m < dynamic_low or m > dynamic_high]) / len(metrics)
    
    return {"dynamic_low": dynamic_low, "dynamic_high": dynamic_high, "iqr": iqr}

# Final fusion logic with critical answer computation
def finalize_filtration(processed_data, thresholds):
    # Key calculation branch
    valid_range = [x for x in processed_data if thresholds['dynamic_low'] <= x <= thresholds['dynamic_high']]
    if not valid_range:
        return -1
    
    # Decoy statistics
    modal_cluster = {}
    for x in processed_data:
        bin_key = int(x * 10)
        modal_cluster[bin_key] = modal_cluster.get(bin_key, 0) + 1
    dominant_bin = max(modal_cluster, key=modal_cluster.get)
    
    # Critical answer computation
    mean_valid = sum(valid_range) / len(valid_range)
    variance = sum((x - mean_valid) ** 2 for x in valid_range) / len(valid_range)
    stability_index = math.exp(-variance)
    reliability_factor = len(valid_range) / len(processed_data)
    
    # Final deterministic score (answer)
    filtration_score = int((mean_valid * stability_index * reliability_factor * 10000) % 100000)
    
    # Dead code path (never reached due to return)
    if filtration_score < 0:
        fallback = sum([x**2 for x in processed_data]) / 1000
        return fallback
    
    return filtration_score

# Unused cryptographic hash (red herring)
def secure_hash_sequence(seq):
    acc = 0
    for i, val in enumerate(seq):
        acc ^= int(val * 1000) << (i % 16)
        acc = (acc * 31) % (2**32)
    return hex(acc)

# Main execution with hidden critical path
if __name__ == "__main__":
    # Acquire and process data
    raw_data = acquire_signals()
    
    # Distractor: frequency analysis (not used later)
    freq_char = analyze_frequency(raw_data)
    
    # Process data through pipeline
    processed_data = preprocess_batch(raw_data)
    
    # Compute thresholds (used in final step)
    thresholds = evaluate_thresholds(processed_data)
    
    # Generate decoy hash
    _ = secure_hash_sequence(processed_data)
    
    # CRITICAL STATEMENT: Answer determined here
    filtration_score = finalize_filtration(processed_data, thresholds)
    
    # Print result as required
    print(f"Result: {filtration_score}")