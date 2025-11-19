from collections import deque
from math import gcd

delivery_stack = []
completed_queue = deque()
priority_scores = []

# Delivery coordinates represented as tuples (x, y)
delivery_coords = [(12, 18), (15, 25), (21, 28), (35, 49)]

for coord in delivery_coords:
    delivery_stack.append(coord)

while delivery_stack:
    x, y = delivery_stack.pop()
    score = gcd(x, y)
    priority_scores.append(score)
    completed_queue.append((x, y))

final_priority_score = sum(priority_scores) * len(completed_queue)
print(f'Result: {final_priority_score}')