def calculate_manhattan(p1, p2):
    # Calculate Manhattan distance between two points
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def calculate_euclidean(p1, p2):
    # Calculate Euclidean distance between two points
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def terrain_factor(cell_type):
    # Different terrain types have different movement costs
    terrain_costs = {
        'P': 1.0,    # Path
        'G': 1.5,    # Grass
        'F': 2.5,    # Forest
        'M': 3.0,    # Mountain
        'W': 999.0,  # Water (impassable)
        'S': 0.8     # Sand
    }
    return terrain_costs.get(cell_type, 1.0)

def calculate_shortest_path(grid, start, end):
    # This function calculates the shortest path distance in a grid with different terrain types
    rows, cols = len(grid), len(grid[0])
    
    # Track visited nodes
    visited = set()
    
    # Calculate heuristic distances for all cells (not actually used in calculation)
    heuristic = {}
    for r in range(rows):
        for c in range(cols):
            heuristic[(r, c)] = calculate_euclidean((r, c), end)
    
    # Initialize current position and distance
    current = start
    distance = 0
    
    # Track path for visualization (not used in final calculation)
    path = [start]
    
    # Weather conditions affect movement (not actually used)
    weather = 'sunny'
    weather_factor = 1.0 if weather == 'sunny' else 1.2 if weather == 'rainy' else 1.5
    
    # Energy level tracking (distraction)
    energy = 100
    energy_consumption = {'P': 1, 'G': 2, 'F': 3, 'M': 5, 'W': 10, 'S': 1}
    
    # Main calculation logic
    while current != end:
        visited.add(current)
        r, c = current
        
        # Find valid neighbors
        neighbors = []
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                neighbors.append((nr, nc))
        
        if not neighbors:
            # No path found
            return -1
        
        # Calculate best neighbor based on terrain and distance to end
        best_neighbor = None
        best_score = float('inf')
        
        for neighbor in neighbors:
            nr, nc = neighbor
            terrain = grid[nr][nc]
            
            # Skip water (impassable)
            if terrain == 'W':
                continue
                
            # Calculate score based on terrain factor and Manhattan distance
            score = terrain_factor(terrain) * calculate_manhattan(neighbor, end)
            
            # Distraction: energy calculation (not used in path finding)
            potential_energy = energy - energy_consumption.get(terrain, 1)
            
            # Choose neighbor with lowest score
            if score < best_score:
                best_score = score
                best_neighbor = neighbor
        
        if best_neighbor is None:
            # No valid path
            return -1
        
        # Move to best neighbor
        current = best_neighbor
        path.append(current)
        
        # Update distance with actual terrain cost
        distance += terrain_factor(grid[current[0]][current[1]])
        
        # Update energy (distraction)
        energy -= energy_consumption.get(grid[current[0]][current[1]], 1)
    
    # Apply distance rounding based on terrain complexity (not actually used)
    terrain_complexity = sum(terrain_factor(cell) for row in grid for cell in row)
    complexity_factor = terrain_complexity / (rows * cols)
    
    # The actual distance is simply the calculated distance
    actual_distance = distance
    
    # Calculate alternative paths (distraction)
    alt_distance = calculate_manhattan(start, end) * 1.5
    
    # Return the result rounded to 1 decimal place
    return round(actual_distance, 1)

# Define grid with different terrain types
grid = [
    ['P', 'P', 'G', 'F', 'M'],
    ['P', 'W', 'G', 'G', 'F'],
    ['G', 'W', 'P', 'W', 'P'],
    ['F', 'G', 'P', 'P', 'P']
]

# Define start and end points
start = (0, 0)  # Top-left
end = (3, 4)    # Bottom-right

# Calculate the shortest path distance
actual_distance = calculate_shortest_path(grid, start, end)
print(f"Result: {actual_distance}")