from itertools import combinations

def analyze_pattern(sequence):
    # Irrelevant helper: computes pairwise sums (not used in final logic)
    pairs = list(combinations(sequence, 2))
    pair_sums = [a + b for a, b in pairs]
    avg_sum = sum(pair_sums) / len(pair_sums) if pair_sums else 0
    return avg_sum

def filter_outliers(data, limit=3):
    # Semi-relevant: filters extreme values but only applied to unused path
    if len(data) <= 1:
        return data
    mean_val = sum(data) / len(data)
    return [x for x in data if abs(x - mean_val) < limit]

def evaluate_performance(metrics, thresholds):
    base_weight = 0.8
    bonus_factor = 1.2
    penalty = 0.5
    
    # Real computation begins
    valid_count = 0
    for i, val in enumerate(metrics):
        if val >= thresholds[i % len(thresholds)]:
            valid_count += 1
    
    # Distractor: complex slicing with no impact
    temp_slice = metrics[::2] + metrics[1::2]
    reversed_combo = temp_slice[::-1]
    _ = sum(reversed_combo) / len(reversed_combo) if reversed_combo else 0  # unused
    
    # Actual score calculation
    raw_score = valid_count * base_weight
    
    # Bonus logic based on pattern continuity
    consecutive = 0
    max_consecutive = 0
    for val in metrics:
        if val > thresholds[0]:
            consecutive += 1
            max_consecutive = max(max_consecutive, consecutive)
        else:
            consecutive = 0
    
    if max_consecutive >= 3:
        raw_score *= bonus_factor
    else:
        raw_score -= penalty
    
    # Dead code branch (never reached due to structure)
    debug_mode = False
    if debug_mode:
        print("Debug info: ", filter_outliers(metrics))
    
    # Final transformation using string manipulation (semi-distracting)
    score_str = f"{raw_score:.4f}"
    decimal_part = score_str.split('.')[1]
    digit_sum = sum(int(d) for d in decimal_part[:3])
    adjustment = digit_sum * 0.01
    
    final_score = raw_score + adjustment  # This will be printed
    
    return final_score

# Main execution
metrics = [78, 92, 88, 65, 96, 77, 83]
thresholds = [80, 70, 85]

# Unused variables to increase cognitive load
baseline = [75, 80, 82, 68, 90]
dummy_labels = ['A', 'B', 'C', 'D', 'E']
shadow_copy = metrics.copy()
analysis_hint = analyze_pattern([len(baseline), len(dummy_labels)])

final_score = evaluate_performance(metrics, thresholds)
print(f"Result: {final_score}")