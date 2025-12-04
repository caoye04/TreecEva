import itertools

product_ids = [1001, 1002, 1003, 1004, 1005]
warehouse_a = [1001, 1003, 1005, 1007]
warehouse_b = [1002, 1003, 1004, 1008]
warehouse_c = [1001, 1004, 1005, 1009]

# Find products in multiple warehouses
overlap_positions = []

# Check each product
for product in product_ids:
    locations = []
    # Record which warehouses have this product
    if product in warehouse_a:
        locations.append(1)
    if product in warehouse_b:
        locations.append(2)
    if product in warehouse_c:
        locations.append(3)
    
    # Only add to overlap if product is in more than one warehouse
    if len(locations) > 1:
        overlap_positions.append(locations)

# Calculate total overlap instances
overlap_count = len(list(itertools.chain(*overlap_positions)))

# For testing purposes - visualize the data
overlap_map = {}
for i, product in enumerate(product_ids):
    warehouses = []
    if product in warehouse_a:
        warehouses.append('A')
    if product in warehouse_b:
        warehouses.append('B')
    if product in warehouse_c:
        warehouses.append('C')
    if len(warehouses) > 1:
        overlap_map[product] = warehouses

print(f"Result: {overlap_count}")