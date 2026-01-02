from itertools import compress

def calculate_final_score(results, weights):
    # Extract passing scores and apply weight only to qualified subjects
    passing_threshold = 50
    passed = [score >= passing_threshold for score in results.values()]
    subject_scores = list(results.values())
    weighted_scores = [a * b for a, b in zip(subject_scores, weights)]
    
    # Irrelevant distraction: unused variable (minimal interference)
    max_possible = sum(weights) * 100
    
    # Compute final score using only passed subjects' weighted scores
    filtered_scores = list(compress(weighted_scores, passed))
    base_total = sum(filtered_scores)
    count_bonus = len(filtered_scores) > 3  # bonus for taking more than 3 subjects
    extra_credit = 5 if count_bonus else 0
    final_score = base_total + extra_credit
    return final_score

# Main data
exam_results = {
    'math': 78,
    'physics': 45,
    'chemistry': 85,
    'biology': 60,
    'history': 55,
    'literature': 40
}

bonus_weights = [1.2, 1.0, 1.5, 1.3, 1.1, 0.9]

# Computation entry point
final_score = calculate_final_score(exam_results, bonus_weights)
print(f"Result: {final_score}")