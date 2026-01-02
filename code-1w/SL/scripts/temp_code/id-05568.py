def analyze_workload(entries):
    total_tasks = sum([e['count'] for e in entries])
    completed_tasks = sum([e['count'] * 0.95 for e in entries if e['status'] == 'completed'])
    pending_tasks = len([e for e in entries if e['status'] == 'pending'])
    failed_tasks = len([e for e in entries if e['retries'] > 2])

    # Irrelevant computation: historical average (not used)
    historical_avg = sum(range(1, len(entries)+1)) / len(entries) if entries else 0

    task_distribution = {e['type']: e['count'] for e in entries}
    high_priority_count = task_distribution.get('urgent', 0)

    # Distractor: unused transformation
    transformed = [{**e, 'tag': 'analyzed'} for e in entries]

    return total_tasks, completed_tasks, high_priority_count


def calculate_efficiency(data, limit):
    base_efficiency = data[1] / data[0] if data[0] > 0 else 0
    priority_factor = 1 + (data[2] / 100)
    efficiency = base_efficiency * priority_factor

    # Red herring adjustment (not actually affecting final logic)
    temp_adjustment = 0.9 if efficiency > 0.8 else 1.0

    # Final capping logic
    if efficiency > limit:
        efficiency = limit
    return efficiency

# Main execution
work_entries = [
    {'count': 50, 'status': 'completed', 'type': 'routine', 'retries': 0},
    {'count': 30, 'status': 'completed', 'type': 'urgent', 'retries': 1},
    {'count': 10, 'status': 'pending', 'type': 'routine', 'retries': 0},
    {'count': 5, 'status': 'completed', 'type': 'critical', 'retries': 3}
]

threshold = 0.92
raw_analysis = analyze_workload(work_entries)

# Intermediate irrelevant state tracking
completion_rate = raw_analysis[1] / raw_analysis[0]
urgency_level = raw_analysis[2] > 20

# Key computation
efficiency_score = calculate_efficiency(raw_analysis, threshold)

# Distractor: secondary unused metric
stability_metric = len(work_entries) - raw_analysis[2]

# Output result
print(f"Result: {efficiency_score}")