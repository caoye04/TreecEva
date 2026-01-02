import math

# Simulated environmental sensor data with noise and calibration offsets
temperature_readings = [23.5, 24.1, 22.9, 25.6, 26.7, 21.4, 20.8, 27.3, 26.9, 25.1]
humidity_data = [45, 47, 50, 52, 48, 55, 53, 49, 46, 51]
elevation_zones = ['low', 'low', 'mid', 'mid', 'high', 'high', 'mid', 'low', 'high', 'mid']

timestamps = ['08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15']

# Irrelevant transformation: Humidity smoothing (dead path)
smoothed_humidity = []
for i, val in enumerate(humidity_data):
    if i == 0:
        smoothed_humidity.append(val)
    else:
        smoothed_humidity.append((val + humidity_data[i-1]) / 2)

# Decoy statistical analysis on elevation (distractor)
elevation_stats = {}
for zone in elevation_zones:
    elevation_stats[zone] = elevation_stats.get(zone, 0) + 1

# Actual processing: Detect anomalies in temperature using rolling window
anomalies = []
moving_avg_window = 3
rolling_averages = []

for i in range(len(temperature_readings) - moving_avg_window + 1):
    window = temperature_readings[i:i + moving_avg_window]
    avg_temp = sum(window) / moving_avg_window
    rolling_averages.append(avg_temp)
    
    # Flag if current reading exceeds average by threshold
    if window[-1] > avg_temp * 1.08:
        anomalies.append(i + moving_avg_window - 1)

# Misleading alternate detection logic (unused branch)
strong_gradients = []
for i in range(1, len(temperature_readings)):
    delta = abs(temperature_readings[i] - temperature_readings[i-1])
    if delta > 1.5:
        strong_gradients.append(i)

# Key signal: Only use anomaly detection based on rolling average
if len(anomalies) == 0:
    anomalies.append(0)

# Simulate diagnostic calibration curve (irrelevant computations)
calibration_curve = {}
for i in range(100):
    x = i / 10.0
    y = math.sin(x) * math.exp(-x/20)
    calibration_curve[round(x, 1)] = round(y, 4)

# Extract raw temperature profile adjusted for sensor bias (relevant)
sensor_bias = 0.7
adjusted_temps = [t - sensor_bias for t in temperature_readings]
temperature_profile = dict(enumerate(adjusted_temps))

# Determine correction factor from auxiliary data (partially relevant)
humidity_ratio = sum(humidity_data) / len(humidity_data)
correction_factor = 1.0

if humidity_ratio > 50:
    correction_factor = 0.95
elif humidity_ratio < 45:
    correction_factor = 1.05
else:
    correction_factor = 1.02

# Spurious string-based timestamp analysis (distractor)
time_categories = {"morning": [], "late_morning": []}
for idx, t in enumerate(timestamps):
    hour = int(t.split(':')[0])
    if hour <= 9:
        time_categories["morning"].append(idx)
    else:
        time_categories["late_morning"].append(idx)

# Use only anomalies list to determine final diagnostic index
anomaly_indices = sorted(list(set(anomalies)))  # Remove duplicates if any

# Introduce bit manipulation red herring (irrelevant)
bit_encoded = 0
for idx in anomaly_indices:
    bit_encoded |= (1 << idx)
bit_decoded = []
for i in range(10):
    if bit_encoded & (1 << i):
        bit_decoded.append(i)

# Final computation: target result
final_diagnostic = temperature_profile[anomaly_indices[-1]] * correction_factor

# Output result
print(f"Result: {final_diagnostic}")