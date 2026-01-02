from itertools import compress, cycle

def analyze_performance(metrics):
    # Irrelevant transformation - distractor
    normalized = [m / sum(metrics) for m in metrics]
    ranked = sorted(enumerate(normalized), key=lambda x: x[1], reverse=True)
    ranks = [0] * len(metrics)
    for i, (orig_idx, _) in enumerate(ranked):
        ranks[orig_idx] = i + 1
    return ranks

def calculate_adjustment_factor(ranks):
    # Complex but partially irrelevant calculation
    total_rank_score = sum((i + 1) * r for i, r in enumerate(ranks))
    adjustment = 1.0
    if total_rank_score > 20:
        adjustment = 0.95
    elif total_rank_score > 10:
        adjustment = 1.05
    else:
        adjustment = 1.0
    
    # Dead code path - misleading
    temp_debug = []
    for r in ranks:
        if r % 2 == 0:
            temp_debug.append(r ** 2)
    
    return adjustment

def calculate_final_score(data, weights):
    # Core logic begins here
    base_scores = [d * 2 for d in data]
    
    # Use of zip and enumerate together - relevant complexity
    indexed_weights = list(enumerate(zip(data, weights)))
    weighted_corrections = []
    
    for i, (d, w) in indexed_weights:
        if i % 2 == 0:
            weighted_corrections.append(d * w / (i + 1))
        else:
            weighted_corrections.append(0)  # Neutralize odd indices
    
    correction_sum = sum(weighted_corrections)
    
    # Real manipulation affecting final result
    cyclic_mod = cycle([1, -1])
    sign_sequence = [next(cyclic_mod) for _ in range(len(base_scores))]
    signed_bases = [sign * score for sign, score in zip(sign_sequence, base_scores)]
    
    raw_total = sum(signed_bases)
    
    # Final computation - depends on prior steps
    final_score = raw_total + correction_sum
    
    # Red herring: unused variable with complex derivation
    filtered_pairs = list(compress(indexed_weights, [r % 3 == 0 for r in data]))
    dummy_aggregate = sum(abs(d * w) for _, (d, w) in filtered_pairs) if filtered_pairs else 0
    
    return final_score

# Main execution flow
if __name__ == "__main__":
    # Input data
    rank_data = [4, 7, 2, 9, 5]
    bonus_weights = [0.8, 1.2, 0.5, 1.6, 0.9]
    
    # Irrelevant preprocessing - adds cognitive load
    performance_metrics = [x ** 1.5 for x in rank_data]
    performance_ranks = analyze_performance(performance_metrics)
    
    # Another distraction: unused adjustment
    adjustment_factor = calculate_adjustment_factor(performance_ranks)
    
    # Key statement
    final_score = calculate_final_score(rank_data, bonus_weights)
    
    print(f"Result: {final_score}")