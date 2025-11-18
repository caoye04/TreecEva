from collections import deque

class ShipmentNode:
    def __init__(self, batch_id, quantity):
        self.batch_id = batch_id
        self.quantity = quantity
        self.next = None

class WarehouseTracker:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_shipment(self, batch_id, quantity):
        new_node = ShipmentNode(batch_id, quantity)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def process_inventory(self):
        # Initialize data structures
        incoming_queue = deque()
        outgoing_stack = []
        window_dp = [0] * 100
        
        # Populate queue with positive quantities (incoming shipments)
        current = self.head
        while current:
            if current.quantity > 0:
                incoming_queue.append(current.quantity)
            current = current.next
        
        # Populate stack with negative quantities (outgoing orders)
        current = self.head
        while current:
            if current.quantity < 0:
                outgoing_stack.append(current.quantity)
            current = current.next
        
        # Process shipments using dynamic programming with sliding window
        window_size = 5
        max_cumulative = float('-inf')
        
        # Process incoming shipments
        for i in range(len(incoming_queue)):
            if i == 0:
                window_dp[i] = incoming_queue[i]
            else:
                window_dp[i] = window_dp[i-1] + incoming_queue[i]
            
            # Update max in sliding window
            if i >= window_size:
                window_sum = window_dp[i] - window_dp[i-window_size]
                max_cumulative = max(max_cumulative, window_sum)
            else:
                max_cumulative = max(max_cumulative, window_dp[i])
        
        # Process outgoing orders
        for i in range(len(outgoing_stack)):
            idx = len(incoming_queue) + i
            window_dp[idx] = window_dp[idx-1] + outgoing_stack[i]
            max_cumulative = max(max_cumulative, window_dp[idx])
        
        return max_cumulative

# Initialize warehouse tracker
warehouse = WarehouseTracker()

# Add shipment batches
shipments_data = [
    (1001, 50),
    (1002, -20),
    (1003, 75),
    (1004, 30),
    (1005, -10),
    (1006, -15),
    (1007, 40),
    (1008, 25),
    (1009, -5),
    (1010, -30)
]

for batch_id, quantity in shipments_data:
    warehouse.add_shipment(batch_id, quantity)

# Process inventory and calculate peak value
peak_inventory_value = warehouse.process_inventory()
print(f"Result: {peak_inventory_value}")