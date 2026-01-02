import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    base_signals = [i * 0.5 for i in range(20)]
    noise_component = [(i % 3) * 0.1 for i in range(20)]
    return [base_signals[i] + noise_component[i] for i in range(20)]

technical_log = generate_telemetry()

# Irrelevant auxiliary data - red herring
aux_cache = {f'key_{i}': i * i for i in range(15)}
shadow_buffer = [x ** 0.5 for x in aux_cache.values() if x % 2 == 0]
dummy_matrix = [[i + j for j in range(5)] for i in range(4)]

# System health thresholds (used later)
system_thresholds = {
    'critical': 7.5,
    'warning': 5.0,
    'decay_rate': 0.85
}

# Diagnostic filters - some are decoys
low_pass_filter = lambda x: [val for val in x if val > 3.0]
high_freq_detect = lambda x: sum(1 for i in range(1, len(x)) if abs(x[i]-x[i-1]) > 1.0)
phase_shift_analyze = lambda x: [round(math.sin(x[i]), 3) for i in range(len(x))]  # unused

# Data transformation pipeline
filtered_signal = low_pass_filter(technical_log)
fluctuation_score = high_freq_detect(technical_log)

# Power envelope calculation - relevant but indirect
envelope = list(map(lambda x: x * system_thresholds['decay_rate'], filtered_signal))

# Misleading intermediate diagnostics
false_diagnostics = {
    'stability': sum(1 for x in envelope if x < 4.0),
    'peak_count': len([x for x in technical_log if x > 8.0]),
    'dummy_metric': sum(dummy_matrix[0])  # dead-end metric
}

# Historical baseline - irrelevant
historical_averages = []
for day in range(7):
    daily_base = 4.0 + day * 0.3
    daily_avg = sum([daily_base + (i * 0.1) for i in range(10)]) / 10
    historical_averages.append(round(daily_avg, 2))

# Core processing function with nested logic
def process_metrics(signal, thresholds):
    # Local configuration
    config = {
        'window_size': 4,
        'tolerance': 0.15,
        'scaling_factor': 2.1
    }

    # Segment signal into windows
    segments = []
    for i in range(0, len(signal) - config['window_size'] + 1, config['window_size']):
        segment = signal[i:i + config['window_size']]
        segments.append(segment)

    # Compute windowed features
    feature_map = []
    for seg in segments:
        avg = sum(seg) / len(seg)
        var = sum((x - avg) ** 2 for x in seg) / len(seg)
        # Only variance above threshold contributes
        if var > config['tolerance']:
            normalized_peak = max(seg) * config['scaling_factor']
            adjusted = normalized_peak * thresholds['decay_rate']
            feature_map.append(adjusted)

    # Aggregate final result
    if not feature_map:
        return thresholds['warning'] * 2
    
    # Apply modular weighting based on fluctuation history
    weight_sequence = [i % 3 + 1 for i in range(len(feature_map))]
    weighted_sum = 0
    for i, val in enumerate(feature_map):
        weighted_sum += val * weight_sequence[i]

    # Final nonlinear transformation
    raw_result = weighted_sum % thresholds['critical']
    final_value = math.floor(raw_result * 100) / 100  # Round down to 2 decimals

    # Dead code branch - never executed due to logic above
    if len(segments) > 100:
        backup_system = [x * 1.5 for x in shadow_buffer]
        final_value = sum(backup_system) // 10

    return final_value

# Execute main diagnostic chain
log_data = phase_shift_analyze(technical_log)  # Note: this transforms data, but process_metrics uses original logic internally
intermediate_checksum = sum(shadow_buffer) / sum([x*x for x in range(1,6)])

# Critical execution point
final_diagnostic = process_metrics(log_data, system_thresholds)

# Output result as required
print(f"Result: {final_diagnostic}")