def process_inventory(items):
    total_items = len(items)
    defective_count = sum(1 for item in items if item.startswith('D'))
    processed_count = sum(1 for item in items if item.isalnum())
    
    # Distractor calculations that don't affect the final result
    quality_score = defective_count * 2
    efficiency_ratio = processed_count / total_items if total_items > 0 else 0
    
    valid_items = [item for item in items if item.isalpha()]
    remaining_items = len(valid_items)
    
    # More distractors
    inventory_value = remaining_items * 10
    storage_cost = remaining_items // 2
    
    bonus_items = 3 if remaining_items > 5 else 1
    final_quantity = remaining_items + bonus_items
    
    print(f"Result: {final_quantity}")

# Test data
inventory_list = ['A123', 'B456', 'C789', 'D001', 'E002', 'F003', 'G004']
process_inventory(inventory_list)