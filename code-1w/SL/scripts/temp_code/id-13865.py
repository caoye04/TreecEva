def calculate_final(marks, weights):
    # Normalize marks to percentage
    normalized = [(mark / 100.0) for mark in marks]
    
    # Irrelevant distraction: compute average deviation (not used)
    mean_mark = sum(marks) / len(marks)
    deviations = [abs(m - mean_mark) for m in marks]
    avg_deviation = sum(deviations) / len(deviations)
    adjusted_weights = [w + 0.01 for w in weights]  # Fake adjustment
    
    # Real computation path
    weighted_sum = sum(w * (m / 100.0) for w, m in zip(weights, marks))
    bonus_factor = 1.0
    if all(m >= 50 for m in marks):  # Check if all marks are passing
        bonus_factor = 1.1
    
    # Apply scaling based on max weight
    max_weight = max(weights)
    scale = 0.9 + (max_weight / 100.0)
    preliminary = weighted_sum * scale * 100
    
    # Secondary logic: extra credit for high performance
    excellence_bonus = 0
    high_performers = list(filter(lambda x: x > 90, marks))
    if len(high_performers) >= 2:
        excellence_bonus = 5.0
    
    final_score = preliminary * bonus_factor + excellence_bonus
    
    # Dead code: unused diagnostic
    diagnostics = {
        'input_marks': marks,
        'weights_used': weights,
        'high_count': len(high_performers)
    }
    
    return final_score

# Main execution
marks = [85, 92, 78, 94, 88]
weights = [15, 25, 20, 30, 10]

# Some unrelated pre-processing
shadow_copy = [m * 1.01 for m in marks]
offset_adjusted = [s - 1 for s in shadow_copy]
placeholder_result = sum(offset_adjusted) / len(offset_adjusted)

final_score = calculate_final(marks, weights)
print(f"Result: {final_score}")