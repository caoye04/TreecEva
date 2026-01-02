def analyze_sensor(node_id, readings):
    threshold = 42.5
    baseline = sum(readings) / len(readings)
    adjusted = [r * 0.98 for r in readings if r > 30]
    anomalies = [i for i, r in enumerate(readings) if abs(r - baseline) > 15]
    
    # Irrelevant calibration data (distractor)
    calibration_matrix = [[1.02, 0.99], [0.98, 1.01]]
    normalization_factor = 1.0
    for row in calibration_matrix:
        for val in row:
            normalization_factor *= val
    temp_correction = normalization_factor ** 0.5  # Unused

    # Simulated noise profile (dead code path)
    noise_floor = 0.05
    if len(readings) < 5:
        interpolated = []
        for i in range(len(readings) - 1):
            interpolated.append((readings[i] + readings[i+1]) / 2)
        readings += interpolated  # Not actually used later

    # Real processing branch
    valid_readings = [r for r in readings if 20 <= r <= 80]
    if len(valid_readings) == 0:
        return 0.0

    peak = max(valid_readings)
    filtered_peaks = [p for p in valid_readings if p > threshold]
    
    # Dummy transformation chain (misleading intermediate)
    transformed = []
    for x in filtered_peaks:
        x = (x ** 1.05) % 60
        x = abs(x - 37.2)
        transformed.append(round(x, 3))
    dummy_aggregate = sum(transformed) / len(transformed) if transformed else 0.0

    # Critical early termination based on node type
    if node_id.startswith('X'):
        return round(dummy_aggregate, 3)

    # Main diagnostic logic
    stability_index = len(filtered_peaks) / len(valid_readings)
    drift_rate = (valid_readings[-1] - valid_readings[0]) / len(valid_readings)
    weighted_score = (peak * 0.6) + (baseline * 0.4)
    
    # Decoy function call with side effect that isn't used
    def compute_ema(data, alpha=0.3):
        ema = [data[0]]
        for i in range(1, len(data)):
            ema.append(alpha * data[i] + (1 - alpha) * ema[i-1])
        return ema
    
    ema_values = compute_ema(valid_readings)  # Computed but not used
    
    # Final decision path
    if stability_index > 0.5 and abs(drift_rate) < 2.0:
        result = weighted_score * 1.25
    else:
        result = (baseline + peak) / 2 * 0.85

    return round(result, 3)


def process_readings(data_list):
    results = []
    for node, readings in data_list:
        score = analyze_sensor(node, readings)
        results.append(score)
    
    # Aggregate distraction
    total_power = 0
    for r in results:
        if r > 0:
            total_power += r ** 0.5
    efficiency_ratio = total_power / len(results) if results else 0  # Unused
    
    final_sum = sum(r for r in results if r > 10)
    return int(final_sum * 1.17)

# Sensor network input (real data)
data_package = [
    ('A7', [45, 67, 38, 72, 51, 44]),
    ('B2', [23, 81, 33, 29, 37, 41, 55]),
    ('C9', [66, 70, 85, 31, 25, 77, 68, 73]),
    ('X1', [50, 55, 45, 60, 53])  # Will trigger early return in analyze_sensor
]

# Filtering step (only non-X nodes are fully relevant)
filtered_data = [(n, r) for n, r in data_package if not n.startswith('X')]

# Key execution point
final_diagnostic = process_readings(filtered_data)
print(f"Target result: {final_diagnostic}")