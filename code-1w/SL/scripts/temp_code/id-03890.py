def sensor_integrity_check(raw_values, baseline):
    accumulated = 0
    temp_flags = []
    decoy_sum = 0
    for val in raw_values:
        if val > 500:
            accumulated += val // 100
        elif val < 0:
            temp_flags.append(True)
        else:
            decoy_sum += val * 2  # Irrelevant computation

    adjusted_vals = [v - baseline for v in raw_values if v > 0]
    outlier_count = 0
    for x in adjusted_vals:
        if x > 400:
            outlier_count += 1
    
    # Distractor: unused transformation
    transformed = {i: (x ** 0.5) for i, x in enumerate(adjusted_vals) if x > 50}

    if len(temp_flags) > 2:
        return -999  # Dead path

    # Core logic begins here
    filtered_data = [x for x in adjusted_vals if x > 50]
    stats_summary = {
        'max_val': max(filtered_data),
        'min_val': min(filtered_data),
        'range': max(filtered_data) - min(filtered_data)
    }

    # Bit manipulation red herring
    bit_fiddle = 0
    for i in range(5):
        bit_fiddle ^= (i << 2) | 1
    
    # Set operations (required feature)
    critical_thresholds = {250, 350, 450, 550}
    observed_levels = set([x // 100 * 100 for x in filtered_data])
    threshold_set = critical_thresholds & observed_levels  # Intersection matters

    secondary_mask = {x for x in observed_levels if x % 150 == 0}  # Unused set

    def analyze_readings(data, thresholds):
        base_score = sum(data) // len(data)
        bonus = 0
        if len(thresholds) >= 2:
            bonus = len(data) * 10
        elif len(thresholds) == 1:
            bonus = 50
        
        penalty = 0
        for d in data:
            if d > 400 and d % 2 == 0:
                penalty += 15

        # Another decoy variable
        phantom_calc = (base_score ^ 255) & 1023

        # Key logic step
        if base_score > 300:
            return base_score + bonus - penalty
        else:
            return base_score - penalty

    # Unused recursive function (distractor)
    def predict_next(val_list, depth):
        if depth == 0 or len(val_list) == 0:
            return 0
        return val_list[-1] + predict_next(val_list[:-1], depth - 1)

    # Early return simulation (not taken)
    if baseline < 0:
        return 0

    final_diagnostic = analyze_readings(filtered_data, threshold_set)
    return final_diagnostic

# Simulate input data
data_stream = [120, -5, 670, 45, 320, 780, 210, -30, 550, 415]
baseline_offset = 70

result = sensor_integrity_check(data_stream, baseline_offset)
print(f"Result: {result}")