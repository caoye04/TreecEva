def calculate_final_score(data, weights):
    base_scores = [d['rank'] * 10 for d in data]
    adjusted_scores = []
    
    multiplier = 1.5
    temp_offset = sum([base // 2 for base in base_scores[:3]])  # Irrelevant accumulation
    offset_tracker = {'value': temp_offset}  # Distractor variable

    for i, score in enumerate(base_scores):
        if i % 2 == 0:
            adjusted_scores.append(score * multiplier)
        else:
            adjusted_scores.append(score + weights.get(i, 1))
    
    # Dead code path (never executed due to prior logic)
    if len(data) > 100:
        fallback = sum(adjusted_scores) / 1000
        return int(fallback)

    filtered_scores = [s for s in adjusted_scores if s > 50]  # Only keep significant scores
    
    # Misleading statistical computation
    avg_score = sum(filtered_scores) / len(filtered_scores) if filtered_scores else 0
    std_deviation_proxy = sum([(s - avg_score) ** 2 for s in filtered_scores]) / len(filtered_scores) if filtered_scores else 0
    
    # Core logic: weighted combination based on index
    final_sum = 0
    for idx, val in enumerate(filtered_scores):
        weight = weights.get(idx, 1.0)
        final_sum += val * weight
    
    scaling_factor = 0.85
    final_score = int(final_sum * scaling_factor)
    
    return final_score

# Main execution context
user_records = [
    {'id': 'A', 'rank': 7},
    {'id': 'B', 'rank': 5},
    {'id': 'C', 'rank': 9},
    {'id': 'D', 'rank': 3},
    {'id': 'E', 'rank': 8}
]

bonus_weights = {0: 1.2, 1: 1.1, 2: 1.3, 3: 0.9}  # Weight mapping by index

# Extraneous preprocessing
sorted_records = sorted(user_records, key=lambda x: x['rank'], reverse=True)
duplicate_check_set = set(r['id'] for r in user_records)  # Not used later

intermediate_total = sum(record['rank'] for record in user_records) * 2  # Unused computation

rank_data = sorted_records  # Reassigned for clarity in function call

final_score = calculate_final_score(rank_data, bonus_weights)
print(f"Result: {final_score}")