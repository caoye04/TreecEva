from collections import deque

class ContainerStack:
    def __init__(self, max_capacity):
        self.containers = []
        self.max_capacity = max_capacity
    
    def can_add(self, container_id):
        return len(self.containers) < self.max_capacity
    
    def add_container(self, container_id):
        if self.can_add(container_id):
            self.containers.append(container_id)
    
    def get_top_container(self):
        return self.containers[-1] if self.containers else 0

def process_shipment(container_ids, stack_capacity):
    stack_queue = deque()  # Queue of stacks
    
    for cid in container_ids:
        placed = False
        # Try to place in existing stacks (greedy approach)
        for stack in stack_queue:
            if stack.can_add(cid):
                stack.add_container(cid)
                placed = True
                break
        
        # If not placed, create new stack
        if not placed:
            new_stack = ContainerStack(stack_capacity)
            new_stack.add_container(cid)
            stack_queue.append(new_stack)
    
    # Calculate security checksum
    checksum = 0
    for stack in stack_queue:
        checksum ^= stack.get_top_container()
    
    return checksum

# Shipment details
shipment_containers = [101, 203, 150, 99, 205, 80, 300, 120, 175, 220]
max_stack_capacity = 3

# Process shipment and calculate checksum
security_checksum = process_shipment(shipment_containers, max_stack_capacity)
print(f"Result: {security_checksum}")