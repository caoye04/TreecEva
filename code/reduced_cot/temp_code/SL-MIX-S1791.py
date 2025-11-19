import heapq
from dataclasses import dataclass
from typing import List, Tuple

def process_packages():
    # Initialize heap with package IDs and urgency scores
    packages_heap: List[Tuple[int, int]] = []
    
    # Package data: (package_id, urgency_score)
    initial_packages = [(101, 256), (102, 143), (103, 872), (104, 905), (105, 334)]
    
    # Push packages into heap using urgency score mod 100 as priority
    for pkg_id, urgency in initial_packages:
        heapq.heappush(packages_heap, (urgency % 100, pkg_id))
    
    # Process packages
    processed_count = 0
    total_mod_sum = 0
    
    while packages_heap and processed_count < 3:
        priority, pkg_id = heapq.heappop(packages_heap)
        
        # Apply modular arithmetic to adjust priority
        adjusted_priority = (priority * 3 + 7) % 23
        
        # Use ternary-like operation to determine if package gets expedited
        expedited = 1 if adjusted_priority < 10 else 0
        
        # Update counters
        total_mod_sum += adjusted_priority
        processed_count += expedited
    
    # Calculate final priority score using remaining heap elements
    remaining_priorities = [p[0] for p in packages_heap]
    final_priority_score = total_mod_sum
    
    # Adjust final score with a ternary operation based on remaining packages
    final_priority_score = final_priority_score + (5 if len(remaining_priorities) > 1 else 0)
    
    return final_priority_score

# Execute the function and capture result
final_priority_score = process_packages()
print(f"Result: {final_priority_score}")