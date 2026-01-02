def analyze_performance(scores, threshold=60):
    # Irrelevant transformation: convert to percentages (already in %)
    adjusted = [round(s * 1.0) for s in scores]
    
    # Distractor: unused filtering
    high_performers = [s for s in adjusted if s > 85]
    outlier_count = len([s for s in adjusted if s < 40 or s > 100])

    # Relevant logic: pass/fail tracking
    passed = [s for s in adjusted if s >= threshold]
    failed = [s for s in adjusted if s < threshold]
    
    # Compute stability metric (semi-relevant, not used directly)
    variance_proxy = sum((s - 70) ** 2 for s in adjusted) / len(adjusted) if adjusted else 0
    
    # Set operations: overlap between top quarter and passed group
    sorted_scores = sorted(set(adjusted))
    top_quarter_threshold = sorted_scores[-len(sorted_scores)//4] if sorted_scores else 0
    top_quarter_set = set(s for s in adjusted if s >= top_quarter_threshold)
    passed_set = set(passed)
    
    # Key intersection: students who passed AND are in top quarter
    strong_and_stable = top_quarter_set & passed_set
    
    # Additional distractor: combinatorics on failed cases (unused)
    import math
    possible_failure_pairs = math.comb(len(failed), 2) if len(failed) >= 2 else 0
    
    # Simulate improvement potential (not used in final score)
    improvement_gaps = [(threshold - f) for f in failed if f < threshold]
    total_gap = sum(improvement_gaps)
    
    # Final scoring logic: base + bonus for strong/stable overlap
    base_score = len(passed) * 10
    bonus = len(strong_and_stable) * 5
    penalty = outlier_count * 3
    final_component = base_score + bonus - penalty
    
    return final_component


def calculate_final_score(raw_data, config=None):
    if config is None:
        config = {'weight_a': 0.6, 'weight_b': 0.4, 'bonus_factor': 1.2}
    
    # Extract and preprocess data
    raw_values = [v['score'] for v in raw_data if v.get('active', True)]
    normalized = [min(max(v, 0), 100) for v in raw_values]  # clamp to 0-100
    
    # Dead code path: debug mode not triggered
    debug_mode = False
    if debug_mode:
        print(f"Raw: {raw_values}, Norm: {normalized}")
    
    # Secondary analysis with side-effect-free function
    auxiliary_result = analyze_performance(normalized, threshold=50)
    
    # Sorting distractor: sort but then use length only
    sorted_norm = sorted(normalized)
    median_val = sorted_norm[len(sorted_norm)//2] if sorted_norm else 0
    
    # Core calculation
    count_above_median = len([x for x in normalized if x >= median_val])
    efficiency_ratio = count_above_median / len(normalized) if normalized else 0
    
    # Use auxiliary result only through one component
    base = auxiliary_result * config['weight_a']
    dynamic_bonus = int(efficiency_ratio * 100) * config['weight_b']
    final_score = int(base + dynamic_bonus)
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
data_input = [
    {'score': 45, 'active': True},
    {'score': 72, 'active': True},
    {'score': 88, 'active': True},
    {'score': 33, 'active': True},
    {'score': 91, 'active': True},
    {'score': 67, 'active': True},
    {'score': 54, 'active': True},
    {'score': 76, 'active': True}
]

result = calculate_final_score(data_input)