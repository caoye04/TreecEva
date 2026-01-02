def calculate_final_score(raw_data, limits):
    # Preprocessing: extract relevant entries based on threshold
    valid_entries = []
    outlier_count = 0
    temp_sum = 0

    for i, (val, flag) in enumerate(zip(raw_data, [x > 50 for x in raw_data])):
        if val < limits['min'] or val > limits['max']:
            outlier_count += 1
            continue
        if flag:
            temp_sum += val * 0.9  # adjusted contribution
        else:
            temp_sum += val
        valid_entries.append(val)

    # Distractor: unused statistical calculation
    mean_entry = sum(raw_data) / len(raw_data) if raw_data else 0
    squared_devs = [(x - mean_entry) ** 2 for x in raw_data]
    stdev_estimate = sum(squared_devs) ** 0.5

    # Scoring logic: uses slicing and conditional boosts
    sorted_valid = sorted(valid_entries)
    mid_range_slice = sorted_valid[len(sorted_valid)//4 : 3*len(sorted_valid)//4]
    base_score = sum(mid_range_slice)

    # Bonus logic based on pattern in flags (uses enumerate and zip indirectly via earlier list comp)
    long_streak = 0
    current_streak = 0
    for above in [x > 50 for x in raw_data]:
        if above:
            current_streak += 1
        else:
            long_streak = max(long_streak, current_streak)
            current_streak = 0
    long_streak = max(long_streak, current_streak)

    streak_bonus = 10 if long_streak >= 3 else 0

    # Final computation
    penalty = outlier_count * 5
    final_score = int(base_score - penalty + streak_bonus)

    # Irrelevant string processing (distractor using string methods)
    log_tag = f"ScoreCalc_v2.1".upper().replace('_', '').strip(".")
    debug_info = "Data processed: {} entries".format(len(raw_data))
    meta_hash = hash(log_tag) % 1000

    return final_score

# Main execution context
sensor_readings = [45, 52, 58, 47, 60, 63, 44, 40, 70, 72, 30]
cutoffs = {'min': 35, 'max': 75}

# Trigger the key computation
final_score = calculate_final_score(sensor_readings, cutoffs)
print(f"Result: {final_score}")