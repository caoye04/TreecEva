def calculate_final_score(results, attendance):
    passing_threshold = 50
    bonus_eligibility = attendance > 0.85
    
    # Compute average excluding any score below threshold
    passed_scores = {k: v for k, v in results.items() if v >= passing_threshold}
    avg_passed = sum(passed_scores.values()) / len(passed_scores) if passed_scores else 0
    
    # Apply attendance-based multiplier
    multiplier = 1.1 if bonus_eligibility else 1.0
    adjusted_avg = avg_passed * multiplier
    
    # Final penalty if any grade is exactly at threshold (indicative of minimal pass)
    has_minimal_pass = any(v == passing_threshold for v in results.values())
    final_score = adjusted_avg - 5 if has_minimal_pass else adjusted_avg
    
    return final_score

# Input data
exam_results = {'math': 78, 'physics': 52, 'chemistry': 50, 'biology': 85}
attendance_rate = 0.92

# Execution
final_score = calculate_final_score(exam_results, attendance_rate)
print(f"Result: {final_score}")