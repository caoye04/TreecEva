import collections
import math

# Shipment data: (volume, weight, type)
shipments = [(120, 45, 'standard'), (80, 30, 'express'), (200, 60, 'bulk'), (95, 25, 'standard')]
incoming_stack = []
outgoing_queue = collections.deque()
priority_scores = {}
discount_map = {'standard': 0.9, 'express': 1.1, 'bulk': 0.8}

# Process shipments
for vol, wt, typ in shipments:
    priority = math.ceil((vol * 0.3 + wt * 0.7) * discount_map[typ])
    priority_scores[(vol, wt, typ)] = priority
    if typ == 'bulk':
        outgoing_queue.append(priority)
    else:
        incoming_stack.append(priority)

# Calculate clearance metrics
stack_sum = sum(incoming_stack)
queue_max = max(outgoing_queue) if outgoing_queue else 0
size_diff = len(incoming_stack) - len(outgoing_queue)

# Apply conditional adjustments
if size_diff > 0:
    adjustment_factor = min(5, abs(size_diff))
else:
    adjustment_factor = max(-5, size_diff)

# Compute final clearance score
final_clearance_score = (stack_sum + queue_max) ^ (adjustment_factor & 0xF)
print(f'Result: {final_clearance_score}')