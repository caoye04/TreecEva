def analyze_system_performance(raw_logs, threshold_multiplier=1.3):
    # Preprocess log data: extract response times and error flags
    response_times = [entry['response'] for entry in raw_logs if entry['type'] == 'request']
    error_flags = [entry['error'] for entry in raw_logs if entry['type'] == 'request']
    heartbeat_intervals = [50, 48, 52, 49]  # Simulated fixed sensor readings (distractor)

    # Irrelevant statistical distraction
    avg_heartbeat = sum(heartbeat_intervals) / len(heartbeat_intervals)
    variance_probe = sum((x - avg_heartbeat) ** 2 for x in heartbeat_intervals)

    # Compute rolling average of response times
    window_size = 3
    smoothed_times = []
    for i in range(len(response_times)):
        if i < window_size - 1:
            smoothed_times.append(response_times[i])  # No smoothing at start
        else:
            window_avg = sum(response_times[i - j] for j in range(window_size)) / window_size
            smoothed_times.append(window_avg)

    # Detect anomalies using dynamic threshold
    base_threshold = sum(response_times) / len(response_times) * threshold_multiplier
    anomalies = 0
    for t in smoothed_times:
        if t > base_threshold:
            anomalies += 1

    # Secondary metric: consecutive high-latency events
    consecutive_high = 0
    max_consecutive = 0
    for t in response_times:
        if t > base_threshold * 0.9:  # Slightly lower threshold for trend detection
            consecutive_high += 1
        else:
            max_consecutive = max(max_consecutive, consecutive_high)
            consecutive_high = 0
    max_consecutive = max(max_consecutive, consecutive_high)

    # Bitwise diagnostic signature (semi-relevant)
    signature = anomalies ^ max_consecutive
    if len(str(signature)) > 2:
        signature = signature & 0xFF  # Clamp to 8 bits

    # Simulate state correlation with external modules (distractor)
    module_health = {'A': True, 'B': False, 'C': True}
    active_modules = sum(1 for v in module_health.values() if v)
    expected_load = active_modules * 42.5

    # Core logic: evaluate system state based on error ratio and anomalies
    critical_errors = sum(1 for e in error_flags if e == 'CRITICAL')
    error_rate = critical_errors / len(error_flags) if error_flags else 0

    # Conditional expression used as required
    risk_level = 'high' if error_rate > 0.1 or anomalies > 5 else 'normal'

    # Final diagnostic computation — key answer point
    stability_score = (100 - (anomalies * 3)) - (critical_errors * 4)
    final_diagnostic = stability_score if risk_level == 'normal' else stability_score - 20

    return final_diagnostic


def process_metrics(logs, state_hint):
    # Additional layer of processing with conditional bypass
    base_value = analyze_system_performance(logs)
    adjustment = 0
    if state_hint.get('redundancy_active'):
        adjustment = 5
    elif state_hint.get('degraded_mode'):
        adjustment = -10
    # This function appears important but only minor effect
    return base_value + adjustment

# Input data setup
log_data = [
    {'type': 'request', 'response': 120, 'error': None},
    {'type': 'request', 'response': 150, 'error': None},
    {'type': 'request', 'response': 160, 'error': 'CRITICAL'},
    {'type': 'request', 'response': 180, 'error': 'CRITICAL'},
    {'type': 'request', 'response': 140, 'error': None},
    {'type': 'request', 'response': 200, 'error': None},
    {'type': 'request', 'response': 220, 'error': 'CRITICAL'},
    {'type': 'request', 'response': 130, 'error': None},
    {'type': 'request', 'response': 170, 'error': None},
    {'type': 'request', 'response': 190, 'error': None}
]

system_state = {
    'load': 0.78,
    'degraded_mode': True,
    'redundancy_active': False,
    'failover_count': 2
}

# Execute main logic
final_diagnostic = process_metrics(log_data, system_state)
print(f"Result: {final_diagnostic}")