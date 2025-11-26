def analyze_sensor_data(readings):
    # Irrelevant helper function for data filtering
    filtered = [r for r in readings if r > -50 and r < 150]
    processed = [(idx, val * 0.5 + 32) for idx, val in enumerate(filtered)]
    return sum(val for _, val in processed)

def validate_temperature_pattern(data):
    # Misleading validation function that doesn't affect main logic
    pattern_check = [d % 2 == 0 for d in data]
    validation_score = len([p for p in pattern_check if p]) * 2.5
    return validation_score

def process_temperature_data(temperature_readings):
    # Dead code path - never executed
    if len(temperature_readings) > 100:
        return sum(temperature_readings) * 0.75
    
    # Main processing logic
    threshold = 25
    valid_readings = [temp for temp in temperature_readings if temp >= -10 and temp <= 40]
    
    # Irrelevant computation with bit operations
    temp_bits = [int(temp) & 0xFF for temp in valid_readings]
    bit_sum = sum(temp_bits)  # Never used
    
    # Key processing steps
    processed_temps = []
    for idx, temp in enumerate(valid_readings):
        if temp > threshold:
            processed_temps.append(temp * 0.8)
        else:
            processed_temps.append(temp * 1.2)
    
    # Final computation with list comprehension
    final_result = sum([temp * (idx + 1) for idx, temp in enumerate(processed_temps)])
    
    # Misleading intermediate calculation
    intermediate = final_result * 0.5 + 15
    
    return final_result

# Temperature sensor readings (some invalid)
temperature_readings = [-5, 18, 32, 27, -15, 45, 22, 38, 19, 24, 31, 28]

# Irrelevant variable assignments
sensor_count = len(temperature_readings)
max_temp = max(temperature_readings)
min_temp = min(temperature_readings)

# Dead code - never used
analysis_result = analyze_sensor_data(temperature_readings)
validation_result = validate_temperature_pattern(temperature_readings)

# Key execution point
final_processing_result = process_temperature_data(temperature_readings)

print(f"Target result: {final_processing_result}")