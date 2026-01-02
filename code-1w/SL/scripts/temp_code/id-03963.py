from collections import defaultdict, Counter
import string

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 22.1, 26.3]
humidity_readings = [45, 48, 52, 44, 55, 49, 58, 43]
co2_levels = [410, 415, 420, 405, 430, 412, 425, 408]

# Irrelevant auxiliary data (distractor)
legacy_system_flags = {f'device_{i}': i % 3 for i in range(8)}
device_status_log = ['active', 'idle', 'active', 'faulty', 'active', 'active', 'idle', 'active']

# Weight configuration for composite score calculation
weights = {
    'temp': 0.4,
    'humidity': 0.3,
    'co2': 0.3
}

# Preprocessing: normalize readings to baseline (20°C, 50%, 400ppm)
normalized_data = []
for i in range(len(temperature_readings)):
    norm_temp = (temperature_readings[i] - 20) / 5
    norm_humidity = (humidity_readings[i] - 50) / 10
    norm_co2 = (co2_levels[i] - 400) / 100
    normalized_data.append((norm_temp, norm_humidity, norm_co2))

# Mapping station performance bands (irrelevant for final result)
performance_band = []
for temp, hum, co2 in normalized_data:
    score = temp * 0.5 + hum * 0.3 + co2 * 0.2
    if score > 1.0:
        performance_band.append('excellent')
    elif score > 0.5:
        performance_band.append('good')
    elif score > 0.0:
        performance_band.append('moderate')
    else:
        performance_band.append('poor')

# Decoy function that looks important but isn't used
def calculate_legacy_index(flags):
    total = 0
    for k, v in flags.items():
        if 'device_' in k and v == 2:
            total += ord(k[-1]) % 7
    return total * 1.5

# String-based encoding of device ids (dead path)
device_ids = [f'DEV{i:03}' for i in range(1, 9)]
encoded_tags = []
for tag in device_ids:
    shifted = ''.join([chr(((ord(c) - ord('A') + 3) % 26) + ord('A')) if c.isalpha() else c for c in tag])
    encoded_tags.append(shifted)

# Aggregate data into dictionary format
station_data = defaultdict(dict)
for i, tag in enumerate(device_ids):
    station_data[tag]['temperature'] = temperature_readings[i]
    station_data[tag]['humidity'] = humidity_readings[i]
    station_data[tag]['co2'] = co2_levels[i]
    station_data[tag]['normalized'] = normalized_data[i]

# Extract sequences for correlation analysis (distractor)
temp_seq = [x[0] for x in normalized_data]
humid_seq = [x[1] for x in normalized_data]
co2_seq = [x[2] for x in normalized_data]

correlation_matrix = []
for a, b in zip([temp_seq, temp_seq, humid_seq], [humid_seq, co2_seq, co2_seq]):
    mean_a = sum(a) / len(a)
    mean_b = sum(b) / len(b)
    cov = sum((a[i] - mean_a) * (b[i] - mean_b) for i in range(len(a)))
    var_a = sum((x - mean_a)**2 for x in a)
    var_b = sum((x - mean_b)**2 for x in b)
    corr = cov / ((var_a**0.5) * (var_b**0.5)) if var_a != 0 and var_b != 0 else 0
    correlation_matrix.append(corr)

# Real processing begins here — this is where the answer logic starts
def analyze_trends(values):
    """Count increasing trend segments"""
    trends = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trends += 1
    return trends

def rank_stations(data_dict):
    """Rank stations by raw temperature (descending)"""
    rankings = []
    for dev_id, metrics in data_dict.items():
        rankings.append((dev_id, metrics['temperature']))
    # Sort by temperature descending, then by CO2 ascending (tiebreaker)
    rankings.sort(key=lambda x: (-x[1], data_dict[x[0]]['co2']))
    return [r[0] for r in rankings]

# Misleading ranking usage (looks relevant)
ranked_devices = rank_stations(station_data)

# Another decoy: character frequency in device IDs
device_letters = ''.join([c for tag in device_ids for c in tag if c.isalpha()])
letter_freq = Counter(device_letters)

# Actual core metric: compute weighted anomaly score across all stations
def process_metrics(norm_data_list, weight_dict):
    total_anomaly = 0.0
    for norm_vals in norm_data_list:
        # Unpack normalized values
        temp_norm, hum_norm, co2_norm = norm_vals
        # Apply weights to deviation magnitudes (absolute values)
        weighted_deviation = (
            abs(temp_norm) * weight_dict['temp'] +
            abs(hum_norm) * weight_dict['humidity'] +
            abs(co2_norm) * weight_dict['co2']
        )
        total_anomaly += weighted_deviation * 1.1  # Scaling factor applied uniformly
    
    # Apply trend bonus only if more than half show increasing trend
    temp_trend_count = analyze_trends(temperature_readings)
    hum_trend_count = analyze_trends(humidity_readings)
    co2_trend_count = analyze_trends(co2_levels)
    
    avg_trend = (temp_trend_count + hum_trend_count + co2_trend_count) / 3
    if avg_trend > 3.5:  # arbitrary threshold
        total_anomaly *= 0.95  # slight reduction for stability
    
    return total_anomaly

# Critical execution point
final_score = process_metrics(normalized_data, weights)

# Print result as required
print(f"Result: {final_score}")