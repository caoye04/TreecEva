def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final result but adds distraction)
    normalized = [(m - min(metrics)) / (max(metrics) - min(metrics) + 1e-8) for m in metrics]
    
    # Apply weights directly on original metrics
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    
    # Additional processing with red herring variables
    adjusted_metrics = [m * 1.1 if i % 2 == 0 else m for i, m in enumerate(metrics)]
    temp_score = sum(adjusted_metrics[i] * weights[i] for i in range(len(weights)))  # unused
    
    # Conditional bonus based on threshold logic
    bonus = 10 if all(m > 50 for m in metrics) else 0
    penalty = 5 if len([m for m in metrics if m < 30]) > 1 else 0
    
    # Bitwise interference: mask out lower bits of sum (has no real effect due to later override)
    masked_sum = int(weighted_sum) & 0xFFFFFF
    
    # Key decision point: override score if consistency condition is met
    consecutive_high = sum(1 for m in metrics if m >= 75)
    if consecutive_high >= 3:
        masked_sum = 95  # Override based on performance streak
    
    # Final computation
    final_score = masked_sum + bonus - penalty
    
    # Dead code path: never executed due to fixed conditions above
    if False and weighted_sum > 1000:
        final_score *= 1.05
        
    return final_score

# Main execution
metrics = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Irrelevant pre-processing
scaled_weights = [w * 100 for w in weights]
dummy_result = [m ** 0.5 for m in metrics if m > 80]

# Core computation
final_score = evaluate_performance(metrics, weights)

# Output result
print(f"Result: {final_score}")