def calculate_final_score(records, importance_weights):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_aggregate = []
    
    # Misleading pre-scan: computes unused statistic
    avg_length = sum(len(str(r)) for r in records) / len(records) if records else 0
    dummy_variance = sum((len(str(r)) - avg_length) ** 2 for r in records) / len(records) if records else 0
    
    for idx, (value, weight) in enumerate(zip(records, importance_weights)):
        if value == 0:
            penalty_adjustment -= 2
            continue
        
        raw_contribution = value * weight
        
        # Secondary logic branch that affects tracking but not core score
        if raw_contribution > 10:
            bonus_tracker.append(idx)
        
        transformed_value = abs(raw_contribution) ** 0.5 if raw_contribution < 0 else raw_contribution ** 0.3
        temp_aggregate.append(transformed_value)
        
        # Core scoring happens here
        base_score += int(transformed_value)
    
    # Another red herring: set-based uniqueness check with no downstream impact
    unique_indices = set(bonus_tracker)
    spurious_metric = len(unique_indices) * 1.5 if unique_indices else 0
    
    # Final adjustment using only base components
    final_score = base_score + penalty_adjustment
    
    # Debug prints removed; only final result matters
    return final_score

# Input data
student_grades = [85, 92, 78, 0, 96]
coefficient_weights = [0.8, 1.1, 0.9, 1.0, 1.2]

# Execution point of interest
temp_result = sum(student_grades)  # irrelevant accumulation
dummy_flag = any(g < 80 for g in student_grades)  # side condition

final_score = calculate_final_score(student_grades, coefficient_weights)
print(f"Target result: {final_score}")