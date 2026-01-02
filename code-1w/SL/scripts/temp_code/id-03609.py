def evaluate_performance(metrics, weights):
    # Initialize relevant and irrelevant variables
    temp_buffer = [0] * len(metrics)
    scaling_factor = 1.2
    adjustment = 0.85
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]

    # Simulate performance metric processing with distractions
    intermediate_results = []
    outlier_count = 0
    for i, metric in enumerate(metrics):
        if metric < 50:
            outlier_count += 1
            adjusted_metric = metric * adjustment
        else:
            adjusted_metric = metric * scaling_factor
        
        # Irrelevant transformation (distraction)
        decayed_value = adjusted_metric * 0.97 ** i
        temp_buffer[i] = decayed_value  # Used nowhere critical

        weighted_contribution = adjusted_metric * normalized_weights[i]
        intermediate_results.append(weighted_contribution)

    # Real computation path
    raw_score = sum(intermediate_results)
    
    # Distractor: unused control flow
    if outlier_count > 10:
        raw_score *= 0.9
    elif outlier_count == 0:
        bonus = 5.0  # Dead code - bonus never used
        raw_score += 2.5

    # Core logic: apply non-linear boost
    performance_boost = 1 + (raw_score / 1000)
    enhanced_score = raw_score * performance_boost

    # Final threshold clamp (not triggered here)
    clamped_score = min(enhanced_score, 950) if enhanced_score > 900 else enhanced_score

    # Actual answer variable
    final_score = int(clamped_score // 1)  # Floor to integer

    # Unrelated data structure manipulation (set operation - distractor)
    unique_metrics = set(metrics)
    redundant_check = len(unique_metrics) - len(metrics)  # Always <= 0
    if redundant_check < 0:
        pass  # Dead branch

    return final_score

# Main execution context
base_metrics = {78, 85, 92, 64, 73, 88, 91}  # Set input for diversity
backup_copy = list(base_metrics)
base_weights = [0.1, 0.15, 0.2, 0.05, 0.1, 0.25, 0.15]

# Misleading pre-processing
sorted_backup = sorted(backup_copy, reverse=True)
effective_metrics = sorted_backup[:len(base_weights)]

# Key statement
final_score = evaluate_performance(effective_metrics, base_weights)
print(f"Target result: {final_score}")