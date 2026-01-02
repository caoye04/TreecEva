from itertools import combinations

# Simulated sensor readings and calibration data
temperature_readings = [23.4, 24.1, 22.9, 25.0, 23.8]
humidity_readings = [45, 47, 50, 44, 46]
pressure_readings = [1013, 1015, 1012, 1016, 1014]

# Misleading auxiliary variables (distractors)
external_bias = sum([x ** 0.5 for x in humidity_readings]) / len(humidity_readings)
baseline_offset = max(pressure_readings) - min(pressure_readings)
synthetic_index = 0
for i in range(len(temperature_readings)):
    synthetic_index += (temperature_readings[i] * humidity_readings[i]) % 7

# Core processing: detect anomalies using pairwise thresholds
anomaly_count = 0
critical_pairs = list(combinations(range(len(temperature_readings)), 2))
for i, j in critical_pairs:
    temp_diff = abs(temperature_readings[i] - temperature_readings[j])
    humid_diff = abs(humidity_readings[i] - humidity_readings[j])
    if temp_diff > 1.0 and humid_diff > 3:
        anomaly_count += 1

# Secondary computation with lambda-based filtering
efficiency_filter = lambda x: x > 23.5
valid_temps = list(filter(efficiency_filter, temperature_readings))
adjustment = len(valid_temps) * 0.8 if anomaly_count < 3 else len(valid_temps) * 0.5

# Red herring: complex but unused calculation
unused_entropy = sum(
    a ^ b for a, b in zip(
        [int(x) for x in pressure_readings], 
        [int(x * 2) % 100 for x in temperature_readings]
    )
) // len(pressure_readings)

# State tracking with conditional updates
system_state = 'STABLE'
if anomaly_count >= 2:
    system_state = 'CAUTION'
    adjustment -= 0.6
elif anomaly_count == 0:
    system_state = 'OPTIMAL'
    adjustment += 0.3

# Final diagnostic score components
base_metric = sum(temperature_readings) / len(temperature_readings)
aggregate_score = int(base_metric * 10) + anomaly_count * 2

correction_factor = 0
correction_factor += len(critical_pairs) % 5
correction_factor += int(external_bias) % 4

# Key assignment statement
final_diagnostic = aggregate_score + correction_factor

print(f"Result: {final_diagnostic}")