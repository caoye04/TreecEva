def process_data_stream(incoming_data):
    processed_values = []
    for idx, value in enumerate(incoming_data):
        if idx % 2 == 0:
            processed_values.append(value * 2)
        else:
            processed_values.append(value // 2)
    return processed_values

def calculate_adjustments(processed_data):
    adjustments = []
    temp_buffer = 0
    for item in processed_data:
        temp_buffer += item * 0.1
        adjustments.append(item + int(temp_buffer))
    return adjustments

def final_calculation(data_sequence):
    intermediate_results = process_data_stream(data_sequence)
    adjusted_values = calculate_adjustments(intermediate_results)
    
    # Distractor calculations that don't affect final result
    redundancy_check = sum(intermediate_results) * 0.05
    validation_sum = sum(adjusted_values) + redundancy_check
    
    zipped_pairs = list(zip(intermediate_results, adjusted_values))
    net_result = 0
    for base, adj in zipped_pairs:
        if base > adj:
            net_result -= (base - adj)
        else:
            net_result += (adj - base)
    
    # More distractor operations
    verification_value = net_result * 1.1
    safety_margin = verification_value - net_result
    
    return net_result

# Main execution
data_stream = [15, 8, 22, 12, 18, 6]
preliminary_sum = sum(data_stream) * 2  # Distractor
net_balance = final_calculation(data_stream)

print(f"Target result: {net_balance}")