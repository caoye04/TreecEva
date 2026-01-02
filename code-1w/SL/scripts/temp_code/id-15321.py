def compute_final_score(data, thresholds):
    # Initialize tracking variables
    total_weighted = 0
    bonus_applied = False
    temp_buffer = []
    debug_log = []

    # Precompute threshold bounds
    lower_bound = thresholds.get('min', 0)
    upper_bound = thresholds.get('max', 100)
    critical_level = thresholds.get('critical', 50)

    # Misleading auxiliary computation (dead-end)
    phantom_sum = sum([x ** 0.5 for x in data if x > 25])
    normalization_factor = len(data) or 1
    adjusted_avg = sum(data) / normalization_factor if data else 0

    # Real processing begins: count valid entries above critical level
    count_above_critical = 0
    cumulative_xor = 0

    for idx, value in enumerate(data):
        # Track index-value relationships
        debug_log.append(f'Index {idx}: {value}')

        if value > critical_level:
            count_above_critical += 1
            cumulative_xor ^= idx  # Bitwise tracking of positions

        # Weighted contribution based on thresholds
        if lower_bound < value < upper_bound:
            weight = 1.0
            if value >= critical_level:
                weight = 1.5  # bonus weight
            total_weighted += value * weight

        # Buffer update (semi-relevant, not used in final score)
        temp_buffer.append(value * 0.1)

    # Conditional bonus logic
    if count_above_critical >= 3 and cumulative_xor % 2 == 1:
        bonus_applied = True
        total_weighted += 10

    # Secondary distraction: set operation with no impact
    unique_data = set(data)
    outlier_check = {x for x in unique_data if x > upper_bound}
    # This set is never used again

    # Final scoring with red herring variables
    base_score = int(total_weighted)
    penalty = len(outlier_check) * 2  # Never actually applied
    final_score = base_score  # No penalty deducted — misleading setup

    return final_score

# Input data
sensor_readings = [12, 45, 55, 60, 30, 70, 20]
config_thresholds = {'min': 10, 'max': 80, 'critical': 50}

# Execution point
final_score = compute_final_score(sensor_readings, config_thresholds)
print(f"Target result: {final_score}")