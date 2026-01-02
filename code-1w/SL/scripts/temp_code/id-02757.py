def analyze_system_metrics(data, limit):
    # Irrelevant counters (distractors)
    debug_count = 0
    temp_buffer = []
    anomaly_flag = False

    # Relevant initialization
    valid_entries = 0
    total_load = 0.0
    peak_moment = -1

    for i, entry in enumerate(data):
        load = entry.get('load', 0)
        timestamp = entry.get('ts', 0)
        status = entry.get('status')

        # Semi-relevant filtering (some distraction)
        if load < 0 or status == 'inactive':
            debug_count += 1
            continue

        # Core logic: track valid data
        valid_entries += 1
        total_load += load

        if load > limit and peak_moment == -1:
            peak_moment = i

        temp_buffer.append(load * 0.1)  # unused later

    # Unused transformation (distractor)
    normalized = list(map(lambda x: round(x, 3), [total_load / (valid_entries or 1)]))

    # Another irrelevant check
    if len(temp_buffer) > 100:
        anomaly_flag = True

    return {
        'count': valid_entries,
        'aggregate': total_load,
        'first_peak_index': peak_moment
    }


threshold = 75.0
logs = [
    {'ts': 1000, 'load': 50.0, 'status': 'active'},
    {'ts': 1001, 'load': 65.0, 'status': 'active'},
    {'ts': 1002, 'load': 80.0, 'status': 'active'},  # First above threshold
    {'ts': 1003, 'load': 40.0, 'status': 'inactive'},
    {'ts': 1004, 'load': 90.0, 'status': 'active'},
    {'ts': 1005, 'load': 70.0, 'status': 'active'},
    {'ts': 1006, 'load': 85.0, 'status': 'active'}
]

# Secondary helper with lambda (required feature)
calculate_performance = lambda records, t: {
    'baseline': sum(r['load'] for r in records if r['status'] == 'active') / len(records),
    'efficiency_score': len([r for r in records if r['load'] > t]) * 10
}

# Execute analysis (does not affect final answer but adds cognitive load)
system_report = analyze_system_metrics(logs, threshold)

# Key statement
final_output = calculate_performance(logs, threshold)

# Extract target variable
efficiency_score = final_output['efficiency_score']

print(f"Result: {efficiency_score}")