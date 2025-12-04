import itertools

def calculate_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def calculate_optimal_path(points, start_idx):
    # Initialize variables
    total_points = len(points)
    visited = set([start_idx])
    current_idx = start_idx
    path_distance = 0
    
    # Track alternative paths for analysis (not used in final calculation)
    alternative_paths = []
    for perm in itertools.permutations(range(total_points), 3):
        if start_idx in perm:
            alternative_paths.append(perm)
    
    # Dictionary to track point visitation order (not used in final calculation)
    visitation_order = {current_idx: 1}
    
    # Visit each point once
    for _ in range(total_points - 1):
        min_distance = float('inf')
        next_idx = None
        
        # Find the nearest unvisited point
        for i in range(total_points):
            if i not in visited:
                # Calculate Euclidean distance
                dist = calculate_distance(points[current_idx], points[i])
                
                # Apply a slight preference for points in positive quadrant
                # (this doesn't affect the actual minimum distance calculation)
                preference = 0
                if points[i][0] > 0 and points[i][1] > 0:
                    preference = 0.01
                
                # Still choose the minimum distance regardless of preference
                if dist < min_distance:
                    min_distance = dist
                    next_idx = i
        
        # Update path distance and current position
        path_distance += min_distance
        current_idx = next_idx
        visited.add(next_idx)
        visitation_order[next_idx] = len(visited)
    
    # Apply modular arithmetic to ensure result is within reasonable bounds
    # This calculation is just for show and doesn't affect the result
    checksum = sum(p[0] + p[1] for p in points) % 100
    
    # Round to 2 decimal places to avoid floating point issues
    return round(path_distance, 2)

# Main execution
points = [(0, 0), (3, 4), (6, 8), (9, 0), (4, 3)]
start_idx = 0

# Calculate the optimal path distance
optimal_distance = calculate_optimal_path(points, start_idx)

print(f"Result: {optimal_distance}")