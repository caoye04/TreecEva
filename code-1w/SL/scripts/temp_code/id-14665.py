def evaluate_performance(metrics):
    base_weight = 0.8
    bonus_factor = 1.2
    penalty_rate = 0.9
    scaling_shift = 5
    temp_adjustment = 0  # Irrelevant accumulator

    # Simulated intermediate diagnostics (distractor computations)
    diagnostic_trace = set()
    for m in metrics:
        if m.startswith('perf_'):
            diagnostic_trace.add(m.upper())
        elif m.startswith('debug_'):
            temp_adjustment += len(m)  # Dead logic path

    # Actual metric processing with set operations
    essential_metrics = {'perf_cpu', 'perf_memory', 'perf_latency'}
    provided_metrics = set(metrics)
    missing_count = len(essential_metrics - provided_metrics)
    coverage_ratio = len(provided_metrics & essential_metrics) / len(essential_metrics)

    raw_score = 0
    for metric in metrics:
        if metric == 'perf_cpu':
            raw_score += 30
        elif metric == 'perf_memory':
            raw_score += 25
        elif metric == 'perf_latency':
            raw_score += 20
        elif metric == 'bonus_throughput':
            raw_score += 15

    # Apply conditional bonuses and penalties
    if 'bonus_throughput' in provided_metrics and coverage_ratio >= 0.75:
        raw_score *= bonus_factor
    if missing_count > 1:
        raw_score *= penalty_rate

    # Secondary adjustment using irrelevant trace (non-impacting)
    noise_offset = 0
    for item in diagnostic_trace:
        if 'LATENCY' in item:
            noise_offset += len(item) % 3

    final_score = int((raw_score * base_weight) + scaling_shift)
    return final_score

# Main execution
config_flags = ['debug_init', 'debug_load']
data_stream = ['perf_cpu', 'perf_memory', 'bonus_throughput']
metric_set = data_stream + config_flags

auxiliary_log = []
for entry in config_flags:
    auxiliary_log.append(entry[::-1])  # Reversed strings, unused later

final_score = evaluate_performance(metric_set)
print(f"Result: {final_score}")