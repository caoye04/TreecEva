import math

# Simulated sensor readings with noise and calibration data
temperature_readings = [23.4, 24.1, 22.9, 25.6, 26.7, 24.3, 23.8]
humidity_readings = [45, 47, 50, 44, 60, 58, 52]
pressure_readings = [1013, 1012, 1015, 1010, 1008, 1009, 1011]

# Irrelevant auxiliary metrics (distractors)
power_cycles = [1, 0, 1, 1, 0, 1, 1]
packet_loss_rate = [0.01, 0.03, 0.02, 0.01, 0.05, 0.04, 0.02]
signal_strength = [-75, -70, -80, -72, -68, -74, -71]

# Calibration offset (red herring - not used in final calculation)
calibration_offset = sum([abs(t - 24.0) for t in temperature_readings]) / len(temperature_readings)

# Noise filter threshold (misleading intermediate)
noise_threshold = 1.5 if len(temperature_readings) > 5 else 0.5

# Data validation function (partially dead code path)
def validate_sensor_data(data, sensor_type):
    if sensor_type == 'temp':
        return all(15 < x < 40 for x in data)
    elif sensor_type == 'humidity':
        return all(20 <= x <= 80 for x in data)
    else:
        return False  # Unused sensor types

# Unused validation calls (dead code - distractor)
valid_temp = validate_sensor_data(temperature_readings, 'temp')
valid_humid = validate_sensor_data(humidity_readings, 'humidity')

# Signal quality score (irrelevant computation)
mean_signal = sum(signal_strength) / len(signal_strength)
adjusted_packet_loss = sum([p * 100 for p in packet_loss_rate]) / len(packet_loss_rate)
signal_quality_score = mean_signal / (1 + adjusted_packet_loss)

# Primary processing pipeline
processed_temps = []
for temp in temperature_readings:
    corrected = temp + 0.2  # Minor calibration
    if corrected < 24.0:
        processed_temps.append(corrected * 1.02)
    else:
        processed_temps.append(corrected)

# Humidity transformation with conditional expression
processed_humidity = [h_val if h_val <= 50 else h_val * 0.95 for h_val in humidity_readings]

# Composite index calculation (relevant but partially obscured)
def compute_stability_index(temps, humidity_vals):
    temp_variability = max(temps) - min(temps)
    humid_range = max(humidity_vals) - min(humidity_vals)
    
    # Complex interaction formula
    base_stability = 100 - (temp_variability * 2.5) - (humid_range * 1.2)
    
    # Adjustments based on trend (not actually used - misleading)
    temp_trend = temps[-1] - temps[0]
    if temp_trend > 1:
        base_stability -= 5
    elif temp_trend < -1:
        base_stability += 3
        
    return base_stability  # This adjustment is ignored later

# Dead-end function (decoy)
def deprecated_analysis(data_list):
    """Old method no longer in use"""
    return sum(d ** 0.5 for d in data_list if d > 0) // len(data_list)

# Unused transformation chain
legacy_processed = list(map(lambda x: x * 0.98 + 0.5, pressure_readings))
deprecated_metric = deprecated_analysis(legacy_processed)

# Main aggregation logic
aggregated_temp = sum(processed_temps) / len(processed_temps)
aggregated_humid = sum(processed_humidity) / len(processed_humidity)

# Weighted contribution model
weight_temp = 0.6
weight_humid = 0.4

# Conditional expression used in core logic
base_score = aggregated_temp * weight_temp + aggregated_humid * weight_humid

# Secondary adjustment using bit manipulation (actual relevance)
adjustment_factor = len([t for t in temperature_readings if t > 24.0])
bit_encoded_adj = adjustment_factor << 2  # Multiply by 4 using left shift

# Final non-linear transformation
def calculate_final_score(cleaned_data):
    raw = base_score  # Base from earlier
    
    # Apply shift-based adjustment
    interim = raw + bit_encoded_adj
    
    # Non-linear compression
    if interim > 50:
        result = math.log(interim) * 10
    else:
        result = interim * 1.5
        
    # Final clamping (never triggered - red herring)
    if result < 0:
        return 0
    elif result > 1000:
        return 1000
    else:
        return result

# Execution point of interest
processed_data = {
    'temps': processed_temps,
    'humidity': processed_humidity,
    'meta': {'count': len(temperature_readings)}
}

final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")