def process_inventory(items):
    # Calculate total items for reference (distractor)
    total_items = len(items)
    
    # Filter items that contain numeric characters
    filtered_items = [item for item in items if any(char.isdigit() for char in item)]
    
    # Calculate average length (distractor calculation)
    avg_length = sum(len(item) for item in items) / len(items) if items else 0
    
    # Count items with vowels (distractor)
    vowel_count = len([item for item in items if any(c in 'aeiouAEIOU' for c in item)])
    
    # Filter items with exactly 2 digits
    target_items = [item for item in filtered_items 
                   if sum(char.isdigit() for char in item) == 2]
    
    # Final count of items meeting criteria
    final_count = len(target_items)
    print(f"Result: {final_count}")

# Sample inventory data
inventory = ["item123", "widget45", "tool7", "gadget", "part99", "device1", "component888", "machine"]
process_inventory(inventory)