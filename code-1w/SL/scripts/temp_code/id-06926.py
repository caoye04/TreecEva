def evaluate_performance(feedback_str, base_points):
    raw_length = len(feedback_str)
    uppercase_count = sum(1 for c in feedback_str if c.isupper())
    
    if raw_length == 0:
        normalized_score = 0
    else:
        normalized_score = round(uppercase_count / raw_length, 3)
    
    trend_data = [base_points, base_points * 1.1, base_points * 0.9]
    avg_trend = sum(trend_data) // len(trend_data)
    
    adjusted_points = int(avg_trend * normalized_score)
    
    performance_tag = feedback_str.lower().strip()
    
    if 'exceeds' in performance_tag:
        performance_rank = 5
    elif 'meets' in performance_tag:
        performance_rank = 3
    else:
        performance_rank = 1
    
    multiplier_flag = performance_tag.startswith('exceeds') or 'outstanding' in performance_tag
    bonus_multiplier = 7 if multiplier_flag else 4
    
    final_score = adjusted_points + bonus_multiplier * performance_rank
    
    return final_score

# Execution context
user_feedback = "EXCEEDS Expectations with Outstanding commitment"
initial_base = 86
result = evaluate_performance(user_feedback, initial_base)
print(f"Result: {result}")