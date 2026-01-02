import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.4, 25.1, 22.8, 26.5, 24.3, 27.8, 28.2, 21.9, 25.6, 26.1]
humidity_readings = [45, 52, 58, 44, 60, 65, 54, 49, 56, 62]
pressure_readings = [1013, 1015, 1012, 1009, 1016, 1018, 1014, 1011, 1017, 1019]

# Irrelevant backup logs (distractor data)
backup_logs = ['OK', 'OK', 'ERROR', 'OK', 'WARNING', 'OK', 'OK', 'ERROR', 'OK', 'OK']
log_status_count = {status: backup_logs.count(status) for status in set(backup_logs)}

# System calibration offset (red herring - not used in final calculation)
calibration_matrix = [[0.98, 1.02], [1.01, 0.99]]
system_offset = sum(sum(row) for row in calibration_matrix)

# Threshold configuration (partially relevant)
thresh_high_temp = 27.0
thresh_low_temp = 22.0
humidity_focus_zone = [50, 60]

# Derived thresholds (only some are used)
threshold_levels = {
    'temp_critical': thresh_high_temp + 1.5,
    'temp_alert': thresh_high_temp,
    'humidity_high': 55,
    'pressure_stable': 1015
}

# Irrelevant signal processing chain (dead path)
def process_signal(raw_data):
    smoothed = [raw_data[0]]
    for i in range(1, len(raw_data)):
        smoothed.append(0.7 * raw_data[i] + 0.3 * smoothed[i-1])
    return [round(x, 2) for x in smoothed]

filtered_signal = process_signal(pressure_readings)  # Unused downstream

# Data fusion and anomaly detection
combined_metrics = []
for i in range(len(temperature_readings)):
    temp_score = 1 if temperature_readings[i] > thresh_high_temp else 0
    humid_score = 1 if humidity_readings[i] > threshold_levels['humidity_high'] else 0
    press_trend = 0
    if i > 0:
        press_trend = 1 if pressure_readings[i] > pressure_readings[i-1] else -1
    
    # Composite risk score (some components irrelevant)
    risk_vector = (
        temp_score * 3 + 
        humid_score * 2 + 
        max(0, press_trend)  # Only positive trend contributes
    )
    combined_metrics.append((temperature_readings[i], humidity_readings[i], risk_vector))

# Filter data based on temperature threshold (key filtering step)
filtered_data = [
    entry for entry in combined_metrics 
    if entry[0] >= thresh_low_temp
]

# Decoy function - appears important but unused
def compute_stability_index(data_list):
    if not data_list:
        return 0.0
    variances = [np.var(d) for d in data_list]  # Would fail (no numpy) - deliberate dead end
    return sum(variances) / len(variances)

# Real analysis function with conditional logic and set operations
def analyze_readings(readings, thresholds):
    if not readings:
        return -1
    
    # Extract unique risk levels
    risk_levels = {item[2] for item in readings}  # Set comprehension
    high_risk_count = len([r for r in readings if r[2] >= 2])  # List comprehension
    
    # Determine dominant humidity pattern
    above_humid_thresh = [h for h in readings if h[1] > thresholds['humidity_high']]
    humid_regime = 'DRY' if len(above_humid_thresh) < 3 else 'HUMID'
    
    # Conditional expression with arithmetic
    base_diagnostic = 100 if humid_regime == 'HUMID' else 85
    
    # Critical adjustment based on maximum risk level
    max_risk = max(risk_levels)
    adjustment_factor = 0.9 if max_risk >= 3 else 1.1
    
    # Final computation (this produces the answer)
    intermediate = base_diagnostic * adjustment_factor
    final_diagnostic = int(intermediate) + len(filtered_data)
    
    # Dead code branch (never reached)
    if False:
        fallback = sum(risk_levels) * 10
        final_diagnostic = fallback  # Never executed
    
    return final_diagnostic

# Execute main analysis
final_diagnostic = analyze_readings(filtered_data, threshold_levels)

# Print result as required
print(f"Target result: {final_diagnostic}")