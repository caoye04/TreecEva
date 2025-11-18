class ShipmentTracker:
    def __init__(self):
        self.incoming_stack = []
        self.outgoing_queue = []
    
    def receive_shipment(self, item_id, base_score):
        # Calculate priority with modular arithmetic
        priority = (base_score * 3 + 7) % 13
        self.incoming_stack.append((item_id, priority))
    
    def dispatch_shipment(self):
        if self.incoming_stack:
            item = self.incoming_stack.pop()
            self.outgoing_queue.append(item)
    
    def process_dispatches(self, count):
        processed = []
        for _ in range(min(count, len(self.outgoing_queue))):
            if self.outgoing_queue:
                processed.append(self.outgoing_queue.pop(0))
        return processed

# Initialize tracker
logistics = ShipmentTracker()

# Receive shipments with base scores
shipments_data = [(101, 5), (102, 12), (103, 8), (104, 15)]
for item_id, base_score in shipments_data:
    logistics.receive_shipment(item_id, base_score)

# Dispatch two shipments to outgoing queue
logistics.dispatch_shipment()
logistics.dispatch_shipment()

# Process one dispatched shipment
processed_items = logistics.process_dispatches(1)

# Calculate final priority score from remaining items
remaining_priorities = [priority for _, priority in logistics.incoming_stack] + \
                      [priority for _, priority in logistics.outgoing_queue]

final_priority_score = sum(remaining_priorities) % 17

print(f'Result: {final_priority_score}')