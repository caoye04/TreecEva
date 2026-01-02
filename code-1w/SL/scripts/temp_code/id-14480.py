def calculate_performance(results):
    # Irrelevant transformation: normalizing unrelated metric
    normalized_weights = list(map(lambda x: x / sum(results), results))
    
    # Semi-relevant preprocessing: filter significant benchmarks
    significant = [x for x in results if x > 50]
    
    # Distractor: unused computation path
    outliers = list(filter(lambda x: x < 30 or x > 95, results))
    adjusted_outliers = [val * 0.9 for val in outliers if val > 90]  # Not used later
    
    # Core logic: counting performance tiers
    tiers = {
        'excellent': len([v for v in significant if v >= 85]),
        'good': len([v for v in significant if 70 <= v < 85]),
        'average': len([v for v in significant if 50 <= v < 70])
    }
    
    # Secondary distraction: dead code computing unused ratio
    if tiers['good'] > 0:
        efficiency_ratio = tiers['excellent'] / tiers['good']
    else:
        efficiency_ratio = 0  # Computed but not used
    
    # Conditional expression combining tier counts with weight bias
    base_score = tiers['excellent'] * 10 + tiers['good'] * 5 + tiers['average'] * 2
    
    # Final adjustment using conditional logic and lambda-based penalty
    apply_penalty = lambda score, count: score * 0.95 if count < 3 else score
    final_adjustment = apply_penalty(base_score, len(significant))
    
    # Key statement
    final_score = int(final_adjustment + (tiers['excellent'] ** 2))
    return final_score

# Simulated benchmark data from system tests
benchmark_results = [65, 72, 88, 45, 90, 58, 83, 94, 77]

# Execution point of interest
final_score = calculate_performance(benchmark_results)
print(f"Target result: {final_score}")