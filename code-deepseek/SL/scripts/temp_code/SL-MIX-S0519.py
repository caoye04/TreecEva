def calculate_performance(scores, weights):
    base_scores = [score * 2 for score in scores]
    weighted_scores = [score * weight for score, weight in zip(base_scores, weights)]
    
    # Distractor calculations that don't affect final result
    bonus_points = sum(scores) * 0.1
    max_possible = max(scores) * len(scores)
    average_unweighted = sum(scores) / len(scores)
    
    weighted_total = sum(weighted_scores)
    penalty_adjustment = 15
    
    # Final computation chain
    intermediate = weighted_total - bonus_points
    final_adjustment = intermediate + 5
    final_score = weighted_total - penalty_adjustment
    
    print(f"Result: {final_score}")
    return final_score

# Test data
student_scores = [85, 92, 78, 88]
assignment_weights = [0.25, 0.30, 0.20, 0.25]

calculate_performance(student_scores, assignment_weights)