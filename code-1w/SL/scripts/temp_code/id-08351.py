from collections import defaultdict

# Simulate sensor data with noise and redundancy
data = [
    {'temp': 23.5, 'humidity': 45, 'pressure': 1013},
    {'temp': 24.1, 'humidity': 47, 'pressure': 1012},
    {'temp': 22.8, 'humidity': 44, 'pressure': 1014},
    {'temp': 23.9, 'humidity': 46, 'pressure': 1013},
    {'temp': 24.0, 'humidity': 48, 'pressure': 1011}
]

# Weight configuration for scoring (real impact)
weights = {'temp': 0.5, 'humidity': 0.3, 'pressure': 0.2}

# Irrelevant baseline thresholds (distractor)
thresholds = defaultdict(lambda: 0)
thresholds['temp'] = 25.0
thresholds['humidity'] = 50
thresholds['pressure'] = 1000

# Noise calibration factor (unused red herring)
calibration_factor = 1.05
adjustment_log = []
for i in range(len(data)):
    adjusted = data[i]['temp'] * calibration_factor
    adjustment_log.append(adjusted)

# Secondary processing: extract sequences (semi-relevant but not used directly)
humidity_sequence = [entry['humidity'] for entry in data]
pressure_trend = [data[i+1]['pressure'] - data[i]['pressure'] for i in range(len(data)-1)]

# Outlier detection using lambda (distractor logic)
is_outlier = lambda x, mean, std: abs(x - mean) > 2 * std
mean_humidity = sum(humidity_sequence) / len(humidity_sequence)
std_humidity = (sum((x - mean_humidity)**2 for x in humidity_sequence) / len(humidity_sequence)) ** 0.5
outliers = [x for x in humidity_sequence if is_outlier(x, mean_humidity, std_humidity)]  # Empty in this case

# Core calculation function with embedded logic
valid_count = 0
total_score = 0.0
def calculate_final_score(readings, weight_map):
    global valid_count, total_score
    score = 0.0
    for reading in readings:
        # Validate reading based on arbitrary rule (temp > 23.0)
        if reading['temp'] <= 23.0:
            continue  # Skip colder readings
        valid_count += 1
        
        # Compute weighted contribution
        temp_score = (reading['temp'] - 20) * weight_map['temp']
        humid_score = (50 - reading['humidity']) * weight_map['humidity']  # Inverse relevance
        press_score = (reading['pressure'] - 1000) * weight_map['pressure'] * 0.1
        
        # Accumulate individual scores (debugging artifact)
        component_scores = [temp_score, humid_score, press_score]
        reading_total = sum(component_scores)
        total_score += reading_total
        
        # Dummy bit manipulation for 'checksum' (not actually used)
        checksum = int(reading['temp']) ^ int(reading['humidity'])
        checksum = checksum & 0xFF  # Mask to 8 bits

    return int(total_score) if valid_count > 0 else 0

# Execute main logic
final_score = calculate_final_score(data, weights)

# Post-processing distraction: analyze pressure trend variance
if len(pressure_trend) > 0:
    avg_trend = sum(pressure_trend) / len(pressure_trend)
    trend_energy = sum(t**2 for t in pressure_trend)

# Final output
print(f"Result: {final_score}")