import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    base_signals = [i * 1.5 for i in range(10)]
    noise_floor = sum([math.sin(i) for i in range(10)]) / 10
    return {f'sensor_{i}': round(base_signals[i] + noise_floor, 3) for i in range(10)}

# Legacy function - unused but looks relevant
def deprecated_analysis(data):
    temp = 0
    for k, v in data.items():
        if 'sensor_3' in k:
            temp += v * 0.7
    return int(temp // 2)

# Signal normalization using outdated method (distractor)
NORMALIZATION_FACTOR = 0.88
def normalize_signal(val):
    return val * NORMALIZATION_FACTOR if val > 1 else val

# Core configuration map (used later)
system_thresholds = {
    'critical': 12.5,
    'warning': 8.0,
    'info': 4.0
}

# Complex metric processor with red herrings
def process_metrics(entries, thresholds):
    # Irrelevant transformation pipeline
    transformed = {k: round(v ** 1.1, 4) for k, v in entries.items()}
    
    # Dummy aggregation path (dead end)
    aggregate_sum = 0
    for val in transformed.values():
        aggregate_sum += val if val < 10 else val * 0.9
    temp_diagnostic = aggregate_sum / len(transformed)
    
    # Secondary processing chain with misleading intermediate
    magnitude_score = sum(math.sqrt(v) for v in transformed.values() if v > 6)
    adjustment_factor = len([v for v in transformed.values() if v < 3])
    
    # Real computation begins here (obscured by prior noise)
    raw_values = list(entries.values())
    filtered_peaks = [v for v in raw_values if v > thresholds['warning']]
    
    # Actual logic buried under abstraction
    peak_count_weight = len(filtered_peaks) * 100
    average_base = sum(raw_values) / len(raw_values)
    stability_ratio = (min(raw_values) + 1) / (max(raw_values) + 1)
    
    # Key nonlinear transformation
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))
    
    nonlinearity_correction = sigmoid(average_base - 6)
    
    # Decoy recursive function (never called)
    def recursive_dampen(x, depth):
        if depth <= 0 or x < 1:
            return x
        return 0.9 * recursive_dampen(x - 1, depth - 1)
    
    # Final integration of metrics
    health_indicator = peak_count_weight + (average_base * 10)
    volatility_penalty = int((1 - stability_ratio) * 50)
    final_diagnostic = int(health_indicator - volatility_penalty)  # <-- Critical assignment
    
    # Unused diagnostic branches
    debug_state = {
        'adjusted': temp_diagnostic,
        'magnitude': magnitude_score,
        'adjustment': adjustment_factor
    }
    
    # Distractor: complex lambda that computes irrelevant metric
    anomaly_detector = lambda data: sum(1 for x in data if x > 9.5) - sum(1 for x in data if x < 2.5)
    _ = anomaly_detector(transformed.values())
    
    return final_diagnostic

# Entry point
if __name__ == '__main__':
    log_entries = generate_telemetry()
    
    # Spurious analysis calls (red herrings)
    _ = deprecated_analysis(log_entries)
    _ = [normalize_signal(v) for v in log_entries.values()]
    
    final_diagnostic = process_metrics(log_entries, system_thresholds)
    print(f"Result: {final_diagnostic}")