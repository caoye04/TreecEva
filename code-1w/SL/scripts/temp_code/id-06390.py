def calculate_performance(data):
    base_offset = 17
    temporal_weights = [0.8, 1.1, 0.9, 1.2, 1.0]
    adjusted_values = []
    
    for i, entry in enumerate(data):
        raw_value = entry * (1 + i * 0.05)
        if i % 2 == 0:
            raw_value += 3
        else:
            raw_value -= 2
        adjusted_values.append(raw_value)
    
    # Irrelevant transformation (distractor)
    transformed_data = [x ** 0.5 for x in data if x > 4]
    dummy_aggregate = sum(transformed_data) / len(transformed_data) if transformed_data else 0
    
    # Core calculation with zip and enumerate
    weighted_sum = 0
    for idx, (val, weight) in enumerate(zip(adjusted_values, temporal_weights)):
        contribution = val * weight
        if idx > 0:
            contribution -= adjusted_values[idx - 1] * 0.1  # lagged penalty
        weighted_sum += contribution
    
    avg_base = sum(data) / len(data)
    volatility = max(data) - min(data)
    
    # Secondary adjustment (partially relevant)
    stability_bonus = 0
    if volatility < 3:
        stability_bonus = 5
    elif volatility < 6:
        stability_bonus = 2

    # Final score computation
    final_score = (weighted_sum / len(temporal_weights)) + stability_bonus
    final_score -= base_offset  # normalize by offset
    return int(final_score)

# Input data
benchmark_data = [4, 5, 4, 6, 5]

# Execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")