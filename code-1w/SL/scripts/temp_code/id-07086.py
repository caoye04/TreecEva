import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0, 21.4]
humidity_readings = [45, 52, 58, 43, 60, 55, 49, 51, 57, 50]
pressure_readings = [1013, 1015, 1012, 1018, 1014, 1016, 1011, 1017, 1013, 1015]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_A = 0.987
CALIBRATION_OFFSET_X = 2.1
REFERENCE_VOLTAGE = 3.3
MAX_SENSOR_RANGE = 1024

# Misleading intermediate processing (dead path)
def calibrate_sensor(data, factor, offset):
    return [x * factor + offset for x in data]

calibrated_temps = calibrate_sensor(temperature_readings, CALIBRATION_FACTOR_A, CALIBRATION_OFFSET_X)  # Unused

# Data fusion function that seems important but isn't used in final path
def fuse_sensors(temp, humid, press):
    return [(t * 0.5 + h * 0.3 + p * 0.001) for t, h, p in zip(temp, humid, press)]

fused_index = fuse_sensors(temperature_readings, humidity_readings, pressure_readings)  # Computed but unused

# Decoy state tracking (red herring)
current_state = {'status': 'active', 'mode': 'normal', 'version': '2.1'}
state_history = []
for i in range(3):  # Limited logging simulation
    current_state['timestamp'] = i * 10
    state_history.append(current_state.copy())

# Real processing begins here
threshold = 22.0
valid_indices = [i for i, t in enumerate(temperature_readings) if t >= threshold]

filtered_data = [temperature_readings[i] for i in valid_indices]

# Secondary filter based on parity of index (bitwise distraction)
even_indexed = [v for i, v in enumerate(filtered_data) if (i & 1) == 0]

# Tertiary transformation with conditional expression
transformed = [val if val < 25 else val * 1.1 for val in even_indexed]

# Accumulation with dummy operations
accum = 0.0
weight_sequence = [1, 2, 1]
for i, val in enumerate(transformed):
    weight = weight_sequence[i % len(weight_sequence)]
    accum += val * weight

# Dummy statistical decoys
mean_temp = sum(temperature_readings) / len(temperature_readings)
std_dev = (sum((x - mean_temp) ** 2 for x in temperature_readings) / len(temperature_readings)) ** 0.5
outlier_count = sum(1 for x in temperature_readings if abs(x - mean_temp) > 1.5 * std_dev)

# Core diagnostic logic (uses only filtered_data and threshold)
def analyze_trend(data):
    if len(data) < 2:
        return 0
    return int(sum(data[i] < data[i+1] for i in range(len(data)-1)) * 10)

def compute_stability_score(data):
    if len(data) == 0:
        return 0
    return int(max(data) - min(data))

def evaluate_variance_level(data):
    if len(data) <= 1:
        return 0
    avg = sum(data) / len(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    return int(variance * 10)

def process_readings(data, limit):
    trend = analyze_trend(data)
    stability = compute_stability_score(data)
    variance_level = evaluate_variance_level(data)
    # Final computation: combines multiple logic paths
    result = (trend * 3) - (stability * 2) + variance_level
    # Additional logic step: correction based on threshold relation
    adjustment = 5 if limit == 22.0 else -5
    return result + adjustment

# Critical execution point
final_diagnostic = process_readings(filtered_data, threshold)

# Print result as required
print(f"Target result: {final_diagnostic}")