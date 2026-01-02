def preprocess_readings(raw_data, threshold=5.0):
    """Irrelevant preprocessing for sensor noise (dead-end function)."""
    filtered = []
    for val in raw_data:
        if val > threshold:
            filtered.append(val * 0.9)
    return [round(x, 2) for x in filtered]


def compute_checksum(data):
    """Distractor: computes a hash-like value not used in final result."""
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= int(val * 31) % 255
    return checksum + 1000


def accumulate_energy(flow_series):
    """Red herring function: simulates energy buildup but unused."""
    total = 0.0
    for val in flow_series:
        if val > 0:
            total += val ** 0.5
    return round(total, 3)


def shift_window(matrix, offset):
    """Bit manipulation decoy: applies XOR shift to matrix rows."""
    shifted = []
    for row in matrix:
        newRow = []
        for x in row:
            newRow.append(x ^ offset if x % 2 == 0 else x)
        shifted.append(newRow)
    return shifted


def validate_coherence(sequence):
    """Misleading validation that returns boolean chain (not directly used)."""
    if len(sequence) < 3:
        return False
    return all(a <= b for a, b in zip(sequence, sequence[1:])) or all(a >= b for a, b in zip(sequence, sequence[1:]))


def analyze_subgrid(grid, size):
    """Relevant recursive function analyzing thermal subregion coherence."""
    if size == 1:
        return grid[0][0]
    
    half = size // 2
    top_left = [row[:half] for row in grid[:half]]
    top_right = [row[half:] for row in grid[:half]]
    bottom_left = [row[:half] for row in grid[half:]]
    bottom_right = [row[half:] for row in grid[half:]]
    
    avg_tl = sum(sum(r) for r in top_left) / (half * half)
    avg_tr = sum(sum(r) for r in top_right) / (half * half)
    avg_bl = sum(sum(r) for r in bottom_left) / (half * half)
    avg_br = sum(sum(r) for r in bottom_right) / (half * half)
    
    deviations = [abs(avg_tl - avg_tr), abs(avg_bl - avg_br), abs(avg_tl - avg_br)]
    return analyze_subgrid(top_left, half) + min(deviations) * 100


def assess_symmetry(matrix):
    """Distractor: calculates symmetry score across diagonals."""
    n = len(matrix)
    score = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == matrix[j][i]:
                score += 1
    return score / (n * n)


def analyze_system_state(sensor_grid, depth_override=None):
    """Main analysis pipeline with mixed relevance and distractions."""
    # Initialize system parameters (some irrelevant)
    baseline = 27.1
    tolerance = 0.05
    critical_threshold = 88.0
    decay_factor = 0.88
    debug_mode = False
    log_entries = []
    
    # Simulated sensor data transformations (some used, some not)
    processed_grid = [[max(0, cell - baseline) for cell in row] for row in sensor_grid]
    
    # Irrelevant string-based logging setup
    status_flag = "NORMAL" if sum(sum(r) for r in processed_grid) < 200 else "ELEVATED"
    log_entries.append(f"[SYS] Mode: {status_flag}, Debug: {str(debug_mode).upper()}")
    
    # Key branching logic based on conditional expression
    grid_size = len(processed_grid)
    effective_depth = depth_override if depth_override and depth_override <= grid_size else grid_size
    
    # Dead-end early exit (never reached due to override)
    if effective_depth < 2:
        return -999
    
    # Red herring: bit-level manipulation
    masked_grid = [[val & 0b11111 for val in row] for row in processed_grid]  # keeps lower 5 bits
    
    # Distractor: checksum computation
    _ = compute_checksum([val for row in sensor_grid for val in row])
    
    # Relevant recursive subgrid analysis
    primary_metric = analyze_subgrid(processed_grid, effective_depth)
    
    # Decoy accumulation path
    energy_pool = 0.0
    for row in processed_grid:
        for v in row:
            if v > tolerance:
                energy_pool += v * decay_factor
    
    # Conditional expression affecting final result
    adjustment = 1.0 if validate_coherence([row[0] for row in processed_grid]) else 0.92
    
    # Final diagnostic calculation (depends only on primary_metric and adjustment)
    intermediate = primary_metric * adjustment
    
    # Noise injection via unused transformation
    _ = shift_window(masked_grid, 7)
    _ = accumulate_energy([val for row in processed_grid for val in row])
    
    # Final result
    final_score = int(intermediate) + (assess_symmetry(sensor_grid) > 0.7)
    
    return final_score

# Simulated thermal imaging matrix from satellite array
thermal_matrix = [
    [30, 32, 35, 40, 50, 60, 70, 80],
    [31, 33, 36, 41, 51, 61, 71, 81],
    [32, 34, 37, 42, 52, 62, 72, 82],
    [33, 35, 38, 43, 53, 63, 73, 83],
    [34, 36, 39, 44, 54, 64, 74, 84],
    [35, 37, 40, 45, 55, 65, 75, 85],
    [36, 38, 41, 46, 56, 66, 76, 86],
    [37, 39, 42, 47, 57, 67, 77, 87]
]

# Execute key statement
final_diagnostic = analyze_system_state(thermal_matrix, 7)

# Output result
print(f"Result: {final_diagnostic}")