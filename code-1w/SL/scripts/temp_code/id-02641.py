import math


def calculate_equilibrium(grid, limit):
    size = len(grid)
    total_energy = 0
    temp_buffer = [0] * size
    decay_factor = 0.85
    adjustment_log = []

    for i in range(size):
        row_energy = 0
        for j in range(len(grid[i])):
            cell_value = grid[i][j]
            if cell_value > limit:
                # Significant energy contribution
                row_energy += cell_value ** 0.5 * (i + 1)
            else:
                # Minimal contribution, but track for logs
                row_energy += cell_value * 0.1
            
            # Distractor: logging irrelevant adjustments
            adjustment_log.append(cell_value % 7 if cell_value > 0 else 0)
        
        # Apply damping
        temp_buffer[i] = row_energy * (decay_factor ** i)
        total_energy += temp_buffer[i]

    # Secondary processing with conditional expression
    scaling_factor = 1.5 if total_energy > 100 else 2.0
    normalized_energy = total_energy * scaling_factor

    # Simulate sensor drift compensation (partially irrelevant)
    drift_compensation = sum([math.sin(i * 0.1) for i in range(size)])
    compensated_energy = normalized_energy - drift_compensation

    # Final filtering via lambda and list comprehension
    valid_readings = list(filter(lambda x: x > 0.5, grid[0]))
    bonus = len(valid_readings) * 0.7 if valid_readings else 0.0

    # Irrelevant string manipulation (distractor)
    status_msg = "Processed_" + "_".join([str(int(x)) for x in grid[0][:3]])

    # Core result computation
    equilibrium_score = int(compensated_energy + bonus)
    return equilibrium_score

# Initialize concentration grid from simulated chemical diffusion
concentration_grid = [
    [49, 121, 64, 25],
    [16, 81, 36, 4],
    [9, 49, 100, 16],
    [25, 64, 121, 81]
]

threshold = 50

# Extraneous variable assignments (distraction)
calibration_data = [0.1, 0.2, 0.3]
baseline_offset = sum(calibration_data) * 10
ignored_intermediate = baseline_offset ** 2

# Key computation step
equilibrium_score = calculate_equilibrium(concentration_grid, threshold)

# Print final result as required
print(f"Result: {equilibrium_score}")