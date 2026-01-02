import math

# Simulated sensor fusion system for environmental monitoring

def collect_readings():
    # Real data sources
    temperature = [23.5, 24.1, 22.9, 25.0, 23.8]
    humidity = [45, 47, 50, 44, 46]
    pressure = [1013, 1015, 1012, 1016, 1014]
    
    # Irrelevant dummy readings (distractor)
    noise_floor = [0.1, 0.2, 0.15, 0.3, 0.25]  # unused
    signal_strength = [-70, -68, -72, -69, -71]  # unused
    
    return temperature, humidity, pressure

# Decoy function - looks relevant but never used
def calculate_air_quality_index(pm25, pm10):
    aqi_pm25 = (pm25 * 10) if pm25 > 0 else 0
    aqi_pm10 = (pm10 * 5) if pm10 > 0 else 0
    return max(aqi_pm25, aqi_pm10)

# Auxiliary transformation with partial relevance
def normalize(data):
    mean_val = sum(data) / len(data)
    normalized = [(x - mean_val) / mean_val for x in data]
    return normalized

# Complex weighting with red herring parameters
weights = {
    'temp_w': 0.4,
    'humid_w': 0.3,
    'press_w': 0.2,
    'fake_w': 0.1  # This weight is never used
}

# Misleading intermediate metrics (some unused)
metrics = {
    'avg_temp_deviation': 0.0,
    'humidity_stability': 0.0,
    'pressure_trend': 0.0,
    'signal_integrity': 0.0,  # Unused metric (distractor)
    'noise_ratio': 0.0  # Unused metric (distractor)
}

# Higher-order function that appears critical but only some outputs matter
def analyze_trends(values):
    trend = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend += 1
        elif values[i] < values[i-1]:
            trend -= 1
    return abs(trend)  # Use absolute stability score

# Data processing pipeline with decoy branches
thresholds = {'high': 24.0, 'low': 45, 'norm_press': 1014}

# Simulate redundant state tracking (only one matters)
status_flags = set()
status_flags.add('sensor_warm')
status_flags.add('calibration_ok')
status_flags.add('data_fresh')

# Begin real processing
temps, humids, press = collect_readings()

# Real computations
mean_temp = sum(temps) / len(temps)
temp_devs = [abs(t - mean_temp) for t in temps]
metrics['avg_temp_deviation'] = sum(temp_devs) / len(temp_devs)

# Humidity stability using set difference (real use of set)
humid_set_current = set(humids[:3])
humid_set_previous = set([46, 48, 45])  # simulated last batch
stability_diff = humid_set_current - humid_set_previous
metrics['humidity_stability'] = len(stability_diff)

# Pressure trend analysis
metrics['pressure_trend'] = analyze_trends(press)

# Dummy transformations to mislead
encrypted_data = [pow(p, 3, 103) for p in press]  # bit manipulation red herring
checksum = sum(encrypted_data) % 256  # irrelevant

# Fake confidence calculation (unused)
confidence = 0
for h in humids:
    if h > thresholds['low']:
        confidence += 0.1

# Critical aggregation function
def aggregate_performance(met, w):
    # Normalize metrics to 0-1 scale (inverse: lower deviation = better)
    temp_score = max(0, 1 - met['avg_temp_deviation'])
    humid_score = max(0, 1 - (met['humidity_stability'] / 10))
    press_score = max(0, 1 - (abs(met['pressure_trend'] - 2) / 10))  # target trend ~2
    
    # Weighted combination (only these three matter)
    score = (
        temp_score * w['temp_w'] +
        humid_score * w['humid_w'] +
        press_score * w['press_w']
    )
    
    # Apply nonlinear boost (logarithmic enhancement)
    final = math.log(1 + score) * 100  # Scale to meaningful range
    
    # Dead code branch (never executed due to logic)
    if 'invalid_flag' in status_flags:
        final *= 0.5  # would degrade, but flag not present
    
    return final

# Execute main computation
final_score = aggregate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")