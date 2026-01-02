def evaluate_performance(ranking, threshold, weight_map):
    adjusted_ranks = []
    for i, rank in enumerate(ranking):
        if rank <= threshold:
            adjusted = rank * weight_map.get(i % 3, 1.0)
            adjusted_ranks.append(round(adjusted))
    
    temp_buffer = [x for x in adjusted_ranks if x > 0]  # Irrelevant filtering (minimal interference)
    filtered_ranks = []
    seen = set()
    for val in temp_buffer:
        if val not in seen:
            filtered_ranks.append(val)
            seen.add(val)
    
    metadata_log = {'entries': len(filtered_ranks), 'source': 'performance'}  # Distractor variable
    final_score = sum(filtered_ranks)
    return final_score

# Input data
rankings = [4, 2, 1, 3, 2, 5]
config_weight = {0: 1.5, 1: 2.0, 2: 0.5}

cutoff = 3
result = evaluate_performance(rankings, cutoff, config_weight)
final_score = result
print(f"Result: {final_score}")