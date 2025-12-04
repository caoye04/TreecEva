def is_valid_position(x, y, size, obstacles):
    # Check if position is within bounds and not an obstacle
    if 0 <= x < size and 0 <= y < size and (x, y) not in obstacles:
        return True
    return False

def calculate_valid_paths(size, obstacles):
    # Create a cache for memoization
    cache = {}
    
    def path_finder(x, y):
        # Base case: reached destination
        if x == size - 1 and y == size - 1:
            return 1
            
        # Check if result is already cached
        if (x, y) in cache:
            return cache[(x, y)]
        
        # Initialize paths counter
        paths = 0
        
        # Try moving right
        if is_valid_position(x + 1, y, size, obstacles):
            paths += path_finder(x + 1, y)
            
        # Try moving down
        if is_valid_position(x, y + 1, size, obstacles):
            paths += path_finder(x, y + 1)
            
        # Store result in cache
        cache[(x, y)] = paths
        return paths
    
    # Start from top-left corner
    return path_finder(0, 0)

# Grid size for the path finding problem
grid_size = 4

# Weather conditions affecting path visibility (unused data)
weather_conditions = {
    'sunny': 0.9,
    'cloudy': 0.7,
    'rainy': 0.5,
    'foggy': 0.3
}

# Calculate average visibility (distraction)
avg_visibility = sum(weather_conditions.values()) / len(weather_conditions)

# Define obstacle positions on the grid
obstacles = {(1, 2), (2, 1), (3, 0)}

# Alternative path calculation (distraction)
def alternative_path_counter(grid_dim):
    # This function calculates total possible paths without obstacles
    # Using combinatorial formula (not used in final answer)
    import math
    return math.comb(2 * (grid_dim - 1), grid_dim - 1)

potential_paths = alternative_path_counter(grid_size)

# Process the obstacles for visualization (not needed for calculation)
visible_grid = [['O' for _ in range(grid_size)] for _ in range(grid_size)]
for ox, oy in obstacles:
    if 0 <= ox < grid_size and 0 <= oy < grid_size:
        visible_grid[oy][ox] = 'X'
visible_grid[0][0] = 'S'  # Start
visible_grid[grid_size-1][grid_size-1] = 'E'  # End

# Calculate valid paths
total_valid_routes = calculate_valid_paths(grid_size, obstacles)

# Apply weather condition factor (distraction)
adjusted_routes = total_valid_routes * avg_visibility

print(f"Result: {total_valid_routes}")