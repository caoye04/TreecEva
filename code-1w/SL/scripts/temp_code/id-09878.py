import math

# Simulated sensor data with noise and redundant readings
temperature_readings = [23.4, 24.1, 22.8, 25.0, 23.9, 24.2, 23.7, 26.1, 25.8, 24.6]
humidity_readings = [45, 48, 50, 44, 52, 49, 47, 55, 53, 46]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1017, 1018, 1015, 1013, 1019]  # Irrelevant for score

# Distractor variables (unused in final logic)
baseline_offset = 0.5
dummy_flag = True
temp_cache = {}
redundant_sum = 0
for i in range(len(temperature_readings)):
    redundant_sum += temperature_readings[i] * humidity_readings[i]  # Dead-end computation

# Misleading intermediate transformation
adjusted_temps = []
for temp in temperature_readings:
    if temp > 25:
        adjusted_temps.append(temp * 0.95)
    elif temp < 24:
        adjusted_temps.append(temp * 1.02)
    else:
        adjusted_temps.append(temp)

# Humidity normalization (partially relevant but overcomplicated)
normalized_humidity = []
counter = 0
for idx, h in enumerate(humidity_readings):
    normalized_value = (h - 40) / 20  # Scale to [0,1] range
    if counter % 2 == 0:
        normalized_humidity.append(round(normalized_value, 3))
    else:
        normalized_humidity.append(normalized_value)
    counter += 1

# Real processing begins: find stable periods using enumerate and zip
deviation_pairs = []
for i, (t, h) in enumerate(zip(adjusted_temps, normalized_humidity)):
    if i == 0:
        continue
    temp_change = abs(adjusted_temps[i] - adjusted_temps[i-1])
    humidity_change = abs(h - normalized_humidity[i-1])
    stability_metric = temp_change + humidity_change
    if stability_metric < 1.0:  # Stable condition
        deviation_pairs.append((i, stability_metric))

# Secondary distractor: pressure trend analysis (never used)
pressure_trend = 0
for p in pressure_readings:
    pressure_trend += math.sin(p / 100)  # Meaningless transformation

# Extract indices of stable segments
stable_indices = [pair[0] for pair in deviation_pairs]

# Compute moving average of adjusted temps only at stable points
moving_avg = 0.0
if len(stable_indices) > 0:
    total = 0.0
    count = 0
    for idx in stable_indices:
        if idx < len(adjusted_temps):
            total += adjusted_temps[idx]
            count += 1
    moving_avg = total / count if count > 0 else 0

# Decoy function that looks important but isn't called in main path
def analyze_pressure_risk(data):
    risk_score = 0
    for d in data:
        risk_score += abs(d - 1015) ** 0.5
    return risk_score / len(data)

# Another decoy: complex bit manipulation on humidity (unused)
bitwise_humidity_fingerprint = 0
for h in humidity_readings:
    bitwise_humidity_fingerprint ^= (h << 2) | (h >> 1)

# Actual scoring logic (hidden among distractions)
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_final_score(data_chunk):
    # Data chunk is adjusted_temps
    base_score = 0
    for val in data_chunk:
        if val >= 24 and val <= 25:
            base_score += 10
        elif val > 25:
            base_score += 5
        else:
            base_score += 7
    
    # Apply penalty based on variance
    variance = calculate_variance(data_chunk)
    penalty = int(variance * 2)
    return base_score - penalty

# Critical statement
processed_data = adjusted_temps
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")