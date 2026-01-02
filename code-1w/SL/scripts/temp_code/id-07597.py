import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 20.4, 21.7, 26.8, 24.9, 23.0]
humidity_readings = [45, 50, 52, 48, 60, 55, 53, 62, 58, 49]
pressure_readings = [1013, 1015, 1012, 1018, 1009, 1014, 1016, 1008, 1010, 1017]

# Irrelevant auxiliary arrays (distractors)
elevation_data = [120, 135, 110, 140, 90, 125, 115, 85, 100, 130]
wind_speed = [5.2, 6.1, 4.8, 5.9, 7.0, 5.5, 6.3, 8.1, 5.7, 6.0]

# Misleading preprocessing: normalizing unrelated metrics
def normalize(values):
    min_val, max_val = min(values), max(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

normalized_elevation = normalize(elevation_data)  # Dead-end computation
normalized_wind = normalize(wind_speed)            # Dead-end computation

# Real signal processing begins here
valid_indices = []
for i, temp in enumerate(temperature_readings):
    if 20 <= temp <= 25:
        valid_indices.append(i)

# Filter relevant data using valid temperature ranges
filtered_humidity = [humidity_readings[i] for i in valid_indices]
filtered_pressure = [pressure_readings[i] for i in valid_indices]
filtered_data = list(zip(filtered_humidity, filtered_pressure))

# Decoy function: looks important but unused
def compute_air_quality(humidities, pressures):
    score = 0
    for h, p in zip(humidities, pressures):
        score += math.log(p) * (h / 10)
    return round(score, 2)

# Unused recursive red herring
def predict_trend(values, depth=3):
    if depth == 0 or len(values) < 2:
        return values[-1] if values else 0
    smoothed = [(values[i] + values[i+1]) / 2 for i in range(len(values)-1)]
    return predict_trend(smoothed, depth-1)

predicted_temp = predict_trend(temperature_readings)  # Distractor assignment

# Core logic hidden among noise
baseline_ref = sum(math.sin(math.radians(p % 100)) for p in pressure_readings)  # Obfuscated constant

data_score = 0
for h, p in filtered_data:
    # Actual contribution: weighted combination with transcendental ops
    data_score += h * math.cos(baseline_ref) + p * 0.1

# Lambda-based transformation chain (key python idiom)
transform = lambda x: x ** 2 if x > 50 else x ** 1.5
enhanced_score = transform(abs(data_score))

# Secondary filter: only high-confidence readings contribute
high_confidence = list(filter(lambda x: x[0] > 50 or x[1] < 1015, filtered_data))
confidence_bonus = len(high_confidence) * 2.5

# Final aggregation with multiple abstraction layers
def analyze_group(pairs):
    total = 0.0
    for idx, (hum, pres) in enumerate(pairs):
        factor = math.tan(math.radians(idx + 1)) if idx % 2 == 0 else 1.0
        total += hum * factor + pres / 100.0
    return total

interim_result = analyze_group(filtered_data)
final_diagnostic = int(enhanced_score + interim_result + confidence_bonus)

# Critical output
print(f"Result: {final_diagnostic}")