def calculate_system_load():
    base_levels = [30, 45, 60, 75, 90]
    thresholds = {40: 1.2, 60: 1.5, 80: 1.8}
    temp_offset = 5

    # Irrelevant debugging log (distractor)
    debug_mode = True
    if debug_mode:
        log_entries = ['init', 'processing', 'complete']

    # Core logic: adjust levels based on threshold rules
    adjusted_levels = []
    for level in base_levels:
        multiplier = 1.0
        for thresh in sorted(thresholds.keys(), reverse=True):
            if level >= thresh:
                multiplier = thresholds[thresh]
                break
        adjusted_value = level * multiplier + temp_offset
        adjusted_levels.append(int(adjusted_value))

    # Secondary computation (minor distraction)
    avg = sum(adjusted_levels) // len(adjusted_levels)
    outlier_count = len([x for x in adjusted_levels if x > avg])

    total_capacity = sum(adjusted_levels)
    return total_capacity

result = calculate_system_load()
print(f"Result: {result}")