from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            count += 1
    return count

def evaluate_performance(metrics, weights):
    weighted_sum = 0
    normalization = len(weights)
    
    # Relevant computation: weighted score
    for i in range(len(metrics)):
        weighted_sum += metrics[i] * weights[i]
    
    # Distractor: complex but unused logic with slicing and combinations
    temp_segments = [sequence[1:-1] for sequence in ['abc', 'def', 'ghi']]
    combo_count = 0
    for seg in temp_segments:
        for combo in combinations(seg, 2):
            combo_count += 1
    
    # Irrelevant character counting
    debug_chars = 0
    for s in temp_segments:
        debug_chars += len(s)
    
    # Dead code path (never executed due to fixed condition)
    aux_value = 0
    if False:
        aux_value = sum([len(s) for s in temp_segments])
    
    # Actual result depends only on weighted_sum and normalization
    raw_score = weighted_sum / normalization
    
    # Additional red herring: unused analysis
    pattern_metric = analyze_pattern([1, 2, 2, 3, 3, 3, 4])
    
    final_score = int(raw_score) + 10  # Final transformation
    return final_score

# Main execution
metrics = [85, 90, 78, 92]
weights = [0.2, 0.3, 0.15, 0.35]

intermediate_result = sum([m**2 for m in metrics]) / len(metrics)  # Unused computation

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")