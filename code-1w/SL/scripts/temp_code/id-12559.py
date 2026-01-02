def analyze_telemetry(data_log):
    # Irrelevant preprocessing step (distractor)
    filtered_data = [x for x in data_log if x > 0.1]
    normalized = list(map(lambda x: x / max(filtered_data), data_log))

    # Misleading statistical computation
    avg_normalized = sum(normalized) / len(normalized)
    variance_proxy = sum((x - avg_normalized) ** 2 for x in normalized)

    return normalized

# Simulated sensor readings over time
telemetry_stream = [0.5, 0.8, 0.3, 0.9, 0.6]

# Secondary system diagnostics (semi-relevant)
system_health = {
    'cpu_load': 0.65,
    'memory_usage': 0.45,
    'disk_iops': 120,
    'network_latency_ms': 25
}

# Weighted evaluation logic for performance scoring
weights = {
    'response_time': 0.4,
    'throughput': 0.3,
    'stability': 0.2,
    'resource_efficiency': 0.1
}

metrics = {
    'response_time': 0.45,  # seconds
    'throughput': 85,           # transactions per second
    'stability': 0.92,          # uptime ratio
    'resource_efficiency': 0.78 # efficiency index
}

# Helper function to simulate calibration offset (dead code path)
def apply_calibration(signal, factor=1.0):
    return [s * factor for s in signal]

# Real evaluation logic with nested logic and distractors
def evaluate_performance(met, w):
    base_scores = {}
    adjustment_factor = 0.0

    # Logical conditions with mixed arithmetic and boolean logic
    for key in met:
        raw_val = met[key]
        if key == 'response_time':
            base_scores[key] = max(0, 1 - raw_val)  # invert since lower is better
        elif key == 'throughput':
            base_scores[key] = min(1, raw_val / 100)
        else:
            base_scores[key] = raw_val  # already normalized

        # Red herring: conditional that never triggers due to domain constraints
        if raw_val > 1000:
            adjustment_factor += 0.05  # unreachable under current data

    # Complex weighted aggregation using dictionary operations
    weighted_sum = sum(base_scores[k] * w[k] for k in w)
    total_weight = sum(w.values())
    composite_score = weighted_sum / total_weight

    # Final nonlinear transformation (modest complexity)
    if composite_score > 0.85:
        bonus = 0.1
    elif composite_score > 0.75:
        bonus = 0.05
    else:
        bonus = 0

    # Distractor: unused intermediate calculation
    hypothetical_max = sum(w[k] for k in w if k != 'resource_efficiency')

    final_score = round(composite_score + bonus, 4)

    return final_score

# Additional irrelevant telemetry processing (adds cognitive load)
processed_signal = analyze_telemetry(telemetry_stream)
calibrated_signal = apply_calibration(processed_signal, 1.05)

# Key execution point
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")