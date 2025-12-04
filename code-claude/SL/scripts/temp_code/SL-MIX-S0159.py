# Analyzing overlapping items in kitchen inventory
fruits_basket = ['apple', 'banana', 'tomato', 'orange', 'kiwi']
vegetables_drawer = ['carrot', 'tomato', 'cucumber', 'kiwi', 'lettuce']

# Count total unique items
total_unique = len(set(fruits_basket) | set(vegetables_drawer))

# Find items that can be classified as both fruit and vegetable
common_elements = set(fruits_basket) & set(vegetables_drawer)

# Get items that are exclusively fruits or vegetables
exclusive_items = set(fruits_basket) ^ set(vegetables_drawer)

# Calculate some inventory statistics
inventory_ratio = len(common_elements) / total_unique if total_unique > 0 else 0

print(f"Common items: {common_elements}")
print(f"Number of common items: {len(common_elements)}")
