import math

# Simulate environmental thermal grid readings over time
def generate_sensor_grid(boundaries):
    grid = []
    for i in range(boundaries[0]):
        row = []
        for j in range(boundaries[1]):
            value = (i ** 2 + j * 3.14) % 25.7
            row.append(round(value, 3))
        grid.append(row)
    return grid

# Misleading function - appears relevant but unused in final calculation
def compute_entropy(data):
    total = 0.0
    for row in data:
        for val in row:
            if val > 0:
                total += val * math.log(val)
    return round(total, 4)

# Auxiliary transformation: applies exponential smoothing to grid (distractor)
def smooth_grid(data, factor=0.1):
    smoothed = []
    for row in data:
        new_row = [round(x * (1 + factor), 3) for x in row]
        smoothed.append(new_row)
    return smoothed

# Core calculation: computes weighted integral above threshold
def calculate_thermal_integral(raw_grid, limit):
    filtered_values = []
    weights = [math.cos(i * 0.1) for i in range(len(raw_grid))]
    
    for idx, row in enumerate(raw_grid):
        # Only consider cells exceeding threshold
        qualified = [v for v in row if v > limit]
        weighted_sum = sum(v * weights[idx] for v in qualified)
        if weighted_sum > 0:
            filtered_values.append(weighted_sum)
    
    # Apply decay based on row count
    decay_factor = math.exp(-1 / len(raw_grid))
    final_integral = sum(filtered_values) * decay_factor
    
    # Red herring: modify a global-looking variable that's not used
    global phantom_total
    phantom_total = sum(sum(r) for r in raw_grid) * 0.5
    
    return round(final_integral, 6)

# Secondary unused path: simulates alternate processing
def resample_grid(data, step=2):
    sample = []
    for i in range(0, len(data), step):
        sample.append(data[i][::step])
    return sample

# Main execution block
if __name__ == "__main__":
    # Initialize parameters
    region_bounds = (12, 15)
    cutoff = 18.9
    adjustment = 0.05
    
    # Generate base sensor data
    grid_data = generate_sensor_grid(region_bounds)
    
    # Dead code path - looks important but never called
    if False:
        entropy_score = compute_entropy(grid_data)
        downsampled = resample_grid(grid_data, 3)

    # Apply irrelevant smoothing (result discarded)
    _ = smooth_grid(grid_data, adjustment)
    
    # Critical computation
    thermal_capacity = calculate_thermal_integral(grid_data, cutoff)
    
    # Print result as required
    print(f"Target result: {thermal_capacity}")