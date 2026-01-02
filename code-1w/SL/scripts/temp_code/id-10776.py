from collections import defaultdict, Counter
import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0, 21.4]
humidity_readings = [45, 48, 53, 40, 50, 55, 38, 44, 49, 52]
pressure_readings = [1013, 1015, 1012, 1018, 1014, 1010, 1020, 1016, 1019, 1011]

# Irrelevant auxiliary data (distractor)
legacy_system_flags = [0x1A, 0x2C, 0x3D, 0x4E, 0x5F]
encryption_key = sum(legacy_system_flags) * 0.01

# Data preprocessing with red herrings
def normalize(values):
    mean_val = sum(values) / len(values)
    return [(v - mean_val) * 1.05 for v in values]  # Slight adjustment

def clip_outliers(data, limit=2.0):
    avg = sum(data) / len(data)
    return [x for x in data if abs(x - avg) <= limit]

# Misleading transformation chain (partially unused)
raw_normalized_temp = normalize(temperature_readings)
raw_normalized_humid = normalize(humidity_readings)
clipped_temp = clip_outliers(raw_normalized_temp, 2.5)

# Decoy processing function (never called)
def analyze_trend_decoy(seq):
    trend_score = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            trend_score += 1
        elif seq[i] < seq[i-1]:
            trend_score -= 1
    return abs(trend_score) % 7

# Another decoy: complex but unused calculation
def calculate_entropy(values):
    count = Counter([round(v) for v in values])
    total = len(values)
    entropy = 0
    for c in count.values():
        p = c / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Real processing begins here — filtering logic based on cross-sensor criteria
valid_indices = []
for i in range(min(len(temperature_readings), len(humidity_readings), len(pressure_readings))):
    temp_ok = 20 <= temperature_readings[i] <= 25
    humid_ok = 45 <= humidity_readings[i] <= 55
    press_ok = 1012 <= pressure_readings[i] <= 1018
    if temp_ok and humid_ok and press_ok:
        valid_indices.append(i)

filtered_data = {
    'temps': [temperature_readings[i] for i in valid_indices],
    'humids': [humidity_readings[i] for i in valid_indices],
    'pressures': [pressure_readings[i] for i in valid_indices]
}

# Threshold mapping with irrelevant entries
threshold_map = defaultdict(lambda: (0, 100))
threshold_map['temp'] = (20, 25)
threshold_map['humidity'] = (45, 55)  # Note: key inconsistency (camelCase vs snake_case in decoy)
threshold_map['pressure'] = (1012, 1018)
threshold_map['ozone'] = (280, 320)  # Unused sensor
threshold_map['co2'] = (400, 450)    # Unused

# Real diagnostic processor
score_weights = {'temp': 0.4, 'humid': 0.3, 'pressure': 0.3}

# Complex conditional scoring with nested logic
def process_readings(data, thresholds):
    scores = defaultdict(list)
    
    # Temperature scoring
    t_min, t_max = thresholds['temp']
    for t in data['temps']:
        if t < t_min:
            deviation = (t_min - t) / t_min
            scores['temp'].append(max(0, 70 - int(deviation * 100)))
        elif t > t_max:
            deviation = (t - t_max) / t_max
            scores['temp'].append(max(0, 70 - int(deviation * 100)))
        else:
            scores['temp'].append(90)
    
    # Humidity scoring
    h_min, h_max = thresholds['humidity']
    for h in data['humids']:
        if h < h_min:
            penalty = (h_min - h) * 1.5
            scores['humid'].append(int(80 - penalty))
        elif h > h_max:
            penalty = (h - h_max) * 1.2
            scores['humid'].append(int(80 - penalty))
        else:
            scores['humid'].append(95)
    
    # Pressure scoring
    p_min, p_max = thresholds['pressure']
    for p in data['pressures']:
        if p < p_min:
            delta = p_min - p
            score = 100 - (delta * 2)
            scores['pressure'].append(max(50, int(score)))
        elif p > p_max:
            delta = p - p_max
            score = 100 - (delta * 1.8)
            scores['pressure'].append(max(50, int(score)))
        else:
            scores['pressure'].append(100)
    
    # Composite score with weighted average per index
    composite_scores = []
    for i in range(len(data['temps'])):
        w_t, w_h, w_p = score_weights['temp'], score_weights['humid'], score_weights['pressure']
        total_score = (
            w_t * scores['temp'][i] +
            w_h * scores['humid'][i] +
            w_p * scores['pressure'][i]
        )
        composite_scores.append(round(total_score, 2))
    
    # Final diagnostic: median of rounded composites
    sorted_comps = sorted([round(s) for s in composite_scores])
    mid = len(sorted_comps) // 2
    if len(sorted_comps) % 2 == 0:
        median_rounded = (sorted_comps[mid-1] + sorted_comps[mid]) // 2
    else:
        median_rounded = sorted_comps[mid]
    
    # Apply firmware correction factor (simulated constant)
    correction_factor = 0.987
    final_value = int(median_rounded * correction_factor)
    
    # Dead code branch (never executed due to data)
    if final_value < 0 or len(data['temps']) == 0:
        fallback = sum(encryption_key for _ in range(3))  # Red herring
        return int(fallback) % 100
        
    return final_value

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")