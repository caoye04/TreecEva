import heapq
from functools import reduce

def calculate_priority(distance, urgency):
    return distance * 2 + urgency * 3

class DeliveryRequest:
    def __init__(self, id, distance, urgency):
        self.id = id
        self.distance = distance
        self.urgency = urgency
        self.priority = calculate_priority(distance, urgency)
    
    def update_urgency(self, new_urgency):
        self.urgency = new_urgency
        self.priority = calculate_priority(self.distance, new_urgency)

# Initialize priority queue with negative values for max-heap behavior
priority_queue = []

# Create initial delivery requests
requests = [
    DeliveryRequest('DL001', 10, 5),
    DeliveryRequest('DL002', 15, 3),
    DeliveryRequest('DL003', 8, 7),
    DeliveryRequest('DL004', 12, 4)
]

# Add requests to priority queue
for req in requests:
    heapq.heappush(priority_queue, (-req.priority, req.id, req))

# Add new request
new_request = DeliveryRequest('DL005', 20, 2)
heapq.heappush(priority_queue, (-new_request.priority, new_request.id, new_request))

# Update urgency of DL003
for i in range(len(priority_queue)):
    if priority_queue[i][1] == 'DL003':
        priority_queue[i][2].update_urgency(9)
        # Re-heapify after update
        heapq.heapify(priority_queue)
        break

# Remove two highest priority items
if priority_queue:
    heapq.heappop(priority_queue)
if priority_queue:
    heapq.heappop(priority_queue)

# Add another request
extra_request = DeliveryRequest('DL006', 5, 8)
heapq.heappush(priority_queue, (-extra_request.priority, extra_request.id, extra_request))

# Check if any request has both distance > 10 AND urgency > 5
high_priority_exists = any(req.distance > 10 and req.urgency > 5 for _, _, req in priority_queue)

# Calculate final priority score
final_score = 0
if priority_queue and high_priority_exists:
    highest_priority_request = priority_queue[0][2]
    final_score = highest_priority_request.priority
elif priority_queue:
    # If no high priority exists, use a complex calculation
    priorities = [req.priority for _, _, req in priority_queue]
    final_score = reduce(lambda x, y: x | y, [p << 1 for p in priorities], 0) & 0xFF

print(f"Result: {final_score}")