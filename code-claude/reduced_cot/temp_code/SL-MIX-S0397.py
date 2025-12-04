# Inventory Management System

def calculate_restock_priority(items, threshold):
    # Calculate priority score for each item (not used in final calculation)
    priority_scores = {}
    for item, count in items.items():
        if count < threshold:
            priority_scores[item] = (threshold - count) * 2
        else:
            priority_scores[item] = 0
    return priority_scores

# Initialize inventory data
supplier_options = ['SupplierA', 'SupplierB', 'SupplierC']
preferred_supplier = supplier_options[1]  # SupplierB

# Current inventory counts
current_inventory = {
    'apples': 45,
    'oranges': 23,
    'bananas': 12,
    'grapes': 18,
    'pears': 30
}

# Price data (not used in final calculation)
pricing = {
    'apples': 0.75,
    'oranges': 0.90,
    'bananas': 0.60,
    'grapes': 2.50,
    'pears': 1.25
}

# Process inventory data
restock_threshold = 20
priorities = calculate_restock_priority(current_inventory, restock_threshold)

# Identify items needing restock
restock_items = [item for item, count in current_inventory.items() if count < restock_threshold]

# Restock simulation (not affecting final result)
for idx, item in enumerate(restock_items):
    # This calculation doesn't affect the final answer
    restock_amount = restock_threshold - current_inventory[item]
    if preferred_supplier == 'SupplierB':
        restock_amount += 5  # Supplier B provides extra units

# Calculate inventory metrics
low_stock_count = len(restock_items)
expensive_items = {k: v for k, v in current_inventory.items() if pricing.get(k, 0) > 1.0}

# Calculate total inventory
target_inventory = sum(current_inventory.values())

# Calculate potential inventory value (not used in final answer)
potential_value = sum(count * pricing[item] for item, count in current_inventory.items())

print(f"Target result: {target_inventory}")