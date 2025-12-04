def process_data(items):
    data_map = {'A': 12, 'B': 7, 'C': 15, 'D': 9, 'E': 22}
    temp_sum = 0
    processed = []
    
    # Distractor: irrelevant string operations
    debug_info = "Processing " + str(len(items)) + " items"
    print(debug_info)
    
    for idx, item in enumerate(items):
        if item in data_map:
            value = data_map[item]
            processed.append(value * 2)
            temp_sum += value
        else:
            # Dead code path - misleading operation
            processed.append(-1)
    
    # Misleading intermediate calculation
    fake_avg = temp_sum / max(len(processed), 1) if processed else 0
    
    # Distractor: unused operation
    bit_check = temp_sum & 0xFF
    
    relevant_values = [x for x in processed if x > 10]
    
    # Key logic chain
    if len(relevant_values) >= 2:
        min_val = min(relevant_values)
        max_val = max(relevant_values)
        result = (max_val - min_val) * 3 + 5
    else:
        result = sum(processed) + 100  # Never taken path
    
    return result

items = ['A', 'B', 'C', 'D', 'A']
temp_calc = len(items) * 10  # Distractor
final_result = process_data(items)
print(f"Target result: {final_result}")