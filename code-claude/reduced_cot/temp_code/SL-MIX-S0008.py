from collections import Counter

# Inventory tracking for a small bookstore
inventory = ['novel', 'textbook', 'magazine', 'novel', 'comic', 'novel', 
           'textbook', 'novel', 'magazine', 'novel']

# Track some metadata about inventory
total_items = len(inventory)
unique_types = set(inventory)

# Count occurrences of each item type
inventory_counts = Counter(inventory)

# Find the most common item frequency
most_common_item = inventory_counts.most_common(1)[0][0]
common_frequency = inventory_counts.most_common(1)[0][1]

# Calculate percentage of inventory for the most common item
percentage = (common_frequency / total_items) * 100

# Display results
print(f"Result: {common_frequency}")