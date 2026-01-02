import math

# Simulated sensor array data from environmental monitoring system
temperature_readings = [22.1, 19.5, 24.3, 26.7, 18.2, 20.8, 25.0, 23.4, 19.0, 27.1]
humidity_readings = [45, 50, 60, 65, 40, 55, 70, 53, 48, 68]
pressure_readings = [1013, 1015, 1010, 1008, 1017, 1014, 1005, 1012, 1016, 1009]

# Irrelevant calibration constants for unused sensors
gas_sensor_offset = 0.87
light_calibration_factor = 1.04
vibration_threshold_bias = -0.33

# Distractor: unused transformation function
def transform_signal(data, factor=1.0, offset=0.0):
    return [x * factor + offset for x in data]

# Unused helper that appears relevant but isn't called
def normalize_range(values, min_val=0, max_val=100):
    actual_min, actual_max = min(values), max(values)
    return [(x - actual_min) / (actual_max - actual_min) * (max_val - min_val) + min_val for x in values]

# Real processing begins here
raw_magnitude = [math.sqrt(t**2 + h**2) for t, h in zip(temperature_readings, humidity_readings)]

# Apply dynamic filtering based on pressure variance
mean_pressure = sum(pressure_readings) / len(pressure_readings)
pressure_deviation = [abs(p - mean_pressure) for p in pressure_readings]

# Determine which readings exceed adaptive threshold
adaptive_mask = [dev > 5 for dev in pressure_deviation]

# Filter magnitude only where pressure deviation is significant
filtered_data = [raw_magnitude[i] for i in range(len(raw_magnitude)) if adaptive_mask[i]]

# Decoy accumulation (dead code path - never used again)
cumulative_index = 0
for i, val in enumerate(filtered_data):
    cumulative_index += i * val % 7

def calculate_entropy(data):
    # This function is defined but not used in critical path
    from collections import Counter
    counts = Counter([round(x) for x in data])
    total = len(data)
    return -sum((freq/total) * math.log(freq/total) for freq in counts.values())

# Threshold levels computed from statistical properties
base_threshold = sum(filtered_data) / len(filtered_data)
variance = sum((x - base_threshold) ** 2 for x in filtered_data) / len(filtered_data)
std_dev = math.sqrt(variance)

# Multiple threshold criteria with some irrelevant combinations
threshold_levels = {
    'critical': base_threshold + 2 * std_dev,
    'warning': base_threshold + 0.5 * std_dev,
    'info': base_threshold - std_dev,
    'unused_mode': base_threshold * 1.1
}

# Red herring: complex state machine that doesn't affect outcome
system_state = 'INIT'
for temp in temperature_readings[:3]:
    if temp > 20:
        system_state = 'ACTIVE' if system_state != 'ERROR' else 'ERROR'
    elif temp < 19:
        system_state = 'ERROR'
    else:
        system_state = 'STANDBY'

# Real analysis function - depends only on filtered_data and threshold_levels['critical']
def analyze_readings(readings, thresholds):
    critical_level = thresholds['critical']
    warning_level = thresholds['warning']
    
    # Count how many readings are in each category
    above_critical = len([r for r in readings if r > critical_level])
    between_levels = len([r for r in readings if warning_level <= r <= critical_level])
    below_warning = len([r for r in readings if r < warning_level])
    
    # Compute weighted diagnostic score
    score = (above_critical * 10) + (between_levels * 3) + (below_warning * 1)
    
    # Apply non-linear correction based on data spread
    if len(readings) > 1:
        range_val = max(readings) - min(readings)
        spread_factor = math.log(1 + range_val) / (1 + math.log(len(readings)))
        score *= spread_factor
    
    # Final adjustment using bit manipulation (obscure but deterministic)
    int_score = int(score)
    processed = (int_score ^ 0xABC) + (int_score & 0x3F) - (int_score >> 4)
    
    # Irrelevant floating point adjustments
    noise_component = math.sin(len(readings) * 0.1) * 0.01
    return round(processed + noise_component, 4)

# Dead code: alternative analysis never invoked
def legacy_analysis(seq):
    result = 0
    for i in range(len(seq)):
        result ^= int(seq[i] * 100) & 0xFF
    return result

# Key execution point
final_diagnostic = analyze_readings(filtered_data, threshold_levels)

# Print result as required
print(f"Result: {final_diagnostic}")