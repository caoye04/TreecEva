from collections import Counter

def analyze_team_scores():
    team_scores = [85, 92, 78, 96, 88, 91, 83, 79, 95, 87]
    score_counter = Counter(team_scores)
    
    # Calculate statistics (some relevant, some not)
    average_score = sum(team_scores) / len(team_scores)
    highest_score = max(team_scores)
    lowest_score = min(team_scores)
    
    # Find most common score (distractor - not used in final answer)
    most_common_score = score_counter.most_common(1)[0][0]
    
    # Calculate score ranges (semi-relevant operations)
    score_range = highest_score - lowest_score
    mid_range = (highest_score + lowest_score) / 2
    
    # Target calculation
    scores_above_90 = [score for score in team_scores if score > 90]
    target_sum = sum(scores_above_90)
    
    # Adjustment calculations (some relevant, some not)
    bonus_points = len(scores_above_90) * 2
    penalty_points = 3  # distractor - never used
    adjustment_factor = bonus_points
    
    # Final result
    final_result = target_sum - adjustment_factor
    
    # Print verification
    print(f"Result: {final_result}")
    return final_result

analyze_team_scores()