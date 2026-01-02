from itertools import combinations

def evaluate_stability(measures):
    return sum(abs(a - b) for a, b in zip(measures, measures[1:]))

def calculate_harmonic_load(factors):
    # Irrelevant calculation - distractor
    if not factors:
        return 0
    reciprocal_sum = sum(1 / f for f in factors if f != 0)
    return len(factors) / reciprocal_sum if reciprocal_sum else 0

def analyze_distribution(pattern):
    # Another misleading computation on subsets
    total_variance = 0
    for r in range(2, len(pattern) + 1):
        for group in combinations(pattern, r):
            total_variance += (max(group) - min(group)) ** 2
    return total_variance

def calculate_optimal_yield(config):
    base_levels = config['levels']
    adjustment_factor = config['factor']
    thresholds = config['thresholds']
    
    # Real logic starts here
    adjusted = [level * adjustment_factor for level in base_levels]
    
    # Filtering based on dynamic threshold logic
    valid_indices = {i for i, v in enumerate(adjusted) if v > thresholds[i % len(thresholds)]}
    
    # Secondary filter using average condition
    avg_val = sum(adjusted) / len(adjusted)
    refined_set = {i for i in valid_indices if adjusted[i] >= avg_val}
    
    # Distractor: unused complex structure
    temp_snapshot = [
        (i, adjusted[i], 'high') if adjusted[i] > 1.5 * avg_val
        else (i, adjusted[i], 'normal')
        for i in range(len(adjusted))
    ]
    
    # More red herring: analyzing unrelated distribution patterns
    _ = analyze_distribution([adjusted[i] for i in sorted(valid_indices)])
    _ = calculate_harmonic_load([0.5, 1.5, 2.5])
    
    # Core computation for final result
    selected_values = [adjusted[i] for i in refined_set]
    if not selected_values:
        return 0
    
    # Final yield determined by stability of selected sequence
    sorted_values = sorted(selected_values)
    final_yield = sum(sorted_values) - evaluate_stability(sorted_values)
    
    return final_yield

# Initialization data
field_config = {
    'levels': [3.0, 6.0, 4.0, 8.0, 5.0],
    'factor': 1.2,
    'thresholds': [4.0, 3.5, 5.0]
}

# Execute main logic
final_yield = calculate_optimal_yield(field_config)
print(f"Result: {final_yield}")