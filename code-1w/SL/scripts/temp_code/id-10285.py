def calculate_final_score(values, limits):
    # Preprocessing: filter and transform values
    filtered = [x for x in values if x > 0]
    adjusted = [x * 1.5 if x < 50 else x * 0.8 for x in filtered]
    
    # Irrelevant statistical distraction
    mean_val = sum(adjusted) / len(adjusted) if adjusted else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in adjusted) / len(adjusted) if adjusted else 0
    
    # Threshold-based scoring logic
    passed_count = 0
    for val in adjusted:
        meets_all = True
        for limit in limits:
            if val < limit:
                meets_all = False
                break
        if meets_all:
            passed_count += 1
    
    # Secondary irrelevant computation (dead-end path)
    bonus_awarded = False
    if passed_count >= 3:
        bonus_awarded = True
        extra_points = 10  # Not used in final score
    
    # Core scoring formula
    base_score = sum(adjusted) // len(adjusted) if adjusted else 0
    penalty = 5 * (len(values) - len(filtered))  # Penalty for original non-positive entries
    final_score = base_score - penalty + (passed_count * 7)
    
    return final_score

# Input data
raw_values = [10, -5, 80, 45, 0, 60, 25]
thresholds = [30, 40]

# Execute main logic
temp_result = sum(x**2 for x in raw_values if x < 0)  # Distractor: unused computation
intermediate_set = set(raw_values)
duplicate_check = len(raw_values) != len(intermediate_set)

final_score = calculate_final_score(raw_values, thresholds)
print(f"Result: {final_score}")