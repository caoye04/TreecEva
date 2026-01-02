import itertools

def preprocess_calibration(data):
    # Irrelevant preprocessing function (dead code path)
    return [x * 1.05 for x in data if x > 10]

def validate_grid_integrity(grid):
    # Misleading validation that isn't used in final computation
    checksum = sum(sum(row) for row in grid)
    return checksum % 7 == 0

def decode_phase_shift(signal):
    # Distractor function with bit manipulation red herring
    shifted = 0
    for val in signal:
        shifted ^= (val << 2) | (val >> 1)
    return shifted & 0xFF

def calculate_thermal_response(grid, factor):
    # Core relevant logic embedded within noise
    rows, cols = len(grid), len(grid[0])
    total_flux = 0
    
    # Real computation: sum of squared even-positioned elements
    for i in range(0, rows, 2):
        for j in range(0, cols, 2):
            total_flux += grid[i][j] ** 2
    
    # Decoy accumulation with unused variables
    temporal_buffer = []
    for i, row in enumerate(grid):
        running_max = max(row)
        temporal_buffer.append(running_max * (i + 1))  # Unused
    
    # Red herring: complex conditional expression with no effect
    adjustment = factor if factor > 0.5 else (1.5 if sum(temporal_buffer) > 100 else 0.8)
    _ = adjustment * 2  # Dead operation
    
    # Actual formula: total_flux * factor, but obscured
    capacity = total_flux * factor
    
    # Fake early exit based on decoy logic
    phase_signal = [rows, cols, int(factor * 10)]
    if decode_phase_shift(phase_signal) > 200:
        return -1  # Never reached due to bit math
    
    # Real result calculation
    return capacity

# Main execution block
if __name__ == "__main__":
    # Initialize grid state (real input)
    grid_state = [
        [3, 7, 2, 8],
        [5, 9, 1, 4],
        [6, 3, 7, 2],
        [1, 5, 8, 3]
    ]
    
    # Efficiency factor used in calculation
    efficiency_factor = 1.2
    
    # Irrelevant data structures (distractors)
    sensor_readings = list(itertools.accumulate([2, -1, 3, 0, -2, 4]))
    calibration_map = {i: val * 0.9 for i, val in enumerate(sensor_readings)}
    anomaly_threshold = max(calibration_map.values()) / 2.5
    
    # Simulated diagnostics (dead code)
    diagnostics = []
    for i in range(3):
        diag_val = (anomaly_threshold + i) ** 1.5
        diagnostics.append(int(diag_val))
    
    # Key assignment - the actual target
    thermal_capacity = calculate_thermal_response(grid_state, efficiency_factor)
    
    # More distraction: unused dictionary operations
    status_log = {
        'grid_valid': validate_grid_integrity(grid_state),
        'calibrated': len(sensor_readings) > 5,
        'phase_locked': decode_phase_shift([7, 3, 1]) == 42
    }
    
    # Final output
    print(f"Result: {thermal_capacity}")