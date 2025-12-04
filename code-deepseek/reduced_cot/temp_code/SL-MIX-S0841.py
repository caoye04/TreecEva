def calculate_weighted_scores(scores_dict):
    # Irrelevant calculation that doesn't affect final result
    temp_sum = sum(scores_dict.values()) * 1.5
    weight_factor = len(scores_dict) ** 2
    
    # Main logic path
    valid_scores = {k: v for k, v in scores_dict.items() if v > 50}
    if not valid_scores:
        return 0
    
    # Distractor calculations
    avg_temp = sum(valid_scores.values()) / len(valid_scores)
    max_temp = max(valid_scores.values())
    
    # Dead code path - never executed
    if avg_temp > 1000:
        scale_factor = 0.1
    else:
        scale_factor = 1.0
    
    # Core calculation
    weighted_sum = sum(score * (i + 1) for i, score in enumerate(valid_scores.values()))
    total_weights = sum(range(1, len(valid_scores) + 1))
    
    # Misleading intermediate variable
    fake_result = (weighted_sum + temp_sum) // weight_factor
    
    # Actual result
    if total_weights > 0:
        processed_value = weighted_sum / total_weights
    else:
        processed_value = 0
    
    return processed_value

# Initial data
student_scores = {"math": 85, "science": 92, "history": 45, "english": 78, "art": 67}
backup_data = {"temp": 100, "secondary": 200}

# Irrelevant processing
backup_sum = sum(backup_data.values())
backup_avg = backup_sum / len(backup_data)

# Main processing
backup_score = 75.0  # Red herring value
processed_data = {"final_value": calculate_weighted_scores(student_scores)}

# Final assignment with dictionary operation
final_score = processed_data.get("final_value", backup_score)

# Print result
print(f"Result: {final_score}")