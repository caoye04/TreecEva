from itertools import compress, cycle

def preprocess_data(raw):
    cleaned = [x for x in raw if isinstance(x, (int, float)) and x >= 0]
    scaled = [x * 0.75 for x in cleaned]
    return scaled

def evaluate_condition(x, thres):
    return x > thres

def calculate_final_score(data, thresholds):
    # Preprocess the input data
    processed = preprocess_data(data)
    
    # Irrelevant transformation (distractor)
    squared_values = [x ** 2 for x in processed if x < 50]  
    temp_sum = sum(squared_values) / len(squared_values) if squared_values else 0
    
    # Actual logic begins: apply threshold filtering
    high_vals = []
    low_threshold = thresholds['low']
    high_threshold = thresholds['high']
    
    for val in processed:
        if evaluate_condition(val, high_threshold):
            high_vals.append(val * 1.2)
        elif evaluate_condition(val, low_threshold):
            high_vals.append(val * 0.8)
        else:
            high_vals.append(val * 0.5)
    
    # Simulate weighted contribution using cycle
    weights = list(cycle([1.1, 0.9]))[:len(high_vals)]
    weighted = [val * weight for val, weight in zip(high_vals, weights)]
    
    # Red herring computation (not used in final result)
    outlier_count = sum(1 for v in weighted if v > 100)
    avg_weighted = sum(weighted) / len(weighted) if weighted else 0
    
    # Final aggregation
    base_score = sum(weighted)
    adjustment = len(processed) * 0.25
    final_score = int(base_score - adjustment)  # deterministic integer result
    
    # Dead code path (never executed due to prior conditions)
    if False and temp_sum > 1000:
        final_score += outlier_count * 10
        backup_list = [base_score, temp_sum, avg_weighted]
        final_score = max(backup_list)
    
    return final_score

# Main execution
raw_input_data = [10, -5, 20, 'ignore', 30, 40, 50, None, 60]
config = {'low': 25, 'high': 45}
intermediate_result = preprocess_data(raw_input_data)
status_flag = True if sum(intermediate_result) > 50 else False

# Key statement
final_score = calculate_final_score(raw_input_data, config)
print(f"Result: {final_score}")