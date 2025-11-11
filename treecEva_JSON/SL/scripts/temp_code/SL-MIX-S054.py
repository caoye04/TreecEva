from collections import deque

def calculate_priority(items):
    return sum(item ** 2 if item > 0 else -item for item in items)

def process_inventory():
    shipments_stack = []
    orders_queue = deque()
    
    # Incoming shipments with item values
    shipments_data = [
        [3, -2, 5],
        [-1, 4, -3],
        [2, 2, 2, 2],
        [-5, -5]
    ]
    
    # Outgoing orders with item requests
    orders_data = [
        [1, -1, 2],
        [-2, 3],
        [4, 4, -3, -3]
    ]
    
    # Load shipments into stack with their priorities
    for shipment_items in shipments_data:
        priority = calculate_priority(shipment_items)
        shipments_stack.append(priority)
    
    # Load orders into queue with their priorities
    for order_items in orders_data:
        priority = calculate_priority(order_items)
        orders_queue.append(priority)
    
    # Process shipments and orders
    while shipments_stack and orders_queue:
        top_shipment = shipments_stack[-1]
        front_order = orders_queue[0]
        
        if top_shipment >= front_order:
            # Shipment fulfills order
            shipments_stack.pop()
            orders_queue.popleft()
        else:
            # Cannot fulfill, check next shipment
            if len(shipments_stack) > 1:
                shipments_stack.pop()  # Remove lower priority shipment
            else:
                break  # Cannot proceed further
    
    # Calculate discrepancy
    highest_remaining_shipment = max(shipments_stack) if shipments_stack else 0
    earliest_pending_order = orders_queue[0] if orders_queue else 0
    discrepancy = highest_remaining_shipment - earliest_pending_order
    
    return discrepancy

final_discrepancy = process_inventory()
print(f"Result: {final_discrepancy}")