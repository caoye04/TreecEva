def analyze_data(raw_input):
    base_offset = 10
    scaling_factor = 2
    
    # Initial transformation: scale and shift values
    scaled_values = [v * scaling_factor + base_offset for v in raw_input]
    
    # Secondary processing: apply conditional adjustment
    adjusted_values = []
    for val in scaled_values:
        if val % 3 == 0:
            adjusted_values.append(val + 1)
        elif val % 5 == 0:
            adjusted_values.append(val - 2)
        else:
            adjusted_values.append(val)
    
    # Threshold filtering using list comprehension
    threshold = 15
    processed_values = [x // 2 for x in adjusted_values]
    filtered_sum = sum([x for x in processed_values if x > threshold])
    
    # Irrelevant tracking variable (minor distraction)
    count_above_avg = len([x for x in processed_values if x > sum(processed_values) / len(processed_values)])
    
    return filtered_sum

# Main execution
input_data = [4, 7, 9, 12, 15]
result = analyze_data(input_data)
print(f"Result: {result}")