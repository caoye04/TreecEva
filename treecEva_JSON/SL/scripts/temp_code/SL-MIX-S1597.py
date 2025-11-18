import collections

def calculate_priority_score(delivery_id, time_factor):
    base_score = (delivery_id << 2) | (time_factor & 0b1111)
    adjusted_score = base_score ^ (delivery_id >> 1)
    return adjusted_score

delivery_stack = [15, 23, 8, 42, 31]
delivery_queue = collections.deque([7, 19, 3, 28])
processed_deliveries = []

while delivery_stack:
    current_delivery = delivery_stack.pop()
    if current_delivery % 2 == 0:
        delivery_queue.appendleft(current_delivery)
    else:
        processed_deliveries.append(current_delivery)
        
    if len(processed_deliveries) >= 3:
        break

priority_scores = set()
while delivery_queue and len(priority_scores) < 4:
    queued_delivery = delivery_queue.popleft()
    score = calculate_priority_score(queued_delivery, 5)
    if score > 50:
        priority_scores.add(score)

frozen_scores = frozenset(priority_scores)
final_priority_score = sum(frozen_scores) & 0xFF

print(f"Result: {final_priority_score}")