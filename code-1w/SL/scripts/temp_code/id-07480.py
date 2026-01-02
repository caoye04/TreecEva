import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7, 22.5, 21.8, 25.1]
humidity_readings = [55, 60, 62, 58, 70, 65, 59, 63, 61, 57]
co2_levels = [410, 425, 405, 430, 460, 440, 415, 435, 420, 418]

# Irrelevant transformation: normalize temperatures to arbitrary scale
def normalize_temp(t):
    return (t - 20) * 1.8 + 32

normalized_temps = [normalize_temp(t) for t in temperature_readings]

# Misleading aggregation: compute average humidity (not used later)
avg_humidity = sum(humidity_readings) / len(humidity_readings)

# Distractor function: simulates air quality index but returns constant
def calculate_aqi(co2):
    if co2 < 400:
        return 3
    elif co2 < 450:
        return 2
    else:
        return 1  # capped for safety (unused in final logic)

# Another red herring: binary encoding of CO2 levels
co2_binary_flags = [bin(int(c))[2:] for c in co2_levels]
high_co2_flags = [len(flag) > 8 for flag in co2_binary_flags]  # always false

# Real processing begins: generate composite metrics using enumerate and zip
composite_metrics = []
for i, (temp, hum, co2) in enumerate(zip(temperature_readings, humidity_readings, co2_levels)):
    # Weighted formula influenced by all three factors
    metric = (temp * 1.1) + (hum * 0.8) - (co2 * 0.01)
    
    # Artificial adjustment based on index parity (adds complexity)
    adjustment = 1.5 if i % 2 == 0 else -1.2
    metric += adjustment
    
    # Conditional expression to simulate sensor reliability
    reliable = hum > 58 and co2 < 450
    final_metric = metric if reliable else metric * 0.9  # slight penalty
    
    composite_metrics.append(round(final_metric, 3))

# Dead code path: hypothetical correction for elevation (never applied)
elevation_correction = []
for j in range(len(composite_metrics)):
    correction = 0.0
    if j < 5:
        correction = math.sin(j * 0.5)
    else:
        correction = math.cos(j * 0.3)
    elevation_correction.append(correction)  # computed but unused

# Key filtering logic: only metrics from even indices with high temp
filtered_metrics = []
for idx, val in enumerate(composite_metrics):
    if idx % 2 == 0 and temperature_readings[idx] > 23.0:
        filtered_metrics.append(val)

# Decoy list comprehension: computes squared differences but unused
unused_deltas = [round((composite_metrics[i] - temperature_readings[i])**2, 2) for i in range(len(composite_metrics))]

# Critical assignment point
filtration_score = sum(filtered_metrics)

# Final output
print(f"Result: {filtration_score}")