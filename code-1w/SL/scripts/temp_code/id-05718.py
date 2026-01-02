from itertools import combinations

# Simulate ranking-based scoring with weighted aggregation and noise filtering
def calculate_final_score(ranks, coeffs):
    base_score = 0
    adjustment = 0
    
    # Real contribution: weighted sum of top-3 ranked items
    sorted_indices = sorted(range(len(ranks)), key=lambda i: ranks[i])[:3]
    for i, idx in enumerate(sorted_indices):
        base_score += coeffs[idx] * (3 - i)  # Higher weight for higher rank

    # Distractor: analyze all pairs but don't use in final score
    pair_contributions = []
    for pair in combinations(range(len(ranks)), 2):
        diff = abs(ranks[pair[0]] - ranks[pair[1]])
        prod = coeffs[pair[0]] * coeffs[pair[1]]
        pair_contributions.append(diff * prod * 0.1)
    
    # Distractor: unused normalization path
    if len(pair_contributions) > 5:
        normalized_pairs = [min(p, 10) for p in pair_contributions]
        adjustment = sum(normalized_pairs) / len(normalized_pairs)
    else:
        adjustment = 0

    # Distractor: redundant variable tracking
    temp_state = {'version': '1.2', 'active': True}
    temp_state['last_updated'] = 'N/A'
    temp_state['score_debug'] = base_score + adjustment

    # Real logic: apply bonus if top item has highest coefficient
    top_index = sorted_indices[0]
    max_coeff_index = coeffs.index(max(coeffs))
    bonus = 15 if top_index == max_coeff_index else 0

    # Final computation
    final_score = int(base_score + bonus)  # No adjustment used
    return final_score

# Input data
rankings = [45, 23, 67, 12, 35, 89]
weights = [2.5, 1.8, 3.4, 0.9, 2.1, 4.0]

# Key statement
final_score = calculate_final_score(rankings, weights)
print(f"Result: {final_score}")