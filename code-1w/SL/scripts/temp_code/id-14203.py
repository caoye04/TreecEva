import itertools

# Simulated sensor array diagnostics with mixed signal processing
def analyze_sensor_stream(raw_readings, calibration_factor):
    filtered = [x for x in raw_readings if abs(x) > 0.1]
    normalized = [round(x * calibration_factor, 6) for x in filtered]
    
    # Irrelevant transformation: frequency harmonics (dead end)
    harmonic_analysis = [val * (2 ** 0.5) for val in normalized[:5]]
    spectral_peak = sum(harmonic_analysis) / len(harmonic_analysis) if harmonic_analysis else 0

    # Actual signal path: trend detection via sliding window
    window_size = 3
    trends = []
    for i in range(len(normalized) - window_size + 1):
        window = normalized[i:i+window_size]
        trend = (window[2] - window[0]) / 2  # Rate of change estimate
        trends.append(trend)
    
    # Distractor: unused smoothing operation
    smoothed_trends = [sum(trends[i:i+3]) / 3 for i in range(len(trends)-2)] if len(trends) > 2 else trends
    
    # Key metric: average absolute trend
    avg_abs_trend = sum(abs(t) for t in trends) / len(trends) if trends else 0
    return avg_abs_trend

# Legacy system compatibility layer (mostly irrelevant)
def legacy_checksum(sequence):
    acc = 0
    for item in sequence:
        acc = (acc * 31 + int(item)) % 10007
    return acc  # Never used in main logic

# Core diagnostic engine
def aggregate_metrics(trend_sequence, reference):
    deviation_scores = [abs(t - reference) for t in trend_sequence]
    weighted_sum = sum(t * w for t, w in zip(deviation_scores, itertools.cycle([0.8, 1.1, 0.9])))
    
    # Red herring: entropy calculation (not used)
    from math import log2
    prob_dist = [d / sum(deviation_scores) for d in deviation_scores if d > 0]
    entropy = -sum(p * log2(p) for p in prob_dist) if prob_dist else 0
    
    # Critical adjustment factor derived from pattern cycles
    cycle_patterns = list(itertools.combinations_with_replacement([1,2], 2))
    pattern_offset = len(cycle_patterns)  # Always 3: (1,1), (1,2), (2,2)
    
    result = weighted_sum * 100 + pattern_offset
    return int(result)

# Unused auxiliary function: buffer integrity verification
def verify_integrity(tag, length_hint):
    return hash((tag, length_hint)) % 17 == 0

# Main execution block
if __name__ == "__main__":
    # Simulated input data
    primary_signal = [-0.34, 0.0, 0.56, -0.78, 0.12, 0.89, -0.45, 0.67]
    calibration_coeff = 1.75
    base_reference = 0.41
    
    # Dead variables: simulated noise profiles
    noise_floor = [0.01 * i for i in range(8)]
    interference_mask = [n * 0.5 for n in noise_floor]
    
    # Execute core analysis
    trend_data = analyze_sensor_stream(primary_signal, calibration_coeff)
    
    # Unused intermediate: historical comparison
    historical_deviation = abs(trend_data - 0.39)
    
    # Buffer sizing heuristic (used later)
    outlier_buffer = max(3, min(12, int(trend_data * 10)))  # Evaluates to 7
    
    # Critical computation point
    final_diagnostic = aggregate_metrics(trend_data, base_reference) // outlier_buffer
    
    # Superfluous logging
    debug_trace = legacy_checksum([int(trend_data * 100)])
    verify_integrity("diagnostic", debug_trace)
    
    print(f"Result: {final_diagnostic}")