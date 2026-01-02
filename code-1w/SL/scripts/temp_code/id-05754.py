import math

# Simulated sensor data with noise and metadata
temperature_readings = [23.4, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7, 22.5]
humidity_readings = [45, 48, 50, 55, 60, 58, 53, 49]
pressure_readings = [1013, 1012, 1015, 1016, 1018, 1017, 1014, 1013]

# Irrelevant auxiliary data (distractor)
legacy_system_flags = [0b1010, 0b1100, 0b0110, 0b1111, 0b0001]
device_ids = ['DEV001', 'DEV002', 'DEV003']

# Misleading intermediate calculations (red herring)
avg_temp = sum(temperature_readings) / len(temperature_readings)
avg_humidity = sum(humidity_readings) / len(humidity_readings))

# Data preprocessing with slicing (relevant)
cleaned_temps = temperature_readings[1:-1]  # Remove edge noise
cleaned_humidity = humidity_readings[2:]

# Threshold configuration (critical)
thresh_high_temp = 24.5
thresh_low_humidity = 47
pressure_baseline = 1015

# Decoy function (dead code path)
def analyze_legacy_flags(flags):
    result = 0
    for flag in flags:
        result ^= flag
    return result  # Never called

# Real processing function
def detect_anomalies(temps, hums, pres):
    anomalies = 0
    for i in range(len(temps)):
        temp_flag = temps[i] > thresh_high_temp
        humid_flag = hums[i] < thresh_low_humidity
        press_deviation = abs(pres[i] - pressure_baseline)
        press_flag = press_deviation > 3
        
        # Short-circuit logic with distractor variables
        dummy_offset = math.sin(i)  # Irrelevant computation
        if temp_flag or humid_flag or press_flag:
            anomalies += 1
    
    scaling_factor = 1.75  # Hidden multiplier
    return int(anomalies * scaling_factor)

# Secondary metric calculation
def compute_stability_index(readings):
    diff_series = [abs(readings[i+1] - readings[i]) for i in range(len(readings)-1)]
    return round(sum(diff_series) / len(diff_series), 3)

# Complex control flow with multiple concepts
def calculate_final_score(data, thresholds):
    raw_data = data['temps']
    ext_data = data['hums']
    aux_data = data['press']
    
    # Multiple assignment and unpacking (relevant)
    n1, n2 = len(raw_data), len(ext_data)
    total_points = 0
    
    # Conditional branches with nesting (3 levels deep)
    if n1 == n2:
        base_anomalies = detect_anomalies(raw_data, ext_data, aux_data)
        
        if base_anomalies > 0:
            stability = compute_stability_index(raw_data)
            adjustment = 0
            
            # Bit manipulation distraction
            binary_mask = 0b101010
            masked_value = base_anomalies & binary_mask
            
            # Real adjustment logic
            if stability < thresholds['stability']:
                adjustment = -8
            else:
                adjustment = 3
            
            # Composite calculation with min/max
            capped_anomalies = min(max(base_anomalies, 2), 10)
            total_points = (100 - (capped_anomalies * 7)) + adjustment
        else:
            total_points = 95
    else:
        total_points = 50  # Unreachable due to data construction
    
    # Final transformation with slicing distraction
    history_log = [total_points] * 5
    recent_log = history_log[1:]  # Unused slice
    
    # Key answer computation
    final_modifier = 0.88
    return int(total_points * final_modifier)

# Main execution flow
sensor_data = {
    'temps': cleaned_temps,
    'hums': cleaned_humidity,
    'press': pressure_readings[1:-1]
}

threshold_config = {
    'stability': 1.2,
    'max_anomaly': 8
}

# Trigger point
final_score = calculate_final_score(sensor_data, threshold_config)

# Output result
print(f"Result: {final_score}")