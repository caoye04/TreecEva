from collections import Counter

def process_data_stream(data):
    irrelevant_tracker = [i * 2 for i in range(10)]
    misleading_buffer = sum(x for x in irrelevant_tracker if x % 3 == 0)
    
    frequency_count = Counter(data)
    processed_values = []
    
    for item in data:
        temp_transform = (item << 1) | 0x0F
        processed_values.append(temp_transform)
        
    dead_code_path = [x * 3 for x in irrelevant_tracker]
    unused_calculation = sum(dead_code_path) // len(dead_code_path)
    
    base_value = sum(processed_values)
    mask_pattern = frequency_count[5] * 0xFF
    filter_mask = 0x3A7
    
    intermediate_check = (base_value | mask_pattern) + 100
    distractor_var = intermediate_check // 2
    
    final_computation = (base_value ^ mask_pattern) & filter_mask
    
    print(f"Result: {final_computation}")

input_data = [5, 2, 5, 8, 3, 5, 1, 7, 5, 4, 2, 6]
process_data_stream(input_data)