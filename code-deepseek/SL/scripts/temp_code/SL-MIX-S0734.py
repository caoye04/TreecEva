from collections import Counter

def process_inventory(items):
    # Analyze item frequency with counter
    item_counter = Counter(items)
    
    # Intermediate processing (distraction)
    total_items = len(items)
    unique_items = len(item_counter)
    
    # Filter items that appear at least twice
    filtered_items = [item for item, count in item_counter.items() if count >= 2]
    
    # Distractor calculation (not used in final result)
    avg_frequency = sum(item_counter.values()) / len(item_counter) if item_counter else 0
    
    # Process case-insensitive variants
    lower_items = [item.lower() for item in filtered_items]
    processed_set = set(lower_items)
    
    # Final count of unique processed items
    final_count = len(processed_set)
    
    # Another distraction calculation
    theoretical_max = len(items) // 2
    
    return final_count

# Inventory data with duplicates and case variations
inventory_data = ['Widget', 'GADGET', 'widget', 'Tool', 'gadget', 'WIDGET', 'sensor', 'Sensor']

# Execute the main processing
result = process_inventory(inventory_data)
print(f"Result: {result}")