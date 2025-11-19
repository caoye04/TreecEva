from collections import defaultdict

def count_non_adjacent_benches(positions):
    # Convert list of positions to a set for O(1) lookup
    position_set = set(positions)
    visited = set()
    max_count = 0
    
    # Sort positions to process them in order
    for x, y in sorted(positions):
        if (x, y) in visited:
            continue
            
        # Greedy selection: take the current position
        max_count += 1
        visited.add((x, y))
        
        # Mark adjacent positions as visited to avoid placing benches there
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            adj_pos = (x + dx, y + dy)
            if adj_pos in position_set:
                visited.add(adj_pos)
    
    return max_count

# Candidate bench positions
bench_positions = [
    (0, 0), (0, 1), (1, 0), (1, 1),
    (2, 2), (2, 3), (3, 2), (3, 3),
    (4, 4)
]

# Compute the maximum number of non-adjacent benches
max_benches = count_non_adjacent_benches(bench_positions)
print(f"Result: {max_benches}")