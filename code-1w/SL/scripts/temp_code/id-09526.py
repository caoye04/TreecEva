import itertools

# Simulated biomedical signal processing system with diagnostic logic
def analyze_waveform(samples):
    if len(samples) < 10:
        return 0
    avg = sum(samples) / len(samples)
    variance = sum((x - avg) ** 2 for x in samples) / len(samples)
    return avg * (variance ** 0.5)

# Irrelevant helper - distractor function
def calculate_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

# Signal filtering - partially relevant but not used in final path
def apply_filter(signal, kernel_size=3):
    filtered = []
    pad = kernel_size // 2
    extended = [signal[0]] * pad + signal + [signal[-1]] * pad
    for i in range(len(signal)):
        window = extended[i:i + kernel_size]
        filtered.append(sum(window) / len(window))
    return filtered

# Core diagnostic engine
def evaluate_risk_level(values, baseline):
    adjusted = [v - baseline for v in values]
    positive_count = sum(1 for v in adjusted if v > 0)
    cumulative_deviation = sum(abs(v) for v in adjusted)
    if positive_count > len(values) // 2:
        return cumulative_deviation * 1.5
    else:
        return cumulative_deviation * 0.7

# Main processing pipeline
def process_metrics(indicators, limits):
    # Step 1: Extract key components
    primary_signals = indicators['waveforms']
    secondary_data = indicators['readings']
    metadata = indicators['meta']  # Unused - red herring

    # Step 2: Compute derived features
    waveform_analysis = [analyze_waveform(w) for w in primary_signals]
    
    # Distractor computation - looks important but unused
    noise_profile = [calculate_entropy(w[:5]) for w in primary_signals]
    smoothed_signals = [apply_filter(s) for s in primary_signals]  # Computed but unused

    # Step 3: Aggregate health metrics
    aggregated_metric = sum(waveform_analysis)
    
    # Step 4: Apply risk model
    risk_score = evaluate_risk_level(waveform_analysis, limits['baseline'])
    
    # Step 5: Threshold crossing analysis using set operations
    high_threshold = {i for i, v in enumerate(waveform_analysis) if v > limits['critical']}
    medium_threshold = {i for i, v in enumerate(waveform_analysis) if v > limits['warning']}
    cross_events = high_threshold & medium_threshold  # Always equals high_threshold - subtle but valid
    event_count = len(cross_events)
    
    # Step 6: Time-series pattern matching with itertools
    trend_pairs = list(itertools.combinations(waveform_analysis, 2))
    rising_trends = sum(1 for a, b in trend_pairs if b > a)
    falling_trends = sum(1 for a, b in trend_pairs if b < a)
    net_trend = rising_trends - falling_trends
    
    # Step 7: Final diagnostic synthesis
    stability_index = abs(net_trend) / (len(trend_pairs) + 1)
    diagnostic_value = risk_score + (event_count * 1000) - (stability_index * 50)
    
    # Dead code path - never executed due to prior logic
    if len(primary_signals) > 100:
        extra_correction = sum(smoothed_signals[i][0] for i in range(0, 100, 10))
        diagnostic_value += extra_correction

    # Final adjustment based on secondary data
    reading_sum = sum(secondary_data)
    if reading_sum > 0:
        diagnostic_value *= 1.1
    
    return int(diagnostic_value)

# Simulated input data
health_indicators = {
    'waveforms': [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    ],
    'readings': [0.5, 0.3, 0.2, 0.1],
    'meta': {'patient_id': 'P99X', 'version': '3.1'}
}

thresholds = {
    'baseline': 15.0,
    'warning': 25.0,
    'critical': 40.0
}

# Execute main logic
final_diagnostic = process_metrics(health_indicators, thresholds)
print(f"Target result: {final_diagnostic}")