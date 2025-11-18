import heapq
from collections import deque

def process_packages(priority_queue, overflow_stack):
    if not priority_queue and not overflow_stack:
        return 0
    
    delivery_count = 0
    
    # Process from priority queue
    while priority_queue:
        priority = heapq.heappop(priority_queue)
        delivery_count += 1 if priority > 10 else 0
    
    # Process from stack with ternary decision
    while overflow_stack:
        item = overflow_stack.pop()
        delivery_count += 1 if item % 2 == 0 else 0
    
    return delivery_count

def distribute_packages(package_list):
    priority_queue = []
    overflow_stack = []
    
    for pkg in package_list:
        # Ternary operator for routing
        (heapq.heappush(priority_queue, pkg) if pkg > 5 else overflow_stack.append(pkg))
    
    # Recursive processing with backtracking
    attempt1 = process_packages(priority_queue[:], overflow_stack[:])
    attempt2 = process_packages(priority_queue[::-1], overflow_stack[::-1]) if priority_queue else 0
    
    # Divide and conquer approach for final count
    final_count = (attempt1 + attempt2) // 2 if attempt1 != attempt2 else attempt1
    return final_count

# Initialize package priorities
packages = [3, 7, 12, 15, 8, 2, 9, 14]
final_delivery_count = distribute_packages(packages)
print(f'Result: {final_delivery_count}')