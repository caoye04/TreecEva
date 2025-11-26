def processing_phase(analysis_data, flags):
    temp_calc = (flags['start'] + analysis_data['base']) * 3
    if flags['enable_filter']:
        temp_calc -= analysis_data['offset'] // 2
    else:
        temp_calc += 17  # dead code path
    
    mask_ops = temp_calc & 0xFF
    step_result = mask_ops if analysis_data['threshold'] > 50 else mask_ops ^ 0x7F
    
    intermediate = step_result << 2
    validation_check = intermediate % 7
    if validation_check == 0:
        return intermediate + flags['adjustment']
    else:
        return intermediate - flags['adjustment'] * 2

def data_analysis_phase(input_values):
    processed_values = [x * 2 if x > 10 else x + 5 for x in input_values]
    slice_result = processed_values[1:4]
    aggregation = sum(slice_result) if len(slice_result) == 3 else 0
    
    base_value = aggregation // 3
    threshold_check = base_value if base_value % 2 == 0 else base_value + 1
    
    return {'base': base_value, 'offset': aggregation, 'threshold': threshold_check}

# Main execution
input_data = [8, 15, 22, 19, 11, 25]
config_flags = {'start': 12, 'enable_filter': True, 'adjustment': 7}

# Irrelevant computations
irrelevant_sum = sum(x ** 2 for x in input_data[:3])
misleading_temp = irrelevant_sum // 5 + 3
dead_code_var = misleading_temp * 2  # never used

# Actual processing
data_analysis = data_analysis_phase(input_data)
final_output = processing_phase(data_analysis, config_flags)

print(f"Result: {final_output}")