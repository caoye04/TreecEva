import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 20.4, 21.9]
humidity_readings = [45, 52, 61, 58, 49, 54, 66, 50]
pressure_readings = [1013, 1015, 1012, 1018, 1009, 1014, 1016, 1011]

# Irrelevant auxiliary metrics (distractor variables)
sound_levels = [32, 41, 38, 45, 50, 42, 39, 43]  # Decoy sensor data
light_intensity = [800, 950, 700, 1000, 600, 850, 900, 750]  # Unused in logic

# Preprocessing: Normalize readings to baseline ranges
def normalize_temperatures(raw_temps):
    min_temp, max_temp = min(raw_temps), max(raw_temps)
    return [(t - min_temp) / (max_temp - min_temp) for t in raw_temps]

def categorize_humidity(values):
    return ['high' if h > 55 else 'normal' for h in values]

# Misleading transformation chain (partially dead code path)
transformed_light = [l / 10 for l in light_intensity if l > 700]
aggregated_sound = sum(abs(a - b) for a, b in itertools.pairwise(sound_levels)) // len(sound_levels)

# Core processing pipeline
normalized_temps = normalize_temperatures(temperature_readings)
humidity_categories = categorize_humidity(humidity_readings)

# Construct multi-dimensional data records
data_records = []
for i in range(len(temperature_readings)):
    record = {
        'idx': i,
        'temp_norm': normalized_temps[i],
        'humidity_label': humidity_categories[i],
        'pressure': pressure_readings[i]
    }
    data_records.append(record)

# Filtering based on anomalous pressure deviations
baseline_pressure = sum(pressure_readings) / len(pressure_readings)
filtered_data = [r for r in data_records if abs(r['pressure'] - baseline_pressure) <= 5]

# Threshold configuration map (used in final computation)
threshold_map = {
    'temp_threshold': 0.35,
    'label_priority': {'high': 2, 'normal': 1},
    'weight_set': [0.4, 0.6]
}

# Decoy function - appears relevant but unused
def analyze_acoustic_patterns(levels):
    peaks = [lvl for lvl in levels if lvl > 40]
    return len(peaks) > 3

# Secondary decoy: complex but irrelevant string operation
status_flags = [f"F{''.join(itertools.islice('LAG', 1, 2))}" + str(i % 3) for i in range(8)]
flag_summary = "".join(status_flags).replace("F", "").count("1")

# Actual critical processing function
def process_readings(records, config):
    score_accum = 0
    for r in records:
        # Weighted contribution based on normalized temperature and thresholds
        temp_influence = r['temp_norm'] * config['weight_set'][0]
        priority_bonus = config['label_priority'][r['humidity_label']]
        
        # Conditional excitation based on threshold crossing
        if r['temp_norm'] > config['temp_threshold']:
            score_accum += temp_influence * priority_bonus
        else:
            score_accum += temp_influence + 0.1
    
    # Final nonlinear transformation
    adjusted_score = int((score_accum ** 2) * 50) + flag_summary  # Subtle link to distractor
    return adjusted_score

# Execute key statement
final_diagnostic = process_readings(filtered_data, threshold_map)
print(f"Result: {final_diagnostic}")