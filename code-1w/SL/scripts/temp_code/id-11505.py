def calculate_performance(results, importance_weights):
    normalized = []
    total_weight = sum(importance_weights)
    weighted_sum = 0
    
    # Normalize scores and apply weights
    for i, score in enumerate(results):
        max_possible = 100
        normalized_score = min(score / max_possible, 1.0)
        weighted_sum += normalized_score * importance_weights[i]
        normalized.append(normalized_score)
    
    final_normalized_avg = sum(normalized) / len(normalized) if normalized else 0
    
    # Dummy tracking variables (not used in final result)
    outlier_count = 0
    for val in results:
        if val < 30 or val > 95:
            outlier_count += 1
    
    # Simulate historical comparison (irrelevant to final_score)
    historical_benchmarks = [78, 82, 79, 85, 80]
    improvement_trend = [curr - prev for prev, curr in zip(historical_benchmarks, historical_benchmarks[1:])]
    avg_improvement = sum(improvement_trend) / len(improvement_trend) if improvement_trend else 0
    
    # Complex filtering using lambda and set operations (semi-relevant)
    passing_indices = set(filter(lambda x: results[x] >= 60, range(len(results))))
    weight_set = set(importance_weights)
    intersection_clue = len(passing_indices & weight_set)  # Misleading use
    
    # Conditional adjustment based on performance profile
    high_performers = [idx for idx, s in enumerate(results) if s > 85]
    bonus_factor = 0.1 if len(high_performers) >= 2 else 0.05
    
    # Final score calculation
    efficiency_ratio = len(high_performers) / len(results) if results else 0
    final_score = weighted_sum + (bonus_factor * efficiency_ratio)
    
    # Dead code path (never executed under current logic)
    if False:
        fallback = sum(results) / len(results)
        final_score = max(final_score, fallback)
    
    return final_score

# Main execution
benchmark_data = [88, 92, 75, 83, 94]
weights = [0.2, 0.3, 0.1, 0.15, 0.25]

# Extra irrelevant computations
shadow_copy = benchmark_data.copy()
decile_map = {i: val // 10 for i, val in enumerate(shadow_copy)}
sorted_pairs = sorted(zip(benchmark_data, weights), key=lambda x: x[1], reverse=True)

# Key statement
final_score = calculate_performance(benchmark_data, weights)
print(f"Target result: {final_score}")