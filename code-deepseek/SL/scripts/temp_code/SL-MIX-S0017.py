def analyze_performance(data_points):
    # Distractor: Complex but irrelevant calculation
    temp_sum = sum([x * 2 for x in data_points if x > 5])
    offset = len(data_points) * 3.14
    adjusted = temp_sum - offset
    return adjusted

def calculate_metrics(values):
    # Main logic path
    processed = [v ** 2 if v % 2 == 0 else v * 3 for v in values]
    weighted_sum = sum([p * (i + 1) for i, p in enumerate(processed)])
    return weighted_sum

def process_results(input_data):
    # Multiple nested function calls with interference
    analysis_result = analyze_performance(input_data)  # Distractor
    
    # Critical path - actual calculation
    metrics_value = calculate_metrics(input_data)
    
    # More interference
    noise_factor = (len(input_data) * 2.5) - 7
    interference = metrics_value + noise_factor
    
    # Final result after removing interference
    actual_result = interference - noise_factor
    return actual_result

# Main execution
metrics_data = [2, 5, 3, 8, 4]

# Distractor variables and operations
preliminary_analysis = sum([x * x for x in metrics_data if x < 6])
secondary_check = preliminary_analysis * 0.75  # Dead code path
validation_score = len(metrics_data) ** 2 + 10

# Target calculation
final_score = process_results(metrics_data)

# Print result
print(f"Result: {final_score}")