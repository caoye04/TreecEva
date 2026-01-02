from collections import defaultdict

# Simulated sensor data with timestamps and readings
data_log = [
    (1001, 'temp', 23.5), (1002, 'pressure', 101.3), (1003, 'temp', 24.1),
    (1004, 'humidity', 45), (1005, 'temp', 22.8), (1006, 'pressure', 100.7),
    (1007, 'humidity', 47), (1008, 'temp', 25.3), (1009, 'pressure', 102.1)
]

# Misleading auxiliary data
aux_data = [(t, 'derived', t * 0.01 + 3) for t in range(1000, 1010)]

# Aggregation structure
counts = defaultdict(int)
totals = defaultdict(float)
status_flags = [False, True, False]
baseline = 100.0

# Redundant transformation
transformed = list(map(lambda x: (x[0] - 1000, x[1], round(x[2] + 0.1, 1)), data_log))

# Spurious intermediate calculation
drift_estimate = sum(abs(totals.get('temp', 0) - baseline) for _ in range(2))

# Core processing function
def process_metrics(log, min_threshold=24.0):
    temp_readings = []
    pressure_baseline = None
    humidity_snapshot = None
    sample_count = 0

    # First pass: extract relevant metrics
    for timestamp, sensor_type, value in log:
        counts[sensor_type] += 1
        totals[sensor_type] += value
        sample_count += 1

        if sensor_type == 'temp':
            temp_readings.append(value)
        elif sensor_type == 'pressure' and not pressure_baseline:
            pressure_baseline = value
        elif sensor_type == 'humidity' and timestamp % 2 == 1:
            humidity_snapshot = value

    # Secondary derived values (some unused)
    avg_temp = sum(temp_readings) / len(temp_readings) if temp_readings else 0
    high_temp_count = sum(1 for t in temp_readings if t > min_threshold)
    temp_variance = sum((t - avg_temp) ** 2 for t in temp_readings) / len(temp_readings) if temp_readings else 0

    # Distractor logic with dead condition
    if len(log) > 100 or any(status_flags):
        correction_factor = 0.95
    else:
        correction_factor = 1.0  # Never actually applied

    # Efficiency metric computation
    efficiency_components = []
    for i, val in enumerate(temp_readings):
        norm_val = val / 25.0
        weight = 0.5 + (i * 0.1)
        adjusted = norm_val * weight
        efficiency_components.append(adjusted)

    raw_efficiency = sum(efficiency_components)
    
    # Final scoring with irrelevant adjustments
    penalty = 0.1 * (counts['pressure'] - 3) ** 2 if counts['pressure'] > 3 else 0
    bonus = 0.05 * counts['humidity']
    
    efficiency_score = raw_efficiency - penalty + bonus

    # Unused debug print simulation
    debug_dump = {k: (totals[k] / counts[k]) for k in counts}
    
    return efficiency_score, debug_dump, avg_temp

# Trigger execution
efficiency_score = 0
threshold = 24.0
final_output = process_metrics(data_log, threshold)
efficiency_score = final_output[0]

# Output result as required
print(f"Target result: {efficiency_score}")