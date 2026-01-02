import math

# Simulated sensor array data (temperature, pressure, humidity)
sensor_inputs = [
    (23.4, 101.3, 45.0),
    (25.1, 102.0, 47.8),
    (19.8, 99.7, 52.1),
    (24.3, 100.5, 44.3),
    (20.0, 101.0, 55.5),
    (22.7, 103.2, 48.9),
    (26.5, 98.4, 43.0),
    (18.2, 102.8, 60.2)
]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.037
CALIBRATION_OFFSET_B = -0.021
REFERENCE_VOLTAGE = 3.3

# Decoy function - looks important but unused
def calibrate_sensor(raw_value, offset):
    return raw_value * (1 + offset) + 0.1

# Auxiliary transformation (not directly used in main path)
def adjust_for_altitude(pressure, altitude_m=150):
    return pressure * math.exp(-altitude_m / 7000)

# Red herring: temperature conversion with no impact
converted_temps = [round((t - 32) * 5/9, 2) for t in [75, 77, 80, 70, 82, 74, 79, 68]]  # Fake F to C

# Real processing begins here
baseline_temp = sum(t for t, p, h in sensor_inputs) / len(sensor_inputs)
baseline_pressure = sum(p for t, p, h in sensor_inputs) / len(sensor_inputs)

# Filter criteria: only readings where temp > avg and humidity < 50%
filtered_data = [(t, p, h) for t, p, h in sensor_inputs if t > baseline_temp and h < 50.0]

# Secondary filter distractor (dead code path)
temp_stable_readings = []
for reading in sensor_inputs:
    t, p, h = reading
    if abs(t - baseline_temp) < 2.0:
        temp_stable_readings.append(reading)

# Another decoy list comprehension (unused)
normalized_humidity = [h / 100.0 for t, p, h in sensor_inputs if h > 0]

# Bit manipulation red herring (simulates checksum but irrelevant)
def compute_fake_checksum(data_list):
    checksum = 0
    for i, (t, p, h) in enumerate(data_list):
        val = int(t * 10) ^ int(p * 10) | (i << 2)
        checksum ^= val
    return checksum & 0xFFFF

fake_diagnostic_code = compute_fake_checksum(sensor_inputs)  # Computed but unused

# Key signal weighting (actual relevant logic)
def weight_reading(temp, press, humid):
    temp_factor = (temp - 20.0) * 1.8
    press_factor = (press - 100.0) * 0.5
    humid_factor = max(0, 50 - humid) * 0.3
    return temp_factor + press_factor + humid_factor

# Apply weighting to filtered data
weighted_scores = [weight_reading(t, p, h) for t, p, h in filtered_data]

# Aggregation with rounding distraction
aggregate_score = sum(weighted_scores)
rounded_aggregate = round(aggregate_score * 100) / 100

# Additional misleading transformation
inverted_diagnostic = 1.0 / (1.0 + math.exp(-rounded_aggregate)) if rounded_aggregate < 10 else 0.99

# Final processing function
def process_readings(readings):
    if not readings:
        return -999.0
    total = 0.0
    for t, p, h in readings:
        contribution = t * 0.4 + p * 0.35 - h * 0.1
        total += contribution
    return round(total, 4)

# Critical execution point
final_diagnostic = process_readings(filtered_data)

print(f"Result: {final_diagnostic}")