def calculate_quiz_performance():
    from collections import Counter
    
    # Student quiz data
    quiz_scores = [85, 92, 78, 96, 88, 74, 92, 85, 90, 82]
    bonus_points = [5, 3, 8, 2, 6, 10, 3, 5, 4, 7]
    penalty_threshold = 80
    
    # Intermediate calculations (some not directly used)
    score_counter = Counter(quiz_scores)
    most_common_score = score_counter.most_common(1)[0][0]
    total_bonus = sum(bonus_points)
    average_bonus = total_bonus / len(bonus_points)
    
    # Distractor: penalty calculation that doesn't affect final result
    penalty_scores = [score for score in quiz_scores if score < penalty_threshold]
    penalty_total = sum(penalty_scores) if penalty_scores else 0
    
    # Core logic: weighted scoring with bonus adjustment
    weighted_scores = []
    for i, score in enumerate(quiz_scores):
        adjusted_score = score + (bonus_points[i] * 0.5)
        weighted_scores.append(adjusted_score)
    
    # Final calculation using slicing and set operations
    top_performers = set(weighted_scores[:5])
    bottom_performers = set(weighted_scores[5:])
    
    # Distractor: intersection that doesn't contribute to final result
    overlap = top_performers & bottom_performers
    
    # Final score calculation
    final_score = sum(weighted_scores) - len(top_performers) * 2
    
    return final_score

result = calculate_quiz_performance()
print(f"Target result: {result}")