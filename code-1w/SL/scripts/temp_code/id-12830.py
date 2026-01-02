def analyze_student_performance(scores, threshold=60):
    # Extract passing scores using slicing and filtering
    passing = [s for s in scores if s >= threshold]
    
    # Irrelevant distraction: compute average of first half (not used in final logic)
    mid = len(scores) // 2
    early_avg = sum(scores[:mid]) / len(scores[:mid]) if mid > 0 else 0
    
    # Compute weighted contribution from recent performance (last 3 scores)
    recent_performance = sum(scores[-3:]) / 3 if len(scores) >= 3 else sum(passing) / len(passing) if passing else 0
    
    # Use dictionary to map performance level to score multiplier
    performance_map = {"low": 1.0, "medium": 1.5, "high": 2.0}
    perf_key = "low"
    if recent_performance >= 80:
        perf_key = "high"
    elif recent_performance >= 70:
        perf_key = "medium"
    
    # Calculate base proficiency
    base_proficiency = sum(passing) / len(passing) if passing else 0
    
    # Final score computation
    final_score = base_proficiency * performance_map[perf_key]
    
    # Additional irrelevant variable
    max_possible = 100 * performance_map[perf_key]
    
    return final_score

# Main execution
student_scores = [55, 72, 78, 67, 85, 90]
final_score = analyze_student_performance(student_scores)
print(f"Result: {final_score}")