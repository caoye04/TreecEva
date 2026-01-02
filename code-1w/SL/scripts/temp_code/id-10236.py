import math

# Simulate sensor data from a thermal regulation system
temperature_readings = [23.5, 24.1, 25.0, 26.8, 27.3, 25.9, 24.7]
humidity_levels = [45, 47, 50, 55, 53, 49, 46]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1013, 1011]

# Misleading intermediate calculations (distractors)
total_variance = 0.0
for i in range(len(temperature_readings) - 1):
    total_variance += (temperature_readings[i+1] - temperature_readings[i]) ** 2

avg_temp = sum(temperature_readings) / len(temperature_readings)
drift_rate = (temperature_readings[-1] - temperature_readings[0]) / len(temperature_readings)

# Irrelevant transformation using string methods (red herring)
data_ids = [f'TEMP_{str(i).zfill(3)}' for i in range(len(temperature_readings))]
valid_sensors = list(filter(lambda x: 'TEMP_0' in x and int(x.split('_')[1]) % 2 == 0, data_ids))

# Data processing pipeline
processed_data = []
for i, temp in enumerate(temperature_readings):
    # Compute derived humidity-adjusted index (semi-relevant)
    adjusted_index = temp * (1 + humidity_levels[i] / 1000)
    
    # Apply non-linear correction based on pressure deviation
    baseline_pressure = 1013
    pressure_ratio = pressure_readings[i] / baseline_pressure
    corrected_value = adjusted_index * math.sqrt(pressure_ratio)
    
    # Store tuple with some redundant fields
    processed_data.append((i, temp, humidity_levels[i], corrected_value))

# Helper function to compute system efficiency
def calculate_efficiency(data_list):
    if not data_list:
        return 0.0
    
    # Extract only the corrected values
    corrected_values = [entry[3] for entry in data_list]
    
    # Compute moving average over 3 points (if possible)
    smoothed = []
    for i in range(len(corrected_values)):
        window = corrected_values[max(0, i-1):min(len(corrected_values), i+2)]
        smoothed.append(sum(window) / len(window))
    
    # Efficiency defined as ratio of variance reduction
    original_var = sum((x - sum(corrected_values)/len(corrected_values))**2 for x in corrected_values) / len(corrected_values)
    smoothed_var = sum((x - sum(smoothed)/len(smoothed))**2 for x in smoothed) / len(smoothed)
    
    # Final efficiency score
    efficiency = (original_var - smoothed_var) / original_var if original_var > 0 else 0
    
    # Dead code branch (never executed due to data size)
    if len(data_list) < 3:
        fallback = 0
        for v in corrected_values:
            fallback += math.log(abs(v) + 1)
        return fallback
    
    return efficiency

# Critical statement
intermediate_flag = len(valid_sensors) > 3
baseline_offset = max(humidity_levels) - min(humidity_levels)
efficiency_score = calculate_efficiency(processed_data)

# Print result
print(f'Result: {efficiency_score}')