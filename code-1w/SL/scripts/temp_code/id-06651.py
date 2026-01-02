def analyze_efficiency(log_data):
    total_entries = len(log_data)
    valid_records = [entry for entry in log_data if 'status' in entry and entry['status'] == 'OK']
    error_count = total_entries - len(valid_records)
    efficiency_ratio = len(valid_records) / total_entries if total_entries > 0 else 0
    return efficiency_ratio

log_stream = [
    {'timestamp': '2023-05-01T10:00:00', 'status': 'OK', 'duration_ms': 45},
    {'timestamp': '2023-05-01T10:01:00', 'status': 'ERROR', 'duration_ms': 200},
    {'timestamp': '2023-05-01T10:02:00', 'status': 'OK', 'duration_ms': 38},
    {'timestamp': '2023-05-01T10:03:00', 'status': 'OK', 'duration_ms': 41}
]

config_flags = {
    'enable_optimization': True,
    'strict_mode': False,
    'version': '2.1'
}

processing_steps = ['parse', 'validate', 'enrich', 'export']
dummy_mask = tuple(ord(step[0]) for step in processing_steps)

baseline_threshold = 0.85

# Simulate system metric collection
current_metrics = {
    'latency': 42.0,
    'throughput': 94,
    'consistency_score': 0.97,
    'uptime_ratio': 0.992
}

benchmark_config = {
    'target_latency': 50,
    'min_throughput': 80,
    'weight_latency': 0.4,
    'weight_throughput': 0.6
}

# Irrelevant string manipulation (distractor)
header_format = "Report-{v}: Summary for Q2"
formatted_header = header_format.format(v=config_flags['version'])
title_clean = formatted_header.upper().replace(' ', '_').strip()

# Efficiency analysis (semi-relevant)
system_efficiency = analyze_efficiency(log_stream)
adjusted_uptime = current_metrics['uptime_ratio'] * (1 + 0.01 * system_efficiency)

# Core scoring logic
latency_bonus = 10 if current_metrics['latency'] <= benchmark_config['target_latency'] else 0
throughput_penalty = 5 if current_metrics['throughput'] < benchmark_config['min_throughput'] else 0

base_performance = (
    current_metrics['weight_latency'] * (benchmark_config['target_latency'] - current_metrics['latency']) +
    current_metrics['weight_throughput'] * (current_metrics['throughput'] - 75)
)

# Additional adjustment using string-derived value (subtle but relevant)
step_offset = dummy_mask[2] % 10  # 'e' -> ord('e')=101 -> 101%10=1

raw_score = base_performance + latency_bonus - throughput_penalty + step_offset

# Normalize score into a 0-100 range
normalized_score = max(0, min(100, round(raw_score * 2.5)))

# Final evaluation with config-based scaling
scaling_factor = 1.1 if config_flags['enable_optimization'] else 1.0
final_score = int(normalized_score * scaling_factor)

Result: final_score