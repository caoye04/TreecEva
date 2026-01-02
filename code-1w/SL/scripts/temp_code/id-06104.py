from itertools import combinations

# System performance evaluation with noise filtering
def analyze_response_times(raw_logs, threshold):
    filtered = [x for x in raw_logs if x > 0]
    anomalies = [t for t in filtered if t > threshold]
    normalized = [round(t / max(filtered), 3) for t in filtered]
    return normalized, len(anomalies)

# Misleading auxiliary function (not directly used in final result)
def compute_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

# Core logic: evaluate system metrics against baseline
def evaluate_performance(metrics, baseline):
    adjustment_factor = 0.85
    deviation_sum = 0
    
    # Simulate multi-step state tracking
    states = {'initial': True, 'calibrated': False, 'finalized': False}
    temp_buffer = []
    
    for key, value in sorted(metrics.items()):
        if key.startswith('sys_'):
            deviation = abs(value - baseline.get(key, 0))
            if deviation > 5:
                temp_buffer.append(deviation * 0.1)
            else:
                temp_buffer.append(deviation * 0.2)
    
    # Use itertools to generate diagnostic pairs (unused red herring)
    diagnostic_pairs = list(combinations(temp_buffer[:4], 2))
    pair_count = len(diagnostic_pairs)
    
    # Actual computation path
    for tb in temp_buffer:
        deviation_sum += tb ** 1.5  # non-linear accumulation
    
    # Dead code branch (never executed due to state)
    if states['calibrated'] and not states['finalized']:
        deviation_sum *= 1.2
    
    # Final transformation
    adjusted_deviation = deviation_sum * adjustment_factor
    score = 100 - adjusted_deviation
    
    # Irrelevant sorting of unused list
    sorted_diagnostics = sorted(temp_buffer, reverse=True)
    shuffled_copy = sorted_diagnostics.copy()
    
    # Final score clamped to realistic range
    final_score = max(10, min(95, round(score, 2)))
    
    # Unused diagnostic print mock-up
    debug_payload = {"diagnostics": pair_count, "buffer_len": len(temp_buffer)}
    
    return final_score

# Input data
system_logs = [120, 150, -5, 200, 180, 0, 210]
normalized_times, anomaly_count = analyze_response_times(system_logs, threshold=190)

baseline_config = {
    'sys_response': 100,
    'sys_throughput': 80,
    'sys_latency': 50,
    'sys_reliability': 95
}

current_metrics = {
    'sys_response': 110,
    'sys_throughput': 85,
    'sys_latency': 58,
    'sys_reliability': 92,
    'debug_flag': 1  # irrelevant key
}

# Execute main logic
temp_analysis = [x * 0.9 for x in normalized_times]
entropy_diagnostic = compute_entropy([int(x*100) for x in normalized_times])

final_score = evaluate_performance(current_metrics, baseline_config)

print(f"Result: {final_score}")