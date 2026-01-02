def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final result)
    normalized = [(m - min(metrics)) / (max(metrics) - min(metrics)) if max(metrics) != min(metrics) else 0 for m in metrics]
    
    # Calculate weighted sum - this is the key computation
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    
    # Apply non-linear transformation (distraction)
    transformed = [x ** 0.5 for x in normalized if x > 0]
    
    # Dummy threshold logic with dead code path
    threshold = 0.7 * max(metrics)
    above_threshold = [m for m in metrics if m > threshold]
    bonus = len(above_threshold) * 0.5 if len(above_threshold) > 2 else 0

    # Bitwise manipulation on index (semi-relevant but not used directly)
    magic_factor = 0
    for i in range(len(metrics)):
        if i % 2 == 0:
            magic_factor ^= int(metrics[i]) & 7  # XOR and bitwise AND

    # Red herring: unused intermediate calculation
    avg_metric = sum(metrics) / len(metrics)
    variance_proxy = sum((m - avg_metric) ** 2 for m in metrics) / len(metrics)

    # Core logic masked by distractions: apply weight mask based on parity
    weight_mask = [1 + ((i & 1) ^ 1) * 0.1 for i in range(len(weights))]  # boost even indices slightly
    adjusted_weights = [w * wm for w, wm in zip(weights, weight_mask)]
    final_adjusted_sum = sum(m * aw for m, aw in zip(metrics, adjusted_weights))

    # Final score depends only on original weighted_sum and magic_factor side effect
    final_score = int(weighted_sum) + (magic_factor % 4)  # deterministic integer result

    return final_score

# Input data
metrics = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Misleading pre-processing
shadow_metrics = [m * 1.05 for m in metrics]
scaling_factor = sum(weights) / len(weights)

# Key execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")