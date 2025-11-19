from collections import deque
import itertools

def calculate_priority_score(categories):
    return sum(hash(cat) % 100 for cat in categories)

# Initialize data structures
incoming_shipments = []  # Stack (LIFO)
outgoing_orders = deque()  # Queue (FIFO)

# Define shipment data
shipments_data = [
    {'id': 'SH001', 'categories': ['electronics', 'fragile']},
    {'id': 'SH002', 'categories': ['clothing', 'standard']},
    {'id': 'SH003', 'categories': ['books', 'media']}
]

orders_data = [
    {'id': 'ORD001', 'items': 2},
    {'id': 'ORD002', 'items': 1}
]

# Process incoming shipments (push to stack)
for shipment in shipments_data:
    priority = calculate_priority_score(shipment['categories'])
    incoming_shipments.append({
        'id': shipment['id'],
        'priority': priority,
        'categories': shipment['categories']
    })

# Process outgoing orders (enqueue to queue)
for order in orders_data:
    outgoing_orders.append({
        'id': order['id'],
        'items': order['items']
    })

# Warehouse processing logic
processed_priorities = []

# Handle first outgoing order
if outgoing_orders:
    order = outgoing_orders.popleft()
    if incoming_shipments:
        shipment = incoming_shipments.pop()
        adjusted_priority = shipment['priority'] * order['items']
        processed_priorities.append(adjusted_priority)

# Handle second outgoing order
if outgoing_orders:
    order = outgoing_orders.popleft()
    # Duplicate remaining shipments for processing
    remaining_shipments = [dict(s) for s in incoming_shipments]
    for shipment in remaining_shipments:
        adjusted_priority = shipment['priority'] // order['items']
        processed_priorities.append(adjusted_priority)

# Calculate final metrics using itertools
final_priority_score = 0
if processed_priorities:
    # Get all pairwise differences
    differences = [abs(a - b) for a, b in itertools.combinations(processed_priorities, 2)]
    # Sum all differences and normalize
    total_difference = sum(differences)
    count_operations = len(processed_priorities) + len(differences)
    final_priority_score = total_difference % (count_operations + 1)

print(f"Result: {final_priority_score}")