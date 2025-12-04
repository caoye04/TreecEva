from collections import defaultdict

# Warehouse inventory analysis
warehouse_zones = ['A', 'B', 'C', 'D']
initial_stock = [125, 340, 210, 85]
restock_amounts = [45, 60, 25, 15]
zone_weights = [1.2, 0.8, 1.5, 1.0]

# Calculate current inventory
current_inventory = []
for i in range(len(warehouse_zones)):
    stock = initial_stock[i] + restock_amounts[i]
    current_inventory.append(stock)

# Temporary calculation (distractor)
zone_efficiency = []
for stock, weight in zip(current_inventory, zone_weights):
    efficiency = stock * weight / 100
    zone_efficiency.append(efficiency)

# Create warehouse totals dictionary
warehouse_totals = defaultdict(int)
for zone, stock in zip(warehouse_zones, current_inventory):
    warehouse_totals[zone] = stock

# Additional processing (distractor)
total_capacity = sum(current_inventory)
average_stock = total_capacity / len(current_inventory)

# Select zone with maximum stock
selected_zone = warehouse_zones[current_inventory.index(max(current_inventory))]
final_inventory_value = warehouse_totals[selected_zone]

print(f"Target result: {final_inventory_value}")