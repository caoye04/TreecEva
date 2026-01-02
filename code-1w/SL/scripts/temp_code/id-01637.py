def process_spectral_data(data_sequence, threshold=0.75):
    """ Analyze spectral response with noise filtering and baseline correction """
    filtered_peaks = []
    baseline_noise = [0.1, -0.05, 0.2, -0.15, 0.08]
    cumulative_shift = 0

    for i, point in enumerate(data_sequence):
        adjusted_point = point - baseline_noise[i % len(baseline_noise)]
        if abs(adjusted_point) > threshold:
            filtered_peaks.append((i, adjusted_point))
            cumulative_shift += adjusted_point * 0.1

    # Irrelevant transformation (dead path)
    transformed_output = [x[1] * 2 for x in filtered_peaks if x[0] % 2 == 0]
    return filtered_peaks, cumulative_shift, transformed_output


def generate_frequency_map(resolution=64):
    """ Generate dummy frequency domain mapping (unused distractor) """
    import math
    frequencies = []
    for i in range(resolution):
        angle = i * math.pi / resolution
        freq = math.sin(angle) * math.exp(-i / resolution)
        frequencies.append(round(freq, 3))
    return frequencies

def calculate_stability_index(matrix, offset):
    """ Compute thermal stability index from configuration matrix """
    size = len(matrix)
    temp_grid = [[0] * size for _ in range(size)]
    checksum = 0

    # Initialize grid with offset-modulated values
    for i in range(size):
        for j in range(size):
            raw_val = (i + 1) * (j + 1) + (offset ^ (i << 1))
            temp_grid[i][j] = raw_val % 17
            checksum ^= temp_grid[i][j]  # Bitwise accumulation

    # Apply convolution-like smoothing (relevant computation)
    smoothed_grid = [[0] * size for _ in range(size)]
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            neighbors = [
                temp_grid[i-1][j], temp_grid[i+1][j],
                temp_grid[i][j-1], temp_grid[i][j+1]
            ]
            center = temp_grid[i][j]
            smoothed_grid[i][j] = (sum(neighbors) + center * 2) // 3

    # Extract central region statistics
    center_sum = 0
    for i in range(2, size - 2):
        for j in range(2, size - 2):
            center_sum += smoothed_grid[i][j]

    # Decoy calculation with string operations (distractor)
    status_code = "STB_" + "_".join([str(checksum), str(center_sum)])
    code_parts = status_code.split('_')
    validation_key = sum(int(p) for p in code_parts[1:] if p.isdigit())

    # Final index calculation (answer path)
    stability_index = (center_sum * 3) - (checksum * 2) + (offset & 15)
    return stability_index

# Main execution block
if __name__ == "__main__":
    # Simulated sensor configuration data
    config_matrix = [
        [1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 1, 0, 1],
        [0, 1, 1, 1, 1, 0, 1, 1]
    ]

    calibration_offset = 42
    sensor_log = "LOG_20241201_SENSORS_ACTIVE"

    # Process dummy spectral input (irrelevant side computation)
    dummy_signal = [0.1, 0.8, -0.3, 0.9, 0.2, -0.7, 0.6, 0.4, -0.5, 0.85]
    peaks, drift, extras = process_spectral_data(dummy_signal)

    # Generate unused frequency map (red herring)
    freq_map = generate_frequency_map(128)

    # Key computational statement
    thermal_gradient = calculate_stability_index(config_matrix, calibration_offset)

    # Additional decoy logic
    if len(peaks) > 5:
        extra_adjustment = len(freq_map) // 100
        thermal_gradient -= extra_adjustment  # Never executed due to peak count

    # Final result output
    Result: {thermal_gradient}