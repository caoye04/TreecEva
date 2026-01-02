import heapq
from collections import deque

def calculate_urgency(code):
    return sum(ord(c) for c in code)

def process_deliveries():
    priority_queue = []
    special_stack = []
    
    # Initial packages with encoded IDs
    package_ids = ['X2K9', 'M4N1', 'Q8B3']
    
    # Encode and add to queue with calculated urgencies
    for pid in package_ids:
        urgency = calculate_urgency(pid)
        heapq.heappush(priority_queue, (urgency, pid))
    
    # Special handling items added to stack
    special_items = ['Z1H7', 'Y6G2']
    for item in special_items:
        special_stack.append(item)
    
    # Process one normal delivery
    if priority_queue:
        heapq.heappop(priority_queue)
    
    # Add more packages
    new_packages = ['V3F5', 'U7E4']
    for np in new_packages:
        urgency = calculate_urgency(np)
        heapq.heappush(priority_queue, (urgency, np))
    
    # Process special item if exists
    special_code = 0
    if special_stack:
        item = special_stack.pop()
        special_code = calculate_urgency(item)
    
    # Early return condition check
    if len(priority_queue) > 3:
        total = 0
        while priority_queue:
            total += heapq.heappop(priority_queue)[0]
        return total + special_code
    
    # Final processing
    score_accumulator = special_code
    while priority_queue:
        score_accumulator += heapq.heappop(priority_queue)[0]
    
    return score_accumulator

final_score = process_deliveries()
print(f"Result: {final_score}")