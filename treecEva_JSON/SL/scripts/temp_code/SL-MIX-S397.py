import math
import cmath

# Vacuum's path as a sequence of complex number moves
path_sequence = [1+0j, 1+0j, 0+1j, 1+0j, 0+1j, 0+1j, -1+0j, -1+0j, 0-1j, 0-1j, -1+0j, 0-1j]

# Initial state
vacuum_position = 0+0j
visited_cells = {vacuum_position}
efficiency_score = 0.0

for move in path_sequence:
    # Update position
    vacuum_position += move
    visited_cells.add(vacuum_position)
    
    # Calculate distance squared from origin
    distance_squared = (vacuum_position.real**2 + vacuum_position.imag**2)
    
    # Prevent log(0) error
    if distance_squared == 0:
        distance_squared = 1
    
    # Calculate efficiency score
    unique_count = len(visited_cells)
    efficiency_score = unique_count * math.log10(distance_squared)
    
    # Check for return condition
    if efficiency_score > 10.0:
        vacuum_position = 0+0j
        visited_cells = {vacuum_position}
        # Note: efficiency_score is not reset

# The final value of efficiency_score before any potential final return
print(f"Target result: {efficiency_score}")