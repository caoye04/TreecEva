import math

# Simulated sensor grid data from environmental monitoring stations
def generate_sensor_grid():
    base_values = [i * 1.7 for i in range(16)]
    noise_offsets = [math.sin(i) * 0.3 for i in range(16)]
    return [[base_values[i*4 + j] + noise_offsets[i*4 + j] for j in range(4)] for i in range(4)]

def calculate_entropy(vector):
    """Irrelevant function: simulates signal randomness analysis"""
    total = 0.0
    for x in vector:
        if x > 0:
            total -= x * math.log(x)
    return round(total, 4)

def validate_checksum(data):
    """Dead code path: used in alternate protocol"""
    checksum = 0
    for row in data:
        for val in row:
            checksum ^= int(val * 100) & 0xFF
    return checksum == 0xAB

def extract_features(grid):
    """Misleading feature extraction with red herring outputs"""
    features = []
    for i, row in enumerate(grid):
        if i % 2 == 0:
            features.append(sum(row) * 0.1)
        else:
            features.append(max(row) - min(row))
    # Decoy transformation
    transformed = [f * 1.5 for f in features]
    normalized = [t / (sum(transformed) + 1e-8) for t in transformed]
    return normalized  # Never actually used

def compute_gradients(grid):
    """Partially relevant: computes spatial gradients but only top-left is used"""
    grads = [[0.0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            dx = grid[i][j+1] - grid[i][j]
            dy = grid[i+1][j] - grid[i][j]
            grads[i][j] = math.sqrt(dx*dx + dy*dy)
    return grads

def map_thresholds(grid):
    """Generates threshold multipliers based on positional logic"""
    thresholds = [[0.0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            factor = (i + 1) * (j + 1)
            thresholds[i][j] = 1.0 / factor if factor % 2 == 1 else 0.5 * (i + j)
    return thresholds

def aggregate_measures(data, thres_map):
    """Core computation: weighted accumulation with slicing and enumeration"""
    accumulator = 0.0
    # Use of enumerate and slicing: key python idiom
    for idx, row in enumerate(data[1:]):  # Skip first row
        sliced = row[:3]  # Take only first three elements
        for jdx, val in enumerate(sliced):
            weight = thres_map[idx+1][jdx]  # Shifted indexing
            accumulator += val * weight
    
    # Case conversion simulation via ASCII shifting (distractor)
    magic_phrase = "DiagnosticsActive"
    shift_value = sum(ord(c) for c in magic_phrase if c.isupper()) % 7  # 69+65+67+73+86 = 360 → 360%7=2
    
    # Irrelevant bit manipulation chain
    decoy_flag = (shift_value << 3) ^ 0xAA
    decoy_flag = (decoy_flag & 0x3F) | (shift_value << 2)
    
    # Final adjustment using summation of diagonal from gradient (only this matters)
    grads = compute_gradients(data)
    diag_sum = sum(grads[i][i] for i in range(3))
    
    # Critical dependency: combines accumulator with diag_sum
    final_diagnostic = int(accumulator * 10) + int(diag_sum)
    
    # Dead assignment: looks important but unused
    final_diagnostic |= 0x1000  
    final_diagnostic &= 0xFFFF  # Masking keeps it within range
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    # Generate core data
    grid_data = generate_sensor_grid()
    
    # Initiate irrelevant validation (prints nothing, just consumes time)
    _ = validate_checksum(grid_data)
    
    # Extract unused features (red herring)
    _ = extract_features(grid_data)
    
    # Generate actual threshold map
    threshold_map = map_thresholds(grid_data)
    
    # Key execution point
    final_diagnostic = aggregate_measures(grid_data, threshold_map)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")