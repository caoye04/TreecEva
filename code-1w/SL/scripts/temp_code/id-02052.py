def compute_performance():
    raw_scores = [84, 92, 75, 88, 95]
    weights = [0.2, 0.3, 0.1, 0.25, 0.15]
    weighted = [raw_scores[i] * weights[i] for i in range(len(raw_scores))]
    average = sum(weighted)
    adjustments = [0.95, 1.05, 0.98, 1.02, 1.00]
    adjusted_values = [weighted[i] * adjustments[i] for i in range(len(weighted))]
    temp_buffer = [x for x in adjusted_values if x > 80]  # Irrelevant filtering
    final_score = max(adjusted_values[1:4])
    return final_score

result = compute_performance()
print(f"Result: {result}")