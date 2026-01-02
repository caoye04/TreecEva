import math

# System calibration and sensor simulation for thermal stability analysis
def generate_sensor_profile(base_temp, noise_factor, size):
    return [base_temp + math.sin(i) * noise_factor for i in range(size)]

def apply_filter(raw_data, kernel=lambda x: sum(x) / len(x)):
    smoothed = []
    for i in range(1, len(raw_data) - 1):
        window = raw_data[i-1:i+2]
        smoothed.append(kernel(window))
    return [raw_data[0]] + smoothed + [raw_data[-1]]

def evaluate_homogeneity(grid):
    row_averages = [sum(row)/len(row) for row in grid]
    col_averages = [sum(col)/len(col) for col in zip(*grid)]
    return abs(max(row_averages) - min(row_averages)) < 0.5

def recursive_energy_decay(value, depth):
    if depth == 0 or value < 0.1:
        return value
    return recursive_energy_decay(value * 0.68, depth - 1)

def detect_anomalies(series, threshold=0.3):
    anomalies = []
    for i, val in enumerate(series):
        if abs(val - series[0]) > threshold:
            anomalies.append(i)
    return anomalies if anomalies else [0]

def compute_stability_index(matrix, offset):
    # Irrelevant preprocessing - red herring
    normalized = [[(cell + offset) / (i + j + 1) for j, cell in enumerate(row)] 
                 for i, row in enumerate(matrix) if sum(row) > 15]
    
    # Distractor: unused complex transformation
    transformed = [[math.tanh(cell) for cell in row] for row in matrix]
    entropy_score = -sum(sum(c * math.log(abs(c)+1e-9) for c in row) for row in transformed)
    
    # Critical path begins: extract diagonal using enumerate
    diagonal_values = []
    for idx, row in enumerate(matrix):
        if idx < len(row):
            diagonal_values.append(row[idx])
    
    # Apply lambda-based weighting filter
    weighted_diag = list(map(lambda x: x * 0.85, diagonal_values))
    
    # Secondary distractor: unused anomaly detection on transposed data
    transposed = list(zip(*matrix))
    _ = [detect_anomalies(row, threshold=0.5) for row in transposed]
    
    # Compute index using recursive decay on max diagonal element
    seed_energy = max(weighted_diag) if weighted_diag else 0
    stabilized_energy = recursive_energy_decay(seed_energy, depth=5)
    
    # Additional interference: irrelevant homogeneity check
    _ = evaluate_homogeneity(matrix)
    
    # Final computation with offset interaction
    adjustment = offset % 3.7
    stability_index = (stabilized_energy * 100) + adjustment
    
    # Dead code path - misleading control flow
    if False:
        backup_grid = [[x**0.5 for x in row] for row in matrix]
        stability_index = sum(sum(backup_grid, []))
    
    return round(stability_index, 6)

# Simulate thermal matrix from sensor array readings
temperature_banks = [
    [21.3, 19.8, 23.1, 18.7],
    [20.5, 22.9, 20.2, 24.3],
    [23.0, 21.1, 22.8, 19.9],
    [19.7, 23.2, 20.0, 22.7]
]

calibration_offset = 4.2

# Apply irrelevant preprocessing chain
filtered_banks = [apply_filter(bank) for bank in temperature_banks]
sensor_log = {f'bank_{i}': generate_sensor_profile(bank[0], 0.4, 5) for i, bank in enumerate(temperature_banks)}

# Core diagnostic computation
final_diagnostic = compute_stability_index(thermal_matrix=temperature_banks, calibration_offset=calibration_offset)

print(f"Result: {final_diagnostic}")