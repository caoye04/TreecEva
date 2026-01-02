def evaluate_performance(metrics, threshold):
    # Irrelevant transformation (distractor)
    normalized = [round(x * 0.98 + 2, 2) for x in metrics]
    
    # Semi-relevant pre-processing
    filtered = list(filter(lambda x: x > threshold * 0.75, metrics))
    
    # Key logic chain begins
    count_above = sum(1 for val in filtered if val > threshold)
    total_contribution = sum(filtered)
    adjustment_factor = len(filtered) % 7 if len(filtered) > 0 else 1
    
    # Red herring: unused complex calculation
    peak_momentum = max(metrics) ** 0.5 if max(metrics) > 0 else 0
    temp_analysis = ''.join([str(int(x // 1))[-1] for x in metrics if x >= 10])
    checksum = sum(int(c) * (i + 1) for i, c in enumerate(temp_analysis)) % 100
    
    # Actual scoring logic
    base_score = count_above * 100
    bonus = int(total_contribution // 10) if adjustment_factor > 3 else int(total_contribution // 20)
    penalty = (5 - adjustment_factor) * 10 if adjustment_factor < 5 else 0
    
    # Final computation
    final_score = base_score + bonus - penalty
    
    # Misleading secondary path (dead code)
    if peak_momentum > 100:
        alternative = checksum * 2
        final_score = alternative  # Never reached
    
    return final_score

# Simulated input data
metric_data = [85, 92, 78, 63, 96, 88]
base_threshold = 80

# Execution point of interest
final_score = evaluate_performance(metric_data, base_threshold)

# Print result
print(f"Result: {final_score}")