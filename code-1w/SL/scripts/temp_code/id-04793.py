def aggregate_performance(entries, limit):
    # Irrelevant tracking variables (distractors)
    total_accesses = 0
    debug_log = []
    cumulative_noise = 0.0

    # Relevant data structures
    valid_durations = []
    penalty_points = set()

    for entry in entries:
        timestamp, user_id, duration, action = entry
        total_accesses += 1

        # Conditional expression for filtering
        is_valid = duration > 0 and action in {'execute', 'commit', 'deploy'}
        exceeds_threshold = duration >= limit

        if is_valid:
            valid_durations.append(duration)
            if exceeds_threshold:
                penalty_points.add(user_id)

        # Dead computation - adds noise but not used
        cumulative_noise += duration * 0.01
        debug_log.append(f"{user_id}:{'valid' if is_valid else 'invalid'}")

    # Slicing: only consider recent 70% of valid durations
    start_idx = len(valid_durations) // 10
    filtered_durations = sorted(valid_durations)[start_idx:]

    # Compute base score using modular arithmetic on sum
    raw_sum = sum(filtered_durations)
    base_score = raw_sum % 97

    # Apply penalty deduction based on unique offenders
    adjustment_factor = len(penalty_points) * 3
    final_score = base_score - adjustment_factor

    # Red herring: complex unused calculation
    outlier_count = 0
    if filtered_durations:
        mean_duration = raw_sum / len(filtered_durations)
        outlier_count = sum(1 for d in filtered_durations if abs(d - mean_duration) > 2 * mean_duration)

    return final_score

# Simulated log data (realistic domain: system performance monitoring)
log_data = [
    (1623450001, 'usr_04', 120, 'execute'),
    (1623450065, 'usr_17', 85, 'fetch'),
    (1623450110, 'usr_04', 200, 'deploy'),
    (1623450180, 'usr_23', 50, 'execute'),
    (1623450250, 'usr_17', 300, 'commit'),
    (1623450301, 'usr_31', 40, 'deploy'),
    (1623450340, 'usr_04', 180, 'execute'),
    (1623450400, 'usr_23', 90, 'rollback')
]

threshold = 100
final_score = aggregate_performance(log_data, threshold)
print(f"Result: {final_score}")