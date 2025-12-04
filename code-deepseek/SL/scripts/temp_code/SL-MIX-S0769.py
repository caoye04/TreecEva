def calculate_student_performance(scores_data):
    base_scores = [85, 92, 78, 96, 88]
    adjustments = [5, -3, 8, -2, 4]
    
    processed_scores = []
    temp_calc = 0
    
    for idx, (score, adj) in enumerate(zip(base_scores, adjustments)):
        adjusted_score = score + adj
        processed_scores.append(adjusted_score)
        temp_calc += idx * 2  # Distractor calculation
    
    score_set = set(processed_scores)
    unique_bonus = len(score_set) * 3
    
    total_score = sum(processed_scores)
    intermediate_val = total_score // len(base_scores)
    
    bonus_adjustment = unique_bonus - 5
    processed_total = total_score - intermediate_val
    
    # Final calculation
    final_score = processed_total + bonus_adjustment
    print(f"Result: {final_score}")

# Execute the function
calculate_student_performance([])