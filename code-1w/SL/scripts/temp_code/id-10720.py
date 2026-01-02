def calculate_performance(results, limit):
    # Irrelevant transformation (distractor)
    normalized = [x * 0.95 for x in results if x > 10]
    
    # Semi-relevant filtering
    filtered = [x for x in results if x >= limit]
    
    # Key computation: harmonic mean of filtered values
    if not filtered:
        return 0
    
    reciprocal_sum = sum(1 / x for x in filtered)
    harmonic_mean = len(filtered) / reciprocal_sum
    
    # Secondary metric (unused but plausible)
    peak_value = max(results) if results else 0
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0
    
    # Conditional adjustment based on diversity of results
    unique_count = len(set(results))
    diversity_bonus = 1.0 + (0.05 if unique_count > 3 else 0)
    
    # Final score calculation (only harmonic_mean and diversity_bonus matter)
    base_score = harmonic_mean * diversity_bonus
    final_score = int(base_score + 0.5)  # Round to nearest integer
    
    # Dead code path (misleading)
    if peak_value < 50:
        final_score *= 2  # This won't execute in this case
    
    return final_score

# Main execution
benchmark_results = [12, 15, 18, 24, 30, 14]
threshold = 13

# Preprocessing step (partially irrelevant)
data_shift = [x - 1 for x in benchmark_results]
shifted_avg = sum(data_shift) / len(data_shift)

# Another distraction: set operation with no impact
outliers = set(benchmark_results) - {min(benchmark_results), max(benchmark_results)}
adjusted_outliers = {x * 2 for x in outliers if x < 20}

# Key statement
final_score = calculate_performance(benchmark_results, threshold)

print(f"Result: {final_score}")