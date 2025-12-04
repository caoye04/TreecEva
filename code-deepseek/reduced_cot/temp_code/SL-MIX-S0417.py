def process_data_records(records):
    temp_sum = 0
    processed_count = 0
    adjustment_factor = 15
    
    # Process each record with data validation
    for record in records:
        if isinstance(record, str):
            clean_record = record.strip().lower()
            if clean_record.isdigit():
                temp_sum += int(clean_record)
                processed_count += 1
    
    # Calculate averages and intermediate values
    average_value = temp_sum / max(processed_count, 1)
    intermediate_result = average_value * 2
    
    # Create dictionary for data tracking
    data_metrics = {
        'sum': temp_sum,
        'count': processed_count,
        'average': average_value,
        'intermediate': intermediate_result
    }
    
    # Calculate processed total (this is the target variable)
    processed_total = data_metrics['sum'] + data_metrics['count'] * 3
    
    # Some intermediate calculations that don't affect final result
    unused_calc = (intermediate_result - average_value) ** 2
    temp_buffer = [x for x in range(5)]  # Distractor list
    
    # Final calculation
    final_calculation = processed_total + adjustment_factor
    
    print(f"Result: {processed_total}")
    return processed_total

# Input data
records_list = [' 42 ', '17', 'invalid', ' 89 ', '5', 'test', ' 100 ']
process_data_records(records_list)