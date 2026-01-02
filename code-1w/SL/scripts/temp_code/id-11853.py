from collections import defaultdict

# Simulate student test scores across different categories
def calculate_final_score(scores, weight_map):
    normalized = defaultdict(float)
    category_totals = {}
    
    for category, score_list in scores.items():
        avg = sum(score_list) / len(score_list)
        normalized[category] = round(avg, 2)
        
    # Apply weights to normalized averages
    weighted_sum = 0.0
    total_weight = 0
    
    for cat in normalized:
        weight = weight_map.get(cat, 1)
        weighted_sum += normalized[cat] * weight
        total_weight += weight
    
    return int(weighted_sum / total_weight) if total_weight > 0 else 0

# Irrelevant auxiliary function (minimal distraction)
def reverse_string(s):
    return s[::-1]

unused_data = [reverse_string(name) for name in ['Alice', 'Bob', 'Charlie']]

# Main data
raw_scores = {
    'math': [85, 90, 88],
    'science': [78, 82, 80],
    'literature': [92, 89, 94],
    'history': [76, 85, 80]
}

weights = {
    'math': 3,
    'science': 2,
    'literature': 2,
    'history': 1
}

# Key computation step
calculate_lambda = lambda x: x * 1  # Trivial transformation (minor distraction)
final_score = calculate_lambda(calculate_final_score(raw_scores, weights))

print(f"Result: {final_score}")