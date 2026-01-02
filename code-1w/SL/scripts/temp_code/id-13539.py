from collections import defaultdict

# Simulate sensor data with noise and calibration offsets
def process_sensor_readings(raw_data, thresholds):
    readings_log = defaultdict(int)
    cumulative_drift = 0
    valid_count = 0
    temp_buffer = []

    for idx, reading in enumerate(raw_data):
        # Irrelevant noise modeling (distractor)
        if idx % 3 == 0:
            cumulative_drift += 0.05 * idx
            readings_log['drift_events'] += 1

        # Core logic: filter valid readings
        if thresholds['min'] < reading < thresholds['max']:
            temp_buffer.append(reading)
            valid_count += 1

        # Misleading statistical tracking (semi-relevant)
        if reading > thresholds['max'] * 0.9:
            readings_log['high_proximity'] += 1

    # Dead code path: never modifies final result (distractor)
    if len(temp_buffer) > 100:
        outlier_count = sum(1 for x in temp_buffer if x > 90)
        readings_log['outliers'] = outlier_count

    # Core processing: compute baseline and adjustment
    baseline_score = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    stability_ratio = valid_count / len(raw_data) if raw_data else 0

    # Secondary correction based on distribution
    variance_proxy = sum((x - baseline_score) ** 2 for x in temp_buffer) / len(temp_buffer) if temp_buffer else 0
    correction_term = 1 if variance_proxy < 25 else -1

    # Adaptive factor influenced by system state (partially relevant)
    adaptive_factor = 5 if stability_ratio > 0.6 else 3

    # Final diagnostic calculation — key statement
    final_diagnostic = baseline_score + adaptive_factor * correction_term

    # Redundant print (not affecting logic)
    print(f'Diagnostic complete: {final_diagnostic}')

    return final_diagnostic

# Input data generation (deterministic)
import math
raw_sensor_data = [40 + 2 * i + math.sin(i) * 3 for i in range(50)]
raw_sensor_data += [85, 95, 105]  # Add some out-of-bound values

# Threshold parameters
tuning_params = {'min': 35, 'max': 88}

# Execute processing
result = process_sensor_readings(raw_sensor_data, tuning_params)
Target result: {result}