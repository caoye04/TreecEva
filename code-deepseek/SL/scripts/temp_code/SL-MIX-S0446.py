def calculate_grid_positions():
    grid_points = [15, 22, 8, 34, 19]
    offset = 3
    
    # Calculate adjusted positions using enumerate
    enumerate_results = []
    for idx, point in enumerate(grid_points):
        adjusted = (point + offset) * (idx + 1)
        enumerate_results.append(adjusted)
    
    # Final computation using sum
    final_coordinate = sum(enumerate_results)
    
    print(f"Result: {final_coordinate}")
    return final_coordinate

calculate_grid_positions()