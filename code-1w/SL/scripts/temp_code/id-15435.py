from itertools import combinations
from functools import reduce

# Simulate crop yield optimization under environmental constraints
def calculate_optimal_harvest():
    # Base growth factors for different crop types
    crop_bases = [0.8, 1.2, 0.9, 1.5, 1.1]
    
    # Environmental stress modifiers (temperature, moisture, pests)
    stress_factors = [0.7, 1.1, 0.9]
    
    # Experimental hybrid indices (irrelevant to final result but looks important)
    hybrid_pool = set([i ^ 3 for i in range(5)])
    unused_mask = sum(hybrid_pool) % 4  # Distractor computation
    
    # Generate all possible planting configurations (triplets)
    configs = list(combinations(range(len(crop_bases)), 3))
    
    # Historical data average (red herring)
    historical_avg = sum(c * 0.6 for c in crop_bases) / len(crop_bases)
    adjusted_reference = historical_avg * stress_factors[0]  # Not used later
    
    # Lambda to compute resilience score for a configuration
    resilience = lambda cfg: reduce(lambda x, y: x * y, [crop_bases[i] for i in cfg])
    
    # Compute yield potential across all configs under stress
    max_yield = 0
    best_config = None
    
    temp_results = []  # Tracking intermediate values (some irrelevant)
    for config in configs:
        base_yield = sum(crop_bases[i] for i in config)
        stress_yield = base_yield * stress_factors[1]  # Only middle factor matters
        
        # Bonus for balanced nutrient uptake (difference < 0.6)
        nutrient_diff = max(crop_bases[i] for i in config) - min(crop_bases[i] for i in config)
        if nutrient_diff < 0.6:
            stress_yield *= 1.15
        
        resilient_score = resilience(config)
        if resilient_score > 1.0:  # Additional threshold
            temp_results.append(stress_yield)
            if stress_yield > max_yield:
                max_yield = stress_yield
                best_config = config
    
    # Final adjustment based on soil pH preference (hardcoded offset)
    pH_factor = 0.95
    final_yield = round(max_yield * pH_factor, 4)
    
    # Unrelated diagnostic trace (dead code path)
    if len(temp_results) > 10:
        avg_temp = sum(temp_results) / len(temp_results)
        deviation = abs(final_yield - avg_temp)
    
    return final_yield

# Execute and print result
def main():
    final_yield = calculate_optimal_harvest()
    print(f"Target result: {final_yield}")

main()