def calculate_performance(results, importance_weights):
    total_score = 0.0
    max_possible = sum(importance_weights)
    
    # Irrelevant baseline metrics
    baseline = [75, 80, 85, 90, 95]
    adjustment_factor = 1.05
    temp_offset = sum(baseline) / len(baseline) * 0.02  # Unused distraction
    
    normalized = [min(100, r) for r in results]  # Cap at 100
    efficiency_ratio = len([r for r in normalized if r >= 90]) / len(normalized) if normalized else 0
    
    # Secondary scoring path (unused but plausible)
    alternative_score = 0
    for i, val in enumerate(normalized):
        if val > 85:
            alternative_score += val * 0.1
    
    # Main scoring logic
    weighted_sum = 0
    for i, (val, weight) in enumerate(zip(normalized, importance_weights)):
        contribution = val * weight
        total_score += contribution
        
        # Dummy tracking variable
        status_flag = "HIGH" if contribution > 700 else "LOW"
    
    final_normalized = total_score / max_possible
    
    # Complex conditional expression for tiered bonus
    bonus = 10.0 if final_normalized >= 90 else (5.0 if final_normalized >= 80 else (2.0 if final_normalized >= 70 else 0.0))
    
    # Final adjustment with red herring computation
    volatility_index = sum(abs(normalized[i] - normalized[i+1]) for i in range(len(normalized)-1)) / len(normalized) if len(normalized) > 1 else 0
    stability_bonus = 3.0 if volatility_index < 8 else 0  # Looks relevant but not used
    
    return final_normalized + bonus  # stability_bonus intentionally omitted

# Primary data
benchmark_results = [92, 88, 95, 76, 83]
weights = [0.2, 0.25, 0.3, 0.15, 0.1]

# Auxiliary irrelevant arrays
historical_data = [88, 85, 90, 78, 80]
dummy_flags = [True, False, True, True, False]

# Execution point of interest
calibration_shift = 0.95  # Unused parameter
temp_cache = []
for idx, (old, new) in enumerate(zip(historical_data, benchmark_results)):
    diff = new - old
    temp_cache.append(diff ** 2)

final_score = calculate_performance(benchmark_results, weights)
print(f"Result: {final_score}")