import itertools
from collections import deque

def process_warehouse_movements():
    # Initialize warehouse zones as a 3x3 matrix
    warehouse_zones = [[0 for _ in range(3)] for _ in range(3)]
    
    # Stack for incoming shipments (LIFO)
    incoming_stack = []
    
    # Queue for outgoing shipments (FIFO)
    outgoing_queue = deque()
    
    # Simulate incoming shipments
    for product_id in range(10, 21):
        incoming_stack.append(product_id)
    
    # Process incoming shipments to zone (0, 1)
    while incoming_stack:
        product = incoming_stack.pop()
        zone_row, zone_col = divmod(product % 9, 3)
        warehouse_zones[zone_row][zone_col] += 1
    
    # Move half of zone (0, 1) inventory to zone (1, 2)
    zone_01_count = warehouse_zones[0][1]
    transfer_amount = zone_01_count // 2 if zone_01_count % 2 == 0 else (zone_01_count // 2) + 1
    warehouse_zones[0][1] -= transfer_amount
    warehouse_zones[1][2] += transfer_amount
    
    # Schedule outgoing shipments from zone (1, 2)
    products_to_ship = warehouse_zones[1][2]
    for i in range(min(products_to_ship, 5)):
        outgoing_queue.append(i + 100)
    
    # Process outgoing shipments (remove 3 items)
    shipped_count = 0
    while outgoing_queue and shipped_count < 3:
        outgoing_queue.popleft()
        shipped_count += 1
    
    # Update zone (1, 2) count after shipping
    warehouse_zones[1][2] -= shipped_count
    
    # Apply dynamic adjustment based on neighboring zones
    neighbors_sum = warehouse_zones[0][2] + warehouse_zones[1][1] + warehouse_zones[2][2]
    adjustment = neighbors_sum % 3
    warehouse_zones[1][2] = warehouse_zones[1][2] + adjustment if warehouse_zones[1][2] > 0 else 0
    
    return warehouse_zones[1][2]

final_inventory_zone_12 = process_warehouse_movements()
print(f"Result: {final_inventory_zone_12}")