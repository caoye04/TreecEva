from collections import defaultdict

def calculate_final_score(assessments, weights):
    raw_scores = defaultdict(float)
    
    # Normalize weight keys to match assessment categories
    for key in assessments:
        if key in weights:
            raw_scores[key] = assessments[key] * weights[key]
    
    total_score = sum(raw_scores.values())
    bonus = 0.0
    
    # Apply performance bonus if all scores are above threshold
    if all(assessments[k] >= 75 for k in assessments):
        bonus = 5.0
    
    total_score += bonus
    return total_score

# Input data
assessments = {
    'quiz': 80,
    'homework': 90,
    'project': 85,
    'exam': 78
}

weights = {
    'quiz': 0.2,
    'homework': 0.25,
    'project': 0.3,
    'exam': 0.25
}

# Irrelevant utility variable (minor distraction)
status_message = "Processing evaluation..."

# Key computation
total_score = calculate_final_score(assessments, weights)

print(f"Result: {total_score}")