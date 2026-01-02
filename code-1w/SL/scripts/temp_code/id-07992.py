def evaluate_performance(items_produced, defects, min_threshold):
    efficiency = items_produced / (defects + 1) if defects >= 0 else 0
    bonus_factor = 1.5 if items_produced > 200 else 1.0
    penalty = 10 if defects > 15 else 0
    
    # Irrelevant tracking variables (distractors)
    audit_log = []
    compliance_status = ""
    review_cycle = 0
    while review_cycle < 3:
        audit_log.append(f"Review {review_cycle}")
        compliance_status += "OK"
        review_cycle += 1

    # Semi-relevant normalization
    normalized_output = items_produced * bonus_factor - penalty
    
    # Conditional expression for quality tier
    quality_tier = "High" if defects <= 5 else "Medium" if defects <= 10 else "Low"
    
    # Actual scoring logic
    base_score = normalized_output * 10
    adjustment = -50 if quality_tier == "Low" else 20
    
    # Final decision with conditional expression
    final_value = base_score + adjustment if items_produced >= min_threshold else base_score * 0.5
    
    # Unused helper computation (dead code path)
    def calculate_risk(a, b):
        return a ** 2 - b * 3.7
    
    return int(final_value)

# Main execution
productivity = 240
errors = 8
target_output = 180
threshold = 150

# Dummy variables for distraction
idle_time = 12.5
overtime_hours = 4.2
worker_id = "EMP789"
shift_complete = True

# Key statement
final_score = evaluate_performance(productivity, errors, threshold)

# Output result
print(f"Result: {final_score}")