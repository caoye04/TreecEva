def analyze_productivity(logs):
    total_hours = 0
    completed_tasks = 0
    idle_periods = 0
    temp_accumulator = 0  # distractor variable

    for i, entry in enumerate(logs):
        if 'work' in entry['type']:
            total_hours += entry['duration']
            completed_tasks += entry['tasks']
        elif 'idle' in entry['type']:
            idle_periods += 1
            temp_accumulator += entry['duration']  # used only here, irrelevant

    efficiency_ratio = completed_tasks / total_hours if total_hours > 0 else 0
    return efficiency_ratio, idle_periods


def validate_data_consistency(data_strings):
    # Irrelevant helper function with dead logic path
    results = []
    for s in data_strings:
        clean = s.strip().lower()
        if clean.startswith('log'):
            results.append(len(clean))
    return results  # never used


def calculate_performance_rating():
    activity_log = [
        {'type': 'work', 'duration': 8, 'tasks': 5},
        {'type': 'idle', 'duration': 2, 'tasks': 0},
        {'type': 'work', 'duration': 4, 'tasks': 3},
        {'type': 'work', 'duration': 6, 'tasks': 7},
        {'type': 'idle', 'duration': 1, 'tasks': 0}
    ]

    metadata_tags = ['Log_2023', 'Entry_Main', 'Version_1']
    tag_lengths = [len(tag) for tag in metadata_tags]  # semi-relevant, not used later

    # Use of zip and enumerate together (required)
    indexed_logs = list(enumerate(activity_log))
    processed = []
    for idx, log in indexed_logs:
        if idx % 2 == 0:
            processed.append((idx, log['tasks']))

    key_indices, task_counts = zip(*processed) if processed else ([], [])

    # Core calculation begins
    base_efficiency, idle_count = analyze_productivity(activity_log)

    adjustment_factor = 1.0
    if idle_count > 1:
        adjustment_factor -= 0.1 * idle_count

    # Additional distraction: complex but unused min/max chain
    duration_list = [entry['duration'] for entry in activity_log]
    peak_load = max(duration_list)
    avg_load = sum(duration_list) / len(duration_list)
    load_variance = sum((x - avg_load)**2 for x in duration_list) / len(duration_list)
    typical_load = min(max(avg_load, 4), 10)  # semi-relevant, not directly used

    # Final score computation
    raw_score = base_efficiency * 100
    adjusted_score = raw_score * adjustment_factor
    bonus = len(key_indices) * 2  # based on even-indexed entries
    final_score = adjusted_score + bonus

    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Trigger execution
calculate_performance_rating()