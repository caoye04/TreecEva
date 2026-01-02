def evaluate_performance(data, threshold):
    # Preprocessing: filter relevant entries
    filtered = [x for x in data if x > threshold - 10]
    
    # Irrelevant transformation (distractor)
    squared_values = list(map(lambda x: x**2, filtered))
    temp_sum = sum(squared_values) // len(squared_values) if squared_values else 0
    
    # Character counting red herring (not used later)
    debug_info = "Metrics processed: " + str(len(filtered))
    char_count = len(debug_info)
    
    # Core logic: weighted moving average of top 3 values
    sorted_vals = sorted(filtered, reverse=True)
    top_three = sorted_vals[:3]
    
    # Conditional expression with fallback
    weight_factor = 1.5 if len(top_three) == 3 else (1.2 if len(top_three) == 2 else 1.0)
    
    # Compute base performance
    base_perf = sum(val * weight_factor for val in top_three)
    
    # Secondary adjustment using unused helper (dead path)
    def adjust_noise(x):  # Never called
        return x + (x % 7) * 0.1
    
    # Additional distraction: simulate historical drift (unused)
    historical_bias = 0
    for i in range(len(top_three)):
        historical_bias += top_three[i] * (0.1 ** i)
    
    # Final score computation
    stability_penalty = len(data) - len(filtered)  # penalty for filtered items
    final_score = int(base_perf - stability_penalty)
    
    return final_score

# Main execution context
metric_data = [12, 15, 8, 23, 19, 5, 14]
base_threshold = 10

# Unused variables (distraction)
max_value = max(metric_data)
min_value = min(metric_data)
spurious_calc = (max_value + min_value) * 0.5

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")