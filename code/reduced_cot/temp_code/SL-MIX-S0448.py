from collections import deque

class PriorityProcessor:
    def __init__(self):
        self.memo = {}
    
    def compute_priority(self, weight, urgency):
        if (weight, urgency) in self.memo:
            return self.memo[(weight, urgency)]
        if weight <= 1 or urgency <= 1:
            result = weight | urgency
        else:
            result = (self.compute_priority(weight >> 1, urgency) ^ self.compute_priority(weight, urgency >> 1)) & 0xFF
        self.memo[(weight, urgency)] = result
        return result

def process_warehouse_operations():
    shipment_stack = []
    delivery_queue = deque()
    processor = PriorityProcessor()
    
    # Incoming shipments (weight, urgency)
    shipments = [(12, 5), (7, 3), (9, 6), (4, 2)]
    
    # Process incoming shipments
    for weight, urgency in shipments:
        priority = processor.compute_priority(weight, urgency)
        shipment_stack.append(priority)
    
    # Move to delivery queue with modified priorities
    while shipment_stack:
        priority = shipment_stack.pop()
        adjusted_priority = priority if priority & 0x80 == 0 else (priority & 0x7F) | ((priority & 0x80) >> 1)
        delivery_queue.append(adjusted_priority)
    
    # Calculate final score using greedy approach
    final_priority_score = 0
    mask = 0xF0
    
    while delivery_queue:
        current = delivery_queue.popleft()
        if (current & mask) != 0 and (final_priority_score & mask) == 0:
            final_priority_score |= current
        elif (current | final_priority_score) > final_priority_score:
            final_priority_score ^= current
    
    return final_priority_score

final_priority_score = process_warehouse_operations()
print(f"Result: {final_priority_score}")