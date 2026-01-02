def evaluate_performance(data):
    base_scores = [d['score'] for d in data if d['category'] == 'technical']
    bonus = len([d for d in data if d['category'] == 'soft_skills']) * 2
    sliced = base_scores[1:4]
    avg = sum(sliced) / len(sliced)
    adjustment = 1.1 if avg >= 80 else 0.9
    return int(avg * adjustment + bonus)

assessment_data = [
    {'category': 'technical', 'score': 75},
    {'category': 'technical', 'score': 82},
    {'category': 'technical', 'score': 90},
    {'category': 'technical', 'score': 78},
    {'category': 'technical', 'score': 85},
    {'category': 'soft_skills', 'score': 88},
    {'category': 'soft_skills', 'score': 91}
]

# Irrelevant auxiliary variable (minor distraction)
temp_result = sum(d['score'] for d in assessment_data) / len(assessment_data)

final_score = evaluate_performance(assessment_data)
print(f"Result: {final_score}")