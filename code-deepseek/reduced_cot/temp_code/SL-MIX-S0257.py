def calculate_weighted_average(scores):
    weight_map = lambda x: 0.4 if x >= 90 else 0.3 if x >= 80 else 0.2
    weighted_sum = sum(score * weight_map(score) for score in scores)
    total_weight = sum(weight_map(score) for score in scores)
    return weighted_sum / total_weight if total_weight > 0 else 0

def process_candidate_scores(data):
    technical_scores = [data['coding_test'], data['system_design']]
    soft_skills = [data['communication'], data['problem_solving']]
    
    tech_avg = calculate_weighted_average(technical_scores)
    soft_avg = sum(soft_skills) / len(soft_skills)
    
    final_score = (tech_avg * 0.7) + (soft_avg * 0.3)
    return round(final_score, 2)

applicant_data = {
    'coding_test': 85,
    'system_design': 92,
    'communication': 78,
    'problem_solving': 88
}

final_score = process_candidate_scores(applicant_data)
print(f"Final score: {final_score}")