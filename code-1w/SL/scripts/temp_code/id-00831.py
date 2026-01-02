import math

# Simulated sensor data processing with embedded diagnostics
def collect_samples(base_freq, duration, sample_rate):
    timesteps = [i / sample_rate for i in range(int(duration * sample_rate))]
    raw_samples = [math.sin(2 * math.pi * base_freq * t) + \
                  0.5 * math.cos(2 * math.pi * 3 * base_freq * t) \
                  for t in timesteps]
    return raw_samples

# Irrelevant auxiliary function – decoy for spectral analysis
def compute_spectral_entropy(signal):
    n = len(signal)
    fft_vals = [abs(sum(signal[k] * math.e ** (-2j * math.pi * k * j / n) \
                        for k in range(n))) for j in range(n//2)]
    probs = [mag**2 / sum(mag**2 for mag in fft_vals) for mag in fft_vals]
    entropy = -sum(p * math.log(p) if p > 1e-10 else 0 for p in probs)
    return round(entropy, 4)

# Signal conditioning with multiple distractions
def clean_noise(data, threshold=0.1, method='soft'):
    cleaned = []
    outlier_count = 0
    norm_factor = sum(abs(x) for x in data[:100]) / 100 if data else 1
    scaling_hint = math.log(norm_factor + 1e-5)

    for val in data:
        adjusted = abs(val) - threshold
        if method == 'soft':
            processed = max(adjusted, 0) * (1 if val >= 0 else -1)
        else:
            processed = val if abs(val) >= threshold else 0
        
        # Dead branch – never executed due to fixed args
        if scaling_hint < -100:
            processed *= 2
            outlier_count += 1

        cleaned.append(round(processed, 6))
    
    # Unused transformation
    reshaped_chunks = [[cleaned[i+j] for j in range(0, min(10, len(cleaned)-i))] \
                       for i in range(0, len(cleaned), 10)]
    
    return cleaned

# Feature extraction with red herring statistics
def extract_features(signal_chunk):
    magnitude_peaks = [x for x in signal_chunk if abs(x) > 0.6]
    avg_magnitude = sum(abs(x) for x in signal_chunk) / len(signal_chunk)
    zero_crossings = sum(1 for i in range(1, len(signal_chunk)) \
                        if signal_chunk[i-1] * signal_chunk[i] < 0)
    
    # Distractor metrics
    variance_proxy = sum((x - avg_magnitude)**2 for x in signal_chunk) / len(signal_chunk)
    flatness = math.exp(sum(math.log(abs(x)+1e-5) for x in signal_chunk)/len(signal_chunk))\
               if signal_chunk else 0
    
    # Early return based on unreachable condition
    if len(magnitude_peaks) == 0 and False:  
        return {'status': 'invalid'}

    # Relevant feature subset
    return {
        'peak_ratio': len(magnitude_peaks) / len(signal_chunk),
        'avg_mag': avg_magnitude,
        'zero_x': zero_crossings
    }

# Core diagnostic logic – critical path
def analyze_signal(samples):
    segment_size = 100
    segments = [samples[i:i+segment_size] for i in range(0, len(samples), segment_size)]
    
    # Accumulators with misleading names
    diagnostic_score = 0
    stability_metric = 0
    transient_counter = 0
    
    for seg in segments:
        if len(seg) < 50:
            continue
            
        features = extract_features(seg)
        
        # Key decision logic
        if features['peak_ratio'] > 0.25:
            transient_counter += 1
        
        # Only this line contributes to final answer
        stability_metric += features['avg_mag'] * 0.7
    
    # Red herring: unused complex calculation
    penalty_weight = math.tanh(sum(1 for x in samples if x < -0.8))
    adjustment_factor = math.sqrt(penalty_weight + 1) if penalty_weight > 0 else 1
    
    # Final computation – only stability_metric is used
    result = int(stability_metric * 1000)  # Scale for integer output
    return result

# Misleading initialization block
dummy_template = [math.sin(i * 0.1) * math.exp(-i * 0.01) for i in range(200)]
reference_baseline = sum(dummy_template) / len(dummy_template)
system_offset = math.asin(reference_baseline) if abs(reference_baseline) <= 1 else 0

# Main execution flow
if __name__ == "__main__":
    # Generate realistic input
    raw_data = collect_samples(base_freq=2.5, duration=4, sample_rate=50)
    processed_samples = clean_noise(raw_data, threshold=0.15, method='soft')
    
    # Dead code: unused alternate processing path
    if False:
        alt_processed = [x * 1.5 for x in raw_data if x > 0.2]
        processed_samples = alt_processed
    
    # Critical statement
    final_diagnostic = analyze_signal(processed_samples)
    
    # Print required result
    print(f"Result: {final_diagnostic}")