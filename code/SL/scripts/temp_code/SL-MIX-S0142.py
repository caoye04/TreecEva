def process_inventory(items):
    # Process warehouse inventory with various calculations
    item_codes = [item * 2 for item in items if item % 3 != 0]
    
    # Intermediate calculations (some not directly used)
    temp_sum = sum(item_codes)
    alternate_calc = len(item_codes) * 5.5
    unused_metric = temp_sum / max(1, len(item_codes))
    
    # Create mapping with lambda for processing
    result_mapping = {code: (lambda x: x ** 1.5)(code) for code in item_codes}
    
    # Filter and process with enumerate
    filtered_value = None
    for idx, code in enumerate(item_codes):
        if idx % 2 == 0:
            filtered_value = code
            break
    
    # Additional unused operations
    potential_result = sum(result_mapping.values()) / 10
    fallback_calc = (temp_sum - alternate_calc) if temp_sum > 100 else temp_sum
    
    # Final calculation with intervention
    final_output = result_mapping.get(filtered_value, fallback_calc)
    
    print(f"Result: {final_output}")

# Execute with sample inventory
inventory_items = [8, 12, 15, 20, 25, 30]
process_inventory(inventory_items)