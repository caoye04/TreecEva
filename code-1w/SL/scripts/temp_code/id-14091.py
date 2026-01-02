from itertools import combinations

def analyze_workload_efficiency(tasks, threshold):
    # Simulate task processing with filtering and scoring
    durations = [t[1] for t in tasks]
    names = [t[0] for t in tasks]
    
    avg_duration = sum(durations) / len(durations)
    above_avg = [d for d in durations if d > avg_duration]
    efficiency_ratio = len(above_avg) / len(durations)

    # Irrelevant computation: count name lengths (distractor)
    total_chars = sum(len(name) for name in names)
    char_frequency_map = {c: total_chars % (ord(c) - 60) for c in 'ABC'}  # Dead-end calculation

    # Generate all 2-task combinations (only used for counting, not final result)
    combo_count = len(list(combinations(tasks, 2)))
    long_tasks = [t for t in tasks if t[1] >= threshold]

    # Scoring logic with conditional branches and integer division
    base_score = 0
    for task in tasks:
        name, duration = task
        if duration < threshold:
            if 'critical' in name:
                base_score += 3
            else:
                base_score += 2
        else:
            base_score -= 1

    adjustment_factor = len(long_tasks) // 2  # Integer division as adjustment
    adjusted_score = base_score - adjustment_factor

    # Additional irrelevant tracking
    status_log = []
    for i, duration in enumerate(durations):
        status_log.append(f'Task {i}: {'Long' if duration > threshold else 'Short'}')

    # Final score computed from adjusted logic
    final_score = adjusted_score * 10 + int(efficiency_ratio * 10)

    return final_score

# Define input data
task_list = [
    ('critical_data_load', 120),
    ('cache_warmup', 45),
    ('user_auth_init', 80),
    ('prefetch_resources', 60),
    ('startup_health_check', 150)
]

threshold_limit = 75

# Execute main function
event_log = [f'Starting analysis with threshold {threshold_limit}']
processing_phase = 'analysis'

final_score = analyze_workload_efficiency(task_list, threshold_limit)

print(f'Result: {final_score}')