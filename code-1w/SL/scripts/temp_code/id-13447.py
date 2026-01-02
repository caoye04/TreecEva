def compute_final_score(data, weight_map):
    base_scores = [entry['value'] for entry in data]
    indices = {i: val for i, val in enumerate(base_scores)}
    
    # Irrelevant transformation (distractor)
    transformed = []
    for x in base_scores:
        temp = x * 0.9 + 5
        if temp > 20:
            transformed.append(temp // 2)
    
    # Semi-relevant normalization (only used in dead branch)
    max_val = max(base_scores)
    normalized = [round(x / max_val, 4) for x in base_scores]
    
    # Actual scoring logic
    weighted_sum = 0.0
    total_weight = 0.0
    for i, entry in enumerate(data):
        key = entry['key']
        raw_val = entry['value']
        weight = weight_map.get(key, 1.0)
        
        # Conditional boost for high performers
        if raw_val > 85:
            bonus = 10 * (weight ** 0.5)
        else:
            bonus = 0
        
        contribution = (raw_val + bonus) * weight
        weighted_sum += contribution
        total_weight += weight
    
    # Dead code path with misleading computation
    if False:
        fallback = sum(normalized) * 100
        weighted_sum = fallback  # Never executed
    
    avg_score = weighted_sum / total_weight if total_weight > 0 else 0
    
    # Secondary adjustment based on rank distribution
    counts = {}
    for v in base_scores:
        bucket = v // 10
        counts[bucket] = counts.get(bucket, 0) + 1
    
    mode_bucket = max(counts, key=counts.get)
    adjustment = 5 if mode_bucket >= 8 else -2
    
    return int(avg_score + adjustment)

# Main execution
rank_data = [
    {'key': 'alpha', 'value': 92},
    {'key': 'beta', 'value': 78},
    {'key': 'gamma', 'value': 88},
    {'key': 'delta', 'value': 95},
    {'key': 'epsilon', 'value': 82}
]

weights = {
    'alpha': 1.2,
    'beta': 0.9,
    'gamma': 1.1,
    'delta': 1.4,
    'epsilon': 1.0
}

intermediate_total = sum(item['value'] * 0.1 for item in rank_data)  # Distractor
scaling_factor = len(rank_data) / (len(weights) + 0.5)  # Unused scaling

final_score = compute_final_score(rank_data, weights)
print(f"Result: {final_score}")