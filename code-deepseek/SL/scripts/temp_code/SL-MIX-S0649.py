import itertools

# Inventory analysis with filtering operations
def analyze_inventory(items_list):
    # Primary data processing
    valid_items = [item for item in items_list if item > 0 and item % 3 != 0]
    processed_count = len(valid_items) * 2
    
    # Distractor computations (irrelevant to final result)
    temp_sum = sum(items_list[:3]) if len(items_list) >= 3 else 0
    alternate_count = processed_count + 5
    
    # Conditional filtering using itertools
    filtered_sequence = list(itertools.islice(valid_items, 0, min(4, len(valid_items))))
    scale_factor = 3 if len(filtered_sequence) > 2 else 5
    
    # More distractor operations
    multiplier = lambda x: x * 2 + 1
    dummy_result = multiplier(processed_count) if processed_count > 10 else 0
    
    # Dead code path (never executed)
    if len(items_list) > 20:
        unused_value = processed_count * 10
        print(f"Debug: {unused_value}")
    
    # Core calculation chain
    adjustment_map = {2: 7, 3: 4, 4: 1}
    adjustment_value = adjustment_map.get(len(filtered_sequence), 0)
    excess_count = len([x for x in items_list if x < 0]) + 2
    
    # Final result computation
    final_quantity = (processed_count - excess_count) * scale_factor + adjustment_value
    
    # Additional misleading operations
    verification_sum = sum(filtered_sequence) + final_quantity
    print(f"Target result: {final_quantity}")

# Execute with test data
sample_items = [8, -2, 15, 22, 3, 7, -1, 14, 6]
analyze_inventory(sample_items)