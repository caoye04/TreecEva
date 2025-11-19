from collections import deque

class Shipment:
    def __init__(self, item_count, weight):
        self.item_count = item_count
        self.weight = weight
    
    def priority_score(self):
        return self.item_count * 10 + self.weight * 2

incoming_stack = []
outgoing_queue = deque()
total_discount_accumulator = 0

# Batch 1
batch1 = [Shipment(5, 20), Shipment(3, 15)]
for shipment in batch1:
    incoming_stack.append(shipment)

while incoming_stack:
    current_shipment = incoming_stack.pop()
    score = current_shipment.priority_score()
    volume = current_shipment.item_count * current_shipment.weight
    discount = (volume > 50) and (score > 50) and (volume // 10) or 0
    total_discount_accumulator += discount
    outgoing_queue.append(current_shipment)

# Batch 2
batch2 = [Shipment(2, 30), Shipment(4, 10)]
for shipment in batch2:
    incoming_stack.append(shipment)

while incoming_stack:
    current_shipment = incoming_stack.pop()
    score = current_shipment.priority_score()
    volume = current_shipment.item_count * current_shipment.weight
    discount = (lambda s, v: v // 5 if s > 40 else 0)(score, volume)
    total_discount_accumulator += discount
    outgoing_queue.append(current_shipment)

# Batch 3
batch3 = [Shipment(6, 25)]
for shipment in batch3:
    incoming_stack.append(shipment)

while incoming_stack:
    current_shipment = incoming_stack.pop()
    score = current_shipment.priority_score()
    volume = current_shipment.item_count * current_shipment.weight
    discount = 10 if score >= 100 else (5 if score >= 50 else 0)
    total_discount_accumulator += discount
    outgoing_queue.append(current_shipment)

# Batch 4
batch4 = [Shipment(1, 40), Shipment(7, 12)]
for shipment in batch4:
    incoming_stack.append(shipment)

while incoming_stack:
    current_shipment = incoming_stack.pop()
    score = current_shipment.priority_score()
    volume = current_shipment.item_count * current_shipment.weight
    # Apply ternary operator with nested conditions
    discount = 15 if volume > 45 else (7 if score > 30 else 0)
    total_discount_accumulator += discount
    outgoing_queue.append(current_shipment)

print(f"Result: {total_discount_accumulator}")