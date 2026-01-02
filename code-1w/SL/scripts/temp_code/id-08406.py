from collections import defaultdict

def calculate_final_score(results, weights):
    base_scores = defaultdict(float)
    for subject, grades in results.items():
        base_scores[subject] = sum(grades) / len(grades)
    
    # Normalize weights
    total_weight = sum(weights.values())
    normalized = {k: v / total_weight for k, v in weights.items()}
    
    final = 0
    for subject in base_scores:
        if subject in normalized:
            final += base_scores[subject] * normalized[subject]
    
    adjustment = len(results.get('math', [])) - len(results.get('history', []))
    final += adjustment * 2.5
    return round(final, 3)

# Irrelevant utility function (minor interference)
def format_report(data):
    return '; '.join(f'{k}: {v}' for k, v in data.items())

exam_results = {
    'math': [85, 90, 92],
    'physics': [78, 85],
    'chemistry': [88, 82, 84],
    'history': [90, 87]
}

bonus_weights = {
    'math': 3,
    'physics': 2,
    'chemistry': 2
}

final_score = calculate_final_score(exam_results, bonus_weights)
print(f"Result: {final_score}")