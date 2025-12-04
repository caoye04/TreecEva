from collections import Counter, defaultdict
import itertools

# Tracking inventory of a small bookstore
inventory = {
    'fiction_paperback': 120,
    'fiction_hardcover': 85,
    'non_fiction_paperback': 95,
    'non_fiction_hardcover': 110,
    'children_paperback': 55,
    'children_hardcover': 70,
    'rare_books': 500,
    'magazines': 30
}

# Price adjustments based on sales data
price_factors = {
    'paperback': 0.8,
    'hardcover': 1.2,
    'rare': 2.5
}

# Track popularity metrics (not directly relevant to inventory value)
popularity = Counter()
popularity.update(['fiction_paperback'] * 25)
popularity.update(['children_paperback'] * 40)
popularity.update(['magazines'] * 15)

# Seasonal items with different pricing structure
seasonal_items = ['magazines', 'rare_books']
seasonal_discount = 0.9 if sum(popularity.values()) > 50 else 1.0

# Apply discounts to certain categories based on inventory size
discount_factor = 1.0
if len([item for item in inventory if 'paperback' in item]) > 2:
    discount_factor -= 0.05

# Calculate potential revenue from seasonal items
seasonal_revenue = sum(inventory[item] for item in seasonal_items) * seasonal_discount

# Track inventory by binding type
binding_counts = defaultdict(int)
for item in inventory:
    if 'paperback' in item:
        binding_counts['paperback'] += inventory[item]
    elif 'hardcover' in item:
        binding_counts['hardcover'] += inventory[item]
    else:
        binding_counts['other'] += inventory[item]

# Calculate average value by binding type
avg_value_by_binding = {}
for binding, count in binding_counts.items():
    relevant_items = [item for item in inventory if binding in item]
    if relevant_items:
        avg_value_by_binding[binding] = sum(inventory[item] for item in relevant_items) / len(relevant_items)

# Apply a small adjustment based on binding distribution
distribution_factor = binding_counts['hardcover'] / (binding_counts['paperback'] + 1)
if distribution_factor > 0.5:
    discount_factor += 0.02
else:
    discount_factor -= 0.01

# Calculate main inventory value excluding seasonal items
inventory_value = sum(item_value for item, item_value in inventory.items() if item not in seasonal_items)

# Calculate total value including seasonal items (for comparison)
total_value = sum(inventory.values())

print(f"Result: {inventory_value}")