def evaluate_employee_performance():
    base_scores = [85, 90, 78, 92, 88]
    weights = [0.2, 0.25, 0.15, 0.3, 0.1]
    
    # Irrelevant distractor: unused data structure
    historical_data = {'Q1': 80, 'Q2': 85, 'Q3': 87, 'Q4': 90}
    temp_buffer = set()
    for i in range(3):
        temp_buffer.add(f"temp_record_{i}")

    # Weighted sum calculation (relevant)
    weighted_sum = sum(score * weight for score, weight in zip(base_scores, weights))
    
    # Secondary metrics with red herring
    attendance_rate = 96.5
    team_feedback = 4.7
    compliance_checks = [True, True, False, True]
    passed_compliance = all(compliance_checks)  # Not actually used later

    # Distractor computation
    lambda_offset = (lambda x: x ** 0.5)(16)  # Always 4, irrelevant
    adjustment_factor = 1.0 + (attendance_rate / 1000)  # Minor effect, but misleading
    
    # Core logic chain
    base_index = weighted_sum * adjustment_factor
    performance_category = "High" if base_index >= 85 else "Medium" if base_index >= 70 else "Low"
    
    # Conditional bonus logic
    apply_bonus = True if base_index > 75 else False
    bonus_multiplier = 1.1 if apply_bonus and performance_category != "Low" else 1.0
    
    # Final scoring with distractor variables
    final_score = base_index * bonus_multiplier
    
    # Unused but plausible-looking state tracking
    audit_log = []
    audit_log.append(f"Finalized score: {final_score:.2f}")
    audit_log.append("Compliance verified")  # Misleading log entry

    # Output the required result
    print(f"Result: {final_score}")

    return final_score

# Execute function
result = evaluate_employee_performance()