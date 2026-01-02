def calculate_final_score(scores, deductions):
    base_total = sum(scores)
    penalty_sum = sum(d for d in deductions if d > 0)
    adjusted_score = base_total - penalty_sum
    
    # Irrelevant string processing (minimal interference)
    status_msg = "Processing complete"
    status_len = len(status_msg.replace(" ", ""))
    
    # Linear search for a specific condition
    threshold_found = False
    for s in scores:
        if s >= 85:
            threshold_found = True
            break
    
    bonus = 10 if threshold_found else 0
    return adjusted_score + bonus

# Main execution
raw_scores = [78, 82, 91, 76]
penalties = [5, 0, 12]
initial_total = sum(raw_scores)  # Distractor variable
final_score = calculate_final_score(raw_scores, penalties)
print(f"Target result: {final_score}")