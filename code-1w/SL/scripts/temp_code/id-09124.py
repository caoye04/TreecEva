import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0]
humidity_readings = [45, 52, 61, 48, 55, 59, 43, 50, 54]
pressure_readings = [1013, 1015, 1010, 1018, 1014, 1012, 1016, 1011, 1017]

# Irrelevant backup sensor data (distractor)
backup_temps = [None] * len(temperature_readings)
for i in range(len(temperature_readings)):
    backup_temps[i] = round(temperature_readings[i] + 0.5, 1)  # Artificial offset

# Bitmask configuration for sensor validation (mixed use of bitwise and logic)
sensor_status_word = 0b1101
sensor_mask_valid = sensor_status_word & 0b1111
is_calibration_active = (sensor_status_word >> 3) & 1

# Decoy function - appears useful but unused in critical path
def validate_sensor_array(data_list, tolerance=0.5):
    return all(abs(a - b) < tolerance for a, b in zip(data_list, data_list[1:]))

# Threshold policy map - key to actual computation
threshold_map = {
    'temp_breach': 25.0,
    'humid_breach': 55,
    'pressure_stable_range': (1012, 1016)
}

# Diagnostic flags with misleading intermediate metrics
spike_count = 0
stability_index = 100.0
for i in range(1, len(temperature_readings)):
    if temperature_readings[i] > temperature_readings[i-1]:
        spike_count += 1
    else:
        stability_index *= 0.97

# Real processing begins: filter readings using combinatorics and enumeration
dynamic_pairs = list(itertools.combinations(range(len(temperature_readings)), 2))
high_temp_indices = [i for i, t in enumerate(temperature_readings) if t > threshold_map['temp_breach']]
valid_humidity_indices = [i for i, h in enumerate(humidity_readings) if h < threshold_map['humid_breach']]

# Cross-reference valid sensors using zip and filtering
filtered_data = []
for i, (t, h, p) in enumerate(zip(temperature_readings, humidity_readings, pressure_readings)):
    in_temp_range = i in high_temp_indices
    in_humid_safe = i in valid_humidity_indices
    in_pressure_stable = threshold_map['pressure_stable_range'][0] <= p <= threshold_map['pressure_stable_range'][1]
    
    # Dead code branch - never executed due to logic, but looks active
    diagnostic_flag = 0
    if False and is_calibration_active:
        diagnostic_flag = sum(backup_temps) // len(backup_temps)
    
    if in_temp_range or in_humid_safe or in_pressure_stable:
        filtered_data.append((t, h, p, i))

# Core processing function with lambda and enumeration
def process_readings(data, thresholds):
    # Weighted scoring using lambda
    weight_func = lambda x: 1.5 if x[0] > thresholds['temp_breach'] else 1.0
    
    total_score = 0.0
    index_offset = 0
    
    # Nested logic with red herring variables
    temp_anomalies = 0
    pressure_variance = 0.0
    for idx, (t, h, p, orig_idx) in enumerate(data):
        weight = weight_func((t, h, p, orig_idx))
        base_score = t * 0.4 + h * 0.3
        
        # Meaningless transformation chain (distractor)
        shifted_p = p - 1000
        normalized_p = shifted_p / 10
        pressure_variance += normalized_p ** 0.5
        
        if t > thresholds['temp_breach']:
            temp_anomalies += 1
            
        # Actual contribution to result
        total_score += base_score * weight
        
        if idx % 2 == 0:
            index_offset += orig_idx

    # Final computation with irrelevant adjustments
    adjustment_factor = 1.0
    if temp_anomalies > 2:
        adjustment_factor = 0.9
    elif temp_anomalies == 0:
        adjustment_factor = 1.1
    
    # Critical answer computation
    final_value = int((total_score - pressure_variance * 2) * adjustment_factor + index_offset)
    
    # Unused derived metrics (decoy outputs)
    avg_diagnostic = total_score / max(len(data), 1)
    system_health = 'STABLE' if avg_diagnostic > 50 else 'UNSTABLE'
    
    return final_value

# Trigger point: this assignment determines the answer
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")