def calculate_final_score(records, importance_weights):
    base_scores = [r['value'] * r['multiplier'] for r in records]
    adjusted_scores = []
    temp_offset = 0
    
    for i, score in enumerate(base_scores):
        if i % 2 == 0:
            adjusted_scores.append(score + len(importance_weights))
        else:
            adjusted_scores.append(score - temp_offset)
            temp_offset += 1  # Only used in odd indices, mildly misleading
    
    # Irrelevant transformation (dead-end computation)
    squared_sum_proxy = sum([x**2 for x in importance_weights])  # Not used later
    normalization_factor = max(adjusted_scores) if adjusted_scores else 1
    
    normalized = [s / normalization_factor for s in adjusted_scores]
    
    # Simulate weighting by index position (only even weights matter)
    weighted_sum = 0
    for idx, w in enumerate(importance_weights):
        if idx % 2 == 0:
            weighted_sum += normalized[idx % len(normalized)] * w
    
    # Auxiliary tracking variables (distractors)
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0
    deviation_total = sum(abs(n - avg_normalized) for n in normalized)  # Unused
    
    final_raw = sum(weighted_sum, 0.0)
    return int(round(final_raw * 10))

# Main execution
config_data = {'threshold': 5, 'padding': 3, 'extra_flag': False}
data = [
    {'value': 4, 'multiplier': 3},
    {'value': 7, 'multiplier': 2},
    {'value': 5, 'multiplier': 4},
    {'value': 2, 'multiplier': 5}
]
weights = [1, 3, 2, 4]

intermediate_total = sum(item['value'] for item in data)  # Distractor
flag_check = config_data['extra_flag'] and intermediate_total > 10  # Dead logic

final_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")