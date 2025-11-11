import heapq
import re

def calculate_priority(weight, distance, urgency):
    return weight * 0.3 + distance * 0.2 + urgency * 0.5

def extract_numeric_value(code_str):
    match = re.search(r'\d+', code_str)
    return int(match.group()) if match else 0

def apply_filters(requests):
    filtered = []
    for req in requests:
        if req['weight'] > 10 and req['distance'] < 1000:
            filtered.append(req)
    return filtered

def update_weights(requests):
    for req in requests:
        code = req['code']
        numeric_part = extract_numeric_value(code)
        if numeric_part > 50:
            req['weight'] *= 1.1
    return requests

# Initial shipment requests data
shipment_requests = [
    {'id': 'PKG001', 'weight': 15, 'distance': 800, 'urgency': 7, 'code': 'EXPRESS55'},
    {'id': 'PKG002', 'weight': 8, 'distance': 1200, 'urgency': 5, 'code': 'STANDARD20'},
    {'id': 'PKG003', 'weight': 25, 'distance': 600, 'urgency': 9, 'code': 'PRIORITY75'},
    {'id': 'PKG004', 'weight': 12, 'distance': 950, 'urgency': 6, 'code': 'REGULAR40'},
    {'id': 'PKG005', 'weight': 30, 'distance': 400, 'urgency': 8, 'code': 'FAST60'}
]

# Calculate priorities and create max-heap (using negative values)
heap = []
for req in shipment_requests:
    priority = calculate_priority(req['weight'], req['distance'], req['urgency'])
    heapq.heappush(heap, (-priority, req))

# Apply filters to remove invalid requests
filtered_data = apply_filters([item[1] for item in heap])

# Update weights based on code values
updated_requests = update_weights(filtered_data)

# Rebuild heap with updated data
heap = []
for req in updated_requests:
    priority = calculate_priority(req['weight'], req['distance'], req['urgency'])
    heapq.heappush(heap, (-priority, req))

# Process the first 3 highest priority requests
for _ in range(min(3, len(heap))):
    heapq.heappop(heap)

# Calculate total weight of remaining packages
remaining_weight_total = sum(item[1]['weight'] for item in heap)

print(f"Result: {remaining_weight_total}")