import itertools

def analyze_performance(activities):
    base_scores = {}
    penalties = {}
    for act in activities:
        duration = act['duration']
        intensity = act['intensity']
        base_scores[act['name']] = duration * intensity
        if duration < 5:
            penalties[act['name']] = 2
        else:
            penalties[act['name']] = 0
    return base_scores, penalties

def normalize_values(scores):
    total = sum(scores.values())
    normalized = {k: v / total for k, v in scores.items()}
    return normalized

def compute_aggregate(metrics, weights):
    temp_product = 1
    temp_sum = 0
    intermediate_results = []
    
    for key in metrics:
        if key in weights:
            weighted_val = metrics[key] * weights[key]
            intermediate_results.append(weighted_val)
            temp_product *= (weighted_val + 1)  # avoid zero multiplication
    
    temp_sum = sum(intermediate_results)
    
    # Distractor computation: irrelevant harmonic mean
    harmonic_mean = 0
    if len(intermediate_results) > 0:
        inv_sum = sum(1 / (x + 1e-5) for x in intermediate_results)
        harmonic_mean = len(intermediate_results) / inv_sum
    
    # Another distractor: permutation count
    perm_count = 0
    if len(intermediate_results) >= 2:
        perms = list(itertools.permutations(intermediate_results, 2))
        perm_count = len(perms)
    
    final_value = temp_sum  # actual determinant of result
    return int(final_value)

# Main execution
activities_list = [
    {'name': 'coding', 'duration': 8, 'intensity': 7},
    {'name': 'debugging', 'duration': 6, 'intensity': 9},
    {'name': 'design', 'duration': 4, 'intensity': 5},
    {'name': 'planning', 'duration': 3, 'intensity': 4}
]

base_metrics, penalty_map = analyze_performance(activities_list)
normalized_metrics = normalize_values(base_metrics)

# Weight assignment
weight_config = {
    'coding': 0.4,
    'debugging': 0.6,
    'design': 0.3,
    'planning': 0.2
}

# Misleading pre-computation
rolling_avg = sum(normalized_metrics.values()) / len(normalized_metrics)
dummy_shift = [x * 0.1 for x in normalized_metrics.values()]

final_score = compute_aggregate(normalized_metrics, weight_config)

print(f"Result: {final_score}")