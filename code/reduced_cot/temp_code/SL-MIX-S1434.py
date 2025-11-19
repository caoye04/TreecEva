import math
from collections import deque

def calculate_priority(weight, volume, category):
    base_score = (weight << 2) & (volume >> 1)
    category_modifier = {
        'A': lambda x: x | 0xF,
        'B': lambda x: x ^ 0xFF,
        'C': lambda x: x & 0xF0
    }
    return category_modifier[category](base_score)

# Initialize data structures
incoming_shipments = []  # Stack (LIFO)
outgoing_orders = deque()  # Queue (FIFO)

# Populate shipments and orders
shipments_data = [
    {'weight': 12, 'volume': 32, 'category': 'A'},
    {'weight': 8, 'volume': 16, 'category': 'B'},
    {'weight': 20, 'volume': 48, 'category': 'C'}
]

orders_data = [
    {'priority': 5, 'quantity': 3},
    {'priority': 3, 'quantity': 7},
    {'priority': 8, 'quantity': 2}
]

for shipment in shipments_data:
    priority = calculate_priority(shipment['weight'], shipment['volume'], shipment['category'])
    incoming_shipments.append(priority)
    
for order in orders_data:
    outgoing_orders.append(order['priority'] * order['quantity'])

# Process inventory movements
processed_priorities = []
while incoming_shipments and outgoing_orders:
    shipment_priority = incoming_shipments.pop()  # Stack pop
    order_priority = outgoing_orders.popleft()    # Queue dequeue
    
    # Apply logical conditions to determine if shipment can fulfill order
    if (shipment_priority > 20) and not (order_priority < 10):
        adjusted_priority = shipment_priority - order_priority
    elif (shipment_priority <= 20) or (order_priority >= 30):
        adjusted_priority = shipment_priority + order_priority
    else:
        adjusted_priority = shipment_priority * order_priority
    
    processed_priorities.append(adjusted_priority)

# Calculate final score using dictionary comprehension and merging
priority_weights = {i: math.log(i+1) for i in processed_priorities if i > 0}
bonus_scores = {i: math.sqrt(i) for i in processed_priorities if i <= 0}
combined_scores = {**priority_weights, **bonus_scores}

final_priority_score = sum(int(k * v) for k, v in combined_scores.items())
print(f"Result: {final_priority_score}")