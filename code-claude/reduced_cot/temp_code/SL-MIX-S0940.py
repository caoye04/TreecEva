import itertools

def calculate_storage_value(items, price_factor):
    # Helper function to calculate storage value
    return sum(len(item) for item in items) * price_factor

# Warehouse inventory tracking
warehouse_a = ['laptop', 'monitor', 'keyboard', 'mouse', 'printer', 'scanner']
warehouse_b = ['desktop', 'monitor', 'keyboard', 'webcam', 'printer', 'headphones']
warehouse_c = ['tablet', 'phone', 'monitor', 'speaker']

# Calculate storage values (not directly used in final answer)
storage_a_value = calculate_storage_value(warehouse_a, 2.5)
storage_b_value = calculate_storage_value(warehouse_b, 3.0)

# Track item frequencies across warehouses
all_items = warehouse_a + warehouse_b + warehouse_c
item_counter = {}
for item in all_items:
    item_counter[item] = item_counter.get(item, 0) + 1

# Find items that appear in exactly two warehouses
items_in_two = [item for item, count in item_counter.items() if count == 2]

# Inventory multiplier calculation
base_multiplier = 4
inventory_adjustment = len([x for x in itertools.chain(warehouse_a, warehouse_b) if len(x) > 6])
inventory_multiplier = base_multiplier - inventory_adjustment

# Calculate unique items in each warehouse (distractor)
unique_a = set(warehouse_a) - set(warehouse_b) - set(warehouse_c)
unique_b = set(warehouse_b) - set(warehouse_a) - set(warehouse_c)

# Lambda for priority calculation (not used in final answer)
priority_calc = lambda x: 10 if x in items_in_two else 5

# This is the key statement
common_items = len(set(warehouse_a).intersection(warehouse_b)) * inventory_multiplier

# Distractor calculation
total_priority = sum(priority_calc(item) for item in all_items)

print(f"Result: {common_items}")