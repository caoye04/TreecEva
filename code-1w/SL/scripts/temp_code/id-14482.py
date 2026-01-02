def evaluate_performance(output, defects):
    base_score = 100
    penalty_factor = 0.9 if len(defects) > 3 else 1.0
    
    # Irrelevant computation: tracking timestamps (distractor)
    timestamps = [12, 15, 17, 20, 25]
    avg_time = sum(timestamps) / len(timestamps) if timestamps else 0
    time_efficiency = 1.0 if avg_time < 20 else 0.8
    
    # Semi-relevant filtering: only count critical defects
    critical_defects = list(filter(lambda x: x > 2, defects))
    defect_penalty = len(critical_defects) * 5
    
    # Productivity scoring with conditional expression
    productivity_bonus = 10 if output > 80 else (5 if output > 60 else 0)
    
    # Core logic for score calculation
    adjusted_score = base_score - defect_penalty + productivity_bonus
    adjusted_score *= penalty_factor  # Apply factor based on total defect count
    
    # Dead code path: never executed under current logic (red herring)
    if False and adjusted_score < 50:
        adjusted_score = 50  # Would cap score, but condition is unreachable
    
    # Unnecessary string manipulation (distractor)
    status_msg = "Performance: " + ("Good" if adjusted_score >= 80 else "Review Needed")
    char_count = len(status_msg)
    
    # Final adjustment using set operations (irrelevant to final result)
    unique_outputs = set(range(1, output + 1))
    bonus_eligible = {x for x in unique_outputs if x % 10 == 0}
    extra_bonus = len(bonus_eligible) // 3  # Not actually added anywhere
    
    # Key statement
    return int(adjusted_score)

# Input data
productivity = 72
errors = [1, 4, 2, 5, 6]

# Execution point
final_score = evaluate_performance(productivity, errors)
print(f"Result: {final_score}")