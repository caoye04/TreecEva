def analyze_productivity(log_data, efficiency_map):
    base_points = 0
    penalty_count = 0
    bonus_tracker = []
    temp_multiplier = 1.0

    for entry in log_data:
        action = entry['action']
        duration = entry['duration']
        urgency = entry.get('urgency', 1)

        if action == 'task_complete':
            base_points += duration * 2
            if duration > 30:
                bonus_tracker.append(5 * urgency)
        elif action == 'idle':
            penalty_count += 1
            base_points -= 3
        elif action == 'error_fix':
            base_points += 10
            temp_multiplier *= 0.9  # simulated stress factor

    raw_efficiency = base_points / (len(log_data) or 1)

    # Irrelevant aggregation: tracks unused metrics
    debug_stats = {
        'total_entries': len(log_data),
        'penalties_applied': penalty_count,
        'bonus_awarded': sum(bonus_tracker)
    }

    # Simulated historical adjustment (unused)
    historical_avg = efficiency_map.get('prev_week', raw_efficiency)
    projected_next = efficiency_map.get('forecast', raw_efficiency * 1.1)

    adjusted_efficiency = raw_efficiency
    if efficiency_map.get('calibration_active', False):
        adjusted_efficiency *= efficiency_map.get('calibration_factor', 1.0)

    # Distractor: complex but unused conditional chain
    if adjusted_efficiency > 50 and penalty_count == 0:
        safety_margin = 1.2
    elif adjusted_efficiency < 30:
        safety_margin = 0.8
    else:
        safety_margin = 1.0

    # Actual key computation path
    stability_bonus = 0
    if len(bonus_tracker) >= 3:
        stability_bonus = sum(bonus_tracker) * 0.3

    # Secondary distractor: dead code path (never executed due to default)
    fallback_mode = False
    if debug_stats['total_entries'] > 1000 and not efficiency_map.get('enable_optimization'):
        fallback_mode = True
        adjusted_efficiency *= 0.5  # not triggered

    return adjusted_efficiency + stability_bonus


def calculate_adjusted_performance(input_logs):
    # Mapping with realistic keys
    config = {
        'prev_week': 42.5,
        'forecast': 48.0,
        'calibration_active': True,
        'calibration_factor': 1.05,
        'enable_optimization': True
    }

    intermediate_result = analyze_productivity(input_logs, config)

    # Extra transformation layer (partially relevant)
    scaling_offset = 10.0
    noise_floor = 0.05 * intermediate_result  # simulated measurement noise
    final_score = int(intermediate_result * 1.1 + scaling_offset - noise_floor)

    # Red herring: string manipulation unrelated to result
    status_label = "PERFORMANCE_" + "_LEVEL_".join(["A", "B"])
    status_label = status_label.replace("B", "X").split("_")

    # Another irrelevant dictionary operation
    metadata_tags = {'version': '2.1', 'mode': 'standard'}
    metadata_tags.update({'timestamp': 'ignored'})

    return final_score

# Input data
log_entries = [
    {'action': 'task_complete', 'duration': 45, 'urgency': 2},
    {'action': 'task_complete', 'duration': 25, 'urgency': 1},
    {'action': 'task_complete', 'duration': 50, 'urgency': 3},
    {'action': 'idle', 'duration': 10},
    {'action': 'task_complete', 'duration': 35, 'urgency': 1},
    {'action': 'error_fix', 'duration': 15},
    {'action': 'task_complete', 'duration': 60, 'urgency': 2}
]

# Execute and print result
final_score = calculate_adjusted_performance(log_entries)
print(f"Target result: {final_score}")