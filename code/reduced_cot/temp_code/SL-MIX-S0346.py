def process_inventory():
    inventory = ["recyclable", "disposable", "reusable", "breakable", "stable", "flexible", "portable"]
    backup_list = ["fragile", "durable", "washable"]
    
    # Distractor operations that don't affect final result
    temp_count = len(inventory) + len(backup_list)
    processed_items = {item for item in inventory if item.lower().endswith("able")}
    filtered_count = len(processed_items)
    
    # More distractors
    unused_set = set(backup_list)
    intermediate_sum = sum(len(item) for item in inventory)
    
    # Key calculation
    final_count = filtered_count * 3 - 2
    
    # Final irrelevant operation
    dummy_result = final_count + intermediate_sum - temp_count
    
    print(f"Result: {final_count}")
    return final_count

process_inventory()