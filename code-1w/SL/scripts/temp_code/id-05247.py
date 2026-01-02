def calculate_performance(response_log, cutoffs):
    correct_count = 0
    time_penalty = 0.0
    base_score = 100

    for i, entry in enumerate(response_log):
        is_correct = entry.strip().lower() == "yes"
        time_taken = len(entry)  # Mock time based on input length
        
        if is_correct and time_taken <= cutoffs[0]:
            correct_count += 1
        elif not is_correct and time_taken > cutoffs[1]:
            time_penalty += 0.5

    raw_score = correct_count * 10
    adjusted_score = raw_score - (time_penalty * 10)
    final_result = max(adjusted_score, 0)
    
    return int(final_result)

# Simulated user responses and thresholds
user_responses = ["Yes", "no", "YES", "No", "yes"]
cutoff_values = [3, 4]  # fast response: <=3, slow incorrect: >4

initial_check = len(user_responses) > 0
status_code = 200 if initial_check else 500

final_score = calculate_performance(user_responses, cutoff_values)
print(f"Result: {final_score}")