def analyze_workload(metrics):
    # Irrelevant preprocessing
    normalized = {k: v / (sum(metrics.values()) + 1e-6) for k, v in metrics.items()}
    threshold = 0.15
    significant = {k: v for k, v in normalized.items() if v > threshold}

    # Distractor: unused transformation
    inverted = {k: 1 / (v + 1e-6) for k, v in metrics.items()}
    decayed = [metrics['throughput'] * (0.9 ** i) for i in range(5)]

    return len(significant)


def validate_pipeline(config):
    # Misleading validation logic
    rules = [
        config.get('timeout') < 30,
        config.get('retries') >= 2,
        config.get('batch_size') % 2 == 0
    ]
    passed = sum(rules)
    score = passed * 10

    # Dead code path (never used)
    if score > 25:
        adjustment = 1.5
    else:
        adjustment = 0.7

    return score  # Unused return


def compute_efficiency_factor(runtime_data):
    base = runtime_data['duration']
    overhead = runtime_data['setup_time'] + runtime_data['teardown_time']
    useful = runtime_data['processing_time']

    efficiency = (useful / (base + 1e-6)) * 100
    penalty = overhead * 2.5

    # Red herring calculation
    synthetic_load = (runtime_data['peaks'][0] + runtime_data['peaks'][-1]) / 2
    noise_ratio = synthetic_load / (sum(runtime_data['peaks']) + 1e-6)

    final_factor = efficiency - penalty
    return max(final_factor, 0)


def extract_signal_strength(log_entries):
    amplitudes = [entry['amplitude'] for entry in log_entries]
    filtered = [a for a in amplitudes if a > 50]
    average_signal = sum(filtered) / len(filtered) if filtered else 0

    # Unused statistical distraction
    variance = sum((x - average_signal) ** 2 for x in filtered) / len(filtered) if filtered else 0
    snr = average_signal / (variance + 1e-6)

    return average_signal


def aggregate_performance(trace, log):
    # Core relevant logic starts here
    step_weights = {'init': 0.1, 'exec': 0.6, 'finalize': 0.3}
    weighted_phases = [
        trace['phases'][p] * step_weights[p]
        for p in ['init', 'exec', 'finalize']
        if p in trace['phases']
    ]
    base_performance = sum(weighted_phases)

    # Key data manipulation using slicing
    recent_logs = log[-5:]  # Last five entries
    activity_burst = sum(recent_logs[i]['ops'] for i in range(len(recent_logs)) if i % 2 == 0)

    # Dictionary-based state tracking
    state_map = {i: {'active': True, 'score': recent_logs[i]['ops'] * 0.7} for i in range(len(recent_logs))}
    bonus = sum(state_map[i]['score'] for i in state_map if i in (1, 3))

    # Critical interference: multiple similar variables
    temp_result = base_performance * 100 + bonus
    preliminary_score = temp_result - 12.5
    adjustment_factor = len([x for x in trace['flags'] if x]) * 2.1

    # Final computation
    final_score = int(preliminary_score + adjustment_factor + activity_burst * 0.3)

    # This print is required for execution visibility
    print(f"Result: {final_score}")
    return final_score

# Simulated input data
execution_trace = {
    'phases': {'init': 0.2, 'exec': 0.65, 'finalize': 0.15},
    'flags': [False, True, False, True, True],
    'context': {'priority': 3, 'mode': 'production'}
}

optimization_log = [
    {'timestamp': '12:01', 'ops': 40, 'optimized': True},
    {'timestamp': '12:02', 'ops': 60, 'optimized': False},
    {'timestamp': '12:03', 'ops': 55, 'optimized': True},
    {'timestamp': '12:04', 'ops': 70, 'optimized': True},
    {'timestamp': '12:05', 'ops': 65, 'optimized': False},
    {'timestamp': '12:06', 'ops': 80, 'optimized': True}
]

# Irrelevant setup
system_metrics = {
    'throughput': 1250,
    'latency': 45,
    'errors': 3
}
config_params = {
    'timeout': 25,
    'retries': 3,
    'batch_size': 64
}
runtime_info = {
    'duration': 120,
    'setup_time': 10,
    'teardown_time': 8,
    'processing_time': 90,
    'peaks': [85, 90, 95, 88, 92]
}
log_data = [
    {'amplitude': 60}, {'amplitude': 70}, {'amplitude': 55},
    {'amplitude': 80}, {'amplitude': 65}, {'amplitude': 75}
]

# Unused function calls (red herrings)
analyze_workload(system_metrics)
validate_pipeline(config_params)
compute_efficiency_factor(runtime_info)
extract_signal_strength(log_data)

# Execution point of interest
final_score = aggregate_performance(execution_trace, optimization_log)