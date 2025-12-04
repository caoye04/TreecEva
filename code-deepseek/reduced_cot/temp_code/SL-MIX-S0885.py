from collections import Counter

# Inventory processing system
inventory_items = ['widget', 'gadget', 'widget', 'tool', 'gadget', 'widget', 'part']
processing_batch = ['gadget', 'part', 'part', 'component', 'gadget']

# Count unique items in inventory
unique_items_counter = Counter(inventory_items)

# Process the batch and identify target
processed_batch = [item.upper() for item in processing_batch]
primary_item = 'widget'
target_item = 'GADGET'

# Calculate final count
final_count = unique_items_counter.get(primary_item, 0) + processed_batch.count(target_item)

print(f"Result: {final_count}")