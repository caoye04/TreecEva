import math
from collections import deque

def calculate_priority_score(weight, priority):
    base_score = weight * priority
    adjustment = int(math.sin(base_score) * 100) & 0xFF
    return base_score ^ adjustment

def load_trucks():
    max_capacity = 1000
    package_queue = deque([(120, 3), (200, 2), (150, 5), (300, 1), (100, 4)])
    package_stack = []
    loading_score = 0
    
    # Reverse queue into stack
    while package_queue:
        package_stack.append(package_queue.popleft())
    
    # Greedy loading from stack
    current_load = 0
    while package_stack:
        weight, priority = package_stack.pop()
        if current_load + weight <= max_capacity:
            current_load += weight
            loading_score += calculate_priority_score(weight, priority)
    
    return loading_score

final_loading_score = load_trucks()
print(f"Result: {final_loading_score}")