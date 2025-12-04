def analyze_data_sets():
    data_sets = [
        {'values': [4, 7, 2, 9], 'weights': [1, 2, 1, 3]},
        {'values': [8, 3, 6, 1], 'weights': [2, 1, 2, 1]},
        {'values': [5, 2, 8, 4], 'weights': [1, 3, 1, 2]}
    ]
    
    processed_values = []
    intermediate_calc = []
    
    for idx, dataset in enumerate(data_sets):
        weighted_sum = sum(v * w for v, w in zip(dataset['values'], dataset['weights']))
        processed_values.append(weighted_sum)
        
        # Distractor calculations that don't affect final result
        dataset_max = max(dataset['values'])
        dataset_min = min(dataset['values'])
        intermediate_calc.append(dataset_max - dataset_min)
    
    # Core processing logic
    final_processing = sum(processed_values)
    processed_total = final_processing - min(processed_values)
    
    # More distractor operations
    temp_calc = sum(intermediate_calc)
    adjusted_temp = temp_calc // 2
    
    print(f"Result: {processed_total}")
    return processed_total

analyze_data_sets()