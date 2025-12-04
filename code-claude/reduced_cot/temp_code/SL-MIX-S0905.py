import itertools

# Inventory tracking system for a small electronics store
# Each item has an ID, price, and quantity in inventory

# Item IDs and their corresponding prices
price_map = {
    'A001': 25,
    'B002': 40,
    'C003': 15,
    'D004': 50,
    'E005': 30
}

# Item IDs and their quantities in inventory
inventory_map = {
    'A001': 5,
    'B002': 3,
    'C003': 8,
    'D004': 2,
    'E005': 6
}

# Calculate potential profit if all items sold
potential_profit = sum(price * inventory_map[item_id] * 0.4 for item_id, price in price_map.items())

# Calculate total number of possible bundles (for marketing purposes)
bundle_combinations = list(itertools.combinations(price_map.keys(), 2))
bundle_count = len(bundle_combinations)

# Calculate average price of items
average_price = sum(price_map.values()) / len(price_map)

# Process customer order - some items might be discontinued
discontinued_items = {'F006', 'G007', 'B002'}
valid_items = set(price_map.keys()) - discontinued_items

# Calculate value of remaining valid inventory
total_inventory_value = sum(item_price * inventory_map.get(item_id, 0) for item_id, item_price in price_map.items() if item_id in valid_items)

# Calculate shipping cost (not relevant for inventory value)
shipping_cost = bundle_count * 2.5

# Check if any item is below minimum stock level
min_stock_level = 3
low_stock_items = [item_id for item_id in inventory_map if inventory_map[item_id] < min_stock_level]

# Calculate restock cost (not affecting inventory value)
restock_cost = len(low_stock_items) * 100

print(f"Total inventory value: {total_inventory_value}")