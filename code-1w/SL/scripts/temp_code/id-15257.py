import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 24.3, 23.9, 25.1]
humidity_readings = [45, 48, 52, 58, 61, 54, 49, 53]
pressure_readings = [1013, 1015, 1012, 1008, 1005, 1009, 1011, 1014]

# Irrelevant auxiliary measurements (distractor data)
sound_levels = [32, 35, 40, 45, 50, 42, 38, 36]  # Decoy sensor data
light_intensity = [800, 950, 1200, 1300, 1100, 900, 850, 980]  # Not used in final calculation

# Preprocessing: normalize readings to baseline ranges
normalized_temp = [round((t - 20) / 10, 3) for t in temperature_readings]
normalized_humid = [h / 100 for h in humidity_readings]

# Misleading transformation chain (dead-end computation)
entropy_approx = 0.0
for i in range(len(sound_levels)):
    if sound_levels[i] > 40:
        entropy_approx += math.log(sound_levels[i]) * (sound_levels[i] / 100)
entropy_approx = round(entropy_approx, 4)

# Threshold configuration map for diagnostics (critical data structure)
threshold_map = {
    'temp_stability': {'upper': 0.5, 'lower': -0.5, 'weight': 1.2},
    'humid_balance': {'upper': 0.6, 'lower': 0.4, 'weight': 0.8},
    'pressure_trend': {'window': 3, 'tolerance': 4, 'weight': 1.5}
}

# Derived metrics with red herring intermediate values
rate_of_change = []
for i in range(1, len(pressure_readings)):
    rate_of_change.append(abs(pressure_readings[i] - pressure_readings[i-1]))

# Fake anomaly detection (unused function - decoy)
def detect_anomaly(signal, sensitivity=0.9):
    """Unused function - deliberate distraction"""
    anomalies = []
    mean_sig = sum(signal) / len(signal)
    for val in signal:
        if abs(val - mean_sig) > sensitivity * mean_sig * 0.1:
            anomalies.append(True)
        else:
            anomalies.append(False)
    return anomalies

# Real processing begins here
rolling_pressure_avg = []
window_size = threshold_map['pressure_trend']['window']
for i in range(len(pressure_readings) - window_size + 1):
    window_avg = sum(pressure_readings[i:i+window_size]) / window_size
    rolling_pressure_avg.append(round(window_avg, 2))

# Compute deviation scores
stable_temps = [1 if abs(norm - 0.4) < 0.1 else 0 for norm in normalized_temp]
temp_score = sum(stable_temps) * threshold_map['temp_stability']['weight']

balanced_humidity = [1 if 0.4 <= h <= 0.6 else 0 for h in normalized_humid]
humid_score = sum(balanced_humidity) * threshold_map['humid_balance']['weight']

# Pressure trend consistency check
tolerance = threshold_map['pressure_trend']['tolerance']
valid_trends = 0
for i in range(1, len(rolling_pressure_avg)):
    if abs(rolling_pressure_avg[i] - rolling_pressure_avg[i-1]) <= tolerance:
        valid_trends += 1
pressure_score = valid_trends * threshold_map['pressure_trend']['weight']

# Combine into processed feature vector
processed_data = {
    'temp_diagnostic': temp_score,
    'humidity_diagnostic': humid_score,
    'pressure_diagnostic': pressure_score,
    'sample_count': len(temperature_readings),
    'baseline_offset': 20.0
}

# Secondary distraction: unused data fusion attempt
fusion_weights = [0.3, 0.3, 0.4]
data_stream_priority = sorted(processed_data.keys(), key=lambda x: len(x), reverse=True)
weighted_fusion = sum(fusion_weights[i] * processed_data[list(processed_data.keys())[i % 3]] for i in range(len(fusion_weights)))

# Critical analysis function
def analyze_readings(data, thresholds):
    # Nested logic with conditional expressions
    t_val = data['temp_diagnostic']
    h_val = data['humidity_diagnostic']
    p_val = data['pressure_diagnostic']
    
    # Complex decision logic with multiple conditions
    if t_val >= 5.0:
        temp_status = 2
    elif t_val >= 3.0:
        temp_status = 1
    else:
        temp_status = 0
    
    humid_status = 2 if h_val >= 4.0 else (1 if h_val >= 2.0 else 0)
    pressure_status = 2 if p_val >= 6.0 else (1 if p_val >= 3.0 else 0)
    
    # Composite scoring with bit manipulation (unusual but valid)
    status_code = (temp_status << 2) | (humid_status << 1) | pressure_status
    
    # Final diagnostic using weighted combination and adjustment
    raw_diagnostic = t_val * 0.4 + h_val * 0.3 + p_val * 0.3
    
    # Adjustment based on status code using dictionary mapping
    adjustment_map = {
        0: -1.0, 1: -0.5, 2: -0.2, 3: 0.0, 4: 0.1, 5: 0.3, 6: 0.4, 7: 0.5,
        8: 0.6, 9: 0.7, 10: 0.8, 11: 0.9, 12: 1.0, 13: 1.2, 14: 1.5, 15: 2.0
    }
    adjusted_diagnostic = raw_diagnostic + adjustment_map.get(status_code, 0.0)
    
    # Final nonlinear transformation
    final_score = math.tanh(adjusted_diagnostic) * 100
    
    return round(final_score, 4)

# Execute critical statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")