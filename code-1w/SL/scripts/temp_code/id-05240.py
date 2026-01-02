def compute_filtered_sum(raw_values):
    offset = 7
    adjusted_values = [val + offset for val in raw_values]
    temp_result = [v for v in adjusted_values if v > 10]
    processed_data = []
    for num in temp_result:
        if num % 2 == 0:
            processed_data.append(num * 2)
        else:
            processed_data.append(num)
    
    # Irrelevant distraction: unused variable
    baseline_reference = sum(raw_values) / len(raw_values)
    
    filtered_sum = sum([x for x in processed_data if x % 3 == 0])
    return filtered_sum

# Main execution
input_data = [1, 3, 5, 4, 8]
result = compute_filtered_sum(input_data)
print(f"Target result: {result}")