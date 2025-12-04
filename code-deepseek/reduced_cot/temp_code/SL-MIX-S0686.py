def process_data(items):
    # Initialize counters and trackers
    primary_count = 0
    secondary_tracker = []
    misleading_total = 0
    temp_buffer = []
    
    # Distractor operations - string processing that won't be used
    test_string = "unused_data_processing_sample"
    unused_length = len(test_string)
    unused_upper = test_string.upper()
    unused_split = test_string.split("_")
    
    # Main logic with complex interdependencies
    for item in items:
        # Primary counting logic
        if (item > 25 and item < 75) or (item % 3 == 0 and item % 5 != 0):
            primary_count += 2
            temp_buffer.append(item * 2)
        elif item % 7 == 0 and len(str(item)) > 1:
            primary_count -= 1
            secondary_tracker.append(item // 2)
        else:
            # Distractor operation that doesn't affect final result
            misleading_total += item * 3
            
        # Dead code path - condition never true for given input
        if item > 1000:
            primary_count = primary_count * 10
            
    # Process collected data with string operations
    result_string = "".join(chr((x % 26) + 65) for x in temp_buffer if x > 0)
    string_length = len(result_string)
    
    # Final calculation with bitwise operations
    if secondary_tracker:
        last_element = secondary_tracker[-1] if secondary_tracker else 0
        bit_shifted = (primary_count << 2) | (last_element & 0xF)
        final_value = bit_shifted - (string_length * 3)
    else:
        final_value = (primary_count * 4) + misleading_total
    
    # Final adjustment based on string analysis
    if result_string and result_string.startswith("B"):
        final_value += 15
    else:
        final_value -= 8
    
    return final_value

# Main execution with test data
items = [42, 63, 28, 91, 35, 14, 77, 21, 56, 84]
final_result = process_data(items)
print(f"Result: {final_result}")