def analyze_log_patterns(log_entries, system_threshold):
    pattern_count = {}
    temp_sum = 0
    debug_flags = []

    for idx, entry in enumerate(log_entries):
        category = entry['type']
        load = entry['load']
        timestamp = entry['time']

        if category not in pattern_count:
            pattern_count[category] = 0
        pattern_count[category] += 1

        temp_sum += load * (idx + 1)

        if load > system_threshold * 2:
            debug_flags.append(f'CRITICAL_{timestamp}')
        elif load > system_threshold:
            debug_flags.append(f'WARNING_{timestamp}')

    return pattern_count, temp_sum, debug_flags


def filter_noisy_logs(log_entries, noise_categories):
    filtered = []n    redundant_total = 0
    for entry in log_entries:
        if entry['type'] not in noise_categories:
            filtered.append(entry)
        else:
            redundant_total += entry['load']
    scale_factor = len(filtered) / (len(log_entries) or 1)
    adjusted = [dict(entry, load=entry['load'] * scale_factor) for entry in filtered]
    return adjusted


def calculate_remaining_capacity(log_entries, system_threshold):
    total_load = 0
    peak_moment = None
    cumulative_weight = 0.0

    base_pattern, raw_sum, flags = analyze_log_patterns(log_entries, system_threshold)

    noise_types = ['debug', 'trace', 'heartbeat']
    cleaned_logs = filter_noisy_logs(log_entries, noise_types)

    max_load = max(entry['load'] for entry in log_entries)
    normalization_factor = 1.0 if max_load == 0 else system_threshold / max_load

    for i, entry in enumerate(cleaned_logs):
        weight = (i + 1) / len(cleaned_logs)
        adjusted_load = entry['load'] * normalization_factor
        total_load += adjusted_load

        status_rank = {'info': 1, 'warn': 2, 'error': 3}.get(entry['status'], 1)
        cumulative_weight += weight * status_rank

        if peak_moment is None or entry['load'] > peak_moment['load']:
            peak_moment = {'index': i, 'load': entry['load'], 'type': entry['type']}

    capacity_pool = 10000
    usage_estimate = total_load * cumulative_weight
    final_capacity = int(capacity_pool - usage_estimate)

    diagnostics = {
        'entries_processed': len(cleaned_logs),
        'peak_category': peak_moment['type'] if peak_moment else None,
        'normalization': round(normalization_factor, 4),
        'estimated_usage': round(usage_estimate, 2)
    }

    # Dummy tracking that doesn't affect result
    audit_trail = []
    for k, v in diagnostics.items():
        audit_trail.append(f'{k}={v}')

    return final_capacity

# Main execution
log_data = [
    {'time': 1001, 'type': 'info', 'load': 120, 'status': 'info'},
    {'time': 1002, 'type': 'debug', 'load': 80, 'status': 'info'},
    {'time': 1003, 'type': 'error', 'load': 450, 'status': 'error'},
    {'time': 1004, 'type': 'warn', 'load': 300, 'status': 'warn'},
    {'time': 1005, 'type': 'trace', 'load': 60, 'status': 'info'},
    {'time': 1006, 'type': 'error', 'load': 520, 'status': 'error'},
    {'time': 1007, 'type': 'info', 'load': 180, 'status': 'info'}
]

system_limit = 400
final_capacity = calculate_remaining_capacity(log_data, system_limit)
print(f'Result: {final_capacity}')