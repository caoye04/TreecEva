def evaluate_performance(data):
    # Preprocessing: extract relevant metrics
    raw_scores = [entry['score'] for entry in data if entry['active']]
    max_score = max(raw_scores)
    min_score = min(raw_scores)
    
    # Distractor: normalization using irrelevant baseline
    baseline = 75
    normalized = [(s - baseline) / (max_score - min_score) * 100 for s in raw_scores]
    
    # Irrelevant statistical analysis
    mean_val = sum(normalized) / len(normalized)
    variance = sum((x - mean_val) ** 2 for x in normalized) / len(normalized)
    std_dev = variance ** 0.5

    # Actual logic: count how many exceed threshold, adjusted by diversity
    threshold = (max_score + min_score) // 2
    high_performers = len([s for s in raw_scores if s > threshold])

    categories = {entry['category'] for entry in data}  # set operation
    category_boost = len(categories) * 2

    # Secondary processing: penalize imbalance
    category_count = {}
    for entry in data:
        cat = entry['category']
        category_count[cat] = category_count.get(cat, 0) + 1
    
    imbalance_penalty = 0
    counts = list(category_count.values())
    if max(counts) - min(counts) > 2:
        imbalance_penalty = 3

    # Core formula: high performers count adjusted by structural factors
    final_score = high_performers * category_boost - imbalance_penalty

    # Red herring: unused transformation
    transformed_data = [\
        {'orig': s, 'adj': s * 1.1 + std_dev} for s in raw_scores\
    ]

    return final_score

# Input data
assessment_data = [
    {'score': 88, 'category': 'math', 'active': True},
    {'score': 92, 'category': 'math', 'active': True},
    {'score': 76, 'category': 'logic', 'active': True},
    {'score': 81, 'category': 'logic', 'active': True},
    {'score': 95, 'category': 'coding', 'active': True},
    {'score': 60, 'category': 'coding', 'active': False},  # inactive
    {'score': 85, 'category': 'math', 'active': True},
    {'score': 70, 'category': 'coding', 'active': True}
]

# Execute
final_score = evaluate_performance(assessment_data)
print(f"Target result: {final_score}")