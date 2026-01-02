from itertools import combinations

def analyze_patterns(data):
    patterns = []
    total = 0
    for i in range(2, len(data) + 1):
        for combo in combinations(data, i):
            if sum(combo) % 3 == 0:
                patterns.append(combo)
                total += len(combo)
    return patterns, total

def compute_redundant_metric(seq):
    # Irrelevant helper function - distractor
    count = 0
    for i in seq:
        for j in seq:
            if (i + j) & 1:
                count += 1
    return count

def filter_significant(values, threshold=5):
    # Semi-relevant but not used in final score
    return {k: v for k, v in enumerate(values) if v > threshold}

def calculate_final_score(entries, importance_weights):
    base_scores = [x * 0.85 for x in entries]
    adjusted = [round(b * w, 3) for b, w in zip(base_scores, importance_weights)]
    
    temp_sum = sum(adjusted)
    correction_factor = 1.0 if temp_sum > 30 else 1.2
    applied = [val * correction_factor for val in adjusted]
    
    # Key logic step: apply penalty if any score below 4 after adjustment
    penalty_applied = False
    for val in applied:
        if val < 4.0:
            penalty_applied = True
            break
    
    final_modifier = 0.9 if penalty_applied else 1.1
    final_score = sum(applied) * final_modifier
    
    # Distractor variables
    debug_info = {'size': len(applied), 'penalty': penalty_applied, 'factor': final_modifier}
    intermediate_trace = [debug_info['size'] * x for x in applied]
    
    return round(final_score, 4)

# Main execution block
raw_data = [7, 9, 12, 5, 8]
weights_config = [1.1, 0.9, 1.2, 0.8, 1.0]

# Irrelevant preprocessing - distractor
expanded = [x for x in raw_data for _ in range(2)]
sorted_expanded = sorted(expanded, reverse=True)
filtered_expanded = [x for x in sorted_expanded if x % 2 == 1]

# Call irrelevant analysis
patterns_list, pattern_total = analyze_patterns(raw_data)
redundant_metric = compute_redundant_metric(raw_data)

# Semi-relevant filtering
significant_only = filter_significant(raw_data)

# Core calculation - this is where final_score is determined
results = [x + 2 for x in raw_data]
final_score = calculate_final_score(results, weights_config)

print(f"Result: {final_score}")