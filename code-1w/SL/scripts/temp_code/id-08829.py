from collections import defaultdict

# Simulate student assessment scores across different categories
def calculate_final_score(scores_by_category, category_weights):
    weighted_sum = 0.0
    total_weight = 0
    
    for category, scores in scores_by_category.items():
        avg_score = sum(scores) / len(scores)
        weight = category_weights.get(category, 1)
        weighted_sum += avg_score * weight
        total_weight += weight

    return weighted_sum / total_weight if total_weight > 0 else 0

# Input data
def create_sample_data():
    data = defaultdict(list)
    data['homework'].append(85)
    data['homework'].append(90)
    data['homework'].append(87)
    data['quiz'].append(78)
    data['quiz'].append(82)
    data['exam'].append(94)
    data['exam'].append(89)
    return data

assessments = create_sample_data()
weights = {'homework': 1, 'quiz': 2, 'exam': 3}

# Irrelevant utility function (minor distraction - intervention level 5)
lambdas = [lambda x: x + 1, lambda x: x * 2]
processed = list(map(lambdas[1], [1, 2, 3]))

# Core computation
total_score = calculate_final_score(assessments, weights)
print(f"Result: {total_score}")