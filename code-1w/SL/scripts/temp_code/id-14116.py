import math

# Simulated sensor data from multiple environmental monitors
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7, 25.1]
humidity_readings = [45, 47, 50, 52, 48, 55, 53, 49]
co2_levels = [400, 410, 395, 420, 430, 415, 425, 405]

# Irrelevant calibration constants (distractors)
CALIBRATION_FACTOR_A = 0.987
REFERENCE_OFFSET_X = 1.023
MAX_TOLERANCE_BAND = 5.5
BASELINE_DRIFT_CORRECTION = 0.003

# Preprocess function with red herring logic
def preprocess_sensors(data, mode='standard'):
    if mode == 'standard':
        scale = 1.0
    elif mode == 'calibrated':
        scale = CALIBRATION_FACTOR_A
    else:
        scale = 1.0

    # Distractor: unused transformation path
    adjusted = []
    for val in data:
        transformed = val * scale + BASELINE_DRIFT_CORRECTION
        if transformed > MAX_TOLERANCE_BAND:  # Never relevant for temperature
            adjusted.append(transformed / 10)
        else:
            adjusted.append(transformed)

    # Actual relevant computation
    cleaned = [round(x, 1) for x in data]  # list comprehension used
    return cleaned

# Misleading auxiliary function that appears important but is unused
def compute_humidity_index(temp, hum):
    # Heat index approximation (not actually used)
    return -8.7846 + 1.611 * hum + 2.3385 * temp - 0.146 * temp * hum

# Another decoy function with bit manipulation red herring
def encode_status_code(code, flags=0b101):
    # Bitwise operations as distraction
    encoded = (code << 2) ^ flags | 0b1100
    parity = bin(encoded).count('1') % 2
    return encoded + parity

# Core processing function with conditional expressions and tuple unpacking
def process_environmental_data(temp_data, humidity_data):
    avg_temp = sum(temp_data) / len(temp_data)
    avg_humidity = sum(humidity_data) / len(humidity_data)

    # Complex conditional expression with tuple returns
    status = ('stable', 'optimal') if avg_temp < 25.0 and avg_humidity < 50 \
             else ('fluctuating', 'suboptimal') if avg_temp >= 25.0 or avg_humidity >= 50 \
             else ('unknown', 'undetermined')

    # Tuple unpacking with irrelevant second element
    primary_status, _ = status

    # Distractor: unused derived metrics
    temp_variance = sum((t - avg_temp) ** 2 for t in temp_data) / len(temp_data)
    dew_point_approx = avg_temp - ((100 - avg_humidity) / 5)

    # Relevant transformation: normalize CO2 relative to baseline
    co2_baseline = 400
    co2_anomalies = [c - co2_baseline for c in co2_levels]
    significant_deviation = any(abs(x) > 20 for x in co2_anomalies)

    # Return tuple: actual usage pattern in next function
    return (avg_temp, avg_humidity, primary_status, significant_deviation)

# Analysis function with string methods as distraction
def analyze_readings(metrics_tuple, sensitivity_threshold):
    mean_temp, mean_humid, sys_status, co2_alert = metrics_tuple

    # String-based status mapping with irrelevant transformations
    status_map = {
        'stable': 1,
        'fluctuating': 2,
        'critical': 3
    }
    numeric_status = status_map.get(sys_status, 0)

    # Distractor: elaborate string processing that doesn't affect outcome
    diagnostic_tag = f"SYS-{numeric_status:02d}-ENV"
    tag_parts = diagnostic_tag.split('-')
    validation_checksum = ''.join([part[0] for part in tag_parts])  # 'SSE'

    # Irrelevant normalization chain
    normalized_temp = (mean_temp - 20) / 5
    adjusted_humidity = mean_humid * 1.02

    # Core logic buried among distractions
    base_score = 100 * (1 + math.sin(math.pi * normalized_temp / 10))

    # Conditional adjustment based on CO2 alert (key dependency)
    modifier = 0.85 if co2_alert else 1.15

    # Final computation - this is what matters
    raw_diagnostic = base_score * modifier * (0.9 + numeric_status * 0.05)

    # Additional red herring: unused precision refinement
    decimal_part = str(raw_diagnostic).split('.')[-1]
    length_penalty = len(decimal_part) * 0.001
    final_diagnostic = round(raw_diagnostic - length_penalty, 4)

    return final_diagnostic

# Execution flow with dead code paths
if __name__ == '__main__':
    # Preprocess all sensor streams (only temperature and humidity are fully used)
    processed_temps = preprocess_sensors(temperature_readings, mode='standard')
    processed_humid = preprocess_sensors(humidity_readings, mode='standard')

    # Dead code branch - never executed
    debug_mode = False
    if debug_mode:
        print("Debug: Raw CO2 levels:", co2_levels)
        encoded = encode_status_code(5, 0b111)
        print("Encoded status:", encoded)

    # Main data processing pipeline
    system_metrics = process_environmental_data(processed_temps, processed_humid)
    threshold = 1.1

    # Critical statement
    final_diagnostic = analyze_readings(system_metrics, threshold)

    # Print result as required
    print(f"Result: {final_diagnostic}")