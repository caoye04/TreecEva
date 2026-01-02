def calculate_performance(data):
    # Preprocessing: Normalize and filter relevant entries
    normalized = [x / max(data) for x in data if x > 0]
    
    # Irrelevant transformation (distractor)
    inverted = [1 / (1 + x) for x in normalized]
    temp_sum = sum(inverted) * 0.1  # Not used later

    # Key metric computation with enumerate
    growth_factors = []
    for i, val in enumerate(normalized):
        if i > 0:
            growth_factors.append(val / normalized[i - 1])
    
    # Misleading statistical calculation (dead end)
    avg_growth = sum(growth_factors) / len(growth_factors) if growth_factors else 1.0
    volatility = sum((g - avg_growth) ** 2 for g in growth_factors) ** 0.5 if growth_factors else 0

    # Core logic: weighted score based on position and magnitude
    weights = [0.5 ** i for i in range(len(normalized))]
    weighted_total = sum(val * weight for val, weight in zip(normalized, weights))

    # Secondary adjustment using lambda-filtered high performers
    threshold = 0.7 * max(normalized)
    high_performers = list(filter(lambda x: x > threshold, normalized))
    bonus = len(high_performers) * 0.25

    # Final performance score
    final_score = weighted_total + bonus
    return final_score

# Simulated benchmark dataset
benchmark_data = [12, 45, 23, 67, 34, 89, 43, 23]

# Execute main logic
intermediate_calc = [x ** 0.5 for x in benchmark_data]  # Distractor: unused path
baseline_shift = sum(benchmark_data) / len(benchmark_data) - 5  # Unused tracking

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")