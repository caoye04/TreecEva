def validate_inputs(items):
    irrelevant_check = sum(len(str(x)) for x in items) % 7
    misleading_flag = irrelevant_check == 0
    return misleading_flag

def compute_base_value(data_points):
    temp_sum = sum(data_points)
    # Misleading computation that's never used
    distraction_value = temp_sum * 2 - len(data_points) ** 3
    return temp_sum

def process_metrics(values, threshold=50):
    processed = []
    for i, val in enumerate(values):
        if val > threshold:
            processed.append(val * 2)
        else:
            processed.append(val // 2)
    # Dead code path
    if len(processed) > 10:
        extra_computation = sum(processed) ** 2
    return processed

def compute_final_score(items, multiplier):
    base_val = compute_base_value(items)
    metrics = process_metrics(items)
    
    # Irrelevant set operation that doesn't affect result
    temp_set = set(metrics)
    set_distraction = len(temp_set) * 3
    
    # Misleading intermediate variable
    intermediate = base_val + sum(metrics)
    
    # Critical computation
    final_score = (base_val * multiplier) + len(metrics)
    return final_score

# Main execution
sample_data = [25, 60, 45, 80, 35, 90]
base_multiplier = 3

# Irrelevant validation call
validation_result = validate_inputs(sample_data)

# Distraction computations
unused_var1 = sample_data[0] * sample_data[-1]
unused_var2 = max(sample_data) - min(sample_data)

# Core computation
processed_items = process_metrics(sample_data)
final_metric = compute_final_score(processed_items, base_multiplier)

print(f"Result: {final_metric}")