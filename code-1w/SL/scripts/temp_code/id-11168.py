def evaluate_performance(data, importance):
    base = sum(x * y for x, y in zip(data, importance))
    adjustment = 0
    
    # Irrelevant transformation chain (distractor)
    temp_data = [x ** 2 for x in data]
    normalized = [(x - min(temp_data)) / (max(temp_data) - min(temp_data) + 1e-8) for x in temp_data]
    derived_features = list(map(lambda z: z * 0.75, normalized))
    unused_aggregate = sum(derived_features) / len(derived_features) if derived_features else 0
    
    # Real logic with moderate nesting and conditions
    penalty = 0
    for i, val in enumerate(data):
        if val < 50:
            for j in range(2):
                penalty += importance[i] * (50 - val) * 0.1
    
    # Secondary correction based on aggregate trend
    avg_val = sum(data) / len(data)
    if avg_val > 60:
        adjustment = 10
    elif avg_val > 40:
        adjustment = 5
    else:
        adjustment = 0
    
    # Final computation
    final_score = base + adjustment - penalty
    
    # Dead code path (misleading)
    if False:
        final_score = max(final_score, 100)
        final_score *= 1.1
    
    return final_score

# Main execution
metrics = [85, 72, 43, 68, 90]
weights = [0.3, 0.2, 0.25, 0.15, 0.1]

# Unused intermediate calculations (distractors)
centered = [x - sum(metrics)/len(metrics) for x in metrics]
doubled_weights = [w * 2 for w in weights if w > 0.1]
shadow_copy = metrics[::-1]

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")