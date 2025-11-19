class ShipmentNode:
    def __init__(self, batch_id, weight):
        self.batch_id = batch_id
        self.weight = weight
        self.next = None

class WarehouseSystem:
    def __init__(self):
        self.head = None
        self.inventory_queue = []
        self.order_stack = []
    
    def add_shipment_to_list(self, batch_id, weight):
        new_node = ShipmentNode(batch_id, weight)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def enqueue_shipment(self, batch_id, weight):
        self.inventory_queue.append((batch_id, weight))
    
    def push_order(self, batch_id):
        self.order_stack.append(batch_id)
    
    def process_inventory(self):
        # Process queue (FIFO)
        while self.inventory_queue:
            batch_id, weight = self.inventory_queue.pop(0)
            self.add_shipment_to_list(batch_id, weight)
    
    def fulfill_orders(self):
        # Process stack (LIFO)
        fulfilled_batches = set()
        while self.order_stack:
            batch_id = self.order_stack.pop()
            fulfilled_batches.add(batch_id)
        
        # Remove fulfilled batches from linked list
        dummy = ShipmentNode(0, 0)
        dummy.next = self.head
        prev = dummy
        current = self.head
        
        while current:
            if current.batch_id in fulfilled_batches:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        self.head = dummy.next
    
    def reconcile_inventory(self, min_weight, max_weight):
        # Collect all remaining batches
        batches = []
        current = self.head
        while current:
            batches.append((current.batch_id, current.weight))
            current = current.next
        
        # Sort by weight using bubble sort
        n = len(batches)
        for i in range(n):
            for j in range(0, n-i-1):
                if batches[j][1] > batches[j+1][1]:
                    batches[j], batches[j+1] = batches[j+1], batches[j]
        
        # Binary search for first batch with weight >= min_weight
        left, right = 0, len(batches) - 1
        start_idx = len(batches)
        while left <= right:
            mid = (left + right) // 2
            if batches[mid][1] >= min_weight:
                start_idx = mid
                right = mid - 1
            else:
                left = mid + 1
        
        # Find last batch with weight <= max_weight
        left, right = 0, len(batches) - 1
        end_idx = -1
        while left <= right:
            mid = (left + right) // 2
            if batches[mid][1] <= max_weight:
                end_idx = mid
                left = mid + 1
            else:
                right = mid - 1
        
        # Return the batch_id of the middle batch in range
        if start_idx <= end_idx:
            mid_range_idx = (start_idx + end_idx) // 2
            return batches[mid_range_idx][0]
        return -1

# Initialize system
warehouse = WarehouseSystem()

# Add initial inventory
initial_shipments = [(101, 45.2), (102, 32.7), (103, 68.9), (104, 28.1), (105, 55.3)]
for batch_id, weight in initial_shipments:
    warehouse.add_shipment_to_list(batch_id, weight)

# Queue new shipments
new_shipments = [(106, 41.8), (107, 72.4), (108, 39.6)]
for batch_id, weight in new_shipments:
    warehouse.enqueue_shipment(batch_id, weight)

# Stack orders
outgoing_orders = [102, 104]
for batch_id in outgoing_orders:
    warehouse.push_order(batch_id)

# Process inventory and fulfill orders
warehouse.process_inventory()
warehouse.fulfill_orders()

# Reconcile inventory for weight range 40.0 to 60.0
target_batch_id = warehouse.reconcile_inventory(40.0, 60.0)
print(f"Result: {target_batch_id}")