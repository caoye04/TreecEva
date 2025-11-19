import heapq
import math

# Delivery request data: (warehouse_x, warehouse_y, dest_x, dest_y, weight, time_factor, request_id)
delivery_requests = [
    (3, 7, 12, 2, 4.5, 1.3, 'REQ001'),
    (8, 1, 15, 9, 2.2, 1.7, 'REQ002'),
    (5, 5, 0, 10, 6.1, 1.1, 'REQ003'),
    (10, 4, 2, 8, 3.8, 1.5, 'REQ004'),
    (1, 9, 11, 3, 5.0, 1.4, 'REQ005')
]

# Hash table to store request_id to priority mappings for tie-breaking
request_hash = {req[6]: hash(req[6]) % 1000 for req in delivery_requests}

# Max-heap implementation using negative values
max_heap = []

for req in delivery_requests:
    wx, wy, dx, dy, weight, time_factor, req_id = req
    # Calculate Manhattan distance
    manhattan_dist = abs(wx - dx) + abs(wy - dy)
    # Calculate base priority
    base_priority = (manhattan_dist * weight) / time_factor
    # Apply modular adjustment for normalization
    mod_adjustment = (request_hash[req_id] % 7) if request_hash[req_id] % 2 == 0 else -(request_hash[req_id] % 5)
    # Final priority with adjustment
    final_priority = base_priority + mod_adjustment
    # Push negative value for max-heap simulation
    heapq.heappush(max_heap, (-final_priority, req_id))

# Process the heap to find the highest priority request
highest_priority_value, top_request_id = heapq.heappop(max_heap)

# Apply short-circuit evaluation and ternary operator for final score calculation
is_high_weight = lambda w: w > 4.0
weight_bonus = 10.0 if is_high_weight(next(req[4] for req in delivery_requests if req[6] == top_request_id)) else 0.0

# Short-circuit: only apply bonus if priority is above threshold
final_priority_score = -highest_priority_value + (weight_bonus if -highest_priority_value > 30.0 else 0.0)

print(f"Result: {round(final_priority_score, 2)}")