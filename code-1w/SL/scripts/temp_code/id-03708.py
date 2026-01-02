from collections import defaultdict

def calculate_final_score(results):
    scores = defaultdict(float)
    
    for subject, grades in results.items():
        if len(grades) >= 3:
            # Only consider top 3 scores
            sorted_grades = sorted(grades, reverse=True)[:3]
            avg = sum(sorted_grades) / 3
            scores[subject] = avg * 1.1 if avg >= 85 else avg
        else:
            scores[subject] = sum(grades) / len(grades)
    
    # Compute overall weighted score
    weights = {'math': 1.2, 'physics': 1.1, 'chemistry': 1.0, 'biology': 0.9}
    total, weight_sum = 0.0, 0.0
    
    for subj, score in scores.items():
        w = weights.get(subj, 1.0)
        total += score * w
        weight_sum += w

    return int(total / weight_sum)

# Irrelevant utility function (minimal distraction)
def format_percentage(val):
    return f'{val:.1f}%'

# Input data
exam_results = {
    'math': [88, 92, 85, 78],
    'physics': [76, 81, 89],
    'chemistry': [90, 87],
    'biology': [75, 80, 85, 90]
}

final_score = calculate_final_score(exam_results)
print(f"Result: {final_score}")