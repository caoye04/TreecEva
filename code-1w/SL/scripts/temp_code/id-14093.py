def calculate_final_score(records, importance_weights):
    base_score = 0
    adjustment_factor = 0.85
    temp_result = []
    
    # Extract relevant performance metrics with slicing
    recent_metrics = records[1:4]
    
    # Initialize tracking variables (some are red herrings)
    peak_value = float('-inf')
    cumulative_shift = 0
    ignored_counter = 0  # Dead variable - not used in final logic
    
    for i, metric in enumerate(recent_metrics):
        if metric > peak_value:
            peak_value = metric
        
        # Simulate bit-shift style weighting (conceptual, not actual bitwise)
        shifted = metric >> 1
        cumulative_shift += shifted
        
        # Update base score using weight map
        weight = importance_weights.get(i, 1.0)
        base_score += metric * weight
    
    # Distractor loop: processes string representations unnecessarily
    str_artifacts = [str(x) for x in records]
    joined = ''.join(str_artifacts)
    digit_sum = sum(int(c) for c in joined if c.isdigit())
    noise_correction = len(joined) - digit_sum % 7  # Computation with no impact
    
    # Conditional logic with short-circuiting (semi-relevant)
    bonus = 10 if peak_value > 50 and (cumulative_shift > 30 or True) else 5
    
    # Final computation involving dictionary lookup side effect
    modifiers = {'bonus': bonus, 'penalty': 0}
    penalty_exemption = modifiers.get('exemption', 0)  # Unused lookup
    
    final_score = int(base_score * adjustment_factor + modifiers['bonus'])
    return final_score

# Input data
sensor_data = [23, 67, 45, 56, 12]
weights_map = {0: 1.2, 1: 0.9, 2: 1.1}  # Only indices 0,1,2 are used

# Execution
final_score = calculate_final_score(sensor_data, weights_map)
print(f"Target result: {final_score}")