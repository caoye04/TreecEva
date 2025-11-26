from collections import Counter

def process_inventory():
    inventory_counts = [5, 3, 5, 2, 5, 3, 4, 2, 5, 4]
    item_frequency = Counter(inventory_counts)
    
    target_items = [k for k, v in item_frequency.items() if v > 2]
    
    # Distractor: processing all items (not used in final result)
    all_items_total = sum(item_frequency.keys()) * 2
    
    # Main logic: sum of qualifying items
    target_sum = sum(target_items) if target_items else 0
    
    # Distractor: adjustment calculation (not used)
    adjustment = len([x for x in inventory_counts if x % 2 == 0]) * 3
    
    # Final correction offset
    offset_correction = -1 if len(target_items) > 1 else 2
    
    final_result = target_sum + offset_correction
    print(f"Target result: {final_result}")

process_inventory()