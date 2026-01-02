def calculate_final_score(points, penalties):
    base_score = points * 1.5
    deduction = penalties * 2
    if base_score >= 50:
        bonus = 10
    else:
        bonus = 5
    adjusted_score = base_score - deduction + bonus
    
    # Irrelevant string processing (distractor)
    status_msg = "Processing complete"
    status_msg = status_msg.upper().replace(" ", "_")
    log_entry = f"SCORE_LOG: {status_msg}"
    
    # Actual computation continues
    multiplier = 1
    if adjusted_score % 7 == 0:
        multiplier = 1.1
    final = int(adjusted_score * multiplier)
    return final

# Main execution
raw_points = 42
penalty_count = 3
initial_score = raw_points + 10  # Distractor assignment
note = "Score calculation start"  # Unused variable

final_score = calculate_final_score(raw_points, penalty_count)
print(f"Result: {final_score}")