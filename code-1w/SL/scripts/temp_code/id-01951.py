import math

# Simulated sensor signal preprocessing for a medical diagnostics system
def preprocess_signal(raw_data, filter_threshold=0.1):
    filtered = [x for x in raw_data if abs(x) > filter_threshold]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-8) for x in filtered]
    return normalized

# Signal entropy calculation (distractor function - not used in final result)
def calculate_entropy(data):
    from collections import Counter
    counts = Counter(map(lambda x: round(x, 1), data))
    total = len(data)
    return -sum((freq/total) * math.log2(freq/total) for freq in counts.values())

# Frequency domain transformation (dead code path - misleading)
def to_frequency_domain(time_series):
    # Simulated FFT - never actually called
    N = len(time_series)
    fft_result = []
    for k in range(N):
        real = sum(time_series[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        imag = sum(-time_series[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        fft_result.append(complex(real, imag))
    return fft_result

# Main processing pipeline
def extract_features(signal_chunk):
    squared_values = [x**2 for x in signal_chunk]
    moving_avg = []
    window_size = 3
    for i in range(len(squared_values) - window_size + 1):
        moving_avg.append(sum(squared_values[i:i+window_size]) / window_size)
    
    # Distractor variables
    temp_analysis_1 = sum(moving_avg) * 0.05
    temp_analysis_2 = max(moving_avg) - min(moving_avg)
    outlier_flags = [1 if x > 0.8 else 0 for x in moving_avg]
    
    return moving_avg

# Secondary transformation with zip and enumerate (relevant usage)
def modulate_response(base_features, rhythm_pattern):
    modulated = []n    for i, (feat, rhythm) in enumerate(zip(base_features, rhythm_pattern)):
        phase_shift = math.sin(i * 0.5)
        # Complex but ultimately unused modulation component
        decoy_component = phase_shift * rhythm * 0.1
        effective_weight = 0.7 + 0.3 * math.cos(rhythm)
        modulated.append(feat * effective_weight + decoy_component)
    return modulated

# Aggregation logic with lambda abstraction (key concept)
def aggregate_health_index(modulated_features):
    # Critical lambda transformation
    severity_map = lambda x: 1 / (1 + math.exp(-10 * (x - 0.3)))
    risk_scores = [severity_map(val) for val in modulated_features]
    
    # Real computation path
    base_index = sum(risk_scores)
    penalty_factor = 0
    for i, score in enumerate(risk_scores):
        if score > 0.7 and i < len(risk_scores) // 2:
            penalty_factor += 0.1
    
    # Distractor: elaborate but unused complexity
    dynamic_weights = [math.tanh(score) for score in reversed(risk_scores)]
    weighted_sum = sum(w * s for w, s in zip(dynamic_weights, risk_scores))
    temporal_decay = sum(risk_scores[i] * (0.9 ** i) for i in range(len(risk_scores)))
    
    # Final index calculation (only this matters)
    return int(round(base_index * 100 + penalty_factor * 50))

# Unused auxiliary analysis (red herring)
def analyze_rhythm_consistency(pattern):
    diffs = [abs(pattern[i+1] - pattern[i]) for i in range(len(pattern)-1)]
    consistency = sum(1 for d in diffs if d < 0.1)
    return consistency / len(diffs)

# Primary execution flow
if __name__ == "__main__":
    # Simulated biomedical signal input
    raw_eeg_data = [
        0.05, -0.03, 0.45, 0.67, -0.23, 0.89, 0.12, -0.01, 0.56,
        0.78, 0.91, -0.34, 0.65, 0.21, 0.55, 0.88, 0.44, 0.76
    ]
    
    cardiac_rhythm = [
        0.33, 0.35, 0.32, 0.34, 0.67, 0.33, 0.31, 0.89, 0.34,
        0.33, 0.21, 0.35, 0.34, 0.36, 0.33, 0.32, 0.35, 0.34
    ]
    
    # Irrelevant preprocessing chain
    cleaned_data = preprocess_signal(raw_eeg_data, 0.05)
    entropy_metric = calculate_entropy(cleaned_data)  # Computed but unused
    
    # Core feature extraction (starts relevant path)
    features = extract_features(cleaned_data)
    
    # Distractor: rhythm analysis (never connected to output)
    rhythm_score = analyze_rhythm_consistency(cardiac_rhythm)
    processed_rhythm = [r * 1.5 for r in cardiac_rhythm if r > 0.3]
    
    # Key transformation using zip and enumerate
    processed_signals = modulate_response(features, processed_rhythm[:len(features)])
    
    # FINAL COMPUTATION - TARGET INTERVENTION POINT
    final_diagnostic = aggregate_health_index(processed_signals)
    
    # OUTPUT REQUIRED RESULT
    print(f"Target result: {final_diagnostic}")