def process_items(item_list):
    # Distractor: Unused lambda for formatting (never called)
    format_data = lambda x: f"Item_{x}"
    
    # Misleading intermediate variable
    temp_sum = sum(len(str(item)) for item in item_list if item > 0)
    
    # Dead code path - unused filtering logic
    filtered_items = [item * 2 for item in item_list if item % 3 == 0]
    
    # Relevant processing with lambda
    count_valid = lambda items: sum(1 for item in items if 10 <= item <= 99)
    
    # More distraction - complex but irrelevant calculation
    bit_ops = [item & 0xF for item in item_list]
    xor_total = sum(bit_ops) ^ 0xFF
    
    # Another dead variable
    string_ops = ''.join(chr(65 + (item % 26)) for item in item_list[:5])
    
    # Actual logic path
    valid_count = count_valid(item_list)
    
    # Final misleading operation that doesn't affect result
    adjusted = valid_count + (xor_total % 10)
    
    return valid_count

# Main execution with distractor setup
items_data = [15, 42, 87, 105, 3, 56, 200, 71, 8, 99]

# Distractor variables that look important
initial_count = len(items_data)
processed_data = [x // 2 for x in items_data]
bitwise_check = items_data[0] | items_data[1]

final_count = process_items(items_data)

print(f"Result: {final_count}")