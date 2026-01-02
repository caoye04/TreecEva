def analyze_performance(raw_input):
    temp_buffer = []
    total_entries = len(raw_input)
    valid_count = 0
    outlier_threshold = 100
    scaling_factor = 2.5
    adjustment = 0.8

    for entry in raw_input:
        if not isinstance(entry, int) or entry < 0:
            continue
        if entry > outlier_threshold:
            temp_buffer.append(outlier_threshold * 0.9)
        else:
            temp_buffer.append(entry * scaling_factor)
        valid_count += 1

    filtered_data = [x for x in temp_buffer if x > 10]
    
    # Irrelevant aggregation (distractor)
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    peak_value = max(temp_buffer) if temp_buffer else 0

    normalized_values = []
    base_offset = 5
    for val in filtered_data:
        adjusted_val = val * adjustment + base_offset
        normalized_values.append(round(adjusted_val))

    # Dead code path - never executed due to logic above
    if len(raw_input) == 0:
        return [0], 0, 0

    processed_data = {
        'values': normalized_values,
        'count': len(normalized_values),
        'sum': sum(normalized_values)
    }

    return processed_data


def calculate_rating(data):
    if data['count'] == 0:
        return 0.0
    
    raw_sum = data['sum']
    item_count = data['count']
    mean_value = raw_sum / item_count
    
    # Apply non-linear transformation
    if mean_value > 50:
        bonus_multiplier = 1.2
    elif mean_value > 30:
        bonus_multiplier = 1.1
    else:
        bonus_multiplier = 1.0
    
    # Secondary adjustment based on size
    size_factor = 1.0 + (item_count * 0.01) if item_count < 50 else 1.5
    
    # Efficiency score calculation (key result)
    efficiency_score = (mean_value * bonus_multiplier * size_factor)
    
    # Red herring computations
    hypothetical_max = item_count * 100
    utilization_ratio = raw_sum / hypothetical_max if hypothetical_max > 0 else 0
    penalty = 1 - (utilization_ratio * 0.1)
    efficiency_score *= penalty  # Minor effect but not central

    return efficiency_score

# Main execution
input_stream = [10, 15, 'err', 20, 25, 30, 101, 40, 102, 50]
processed_data = analyze_performance(input_stream)
final_rating = calculate_rating(processed_data)
efficiency_score = final_rating

print(f"Result: {efficiency_score}")