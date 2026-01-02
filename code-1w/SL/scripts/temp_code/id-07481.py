from collections import defaultdict, Counter
import math

# Simulated sensor data from a distributed environmental monitoring system
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0]
humidity_readings = [45, 52, 58, 43, 60, 55, 48, 51, 59]
co2_levels = [410, 425, 430, 405, 440, 418, 422, 435, 412]

# Irrelevant auxiliary data (distractor)
power_cycles = [1, 0, 1, 1, 0, 1, 1, 1, 0]
uptime_seconds = [3600, 7200, 1800, 5400, 9000, 300, 8100, 6300, 4500]

def normalize(values):
    min_val, max_val = min(values), max(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

def rolling_average(values, window=3):
    smoothed = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        smoothed.append(sum(values[start:i+1]) / (i - start + 1))
    return smoothed

def detect_anomalies(data, threshold=0.1):
    avg = sum(data) / len(data)
    return [abs(x - avg) > threshold * avg for x in data]

def calculate_entropy(values):
    counts = Counter(values)
    total = len(values)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

# Dead function - never called (distractor)
def deprecated_calibration(sequence):
    return [x * 0.98 + 2.1 for x in sequence]

def transform_readings(temp, hum, co2):
    # Apply normalization
    norm_temp = normalize(temp)
    norm_hum = normalize(hum)
    norm_co2 = normalize(co2)
    
    # Compute derived metrics
    heat_index = []
    for t, h in zip(norm_temp, norm_h):
        hi = t * (h + 0.5)  # Simplified proxy
        heat_index.append(round(hi, 4))
    
    # Rolling average on heat index
    smooth_hi = rolling_average(heat_index, window=2)
    
    # Detect anomalies in CO2 (this affects final processing)
    co2_anomalies = detect_anomalies(co2)
    
    # Build processed dataset
    processed = defaultdict(dict)
    for i, (t, h, c) in enumerate(zip(norm_temp, norm_h, norm_co2)):
        processed[i]['temp'] = t
        processed[i]['humidity'] = h
        processed[i]['co2'] = c
        processed[i]['heat_index'] = smooth_hi[i]
        processed[i]['anomaly_flag'] = co2_anomalies[i]
    
    return processed

# Unused transformation path (distractor)
synthetic_data = []
for idx, val in enumerate(temperature_readings):
    adjusted = val * (1 + humidity_readings[idx] / 1000)
    synthetic_data.append({'id': idx, 'value': adjusted, 'type': 'simulated'})

# Core processing pipeline
processed_data = transform_readings(temperature_readings, humidity_readings, co2_levels)

# Red herring: entropy calculation on irrelevant field (never used)
flag_entropy = calculate_entropy([v['anomaly_flag'] for v in processed_data.values()])

# Another dead-end computation
aggregated_shift = 0
for k in processed_data:
    if processed_data[k]['anomaly_flag']:
        aggregated_shift ^= int(processed_data[k]['co2'] * 10)  # Bitwise distraction

# Real analysis function
metrics_log = []

def analyze_metrics(data_map):
    scores = []
    for _, record in sorted(data_map.items()):
        base_score = record['temp'] * 0.4 + record['humidity'] * 0.3
        
        # Conditional adjustment based on CO2 level
        if record['co2'] > 0.5:
            base_score += 0.2
        else:
            base_score -= 0.1
        
        # Heat index boost if above median
        hi_values = [r['heat_index'] for r in data_map.values()]
        if record['heat_index'] >= sorted(hi_values)[len(hi_values)//2]:
            base_score += 0.05
        
        scores.append(base_score)
    
    # Final diagnostic is the scaled sum of all scores
    raw_total = sum(scores)
    final_diagnostic = int(raw_total * 1000)  # Scale and convert to integer
    
    # This log line is just for traceability (but not part of answer)
    metrics_log.append(f'Diagnostic computed: {final_diagnostic}')
    
    return final_diagnostic

# Key statement
final_diagnostic = analyze_metrics(processed_data)

# Print result as required
print(f"Result: {final_diagnostic}")