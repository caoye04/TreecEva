def evaluate_performance(scores, thresholds):
    adjusted = [max(0, s - 5) for s in scores]
    filtered = [s for s in adjusted if s >= thresholds['minimum']]
    
    # Irrelevant distraction: unused variable
    temp_debug = [i for i, x in enumerate(filtered) if x > 10]
    
    normalized = [min(x, thresholds['cap']) for x in filtered]
    scaling_factor = 1.5
    normalized_ratings = [x * scaling_factor for x in normalized]
    
    # Key computation
    total_score = sum(normalized_ratings)
    return total_score

# Input data
evaluation_scores = [12, 8, 20, 3, 15, 7]
config = {'minimum': 3, 'cap': 10}

result = evaluate_performance(evaluation_scores, config)
print(f"Result: {result}")