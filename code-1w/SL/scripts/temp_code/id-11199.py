def calculate_final_score(items, importance):
    temp_total = 0
    adjustment_factor = 0.85
    penalty = 0
    bonus_tracker = []

    for i in range(len(items)):
        if items[i] < 0:
            penalty += abs(items[i]) * 0.1
        normalized = (items[i] + 10) / 20 if items[i] >= 0 else 0
        weighted_val = normalized * importance[i]
        
        # Irrelevant transformation
        squared_log = (lambda x: (x ** 2) * 0.01 if x > 0 else 0)(weighted_val)
        
        temp_total += weighted_val

        # Distractor: tracking unused values
        if weighted_val > 0.4:
            bonus_tracker.append(squared_log)

    # Simulated post-processing step (partially irrelevant)
    if len(bonus_tracker) > 2:
        adjustment_factor = 0.9
    elif len(bonus_tracker) == 0:
        adjustment_factor = 0.7

    base_score = temp_total * 100
    applied_adjustment = base_score * adjustment_factor
    
    # Final computation chain
    outlier_check = [x for x in items if x > 90]
    if len(outlier_check) > 0:
        applied_adjustment -= 5
    
    final_score = int(applied_adjustment - penalty)
    
    # Dead code path - never executed under current logic
    if False and penalty > 100:
        final_score = -1
        
    return final_score

# Main execution
raw_data = [85, 72, 90, 45, 63, -5, 98]
weights = [0.2, 0.15, 0.25, 0.1, 0.15, 0.05, 0.1]

intermediate_stats = [sum(raw_data), max(raw_data), min(raw_data)]
discount_window = 3
projection_factor = 1.05

# Unused helper
find_max_with_offset = lambda lst, offset: max(lst) + offset

# Key computation
final_score = calculate_final_score(raw_data, weights)

print(f"Result: {final_score}")