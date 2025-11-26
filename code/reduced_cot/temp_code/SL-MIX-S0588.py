def process_metrics(raw_data):
    processed = []
    for item in raw_data:
        temp_val = item * 2 - 5
        if temp_val > 10:
            processed.append(temp_val + 3)
        else:
            processed.append(temp_val - 2)
    return processed

def calculate_weighted_scores(scores, weights):
    weighted_sum = 0
    total_weight = sum(weights)
    for i in range(len(scores)):
        weighted_sum += scores[i] * weights[i]
    return weighted_sum / total_weight if total_weight != 0 else 0

def analyze_performance(data_points, min_threshold):
    # Distractor variables
    unused_temp = [x % 7 for x in data_points]
    misleading_calc = sum(data_points) * 2 - 15
    
    # Dead code path
    if min_threshold > 100:
        redundant_val = misleading_calc + 25
        # This path is never taken
        return redundant_val * 0.5
    
    # Main logic
    processed_data = process_metrics(data_points)
    weights = [0.3, 0.4, 0.2, 0.1]
    base_score = calculate_weighted_scores(processed_data, weights)
    
    # More distractions
    irrelevant_set = {x // 2 for x in data_points if x > min_threshold}
    fake_adjustment = len(irrelevant_set) * 3.5
    
    # Final calculation with string operation distraction
    category = "HIGH" if base_score > 20 else "LOW"
    category_modifier = 1.5 if category.lower() == "high" else 0.8
    
    final_score = (base_score * category_modifier) - fake_adjustment + 7.25
    return final_score

# Main execution
metrics_data = [15, 8, 22, 12]
threshold = 10

# Irrelevant intermediate computations
intermediate_sum = sum(metrics_data) + 5
dummy_list = [x * 3 for x in metrics_data]
unused_string = "performance_analysis_" + str(threshold)

# Key execution point
result = analyze_performance(metrics_data, threshold)

# Final output
print(f"Result: {result}")