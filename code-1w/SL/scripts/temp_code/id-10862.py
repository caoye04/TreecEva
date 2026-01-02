import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 18.2, 20.9, 24.5, 23.8]
humidity_readings = [45, 50, 52, 48, 60, 65, 40, 55, 49, 53]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1005, 1018, 1020, 1016, 1014]

# Irrelevant calibration coefficients (distractor)
calib_a, calib_b, calib_c = 1.02, 0.98, 1.05
offset_x, offset_y = 0.5, -0.3

# Misleading intermediate transformations (dead path)
adjusted_temps = [t * calib_a + offset_x for t in temperature_readings]
scaled_humidity = [(h + offset_y) * calib_b for h in humidity_readings]

# Data fusion function that isn't actually used (decoy)
def fuse_sensors(temp, hum, pres):
    return (temp * 0.6) + (hum * 0.3) + (pres * 0.001)

# Unused historical baseline (red herring)
historical_avg = {
    'temp': 22.5,
    'humidity': 51.0,
    'pressure': 1015.0
}

# Spurious alert system with unreachable logic (distractor)
alarm_triggered = False
threshold_deviation = 3.0
for t in temperature_readings:
    if abs(t - historical_avg['temp']) > threshold_deviation * 2:
        alarm_triggered = True
        break  # This loop never triggers due to data range

# Irrelevant bit manipulation on pressure values (misleading)
shifted_pressures = []
for p in pressure_readings:
    raw_val = int(p - 1000)
    processed = ((raw_val << 2) ^ 0x3) & 0xFF  # Obfuscated but unused
    shifted_pressures.append(processed)

# Real processing begins here — filtering based on valid temp-humidity correlation
def is_valid_reading(temp, hum):
    expected_hum = 30 + (temp - 18) * 2.5
    return abs(hum - expected_hum) <= 8

# Filter data using list comprehension (required feature)
valid_indices = [i for i in range(len(temperature_readings)) 
                 if is_valid_reading(temperature_readings[i], humidity_readings[i])]

filtered_data = [(temperature_readings[i], humidity_readings[i], pressure_readings[i]) 
                  for i in valid_indices]

# Secondary filter: remove readings where pressure < 1010 (additional logic)
filtered_data = [entry for entry in filtered_data if entry[2] >= 1010]

# Ancillary computation: average deviation (irrelevant result)
avg_temp = sum(t for t, _, _ in filtered_data) / len(filtered_data)
avg_deviation = sum(abs(t - avg_temp) for t, _, _ in filtered_data) / len(filtered_data)

# Core diagnostic algorithm
prev_factor = 1.75
running_score = 0.0

for temp, hum, pres in filtered_data:
    # Complex scoring with multiple dependencies
    base_score = math.log(pres) * (temp / 10)
    adjustment = math.sin(math.radians(hum)) * prev_factor
    running_score += base_score - adjustment
    prev_factor = adjustment  # Stateful dependency

    # Early termination condition based on internal state (key logic step)
    if running_score > 120:
        running_score *= 0.85
        break  # Break alters final accumulation

# Additional transformation chain
transformed_scores = []
current = running_score
for _ in range(4):
    current = math.sqrt(current + 10) if current > 0 else 0
    transformed_scores.append(current)

# Final aggregation with slicing (required feature)
use_last_three = transformed_scores[-3:]  # Slice operation
aggregate = sum(use_last_three) / len(use_last_three)

# Final diagnostic calculation
final_diagnostic = int((aggregate * 17.3) + 0.5)  # Rounded integer result

print(f"Result: {final_diagnostic}")