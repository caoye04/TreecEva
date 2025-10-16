from collections import deque

class Container:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_weight = 0
        self.items = []
    
    def add_item(self, item):
        item_id, weight = item
        if self.current_weight + weight <= self.max_capacity:
            self.items.append(item)
            self.current_weight += weight
            return True
        return False

def process_shipments(incoming_queue, outgoing_queue, container_limit):
    transferred_items = 0
    
    while incoming_queue:
        shipment = incoming_queue.popleft()
        container = Container(container_limit)
        
        for item in shipment:
            if container.add_item(item):
                outgoing_queue.append(item)
                transferred_items += 1
    
    return transferred_items

# Initialize queues
incoming_shipments = deque([
    [(101, 15), (102, 25), (103, 10)],
    [(201, 30), (202, 20)],
    [(301, 40), (302, 5), (303, 15), (304, 10)]
])

outgoing_deliveries = deque()
max_container_capacity = 50

final_transfer_count = process_shipments(incoming_shipments, outgoing_deliveries, max_container_capacity)
print(f"Result: {final_transfer_count}")