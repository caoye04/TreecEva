def calculate_final_score(scores, penalties):
    base_total = sum(scores)
    deduction = 0
    temp_result = 0
    
    for item in penalties:
        if item in scores:
            deduction += penalties[item]
    
    adjusted_total = base_total - deduction
    
    # Apply bonus if all scores are above threshold
    if all(s > 40 for s in scores):
        adjusted_total += 10
    
    # Irrelevant string processing (minimal interference)
    status_msg = "Processing complete."
    status_msg = status_msg.upper().replace(" ", "_")
    
    final_multiplier = 1.5
    temp_result = adjusted_total * final_multiplier
    
    return int(temp_result)

# Input data
raw_scores = [85, 76, 92, 88, 70]
penalty_map = {'missing_task': 5, 'late_submission': 3}

# Add irrelevant variable
aux_data = [1, 2, 3]

final_score = calculate_final_score(raw_scores, penalty_map)
print(f"Result: {final_score}")