import itertools

# Sensor array diagnostics with noise filtering and calibration
sensor_ids = [101, 102, 103, 104, 105]
raw_readings = [987, 1003, None, 1021, 996, 1000, 1015, 988, 1009, None]
calibration_log = {101: 1.02, 102: 0.99, 103: 1.01, 104: 1.00, 105: 0.98}
timestamps = ['t0', 't1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9']

# Irrelevant metadata (distractor)
device_status = {'power': 'stable', 'firmware': 'v2.1.3', 'location': 'chamber_4'}
system_uptime = 14285
redundant_checksum = sum(len(str(x)) for x in sensor_ids + [system_uptime])

# Simulate auxiliary data stream (dead path)
aux_stream = list(itertools.accumulate([1, -1, 2, -2, 3]))
baseline_shift = aux_stream[-1] * 0.01  # Minor red herring

# Primary processing pipeline
valid_readings = [r for r in raw_readings if r is not None]
outlier_threshold = 1010
high_noise = [v for v in valid_readings if abs(v - 1000) > 15]
normalized = [v / 1000.0 for v in valid_readings]

# Misleading intermediate diagnostic (decoy)
apparent_drift = sum(normalized) / len(normalized) - 1.0

# Real signal extraction using cross-referenced calibration
paired_data = list(zip(valid_readings, itertools.cycle(sensor_ids)))
filtered_data = [(val, sid) for val, sid in paired_data if val <= outlier_threshold]

def apply_calibration(readings_with_id, log):
    calibrated = []
    for value, sensor_id in readings_with_id:
        factor = log[sensor_id]
        adjusted = value * factor
        calibrated.append(adjusted)
    return calibrated

def analyze_trend(data_sequence):
    # Unused function - dead code path
    if len(data_sequence) < 3:
        return 0
    return sum(b - a for a, b in zip(data_sequence, data_sequence[1:]))

def process_readings(data_tuples, adjustment):
    values = [item[0] for item in data_tuples]
    ids = [item[1] for item in data_tuples]
    
    # Core calculation
    base_avg = sum(values) / len(values)
    id_entropy = len(set(ids)) / len(ids)
    
    # Secondary adjustment
    if base_avg > 995:
        stage_flag = 'A'
    else:
        stage_flag = 'B'
    
    # Tertiary transformation
    transformed = base_avg * (1 + (adjustment - 1) * id_entropy)
    
    # Redundant smoothing (irrelevant to final result)
    smoothed = [transformed * 0.99, transformed * 1.01]
    temp_offset = max(smoothed) - min(smoothed)
    
    # Final deterministic output
    final_score = int(round(transformed - 50))
    return final_score

# Unused analysis branch (misleading path)
if apparent_drift < 0:
    fallback_mode = True
    emergency_adjust = sum(high_noise) if high_noise else 0
else:
    fallback_mode = False
    emergency_adjust = -1

# Actual execution path
reference_factor = calibration_log[101]  # Key anchor point
interim_set = apply_calibration(filtered_data, calibration_log)

# Critical statement
final_diagnostic = process_readings(filtered_data, reference_factor)

print(f"Result: {final_diagnostic}")