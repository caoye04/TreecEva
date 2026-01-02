from collections import Counter, defaultdict

# Simulate system performance monitoring with diagnostic logging
def monitor_system_operations(requests_log):
    request_counts = Counter()
    error_flags = []
    latency_samples = []
    throughput_tracker = defaultdict(int)
    temp_analysis_buffer = []

    for entry in requests_log:
        method = entry['method']
        status = entry['status']
        response_time = entry['time_ms']
        payload_size = entry['size_kb']

        # Core metrics accumulation
        request_counts[method] += 1
        if status >= 400:
            error_flags.append(status)
        latency_samples.append(response_time)
        throughput_tracker[method] += payload_size

        # Distractor: irrelevant pattern tracking
        if method == 'POST' and payload_size > 50:
            temp_analysis_buffer.append((response_time * 0.85) + 12.5)

    # Real computation: average latency
    avg_latency = sum(latency_samples) / len(latency_samples) if latency_samples else 0

    # Distractor: unused complex structure
    detailed_breakdown = {
        'per_method_avg': {m: sum(e['time_ms'] for e in requests_log if e['method'] == m) / request_counts[m]
                          for m in request_counts},
        'error_distribution': Counter(error_flags),
        'total_bytes': sum(throughput_tracker.values())
    }

    # Simulated feedback analysis (semi-relevant)
    feedback_cycle = [1 if code in [200, 201] else 0 for code in [e['status'] for e in requests_log]]
    feedback_streak = 0
    max_streak = 0
    for outcome in feedback_cycle:
        if outcome == 1:
            feedback_streak += 1
            max_streak = max(max_streak, feedback_streak)
        else:
            feedback_streak = 0

    # Feedback counter has impact on final result
    feedback_counter = sum(feedback_cycle) * max_streak

    # Distractor: bitwise obfuscation with no effect
    masked_value = 0
    for i in range(len(error_flags)):
        masked_value ^= (i * 3 + 7) & 0xF

    # Distractor: redundant state tracking
    system_state_log = []
    for i in range(0, len(latency_samples), max(len(latency_samples)//3, 1)):
        state_flag = 'STABLE' if latency_samples[i] < avg_latency else 'VOLATILE'
        system_state_log.append(state_flag)

    # Key statement: this determines the final answer
    final_score = evaluate_performance(feedback_counter, avg_latency)

    # Final reporting
    print(f"Result: {final_score}")
    return final_score


def evaluate_performance(feedback_counter, avg_latency):
    base_score = feedback_counter * 100
    penalty = int(avg_latency // 2)
    return base_score - penalty

# Synthetic input data
events = [
    {'method': 'GET', 'status': 200, 'time_ms': 45, 'size_kb': 12},
    {'method': 'POST', 'status': 201, 'time_ms': 120, 'size_kb': 64},
    {'method': 'GET', 'status': 200, 'time_ms': 30, 'size_kb': 8},
    {'method': 'PUT', 'status': 400, 'time_ms': 200, 'size_kb': 20},
    {'method': 'POST', 'status': 201, 'time_ms': 95, 'size_kb': 75},
    {'method': 'GET', 'status': 200, 'time_ms': 40, 'size_kb': 10},
    {'method': 'POST', 'status': 201, 'time_ms': 110, 'size_kb': 58},
    {'method': 'GET', 'status': 200, 'time_ms': 50, 'size_kb': 15},
    {'method': 'GET', 'status': 500, 'time_ms': 300, 'size_kb': 5},
    {'method': 'POST', 'status': 201, 'time_ms': 85, 'size_kb': 80}
]

# Execute
target_result = monitor_system_operations(events)