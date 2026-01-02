def evaluate_performance(data, importance):
    base = sum(x * y for x, y in zip(data, importance))
    adjustment = 0
    
    # Distraction: irrelevant computation on transformed data
    transformed = [x ** 0.5 for x in data if x > 10]
    temp_sum = sum(transformed) / len(transformed) if transformed else 0
    noise = temp_sum * 0.1

    # Real logic: apply conditional bonus
    total_metrics = len(data)
    high_performers = sum(1 for x in data if x >= 15)
    
    if high_performers > total_metrics * 0.5:
        adjustment += 8.5
    elif high_performers > total_metrics * 0.3:
        adjustment += 4.2
    else:
        adjustment -= 2.1

    # More distraction: unused branch with complex logic
    if all(x < 20 for x in data) and any(x > 18 for x in data):
        fallback_score = max(data) * 0.75
        secondary_adjust = fallback_score // 3

    # Another red herring: complicated but unused formula
    derived_weight = [(w + 0.1) ** 2 for w in importance]
    phantom_impact = sum(d * w for d, w in zip(data, derived_weight)) * 0.01

    # Actual contribution: penalty for low consistency
    deviations = [abs(x - sum(data)/len(data)) for x in data]
    avg_deviation = sum(deviations) / len(deviations)
    if avg_deviation > 5:
        adjustment -= 3.0

    final_score = base + adjustment
    return final_score

# Input data
metrics = [12, 16, 14, 18, 9]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Output result
print(f"Result: {final_score}")