def calculate_final_score(records, importance):
    base_scores = []
    temp_debug_log = []
    
    for idx, (record, weight) in enumerate(zip(records, importance)):
        raw_value = sum([v for k, v in record.items() if k in ['metric_a', 'metric_b']])
        adjustment_factor = 1.0
        
        if idx % 2 == 0:
            adjustment_factor += 0.1
        else:
            adjustment_factor -= 0.05

        # Irrelevant debug accumulation
        temp_debug_log.append(f"Step {idx}: raw={raw_value}, adj={adjustment_factor}")

        adjusted_score = raw_value * weight * adjustment_factor
        base_scores.append(adjusted_score)

    # Distractor: unused computation
    outlier_count = sum(1 for s in base_scores if s < 5)
    normalized = [max(s, 2) for s in base_scores]

    # Real logic continues
    cumulative = 0
    decay = 0.9
    for i, val in enumerate(base_scores):
        cumulative += val * (decay ** i)

    # Secondary adjustment based on control flag
    control_flags = [len(r) > 2 for r in records]
    if all(control_flags):
        cumulative *= 1.05

    # Final aggregation
    penalty = 0
    for r in records:
        if 'special' in r and r['special']:
            penalty -= 3
    
    final_score = int(cumulative + penalty)
    
    # Print required result
    print(f"Result: {final_score}")
    return final_score

# Input data
data = [
    {'metric_a': 4, 'metric_b': 6, 'extra': 100},
    {'metric_a': 5, 'metric_b': 3, 'flag': True},
    {'metric_a': 7, 'metric_b': 2, 'special': True}
]

weights = [1.2, 0.8, 1.5]

# Execution entry point
final_score = calculate_final_score(data, weights)