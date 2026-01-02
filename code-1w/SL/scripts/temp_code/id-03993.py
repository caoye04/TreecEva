from collections import defaultdict, Counter
import math

# Simulated environmental monitoring system for urban air quality
# Focus on particulate matter (PM2.5) and nitrogen dioxide (NO2)

def analyze_trend(data_stream):
    """Analyzes trend direction using slope approximation (simplified)"""
    if len(data_stream) < 3:
        return 0
    recent = data_stream[-3:]
    return int((recent[2] - recent[0]) / 2)

def rolling_average(values, window=3):
    """Computes rolling average with given window size"""
    if len(values) < window:
        return [0]
    averages = []
    for i in range(len(values) - window + 1):
        averages.append(sum(values[i:i+window]) / window)
    return averages

def detect_anomalies(readings, baseline):
    """Detects significant deviations from baseline levels"""
    anomalies = []
    for i, val in enumerate(readings):
        if abs(val - baseline) > baseline * 0.3:
            anomalies.append(i)
    return anomalies

# Irrelevant helper function - dead code path (red herring)
def legacy_compatibility_mode(config):
    mode_flag = config.get('version', 0) % 2 == 1
    buffer_size = config.get('buffer', 1024)
    return {'active': mode_flag, 'size': buffer_size * 2}

# Another decoy function that is never called
def calculate_wind_correction(speed, direction):
    corrected = speed * math.sin(math.radians(direction))
    adjustment = 0
    if direction > 180:
        adjustment = corrected * 0.15
    return corrected + adjustment

# Main processing pipeline
sensor_data = [
    [45, 47, 46, 50, 60, 75, 80, 78, 70, 65],  # PM2.5 readings over time
    [30, 32, 33, 35, 34, 36, 40, 42, 41, 43],   # NO2 readings over time
    [55, 54, 53, 52, 54, 58, 60, 59, 57, 55]    # O3 readings (irrelevant)
]

# Extract only relevant streams (PM2.5 and NO2)
primary_streams = sensor_data[:2]
secondary_stream = sensor_data[2]  # Unused but referenced to mislead

# Baseline thresholds (μg/m³)
threshold_map = {
    'pm25': {'safe': 50, 'warning': 75, 'danger': 100},
    'no2': {'safe': 40, 'warning': 50, 'danger': 60},
    'o3': {'safe': 60}  # Partial entry to distract
}

# Distractor variables - not used in final computation
calibration_offset = 2.5
maintenance_log = [1, 0, 1, 1, 0]
uptime_hours = 127
deprecated_flag = False

# Data preprocessing with distractors
processed_sets = []
for idx, stream in enumerate(primary_streams):
    avg_val = sum(stream) / len(stream)
    trend = analyze_trend(stream)
    
    # Rolling average distraction - computed but not used directly
    roll_avgs = rolling_average(stream)
    smoothed = roll_avgs[-1] if roll_avgs else avg_val
    
    # Anomaly detection (used only indirectly)
    base_line = threshold_map['pm25']['safe'] if idx == 0 else threshold_map['no2']['safe']
    anomalies = detect_anomalies(stream, base_line)
    
    # Only the count of anomalies matters in final logic
    processed_sets.append({
        'data': stream,
        'average': avg_val,
        'trend_score': trend,
        'anomaly_count': len(anomalies),
        'smoothed_value': smoothed  # Red herring
    })

# Filtering based on trend significance (only increasing trends considered)
filtered_data = []
for entry in processed_sets:
    if entry['trend_score'] > 0:  # Only positive trends included
        filtered_data.append(entry)

# Decoy data structure - looks important but unused
system_health = {
    'sensors_active': 2,
    'last_calibration': '2023-11-05',
    'firmware': 'v2.1.8',
    'battery': 87
}

# Critical intermediate values with distractions
impact_weights = [1.8, 0.9]  # Weighting PM2.5 more than NO2
adjustment_factor = 0.95

# Auxiliary calculation - appears relevant but isn't used
composite_index = 0
for entry in processed_sets:
    primary = entry['average']
    secondary = entry['trend_score']
    contribution = (primary * 0.7) + (secondary * 2.5)
    composite_index += contribution
composite_index /= len(processed_sets)

# Real processing begins here - depends only on filtered_data and threshold_map
def process_readings(valid_entries, limits):
    score = 0
    for item in valid_entries:
        raw_avg = item['average']
        anomaly_penalty = item['anomaly_count'] * 3
        
        # Determine pollutant type by index (first is PM2.5, second NO2)
        limit_key = 'pm25' if score == 0 else 'no2'
        danger_level = limits[limit_key]['danger']
        warning_level = limits[limit_key]['warning']
        
        # Base impact based on threshold crossing
        if raw_avg >= danger_level:
            level_impact = 8
        elif raw_avg >= warning_level:
            level_impact = 5
        else:
            level_impact = 2
        
        # Modify by trend (already ensured positive via filter)
        trend_boost = int(item['trend_score'])
        
        # Accumulate score (this modifies external scope due to closure-like behavior)
        nonlocal score
        score += level_impact + trend_boost - anomaly_penalty
    
    # Apply hidden correction: if both entries pass through, extra weight
    if len(valid_entries) == 2:
        score = int(score * 1.2)
    
    # Final transformation
    return max(1, min(100, int(score)))

# Execute main logic
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")