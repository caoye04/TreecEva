import itertools

def process_data_sequence():
    data_stream = [3, 7, 2, 9, 5, 1, 8, 4]
    temp_sum = sum(data_stream)
    
    # Distractor: Calculate combinations but don't use them
    combinations_list = list(itertools.combinations(data_stream, 3))
    combo_count = len(combinations_list)
    
    # Intermediate processing
    filtered_data = [x for x in data_stream if x % 2 == 1]
    product_temp = 1
    for num in filtered_data[:3]:
        product_temp *= num
    
    # Redundant calculation
    average_all = temp_sum / len(data_stream)
    
    # Core logic
    target_numbers = [x for x in data_stream if x > 3 and x < 8]
    final_product = 1
    for num in target_numbers:
        final_product *= num
    
    # Distractor: More unused computations
    sorted_data = sorted(data_stream)
    range_diff = sorted_data[-1] - sorted_data[0]
    
    return final_product

def result_calculation():
    base_value = process_data_sequence()
    
    # Additional processing with distractors
    offset_calc = (base_value % 10) * 2
    adjustment = offset_calc - 3
    
    # Unused intermediate
    dummy_operations = [x + y for x, y in itertools.product([1, 2], [3, 4])]
    
    final_result = base_value + adjustment
    print(f"Target result: {final_result}")
    return final_result

result_calculation()