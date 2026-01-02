from collections import defaultdict

def analyze_trends(data_points):
    trends = defaultdict(int)
    for point in data_points:
        if point > 0:
            trends['positive'] += 1
        elif point < 0:
            trends['negative'] += 1
        else:
            trends['neutral'] += 1
    return dict(trends)

def calculate_baseline(reference_values):
    total = 0
    count = 0
    temp_result = 0
    for val in reference_values:
        if val % 2 == 0 and val > 5:
            total += val ** 0.5
            count += 1
        else:
            temp_result -= val // 2
    return total / count if count else 0

def evaluate_performance(feedbacks, importance_weights):
    weighted_sum = 0.0
    adjustment_factor = 0.0
    base_offset = calculate_baseline([3, 7, 8, 10, 12])
    
    # Simulate feedback processing with distraction logic
    debug_info = []
    temp_store = []
    for i, (fb, weight) in enumerate(zip(feedbacks, importance_weights)):
        raw_value = fb * weight
        if i % 2 == 0:
            adjusted_value = raw_value * 1.1
        else:
            adjusted_value = raw_value * 0.95
        
        # Irrelevant filtering (distractor)
        if adjusted_value > 100:
            debug_info.append(f"High value at {i}")
        elif adjusted_value < 10:
            temp_store.append(adjusted_value)
        
        weighted_sum += adjusted_value
    
    # Additional irrelevant computation
    secondary_total = 0
    for j, _ in enumerate(debug_info):
        secondary_total += len(_) * 0.1
    
    # Actual key logic
    adjustment_factor = len(temp_store) * 0.5
    final_score = weighted_sum - adjustment_factor + base_offset
    
    # Red herring: unused transformation
    transformed = [x * 2 for x in importance_weights if x > 0.5]
    ignored_result = sum(transformed) // 2 if transformed else 0
    
    return int(final_score)

# Main execution
feedback_levels = [45, 62, 33, 71, 50, 29]
weights = [0.8, 1.2, 0.5, 1.5, 1.0, 0.7]
baseline_data = [-2, -1, 0, 1, 2]

# Unused but plausible-looking analysis
pattern_analysis = analyze_trends(baseline_data)
summary_stats = {key: val * 2 for key, val in pattern_analysis.items()}

final_score = evaluate_performance(feedback_levels, weights)
print(f"Result: {final_score}")