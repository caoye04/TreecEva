from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and irrelevant entries
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.0, 23.7]
humidity_readings = [45, 47, 50, 44, 60, 55, 53, 48]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1011, 1014]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G5', 'H3']
error_flags = [False, False, True, False, False, False, False, True]

# Misleading preprocessing (dead path)
def validate_sensors(raw_data):
    if not raw_data:
        return []
    cleaned = []
    for val in raw_data:
        if isinstance(val, float) and 10 <= val <= 100:
            cleaned.append(round(val))
    return cleaned

# Unused transformation (red herring)
def smooth_signal(signal):
    smoothed = []
    for i in range(len(signal)):
        neighbors = signal[max(0, i-1):min(i+2, len(signal))]
        smoothed.append(sum(neighbors) / len(neighbors))
    return smoothed

# Decoy function that looks important but isn't used
def compute_variance(values):
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

# Real processing begins here
raw_data_stream = [
    {'temp': t, 'hum': h, 'pres': p, 'err': e} 
    for t, h, p, e in zip(temperature_readings, humidity_readings, pressure_readings, error_flags)
]

data = []
for entry in raw_data_stream:
    if not entry['err']:  # Filter out erroneous readings
        data.append(entry)

# Weight configuration (some are decoys)
weights = {
    'temp_w': 0.4,
    'hum_w': 0.3,
    'pres_w': 0.2,
    'fake_w': 0.1,  # unused weight
    'bonus_w': 0.05  # another unused
}

# Auxiliary counters (partly relevant, partly distraction)
diagnostic_counter = Counter()
for d in data:
    temp_bin = int(d['temp'] // 5) * 5
    diagnostic_counter[f'temp_range_{temp_bin}'] += 1

def analyze_trend(values):
    trend_score = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_score += 1
        elif values[i] < values[i-1]:
            trend_score -= 0.5
    return trend_score

# Distractor: unused trend analysis on irrelevant metric
temp_trend = analyze_trend([d['temp'] for d in raw_data_stream])
hum_trend = analyze_trend([d['hum'] for d in raw_data_stream])

# Core logic hidden among distractions
def extract_features(dataset):
    features = defaultdict(float)
    temps = [d['temp'] for d in dataset]
    hums = [d['hum'] for d in dataset]
    press = [d['pres'] for d in dataset]
    
    # Real feature extraction
    features['avg_temp'] = sum(temps) / len(temps)
    features['norm_hum'] = sum(hums) / max(hums)  # normalized average
    features['delta_pres'] = max(press) - min(press)
    
    # Irrelevant derived metrics (distraction)
    features['entropy_temp'] = sum(math.log(t + 1) for t in temps) / len(temps)
    features['skew_hum'] = (sum(hums) / len(hums)) / (sum(hums) % 10 + 1)
    
    return features

# Another decoy function
def generate_report(features):
    report_lines = []
    for k, v in features.items():
        report_lines.append(f'{k}: {v:.2f}')
    return '\n'.join(report_lines)

# Critical processing function
def process_results(sensor_data, weight_map):
    feats = extract_features(sensor_data)
    
    # Meaningful intermediate variables
    base_score = 0.0
    base_score += feats['avg_temp'] * weight_map['temp_w']     # Relevant
    base_score += feats['norm_hum'] * weight_map['hum_w']       # Relevant
    base_score += feats['delta_pres'] * weight_map['pres_w']    # Relevant
    
    # Dead calculations with decoy weights (misleading)
    fake_boost = feats.get('entropy_temp', 0) * weight_map.get('fake_w', 0)
    bonus_adj = feats.get('skew_hum', 0) * weight_map.get('bonus_w', 0)
    
    # Final adjustment based on data quality
    completeness_ratio = len(sensor_data) / len(raw_data_stream)
    quality_adjustment = 1.0 + (completeness_ratio * 0.1)
    
    final_score = (base_score + fake_boost + bonus_adj) * quality_adjustment
    
    # This print is required to expose the result
    print(f"Result: {final_score}")
    return final_score

# Execute main logic
final_score = process_results(data, weights)