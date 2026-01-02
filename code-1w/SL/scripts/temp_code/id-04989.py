def evaluate_performance(feedback, thresh):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_result = 0

    for key, values in feedback.items():
        if not isinstance(values, list):
            continue

        entry_sum = sum(v for v in values if v > 0)
        entry_count = len([v for v in values if isinstance(v, int)])
        
        # Distractor: irrelevant averaging of positive entries
        avg_positive = entry_sum / entry_count if entry_count else 0
        
        if entry_count > thresh:
            base_score += entry_sum % 7
            if 'critical' in key:
                penalty_adjustment -= (entry_sum // 5)
        else:
            base_score += entry_count % 4

        # Dead computation: collected but never used
        if entry_sum > 10:
            bonus_tracker.append(entry_sum * 0.1)

    # Semi-relevant transformation
    adjusted_base = max(base_score, abs(penalty_adjustment))

    # Secondary distractor loop: counts characters in keys (semi-relevant)
    total_chars = 0
    for k in feedback.keys():
        total_chars += len(k)
    
    char_bonus = total_chars % 11 if total_chars > 20 else 0

    # Final logic: only base_score and char_bonus matter
    final_calc = adjusted_base + char_bonus

    # Misleading intermediate with no effect
    temp_result = (base_score * 2) - penalty_adjustment
    
    return final_calc

# Setup data
feedback_dict = {
    'user_feedback': [4, -1, 8, 2],
    'critical_issues': [6, 3, 9, -2, 5],
    'notes': [1, 1],
    'critical_edge_cases': [7, 8]
}

threshold = 3

# Execution
interim_value = sum(len(arr) for arr in feedback_dict.values())  # Red herring
flag_state = (threshold % 2 == 1)

final_score = evaluate_performance(feedback_dict, threshold)

print(f"Result: {final_score}")