def evaluate_performance(score_str, bonus_flag):
    base_points = int(score_str[:3])
    penalty = len(score_str.strip('0'))
    normalized = base_points / 10
    
    # Irrelevant metric (distractor)
    avg_char_code = sum(ord(c) for c in score_str) / len(score_str)
    
    if bonus_flag and normalized > 7.5:
        multiplier = 2
    else:
        multiplier = 1
    
    raw_score = normalized * multiplier
    final_score = int(raw_score) if raw_score % 1 < 0.5 else round(raw_score)
    adjustment = -penalty if final_score > 15 else +penalty
    result = final_score + adjustment
    return result

# Main execution
target_input = "857abc"
flag = True
output = evaluate_performance(target_input, flag)
print(f"Result: {output}")