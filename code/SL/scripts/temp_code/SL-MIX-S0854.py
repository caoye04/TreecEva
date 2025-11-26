def process_data(data_sequence):
    intermediate_sum = sum(data_sequence)
    processed_values = [x * 2 for x in data_sequence if x > 5]
    
    # Distractor calculation - not used in final result
    temp_product = 1
    for num in data_sequence:
        temp_product *= (num + 1)
    
    filtered_numbers = [x for x in processed_values if x < 25]
    
    # Another distractor operation
    redundant_check = len([x for x in filtered_numbers if x % 2 == 0])
    
    final_result = [x for x in filtered_numbers if x % 3 == 0]
    target_value = sum(final_result)
    
    # More distraction
    unused_calculation = intermediate_sum - temp_product % 10
    
    print(f"Result: {target_value}")

# Main execution
sample_data = [3, 7, 4, 9, 2, 8, 6]
process_data(sample_data)