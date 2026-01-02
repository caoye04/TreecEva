def analyze_performance(marks, thresholds):
    above_threshold = [m for m in marks if m >= thresholds['pass']]
    below_threshold = [m for m in marks if m < thresholds['pass']]
    
    # Distractor: unused computation
    avg_deviation = sum(abs(m - 70) for m in marks) / len(marks) if marks else 0
    
    passed_count = len(above_threshold)
    failed_count = len(below_threshold)
    
    # Conditional expression (required feature)
    performance_level = 'high' if passed_count > failed_count * 2 else 'moderate' if passed_count > failed_count else 'low'
    
    bonus_points = 10 if performance_level == 'high' else 5 if performance_level == 'moderate' else 0
    
    # Complex but irrelevant string transformation (distractor)
    status_msg = "Performance: " + ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(performance_level)])
    
    base_score = sum(above_threshold) // len(above_threshold) if above_threshold else 0
    penalty = failed_count * 3
    
    # Multiple assignments and distractor variables
    temp_factor, noise_offset, _ = (1.1, -2, 'irrelevant')
    
    # Real calculation path with interference
    adjusted_score = base_score * temp_factor - noise_offset
    final_score = int(adjusted_score) - penalty + bonus_points
    
    # Dead code path (interference)
    if False:
        final_score *= 1.5
        final_score += sum(len(thresholds[k]) * 2 for k in thresholds if isinstance(thresholds[k], list))
    
    return final_score

# Main execution
exam_marks = [88, 92, 67, 74, 55, 90, 78, 83]
score_thresholds = {
    'pass': 70,
    'distinction': 85,
    'categories': ['math', 'science', 'english']  # Unused
}

# Trigger key computation
total_valid = len([m for m in exam_marks if m >= score_thresholds['pass']])
scaling_factor = 1.05 if total_valid >= 5 else 1.0

final_score = analyze_performance(exam_marks, score_thresholds)
final_score = int(final_score * scaling_factor)  # Final adjustment

print(f"Result: {final_score}")