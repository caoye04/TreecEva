import heapq

def adjust_weights(current_weight, target_weight, depth=3):
    if depth == 0:
        return current_weight
    delta = (target_weight - current_weight) * 0.5
    new_weight = current_weight + delta
    return adjust_weights(new_weight, target_weight, depth - 1)

transactions = [
    (100, 120),
    (80, 90),
    (150, 140),
    (200, 180)
]

priority_heap = []
for curr, targ in transactions:
    adjusted = adjust_weights(curr, targ)
    priority = abs(targ - adjusted)
    heapq.heappush(priority_heap, (priority, adjusted))

final_balance = priority_heap[0][1] if priority_heap else 0
print(f"Result: {final_balance}")