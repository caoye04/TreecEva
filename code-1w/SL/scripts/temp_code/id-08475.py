import math

# Simulated environmental sensor readings
temperature_readings = [22.3, 23.1, 24.5, 25.0, 26.7, 27.2, 28.0, 27.8, 26.9, 25.6]
humidity_readings = [45, 47, 50, 53, 56, 59, 62, 65, 68, 70]
pressure_readings = [1013, 1015, 1017, 1019, 1021, 1020, 1018, 1016, 1014, 1012]

# Irrelevant transformation: smoothing pressure with moving average (unused)
def smooth(data, window=3):
    return [sum(data[i:i+window]) / window for i in range(len(data) - window + 1)]
smoothed_pressure = smooth(pressure_readings)

# Generate timestamp indices (distraction)
timestamps = [i * 300 for i in range(len(temperature_readings))]  # 5-minute intervals

# Core logic: detect anomalies based on temperature thresholds
anomalies = []
anomaly_count = 0
for temp in temperature_readings:
    if temp > 27.5 or temp < 23.0:
        anomalies.append(temp)
        anomaly_count += 1

# Decoy function: unrelated air quality index calculation
def calculate_aqi(pm25):
    if pm25 <= 50:
        return 50
    elif pm25 <= 100:
        return 100
    else:
        return 200
aqi = calculate_aqi(35)  # Irrelevant result

# Compute derived humidity ratios (distractor)
humidity_ratios = [h / sum(humidity_readings) for h in humidity_readings]
mean_ratio = sum(humidity_ratios) / len(humidity_ratios)

# Determine active trend windows (red herring)
trend_windows = []
for i in range(len(temperature_readings) - 2):
    window = temperature_readings[i:i+3]
    if window[2] > window[1] > window[0]:
        trend_windows.append('rising')
    elif window[2] < window[1] < window[0]:
        trend_windows.append('falling')
    else:
        trend_windows.append('stable')

total_rising = trend_windows.count('rising')

# Generate set of prime numbers up to 30 for encoding purposes
prime_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
composite_set = {c for c in range(2, 30) if c not in prime_set and c != 1}

# Bitwise manipulation of sensor ID (decoy)
sensor_id = 0b110101
encoded_id = sensor_id ^ 0b101110 & 0b111111
mask_applied = encoded_id | 0b000010

# Conditional expression used in entropy weight assignment
base_entropy = 1.5
adjustment_factor = 0.8 if len(anomalies) > 3 else 1.2
entropy_weight = base_entropy * adjustment_factor

# Key computational step: determine filtration efficiency score
# What is the value of variable 'filtration_score' after executing this statement?
filtration_score = entropy_weight * (len(prime_set) - anomaly_count)

# Final output
print(f"Result: {filtration_score}")