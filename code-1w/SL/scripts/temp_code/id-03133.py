import itertools

# Simulated sensor grid analysis with fault detection
def analyze_sensor_cluster(readings, threshold=0.75):
    anomalies = []
    for i, row in enumerate(readings):
        for j, val in enumerate(row):
            if abs(val) > threshold and (i + j) % 3 != 0:
                anomalies.append((i, j, val))
    return anomalies

# Irrelevant helper - looks important but unused in final result
def calculate_entropy(data):
    total = sum(x ** 2 for x in itertools.chain.from_iterable(data))
    norm = total / len(data) if data else 0
    return round(norm * 0.673, 4)

# Core transformation: apply phase shift and fold matrix
def apply_phase_shift(grid, shift):
    shifted = []
    for idx, row in enumerate(grid):
        shifted_row = [(x * shift) % 1.8 for x in row]
        shifted.append(shifted_row)
    return shifted

# Misleading diagnostic path - appears critical but is bypassed
def legacy_diagnostic_protocol(matrix):
    flat = list(itertools.chain.from_iterable(matrix))
    outlier_count = sum(1 for x in flat if x > 1.0)
    return {'status': 'FAILED', 'code': -999, 'outliers': outlier_count}

# Signal validation with temporal correlation
def validate_temporal_signal(signal_sequence):
    validated = []
    for t, point in enumerate(signal_sequence):
        if t == 0:
            continue
        delta = abs(point - signal_sequence[t-1])
        if delta < 0.45 or t % 5 == 0:
            validated.append(delta * 0.8)
    return validated

# Main aggregation logic combining spatial and temporal metrics
def aggregate_metrics(anomaly_list, time_series):
    spatial_score = len(anomaly_list) * 17
    temporal_score = int(sum(time_series) * 100)
    # Key computation: modular weighting based on pattern density
    density = len(anomaly_list) / (1 + len(time_series))
    adjustment = (density * 1000) % 23
    return spatial_score + temporal_score - int(adjustment)

# --- Simulated Input Data ---
sensor_readings = [
    [0.12, 0.81, -0.33, 1.05],
    [0.67, 0.44, 0.91, 0.21],
    [-0.52, 1.11, 0.09, 0.76],
    [0.88, -0.29, 0.63, 0.99]
]

# Distraction block: looks like system calibration but irrelevant
calibration_matrix = [
    [1.0, 0.5, 0.25, 0.125],
    [2.0, 1.0, 0.5, 0.25],
    [4.0, 2.0, 1.0, 0.5],
    [8.0, 4.0, 2.0, 1.0]
]

# Unused function call that seems important
decoy_checksum = calculate_entropy(calibration_matrix)

# Step 1: Detect spatial anomalies in grid
grid_anomalies = analyze_sensor_cluster(sensor_readings)

# Step 2: Apply non-linear transformation to raw grid (distractor)
transformed_grid = apply_phase_shift(sensor_readings, shift=1.3)

# Step 3: Extract temporal signal from diagonal components
signal_path = [sensor_readings[i][i] for i in range(len(sensor_readings))]

# Step 4: Validate temporal coherence
validation_trace = validate_temporal_signal(signal_path)

# Step 5: Run decoy diagnostic (never used)
_ = legacy_diagnostic_protocol(transformed_grid)

# Step 6: Perform final metric aggregation using only relevant components
final_diagnostic = aggregate_metrics(grid_anomalies, validation_trace)

# Additional red herring variables
temp_buffer = list(zip([x[0] for x in grid_anomalies], [x[1] for x in grid_anomalies]))
index_set = set(itertools.combinations(temp_buffer, 2))

# Critical output - do not modify format
print(f"Result: {final_diagnostic}")