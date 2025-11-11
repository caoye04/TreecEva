import heapq
from itertools import permutations
from dataclasses import dataclass
from typing import List, Tuple

def optimize_truck_loading(truck_capacity: int, packages: List[Tuple[int, int]]) -> int:
    # packages: list of (weight, priority)
    # Sort packages by priority-to-weight ratio (greedy approach)
    packages_sorted = sorted(packages, key=lambda x: x[1]/x[0] if x[0] > 0 else float('inf'), reverse=True)
    
    loaded_weight = 0
    total_priority = 0
    loaded_packages = []
    
    for weight, priority in packages_sorted:
        if loaded_weight + weight <= truck_capacity:
            loaded_weight += weight
            total_priority += priority
            loaded_packages.append((weight, priority))
    
    # Analyze permutations of top 3 priority packages for optimal arrangement
    top_packages = sorted(packages, key=lambda x: x[1], reverse=True)[:3]
    perm_priority_max = 0
    
    for perm in permutations(top_packages):
        perm_weight = sum(p[0] for p in perm)
        if perm_weight <= truck_capacity:
            perm_priority = sum(p[1] for p in perm)
            perm_priority_max = max(perm_priority_max, perm_priority)
    
    # Maintain a min-heap of package priorities for dynamic adjustment
    priority_heap = [priority for _, priority in packages]
    heapq.heapify(priority_heap)
    
    # Remove lowest priorities until we have top 50%
    while len(priority_heap) > len(packages) // 2:
        heapq.heappop(priority_heap)
    
    heap_adjustment = sum(priority_heap)
    
    # Final optimization score
    optimal_priority = total_priority + perm_priority_max + heap_adjustment
    return optimal_priority

# Package data: (weight, priority)
shipment_manifest = [
    (15, 40), (10, 35), (20, 50), (5, 20), (25, 60),
    (12, 30), (18, 45), (8, 25), (22, 55), (30, 70),
    (7, 15), (14, 33), (16, 38), (9, 28), (27, 65)
]

capacity_limit = 100

# Execute optimization
optimal_priority = optimize_truck_loading(capacity_limit, shipment_manifest)
print(f"Result: {optimal_priority}")