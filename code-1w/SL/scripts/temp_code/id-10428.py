def analyze_performance(metrics, thresholds):
    score = 0
    bonus_tier = {}
    penalty_flag = False
    temp_result = 0

    # Irrelevant accumulator for distraction
    debug_sum = 0
    for k in metrics:
        debug_sum += len(k)

    base_multiplier = 1.0
    if metrics['accuracy'] > thresholds['accuracy']:
        score += 25
        base_multiplier *= 1.2
    else:
        penalty_flag = True

    if metrics['throughput'] > thresholds['throughput']:
        score += 20
        base_multiplier *= 1.15

    consistency_factor = 0
    if metrics['stability'] >= 95:
        consistency_factor = 10
        bonus_tier['stability'] = True
    else:
        consistency_factor = -5

    # Complex dictionary-based weight map (used later)
    weight_map = {
        'high': 3,
        'medium': 2,
        'low': 1
    }

    priority_level = 'medium'
    if metrics['critical_tasks'] > 5:
        priority_level = 'high'
    elif metrics['critical_tasks'] == 0:
        priority_level = 'low'

    priority_bonus = weight_map[priority_level]

    # Simulated calibration sequence (partially irrelevant)
    calibration_offset = 0
    for i in range(3):
        for j in range(2):
            calibration_offset += (i * j) % 2

    # Main scoring with multiplier application
    raw_score = score + consistency_factor + priority_bonus
    final_score = int(raw_score * base_multiplier)

    # Bonus system with early exit red herring
    def apply_bonus_system():
        nonlocal final_score
        surge_multipliers = [1.1, 1.25, 1.05]
        cumulative_boost = 0

        for m in surge_multipliers:
            if final_score < 80:
                cumulative_boost += m
            else:
                break  # Early break not always taken

        # Actual bonus logic
        if final_score > 70 and metrics['uptime'] == 100:
            final_score += 15

        # Dead code path (never executed due to condition)
        if threshold['fake_param'] > 1000:  # NameError unless defined
            final_score *= 2

        return final_score

    # Initialize missing key to prevent error
    threshold = {'fake_param': 50}

    # Execute bonus system
    final_score = apply_bonus_system()

    # Unused transformation
    normalized = round(final_score / 1.5, 3)

    print(f"Result: {final_score}")

# Input data
metrics_data = {
    'accuracy': 96,
    'throughput': 420,
    'stability': 97,
    'critical_tasks': 6,
    'uptime': 100
}

thresholds_config = {
    'accuracy': 95,
    'throughput': 400
}

analyze_performance(metrics_data, thresholds_config)