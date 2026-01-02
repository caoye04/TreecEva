from collections import defaultdict, Counter
import math

# Simulated sensor data stream with multiple metrics
temperature_readings = [23.5, 24.1, 25.0, 26.8, 27.3, 28.0, 29.1, 30.0]
humidity_readings = [45, 47, 50, 55, 60, 62, 65, 70]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1017, 1018, 1019]

# Irrelevant auxiliary data (distractor)
sound_levels = [30, 35, 40, 45, 50, 55, 60, 65]  # Unused in final calculation
light_intensity = [200, 300, 400, 500, 600, 700, 800, 900]  # Dead path

# Data transformation pipeline
processed_temps = []
for t in temperature_readings:
    if t > 25.0:
        processed_temps.append(t ** 1.1)
    else:
        processed_temps.append(t ** 0.9)

# Compute derived humidity ratios (partially relevant)
humidity_ratios = []
for h in humidity_readings:
    ratio = h / sum(humidity_readings) * 100
    humidity_ratios.append(round(ratio, 2))

# Entropy calculation for anomaly detection
entropy_values = []
for i in range(len(processed_temps)):
    temp_contrib = math.log(processed_temps[i])
    humid_contrib = math.log(humidity_readings[i] + 1)
    pressure_contrib = math.log(pressure_readings[i] / 1000)
    entropy = temp_contrib * humid_contrib * pressure_contrib
    entropy_values.append(abs(entropy))

# Decoy statistical analysis (distractor block)
mean_temp = sum(temperature_readings) / len(temperature_readings)
median_humidity = sorted(humidity_readings)[len(humidity_readings)//2]
mode_pressure = Counter(pressure_readings).most_common(1)[0][0]  # Always 1013 (uniform)

# Spurious correlation matrix (unused)
correlation_cache = defaultdict(dict)
for i in range(len(temperature_readings)):
    for j in range(i+1, len(temperature_readings)):
        delta_t = temperature_readings[i] - temperature_readings[j]
        delta_p = pressure_readings[i] - pressure_readings[j]
        correlation_cache[i][j] = delta_t * delta_p * 0.01  # Not used

# Red herring: complex but irrelevant transformation
transformed_light = []
for x in light_intensity:
    val = x
    for _ in range(3):
        val = (val ** 0.5) * 1.5
    transformed_light.append(round(val, 3))

# Real computation path begins here
baseline_entropy = sum(entropy_values) / len(entropy_values)
anomaly_scores = [e / baseline_entropy for e in entropy_values]

# Bit manipulation decoy (distractor)
bitmask = 0b101010
shifted_mask = bitmask << 3
inverted_mask = ~shifted_mask & 0xFF

# Actual signal weighting
weight_schedule = []
for i in range(len(anomaly_scores)):
    weight = (i + 1) / len(anomaly_scores)
    weight_schedule.append(weight)

weighted_anomalies = []
for i in range(len(anomaly_scores)):
    weighted_anomalies.append(anomaly_scores[i] * weight_schedule[i])

aggregate_score = sum(weighted_anomalies) * 1000

# Unused recursive distraction
def useless_tree_sum(n):
    if n <= 1:
        return 1
    return n + useless_tree_sum(n-2) + useless_tree_sum(n-3)

# Anomaly detector function (critical)
def anomaly_detector(entropies):
    total = 0
    for e in entropies:
        if e > 1.5:
            total += e * 0.7
    return int(total)

# Final diagnostic fusion point
final_diagnostic = aggregate_score + anomaly_detector(entropy_values)

# Output result
print(f"Result: {final_diagnostic}")