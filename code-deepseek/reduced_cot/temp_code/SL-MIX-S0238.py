def process_inventory_data(items_string):
    items = items_string.split(',')
    total_count = len(items)
    processed_count = sum(1 for item in items if len(item.strip()) > 3)
    
    result = processed_count * 15 - (total_count - processed_count) * 5
    threshold = 25
    
    # Critical execution point
    target_value = result if result > threshold else threshold + result
    
    print(f"Target result: {target_value}")

# Execute the function
process_inventory_data("apple, pear, banana, kiwi, orange, plum")