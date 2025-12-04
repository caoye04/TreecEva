def process_inventory_data(item_records):
    # Distractor: unused helper function
    def calculate_discount(base_price, discount_rate):
        return base_price * (1 - discount_rate)
    
    inventory_counts = {'A': 15, 'B': 23, 'C': 8, 'D': 42, 'target_key': 187}
    processed_data = {}
    
    # Misleading intermediate calculations
    total_items = sum(inventory_counts.values())  # This is a distraction
    average_count = total_items / len(inventory_counts)  # Irrelevant computation
    
    # Red herring operations
    temp_calculation = (inventory_counts['A'] * 3 + inventory_counts['B'] * 2) // 5
    offset_adjustment = temp_calculation % 7  # Dead code path result
    
    # Actual processing with distractions
    processed_data = {k: v * 2 if k != 'target_key' else v // 2 for k, v in inventory_counts.items()}
    
    # More misleading variables
    running_total = 0
    for count in processed_data.values():
        running_total += count  # Unused computation
    
    # Critical execution point
    offset_correction = processed_data.get('C', 0) - 4
    
    # Dead code block that never executes
    if running_total > 1000:
        extra_offset = 25
    else:
        extra_offset = 0  # This path is never taken
    
    # The key statement
    final_output = processed_data.get("target_key", 0) + offset_correction
    
    print(f"Result: {final_output}")

# Execute the function
process_inventory_data([])