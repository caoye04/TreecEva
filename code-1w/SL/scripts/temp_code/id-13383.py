def analyze_system_load():
    # Simulate a sensor grid with initial readings
    raw_readings = [12.4, 18.9, 25.1, 9.7, 14.3, 30.2, 8.8, 11.6, 22.5]
    
    # Normalize readings to a 0-1 scale
    max_reading = max(raw_readings)
    normalized = [r / max_reading for r in raw_readings]
    
    # Partition into 3x3 grid (simulated)
    grid_state = [normalized[i:i+3] for i in range(0, len(normalized), 3)]
    
    # Irrelevant environmental offset (not used in final calculation)
    env_offset = 0.037
    calibration_factor = sum([abs(a - b) for a, b in zip(raw_readings[:-1], raw_readings[1:])]) / len(raw_readings)

    # Secondary derived metric (distractor)
    fluctuation_score = 0
    for row in grid_state:
        for val in row:
            if val > 0.5:
                fluctuation_score += val ** 1.5

    # Simulate historical comparison (dead code path)
    historical_baseline = [0.4, 0.5, 0.35, 0.6, 0.2, 0.8, 0.45, 0.3, 0.7]
    variance_drift = [abs(h - n) for h, n in zip(historical_baseline, normalized)]
    
    # Unused transformation
    inverted_grid = [[1 - cell for cell in row] for row in grid_state]

    def calculate_stability_index(grid):
        stability = 0.0
        edge_sum = 0.0
        center_contributions = []
        
        # Analyze edge vs center cells in 3x3 grid
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if i == 1 and j == 1:  # Center cell
                    stability += cell * 2.1
                    center_contributions.append(cell)
                elif i == 0 or i == 2 or j == 0 or j == 2:  # Edge or corner
                    edge_sum += cell
        
        # Combine center and edge effects
        stability += edge_sum * 0.8
        
        # Apply correction based on symmetry (slicing used here)
        top_row = grid[0]
        bottom_row = grid[2]
        symmetry_diff = sum([abs(a - b) for a, b in zip(top_row, bottom_row[::-1])])
        symmetry_penalty = 0.5 * symmetry_diff
        
        # Final adjustment
        stability -= symmetry_penalty
        
        # Distractor: unused neighbor analysis
        neighbors = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[i])-1):
                neighbors += int(grid[i][j] > grid[i-1][j])

        return round(stability, 4)

    # Key statement
    energy_threshold = calculate_stability_index(grid_state)
    
    # Additional irrelevant computation
    cumulative_skew = 0
    for segment in grid_state:
        sorted_seg = sorted(segment)
        if len(sorted_seg) > 1:
            cumulative_skew += sorted_seg[-1] - sorted_seg[0]
    
    # Output result as required
    print(f"Target result: {energy_threshold}")

analyze_system_load()