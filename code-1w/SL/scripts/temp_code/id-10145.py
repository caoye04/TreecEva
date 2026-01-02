def calculate_processed_weight(data_string, base_factor):
    # Parse input string to extract numeric components
    parts = data_string.split(':')
    raw_values = parts[1].split(',')
    
    # Extract and convert numerical fields
    weight = float(raw_values[0])
    adjustment = float(raw_values[1])
    
    # Normalize weight using base factor and apply adjustment
    normalized_value = (weight + adjustment) / base_factor
    
    # Irrelevant string transformation (distractor)
    label = parts[0].upper().replace('_', ' ')
    description = ''.join([label[i] for i in range(0, len(label), 2)])
    
    # Determine scaling based on magnitude
    if normalized_value < 1.0:
        final_scale = 10
    elif normalized_value < 2.0:
        final_scale = 15
    else:
        final_scale = 20
    
    # Critical computation point
    processed_weight = final_scale * normalized_value
    
    return processed_weight

# Main execution
input_data = "sample_7:8.5,1.5"
base_multiplier = 5.0
result = calculate_processed_weight(input_data, base_multiplier)
print(f"Target result: {result}")