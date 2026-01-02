from itertools import cycle

# Simulate sensor data readings over time with some noise
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.0, 23.7]
humidity_readings = [45, 47, 50, 44, 52, 48, 46, 51]

# System thresholds
TEMP_THRESHOLD = 24.0
HUMIDITY_WARNING = 49

# Misleading auxiliary variables (distractors)
baseline_offset = 0.5
compensation_factor = 1.02
adjusted_values = []
normalization_sum = 0.0

# Tracking state across sensors
sensor_status = {}
reading_cycles = 0
valid_data_count = 0

# Simulate cycling through sensors
clock_cycle = cycle([1, 2, 3])

for i in range(len(temperature_readings)):
    # Pull current sensor data
    temp = temperature_readings[i]
    humid = humidity_readings[i]
    
    # Apply meaningless compensation (distractor logic)
    compensated_temp = (temp + baseline_offset) * compensation_factor
    adjusted_values.append(round(compensated_temp, 2))

    # Normalize humidity with irrelevant sum accumulation
    normalized_humid = humid / 100.0
    normalization_sum += normalized_humid  # Not used later

    # Determine status based on thresholds
    temp_alert = temp >= TEMP_THRESHOLD
    humid_alert = humid >= HUMIDITY_WARNING

    # Update status with misleading complexity
    status_flag = 'OK'
    if temp_alert and humid_alert:
        status_flag = 'CRITICAL'
    elif temp_alert or humid_alert:
        status_flag = 'WARNING'
    
    sensor_status[f'Sensor_{i+1}'] = status_flag

    # Count valid high-temp readings (actually used later)
    if temp > TEMP_THRESHOLD:
        valid_data_count += 1

    # Simulate clock tick (irrelevant to final result)
    reading_cycles += next(clock_cycle)

# Secondary processing: analyze pattern of valid counts
pattern_match = 0
for count in range(1, valid_data_count + 1):
    # Some arbitrary modular pattern check
    if (count * 3) % 4 == 1:
        pattern_match += 1

# Introduce conditional expression using itertools result
sequence_active = any(x > 25 for x in temperature_readings)
bonus_weight = 1.5 if sequence_active else 1.0

# Actual key computation chain
raw_score = 0
for temp in temperature_readings:
    if temp >= TEMP_THRESHOLD:
        raw_score += int(temp)  # truncate and accumulate

# Final performance rating depends only on raw_score, bonus_weight, and pattern_match
def calculate_performance_rating():
    base = raw_score * 2
    adjustment = pattern_match * 5
    total = base + adjustment
    return int(total * bonus_weight)  # Only this matters

final_score = calculate_performance_rating()
print(f"Result: {final_score}")