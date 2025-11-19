from collections import deque

class InventoryItem:
    def __init__(self, item_id, status='received'):
        self.item_id = item_id
        self.status = status
    
    def __repr__(self):
        return f"InventoryItem({self.item_id}, '{self.status}')"

def process_inventory():
    # Initialize data structures
    incoming_queue = deque()  # FIFO for incoming items
    storage_area = []         # Storage as list
    shipping_stack = []       # LIFO for shipments
    
    # State machine definition
    state_transitions = {
        'received': 'stored',
        'stored': 'shipped',
        'shipped': None
    }
    
    # Simulate 8 inventory events
    for i in range(1, 9):
        # Event 1,3,5,7: New items received
        if i % 2 == 1:
            new_item = InventoryItem(i*10)
            incoming_queue.append(new_item)
        
        # Event 2,4,6,8: Process items
        else:
            # Move from queue to storage if possible
            if incoming_queue and len(storage_area) < 3:
                item = incoming_queue.popleft()
                item.status = state_transitions[item.status]
                storage_area.append(item)
            
            # Move from storage to shipping if storage full or every other cycle
            if storage_area and (len(storage_area) >= 3 or i % 4 == 0):
                item = storage_area.pop()
                item.status = state_transitions[item.status]
                shipping_stack.append(item)
    
    # Count items ready for shipment
    pending_shipments_count = len(shipping_stack)
    
    return pending_shipments_count

# Execute the inventory processing
result = process_inventory()
print(f"Result: {result}")