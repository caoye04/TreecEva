def calculate_performance(employee_data):
    base_score = 75
    irrelevant_bonus = 42
    misleading_multiplier = 1.5
    
    # Distractor operations with strings
    employee_names = ['alice', 'bob', 'charlie', 'diana']
    name_lengths = [len(name.upper()) for name in employee_names]
    total_chars = sum(name_lengths)
    
    # Relevant logic starts here
    performance_scores = []
    for i, employee in enumerate(employee_data):
        base = employee['hours'] * 2
        quality_bonus = employee['quality'] * 3
        score = base + quality_bonus
        
        # Distractor condition that never executes
        if score > 1000:
            score = score * misleading_multiplier
        
        performance_scores.append(score)
    
    # More distractor operations with sets
    unique_scores = set(performance_scores)
    score_difference = max(unique_scores) - min(unique_scores) if unique_scores else 0
    
    # Relevant computation
    final_score = sum(performance_scores)
    scaling_factor = 1.25
    
    # Dead code path - unused variable
    unused_adjustment = final_score / len(employee_data) if employee_data else 0
    
    # Target operation
    target_result = final_score * scaling_factor
    
    # Final distractor that doesn't affect result
    misleading_total = total_chars * irrelevant_bonus
    
    print(f"Target result: {target_result}")

# Test data
employee_records = [
    {'hours': 40, 'quality': 8},
    {'hours': 35, 'quality': 9},
    {'hours': 45, 'quality': 7}
]

calculate_performance(employee_records)