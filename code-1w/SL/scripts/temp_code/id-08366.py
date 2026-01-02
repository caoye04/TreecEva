from collections import defaultdict, Counter

# Simulated sensor data from multiple environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 25.0, 22.7, 20.3, 26.5, 24.8, 21.0, 23.2]
humidity_readings = [45, 50, 52, 60, 58, 48, 65, 70, 55, 49]
co2_levels = [400, 410, 395, 420, 430, 390, 415, 425, 405, 398]

# Irrelevant auxiliary data (distractor)
sound_decibels = [35, 40, 38, 42, 45, 37, 41, 39, 43, 44]
lux_levels = [500, 600, 550, 700, 680, 520, 620, 580, 650, 590]

# Mapping stations to regions (used later)
station_regions = {i: region for i, region in enumerate(['North', 'South', 'East', 'West', 'Central'] * 2)}

# Misleading transformation (dead path)
def transform_co2(x):
    return x * 1.02  # Slight inflation - never actually used

# Unused function (decoy)
def compute_air_quality_index(temp, hum, co2):
    return (temp * 2) + (hum / 10) + (co2 / 100)

# Data normalization function with red herring logic
def normalize_readings(raw_data):
    mean_val = sum(raw_data) / len(raw_data)
    normalized = [(x - mean_val) / mean_val for x in raw_data]
    
    # Distractor computation
    squared_sum = sum([x**2 for x in raw_data])
    variance_proxy = squared_sum / len(raw_data) - mean_val**2
    
    # Actual return value used downstream
    return [round(x, 3) for x in normalized]

# Complex preprocessing with multiple concepts
def preprocess_sensors(temp_data, hum_data, co2_data):
    processed = defaultdict(dict)
    stats_summary = []
    
    for i in range(len(temp_data)):
        # Real processing step
        processed[i]['temp_norm'] = normalize_readings(temp_data)[i]
        processed[i]['hum_norm'] = normalize_readings(hum_data)[i] / 100
        processed[i]['co2_anomaly'] = co2_data[i] - 400  # Baseline adjustment
        
        # Irrelevant derived values
        processed[i]['temp_hum_ratio'] = temp_data[i] / hum_data[i]  # unused
        processed[i]['region'] = station_regions[i]
        
        # Fake diagnostic flag (misleading)
        if temp_data[i] > 24 and hum_data[i] > 55:
            processed[i]['risk_flag'] = 'ELEVATED'
        else:
            processed[i]['risk_flag'] = 'NORMAL'
    
    # Dead code path
    summary_counter = Counter([processed[i]['region'] for i in processed])
    for region, count in summary_counter.items():
        stats_summary.append(f'{region}: {count} entries')
    
    return processed

# Threshold configuration map (critical)
threshold_map = {
    'temp_norm': 0.05,
    'hum_norm': 0.02,
    'co2_anomaly': 15
}

# Core analysis function with early returns and nesting
def analyze_readings(data_dict, thresholds):
    alert_count = 0
    diagnostic_scores = []
    
    for idx, readings in data_dict.items():
        score = 0
        anomaly_flags = []
        
        # Evaluate each parameter (3-level nesting)
        for param, value in readings.items():
            if param == 'region' or param == 'temp_hum_ratio' or param == 'risk_flag':
                continue  # Skip non-numeric metadata
            
            if param in thresholds:
                if abs(value) > thresholds[param]:
                    anomaly_flags.append(param)
                    
                    # Real scoring logic
                    if param == 'temp_norm':
                        score += abs(value) * 100
                    elif param == 'hum_norm':
                        score += abs(value) * 50
                    elif param == 'co2_anomaly':
                        score += abs(value) * 10
        
        # Secondary evaluation
        if len(anomaly_flags) >= 2:
            score *= 1.25  # Multiplier for compound anomalies
        
        diagnostic_scores.append(score)
        
        # Early termination red herring (never triggered due to data)
        cumulative = sum(diagnostic_scores)
        if cumulative > 1000:
            return -999  # Fake emergency override
    
    # Final aggregation (key computation)
    base_total = sum(diagnostic_scores)
    count_adjustment = len([s for s in diagnostic_scores if s > 0])
    final_score = base_total - (count_adjustment * 2.5)
    
    # Critical but misleading transformation
    string_encoded = ''.join([str(int(s))[-1] for s in diagnostic_scores if s > 0])
    if string_encoded.startswith('1'):
        final_score += 10  # Minor boost
    
    return int(round(final_score))

# Main execution flow
normalized_temps = normalize_readings(temperature_readings)
normalized_humid = normalize_readings(humidity_readings)

# Process all sensor streams
processed_data = preprocess_sensors(
    temperature_readings,
    humidity_readings,
    co2_levels
)

# Trigger point: this statement computes the answer
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output result
print(f"Result: {final_diagnostic}")