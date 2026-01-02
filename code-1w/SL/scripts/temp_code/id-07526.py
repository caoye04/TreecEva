import math

# Irrelevant helper function (decoy)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm else v

# Misleading data transformation (distractor)
def transform_coordinates(coords):
    return [(c[0] * 1.5, c[1] * 0.8) for c in coords]

# Unused but plausible-looking utility
def smooth_data(data):
    return [sum(data[max(0, i-1):min(len(data), i+2)]) / min(3, len(data)) for i in range(len(data))]

# Core logic: nested bit manipulation and conditional aggregation
def calculate_thermal_output(matrix, thresholds):
    rows, cols = len(matrix), len(matrix[0])
    accumulator = 0
    
    # Simulated sensor grid with masking logic
    for i in range(rows):
        row_contribution = 0
        mask = (1 << (i % 5)) | (1 << ((i + 2) % 5))  # Bitwise red herring
        
        for j in range(cols):
            cell_value = matrix[i][j]
            threshold = thresholds[i % len(thresholds)][j % len(thresholds[0])]
            
            # Conditional expression with arithmetic twist
            adjusted = cell_value * 1.1 if cell_value > threshold else cell_value * 0.9
            
            # Irrelevant coordinate tracking (dead path)
            pixel_x, pixel_y = i * 16 + j % 4, j * 16 + i % 4
            if pixel_x % 7 == 0:
                continue  # Artificial filter with no impact
            
            # Key computation hidden among noise
            exponent = int(math.log(adjusted + 1, 2)) if adjusted > 0 else 0
            contribution = (adjusted ** 0.5) * (exponent + 1)
            
            # Conditional aggregation using set membership check
            valid_cols = {1, 3, 4, 6, 8}
            if j in valid_cols:
                row_contribution += contribution * (0.8 + 0.2 * (j % 3))
            
        # Only every second row contributes meaningfully
        if i % 2 == 0:
            accumulator += row_contribution * (1 + (i // 2) * 0.25)
    
    # Final adjustment based on global properties
    flat_vals = [val for row in matrix for val in row]
    avg_val = sum(flat_vals) / len(flat_vals)
    peak_val = max(flat_vals)
    
    # Decoy use of smoothed data
    smoothed_avg = sum(smooth_data(flat_vals)) / len(flat_vals)  # Unused
    
    # Actual final formula
    thermal_capacity = accumulator * (0.5 + avg_val / (peak_val + 1))
    return thermal_capacity

# Misdirection: unused physics constants
c = 299792458  # speed of light
e_charge = 1.602e-19
boltzmann = 1.380649e-23

# Simulated input data
energy_matrix = [
    [12, 18, 7, 23, 15, 9, 20, 13, 17, 11],
    [14, 21, 8, 19, 16, 10, 22, 12, 18, 14],
    [10, 15, 6, 20, 13, 8, 19, 11, 16, 9],
    [16, 22, 9, 24, 17, 11, 21, 14, 19, 13],
    [11, 17, 8, 20, 14, 9, 18, 12, 15, 10]
]

threshold_map = [
    [10, 15, 5, 20, 12],
    [13, 18, 8, 22, 14],
    [9, 16, 7, 19, 11]
]

# Spurious coordinate list (distractor)
sensor_positions = [(x*2.1, y*1.8) for x in range(3) for y in range(4)]
transformed_positions = transform_coordinates(sensor_positions)

# Dead code block: looks important but unused
def analyze_pattern(seq):
    freq = {}
    for s in seq:
        freq[s] = freq.get(s, 0) + 1
    return sorted(freq.items(), key=lambda x: -x[1])

# Main execution flow
if __name__ == "__main__":
    baseline = sum(sum(row) for row in energy_matrix) / 50  # Irrelevant metric
    scaling_factor = math.sin(math.pi / 6) + 0.5  # Constant disguised as dynamic
    
    # Key statement
    thermal_capacity = calculate_thermal_output(energy_matrix, threshold_map)
    
    # Output result
    print(f"Result: {thermal_capacity}")