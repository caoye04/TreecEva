from collections import defaultdict, Counter
from itertools import permutations

def calculate_route_diversity(route_string):
    diversity_counter = 0
    segment_hashes = set()
    
    # Process each 3-character segment
    for i in range(len(route_string) - 2):
        segment = route_string[i:i+3]
        # Generate all unique permutations of the segment
        perms = set(permutations(segment))
        # Hash each permutation and add to our tracking
        for perm in perms:
            perm_hash = hash(''.join(perm))
            if perm_hash not in segment_hashes:
                segment_hashes.add(perm_hash)
                diversity_counter += 1
    return diversity_counter

route = "XYZABCXYZ"
diversity_counter = calculate_route_diversity(route)
print(f"Result: {diversity_counter}")