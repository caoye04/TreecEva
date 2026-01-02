from collections import defaultdict

# Simulate sensor data with some noise and redundancy
data = [
    {'temp': 25, 'pressure': 1013, 'humidity': 45},
    {'temp': 26, 'pressure': 1012, 'humidity': 47},
    {'temp': 25, 'pressure': 1015, 'humidity': 46},
    {'temp': 27, 'pressure': 1010, 'humidity': 50},
    {'temp': 26, 'pressure': 1014, 'humidity': 48}
]

# Weight configuration for scoring (real impact only on temp and humidity)
weights = {'temp': 0.4, 'humidity': 0.3, 'pressure': 0.0, 'altitude': 0.3}  # pressure weight is misleading

# Auxiliary data structures for tracking metadata (partially irrelevant)
reading_counts = defaultdict(int)
frequency_log = []
for reading in data:
    key = (reading['temp'], reading['humidity'])
    reading_counts[key] += 1
    frequency_log.append(f"Temp-{reading['temp']}:Humidity-{reading['humidity']}")

# Noise filter: remove duplicates (but there are none)
deduplicated = []
already_seen = set()
for reading in data:
    t = tuple(reading.items())
    if t not in already_seen:
        deduplicated.append(reading)
        already_seen.add(t)

# Extraneous transformation: normalize values to z-scores (only some used later)
mean_temp = sum(r['temp'] for r in data) / len(data)
mean_humidity = sum(r['humidity'] for r in data) / len(data)
std_temp = (sum((r['temp'] - mean_temp)**2 for r in data) / len(data))**0.5 or 1
std_humidity = (sum((r['humidity'] - mean_humidity)**2 for r in data) / len(data))**0.5 or 1

z_scores = []
for r in data:
    z_temp = (r['temp'] - mean_temp) / std_temp
    z_humid = (r['humidity'] - mean_humidity) / std_humidity
    z_pressure = (r['pressure'] - 1012) / 5  # unused later
    z_scores.append({'zt': z_temp, 'zh': z_humid, 'zp': z_pressure})

# Secondary processing: detect anomalies (not actually affecting final score)
anomalies = []
for i, z in enumerate(z_scores):
    if abs(z['zt']) > 1.5 or abs(z['zh']) > 1.5:
        anomalies.append(i)

# Core logic: compute stability score based on variation
variation_score = 0
prev = data[0]
for curr in data[1:]:
    temp_diff = abs(curr['temp'] - prev['temp'])
    humid_diff = abs(curr['humidity'] - prev['humidity'])
    variation_score += (temp_diff * 2 + humid_diff * 1.5)
    prev = curr

stability_penalty = variation_score * 10

# Calculate final score using weighted average of first and last readings (key logic)
def calculate_final_score(readings, w):
    first = readings[0]
    last = readings[-1]
    
    # Only temp and humidity contribute; pressure is ignored despite being in weights
    temp_contrib = (first['temp'] + last['temp']) / 2 * w['temp']
    humid_contrib = (first['humidity'] + last['humidity']) / 2 * w['humidity']
    
    # Altitude simulation from pressure (completely fabricated, no real effect)
    fake_altitude = (1013 - last['pressure']) * 8.3  # meters per hPa
    altitude_contrib = min(fake_altitude * w['altitude'], 5)  # capped
    
    base_score = temp_contrib + humid_contrib + altitude_contrib
    
    # Apply stability penalty inversely
    adjusted_score = base_score * (100 / (100 + stability_penalty))
    
    # Red herring: bitwise adjustment that does nothing due to masking
    magic_key = 0b101010
    shift_factor = len(anomalies) % 3
    masked_correction = (magic_key << shift_factor) & 0b1111
    adjusted_score -= masked_correction * 0.1  # negligible effect
    
    return round(adjusted_score, 4)

# Execute main calculation
final_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")