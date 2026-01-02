def evaluate_performance(metrics, weights):
    # Normalize metrics using lambda for dynamic scaling
    normalized = list(map(lambda x: x / max(metrics) if max(metrics) != 0 else 0, metrics))

    # Irrelevant computation: track hypothetical growth rate (not used)
    projected_growth = [m * 1.05 for m in metrics]
    avg_growth = sum(projected_growth) / len(projected_growth)

    # Distractor: calculate entropy-like measure (unused)
    import math
    entropy = sum(-x * math.log(x + 1e-9) for x in normalized)

    # Weighted score calculation - only this matters
    weighted_sum = sum(n * w for n, w in zip(normalized, weights))
    bonus = 10 if all(m > 0.1 for m in normalized) else 0  # small conditional bonus

    # Additional distraction: simulate ranking tiers
    tiers = ['Low', 'Medium', 'High']
    tier_index = min(int(sum(normalized) / 3), 2)
    assigned_tier = tiers[tier_index]

    # Final score depends only on weighted_sum and bonus
    final_score = int(weighted_sum * 100) + bonus
    return final_score

# Main execution
metrics = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Dead code path: preprocessing that isn't used
processed_metrics = [m * 0.95 for m in metrics if m > 80]
buffer = ''.join([chr(65 + i % 26) for i in range(20)])  # irrelevant string op

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")