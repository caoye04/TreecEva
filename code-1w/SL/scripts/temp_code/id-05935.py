import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 19.3, 26.7, 27.1, 24.9, 23.8]
humidity_readings = [45, 48, 52, 43, 60, 39, 35, 50, 47]
pressure_readings = [1013, 1015, 1012, 1016, 1018, 1010, 1008, 1014, 1017]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.023
CALIBRATION_OFFSET_B = -0.017
REFERENCE_VOLTAGE = 3.3
MAX_SENSOR_NOISE = 0.05

# Decoy function - looks important but unused
def calibrate_sensor(raw_value, offset):
    return raw_value * (1 + offset) + 0.1

# Another red herring: complex noise filter never invoked
def apply_fourier_filter(signal):
    n = len(signal)
    transformed = [0] * n
    for k in range(n):
        for t in range(n):
            transformed[k] += signal[t] * (2 / n) ** 0.5 * (k * t / n)
    return transformed

# Misleading intermediate transformation
aggregated_stats = []
for i in range(len(temperature_readings)):
    score = (temperature_readings[i] * 0.4 + humidity_readings[i] * 0.3 + pressure_readings[i] * 0.001)
    aggregated_stats.append(round(score, 2))

# Fake anomaly detection with dead code path
def detect_anomaly(value, threshold=24.0):
    if value > threshold:
        return True
    else:
        return False  # Dead code below
    print('Anomaly flagged')
    log_entry = f"ALERT: {value} exceeds threshold"
    return True

# Real processing begins here — filtering based on temperature threshold
critical_threshold = 24.5
temp_above_threshold = list(filter(lambda x: x > critical_threshold, temperature_readings))
indices_of_interest = [i for i, temp in enumerate(temperature_readings) if temp > critical_threshold]

# Extract corresponding humidity and pressure using indices
humidity_subset = [humidity_readings[i] for i in indices_of_interest]
pressure_subset = [pressure_readings[i] for i in indices_of_interest]

# Construct tuples of relevant multi-sensor data
filtered_data = list(zip(temp_above_threshold, humidity_subset, pressure_subset))

# Auxiliary string processing distraction
sensor_location = "NORTH-WEST ARRAY"
formatted_tag = sensor_location.lower().replace('-', '_').upper()  # Result: "NORTH_WEST ARRAY"
encoded_prefix = ''.join([chr(ord(c) + 1) if c.isalpha() else c for c in formatted_tag[:5]])  # Distractor encoding

# Use of itertools to create redundant combinations (distraction)
all_combinations = list(itertools.combinations_with_replacement(['T', 'H', 'P'], 2))
dummy_mapping = {key: idx for idx, key in enumerate(all_combinations)}

# Core logic buried among noise
scaling_factor = 1.8
offset_correction = 32

# Simulated diagnostic computation chain
intermediate_values = []
for reading in filtered_data:
    temp_c, humidity_val, pressure_val = reading
    
    # Convert to Fahrenheit as part of diagnostic (has downstream impact)
    temp_f = temp_c * scaling_factor + offset_correction
    
    # Diagnostic score formula (key logic)
    diagnostic_score = (temp_f * 0.7) + (humidity_val * 0.2) - (pressure_val * 0.001)
    intermediate_values.append(diagnostic_score)

# Final aggregation step
baseline_shift = sum([(x - 24) for x in temp_above_threshold if x > 24.5])

# Main result calculation
raw_average = sum(intermediate_values) / len(intermediate_values)
adjusted_diagnostic = raw_average + (baseline_shift * 0.1)

# Secondary adjustment using string-derived value (subtle but valid)
shift_from_tag = len(encoded_prefix) * 0.2  # Depends on earlier string manipulation
final_diagnostic = round(adjusted_diagnostic + shift_from_tag, 4)

# Red herring: unused dictionary structure
data_summary = {
    'readings_count': len(filtered_data),
    'average_temperature': sum(temp_above_threshold) / len(temp_above_threshold),
    'max_humidity': max(humidity_subset),
    'diagnostic_debug': [f'{v:.1f}' for v in intermediate_values]
}

# This variable is the true answer target
print(f"Result: {final_diagnostic}")