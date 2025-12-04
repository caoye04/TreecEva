def process_inventory_data():
    # Initialize inventory data with mixed types
    raw_items = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Printer']
    item_quantities = [15, 42, 28, 9, 17]
    
    # Create inventory mapping using lambda and zip
    inventory_map = dict(zip(raw_items, map(lambda x: x * 2, item_quantities)))
    
    # Process data with set operations (distractor)
    processed_set = set(raw_items)
    temp_analysis = len(processed_set) * 5  # Unused computation
    
    # Key logic: filter and transform inventory
    filtered_items = [item for item in raw_items if len(item) > 5]
    processed_data = sum([inventory_map[item] for item in filtered_items])
    
    # Create result mapping with bitwise operations
    result_map = {}
    base_value = processed_data
    for i in range(3):
        result_map[base_value] = (base_value ^ 0b1010) & 0xFF
        base_value += 10  # Unnecessary increment
    
    # Final computation with string method (distractor)
    debug_info = ''.join(filtered_items).upper().count('O')  # Unused
    
    final_output = result_map[processed_data]
    print(f"Target result: {final_output}")

process_inventory_data()