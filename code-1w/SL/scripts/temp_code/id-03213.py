from itertools import combinations

def calculate_final_score(results, weights):
    # Extract raw scores and apply weight multipliers using lambda
    weighted_scores = list(map(lambda x: x[0] * weights[x[1]], enumerate(results)))
    
    # Compute average of top 3 weighted scores
    top_three_avg = sum(sorted(weighted_scores, reverse=True)[:3]) / 3
    
    # Apply conditional adjustment based on performance threshold
    if top_three_avg >= 85:
        adjustment = 5
    else:
        adjustment = 2
    
    # Final score calculation
    final_score = top_three_avg + adjustment
    return final_score

# Simulated exam results (e.g., midterm, final, projects)
exam_results = [88, 92, 76, 95, 83]
bonus_weights = {0: 1.1, 1: 1.2, 2: 1.0, 3: 1.3, 4: 1.1}

# Irrelevant auxiliary variable (minor distraction, intervention level 4)
temp_diagnostic = list(combinations(exam_results, 2))

final_score = calculate_final_score(exam_results, bonus_weights)
print(f"Result: {final_score}")