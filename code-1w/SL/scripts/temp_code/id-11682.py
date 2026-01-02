from collections import defaultdict, Counter
import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1, 23.7]
humidity_readings = [45, 47, 50, 44, 46, 52, 43, 48]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017, 1013]

# Irrelevant transformation - red herring for atmospheric modeling
transformed_pressure = [p * 0.001 for p in pressure_readings]
decoy_integral = sum(transformed_pressure) * len(pressure_readings)

# Real processing path begins: anomaly detection in temperature
moving_avg_temp = []
for i in range(2, len(temperature_readings)):
    avg = (temperature_readings[i-2] + temperature_readings[i-1] + temperature_readings[i]) / 3
    moving_avg_temp.append(avg)

# Identify deviations exceeding threshold
anomalies = []
for i, temp in enumerate(temperature_readings[2:], start=2):
    if abs(temp - moving_avg_temp[i-2]) > 0.8:
        anomalies.append(i)

# Humidity correlation tracking (partially relevant)
correlation_map = defaultdict(int)
for idx in anomalies:
    if idx < len(humidity_readings):
        band = (humidity_readings[idx] // 5) * 5
        correlation_map[band] += 1

# Decoy statistical analysis with chi-squared (irrelevant)
decoy_freq = Counter(humidity_readings)
expected = sum(decoy_freq.values()) / len(decoy_freq)
chi_squared = sum((v - expected) ** 2 / expected for v in decoy_freq.values())

# Real signal: counting consecutive high-pressure sequences
high_pressure_streaks = 0
current_streak = 0
for p in pressure_readings:
    if p > 1014:
        current_streak += 1
    else:
        if current_streak >= 2:
            high_pressure_streaks += 1
        current_streak = 0
if current_streak >= 2:
    high_pressure_streaks += 1

# Misleading entropy calculation (dead end)
entropy_decoy = 0
value_counts = Counter(temperature_readings)
total = len(temperature_readings)
for count in value_counts.values():
    prob = count / total
    entropy_decoy -= prob * __import__('math').log2(prob) if prob > 0 else 0

# Key diagnostic logic
baseline_anomaly_weight = len(anomalies) * 100
streak_bonus = high_pressure_streaks * 50
aggregate_score = baseline_anomaly_weight + streak_bonus

# Correction based on humidity-pressure co-occurrence (critical)
validations = 0
for i in range(len(pressure_readings)):
    if i < len(humidity_readings) and pressure_readings[i] > 1015 and humidity_readings[i] < 45:
        validations += 1

# Dead code path - looks important but unused
unused_validation_score = 0
for window in itertools.combinations(pressure_readings, 3):
    if sum(window) > 3045:
        unused_validation_score += 1

# Critical correction factor
if validations >= 2:
    correction_factor = 23
else:
    correction_factor = -17

# Final diagnostic computation (target statement)
final_diagnostic = aggregate_score + correction_factor

# Output result
print(f"Result: {final_diagnostic}")