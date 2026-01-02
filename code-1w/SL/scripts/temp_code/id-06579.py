def preprocess_readings(raw_readings):
    # Irrelevant transformation (distractor)
    normalized = [x * 0.98 + 2.1 for x in raw_readings]
    filtered = [x for x in normalized if x > 25.0]
    return [x - 273.15 for x in filtered]  # Convert from Kelvin to Celsius (unused path)


def calculate_baselines(sensory_inputs):
    # Complex but irrelevant baseline calculation
    avg = sum(sensory_inputs) / len(sensory_inputs)
    variance = sum((x - avg) ** 2 for x in sensory_inputs) / len(sensory_inputs)
    deviation_flag = variance > 150
    baselines = { 'mean': avg, 'variance': variance, 'stable': not deviation_flag }
    return baselines

# Decoy function that looks important but is never called
def deprecated_analysis(data_log):
    import math
    return [math.log(abs(x) + 1) for x in data_log if x != 0]

# Sensor IDs and their calibration offsets (some are red herrings)
sensor_calibrations = {
    'S101': 1.05,
    'S102': 0.98,
    'S103': 1.12,
    'S104': 0.89,
    'DUMMY_SENSOR': 999.9  # Deliberate decoy
}

# Raw sensor inputs from field devices
raw_sensor_data = [298.5, 301.2, 296.8, 303.0, 299.4, 305.1, 297.3, 302.7, 295.9]

# Unused secondary dataset to distract
auxiliary_readings = [1.2, 0.9, 1.5, 1.1, 1.0, 0.8, 1.3]

# Apply meaningless aggregation across sensors (dead code path)
temporal_aggregates = {}
for i, val in enumerate(raw_sensor_data):
    key = f'S10{i+1}'
    if key in sensor_calibrations:
        calibrated = val * sensor_calibrations[key]
        temporal_aggregates[key] = round(calibrated, 2)

# Real processing begins here — extract only relevant portion
processed_readings = [x - 273.15 for x in raw_sensor_data]  # Kelvin to Celsius

# Generate time-indexed pairs (using enumerate)
indexed_readings = list(enumerate(processed_readings))

# Pair with dummy labels using zip (looks meaningful but partially irrelevant)
dummy_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
labeled_readings = list(zip(dummy_labels, indexed_readings))

# Extract clean values above threshold
threshold_filtered = [temp for temp in processed_readings if temp > 22.0]

# Compute dynamic thresholds based on position (complex distraction)
position_weights = [abs(i - 4) * 0.1 for i in range(len(threshold_filtered))]
weighted_thresholds = [22.5 + w for w in position_weights]

# Mapping thresholds per index (used later)
threshold_map = {i: weighted_thresholds[i] for i in range(len(weighted_thresholds))}

# Transform data through filtering and scaling
scaled_data = []
for idx, temp in enumerate(threshold_filtered):
    if idx % 2 == 0:
        scaled_data.append(temp * 1.02)
    else:
        scaled_data.append(temp * 0.99)

# Simulate multi-stage validation flags
validation_phases = [True, False, True]
current_phase = validation_phases[0]

# Core transformation logic (actually used)
processed_data = []
for i, val in enumerate(scaled_data):
    if i in threshold_map and val > threshold_map[i]:
        processed_data.append(val * 1.05)
    elif val > 22.5:
        processed_data.append(val * 1.01)
    else:
        processed_data.append(val)

# Another layer of conditional refinement
refined_set = set()
for x in processed_data:
    if x > 23.0:
        refined_set.add(round(x, 1))
    else:
        refined_set.add(round(x - 0.5, 1))

# Final analysis function
def analyze_metrics(metrics, thresholds):
    base_score = sum(metrics) / len(metrics)
    threshold_count = sum(1 for t in thresholds.values() if t > 22.6)
    adjustment_factor = 0.95 if threshold_count > 3 else 1.05
    
    # Red herring: unused complex bit manipulation
    binary_mask = 0b101010
    masked_result = len(metrics) ^ binary_mask & threshold_count
    
    # Actual determinant
    final_value = base_score * adjustment_factor
    
    # Multiple assignment distraction
    interim, final_diagnostic = 999.99, final_value
    return final_diagnostic

# Execute main logic
final_diagnostic = analyze_metrics(processed_data, threshold_map)
print(f"Target result: {final_diagnostic}")