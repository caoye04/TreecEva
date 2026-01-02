import math

# Sensor calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.023
REFERENCE_VOLTAGE = 3.3
MAX_SENSOR_COUNT = 16

# System state flags (some are decoys)
SYSTEM_ACTIVE = True
EMERGENCY_OVERRIDE = False
LOGGING_ENABLED = True
DEBUG_MODE = False
THRESHOLD_BREACHED = False

# Irrelevant sensor metadata
sensor_metadata = {
    's1': {'type': 'temperature', 'unit': 'C', 'scale': 'linear'},
    's2': {'type': 'pressure', 'unit': 'kPa', 'scale': 'log'},
    's3': {'type': 'humidity', 'unit': '%', 'scale': 'linear'},
    's4': {'type': 'flow', 'unit': 'L/min', 'scale': 'sqrt'}
}

# Simulated raw sensor readings (partially relevant)
raw_readings = [23.5, 101.3, 65.0, 4.7, 22.1, 102.1, 63.2, 5.1, 24.3, 99.8]

# Noise filter mask (unused in actual logic)
noise_filter = [0.98, 1.02, 0.99, 1.01, 0.97]

# Apply fake preprocessing (distractor)
def apply_calibration(data, offset=CALIBRATION_OFFSET):
    calibrated = []
    for x in data:
        calibrated.append(round(x * REFERENCE_VOLTAGE / 5.0 + offset, 3))
    return calibrated  # Never actually used

# Linear search for anomaly (dead code path)
def find_first_anomaly(data, limit=105.0):
    for i, val in enumerate(data):
        if val > limit:
            return i
    return -1

# Unused recursive smoothing function (decoy)
def smooth_recursive(data, factor=0.85, depth=0):
    if depth >= 3 or len(data) <= 1:
        return data
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(factor * data[i] + (1-factor) * smoothed[i-1])
    return smooth_recursive(smoothed, factor, depth+1)

# Actual processing begins here
processed_data = []
for val in raw_readings:
    if val > 0:
        processed_data.append(abs(math.log(val)) * 1000)  # Transform readings

# Threshold configuration map (critical)
threshold_map = {
    'low': {'bound': 2200, 'weight': 0.7},
    'high': {'bound': 3800, 'weight': 1.3},
    'critical': {'bound': 4500, 'weight': 2.0}
}

# Diagnostic accumulator
running_score = 0
breach_count = 0

# Main analysis loop with conditional logic and dictionary lookups
for reading in processed_data:
    if reading < threshold_map['low']['bound']:
        running_score += 5
    elif threshold_map['low']['bound'] <= reading < threshold_map['high']['bound']:
        running_score += 10
        temp_adj = reading / 100
        # Red herring calculation
        debug_val = temp_adj ** 2 - 2*temp_adj + 1
    else:
        running_score += 15
        breach_count += 1
        if reading > threshold_map['critical']['bound']:
            running_score += 25  # Critical bonus (not triggered)

# Secondary adjustment based on breach history (unused)
correction_factor = 1.0
if breach_count > 3:
    correction_factor = 0.9
elif breach_count == 0:
    correction_factor = 1.1

# Final diagnostic function with dictionary-based weighting
def analyze_readings(data, thresholds):
    base = running_score  # Captures outer scope variable
    extra_weight = 0
    
    # Simulate multi-condition assessment
    for r in data:
        if r > thresholds['high']['bound']:
            extra_weight += thresholds['high']['weight']
        if r < thresholds['low']['bound'] * 0.5:
            extra_weight -= 0.5  # Rare condition (not met)
    
    # Apply weights
    adjusted = base * (1 + (extra_weight * 0.01))
    
    # Bit manipulation red herring
    bit_mask = 0b1101
    masked = int(adjusted) & bit_mask
    
    # Final transformation using trigonometric distraction
    angle = math.pi / 6
    cosine_influence = math.cos(angle) * 0.02 * base
    
    # Real computation
    result = adjusted + cosine_influence
    
    # Dead code: logging simulation
    if LOGGING_ENABLED and DEBUG_MODE:
        print(f'Diagnostic trace: {result}')
    
    return round(result, 3)

# Execute main analysis
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")