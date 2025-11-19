from collections import deque
import heapq

def prepare_ingredients():
    ingredients = [
        {'name': 'saffron', 'priority': 3, 'prep_time': 5},
        {'name': 'truffle', 'priority': 1, 'prep_time': 10},
        {'name': 'lobster', 'priority': 2, 'prep_time': 7},
        {'name': 'caviar', 'priority': 4, 'prep_time': 3}
    ]
    
    # Priority queue for ingredients (min-heap based on priority)
    priority_queue = []
    for ingredient in ingredients:
        heapq.heappush(priority_queue, (ingredient['priority'], ingredient['prep_time'], ingredient['name']))
    
    # Stack for preparation steps
    prep_stack = deque()
    
    # Process ingredients
    total_time = 0
    while priority_queue:
        priority, prep_time, name = heapq.heappop(priority_queue)
        total_time += prep_time
        prep_stack.append((name, total_time))
    
    # Calculate final score based on preparation efficiency
    final_score = 0
    step_count = 0
    while prep_stack:
        name, time = prep_stack.pop()
        step_count += 1
        if step_count % 2 == 0:
            final_score += time * 2
        else:
            final_score -= time
    
    return final_score

final_score = prepare_ingredients()
print(f"Result: {final_score}")