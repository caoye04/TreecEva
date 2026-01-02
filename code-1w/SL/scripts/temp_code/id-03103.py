import math

# Simulated sensor array data with noise and calibration offsets
temperature_readings = [23.4, 24.1, 22.9, 25.6, 26.7, 24.3, 23.8]
humidity_readings = [45, 47, 50, 44, 52, 48, 46]
pressure_readings = [1013, 1012, 1015, 1010, 1008, 1014, 1016]

# Irrelevant backup data (distractor)
backup_temperatures = [22.1, 23.0, 24.2]  # Not used in main logic
legacy_mode_enabled = True  # Misleading flag, not actually used

# Calibration parameters (some are decoys)
calibration_offset_A = 0.3
scaling_factor_X = 1.02  # Unused scaling factor
calibration_curve = lambda x: x * 0.98 + 0.15

# Preprocess: apply real calibration and filter anomalies
def preprocess_sensor_data(raw_temps):
    calibrated = []
    for t in raw_temps:
        adjusted = calibration_curve(t)
        if 20 <= adjusted <= 30:  # Valid range
            calibrated.append(adjusted)
    return calibrated

# Secondary transformation chain (partially irrelevant)
def enhance_data(seq):
    return [round(x ** 0.5 * 1.1, 3) for x in seq if x > 0]  # Unused later

# Signal validation using bitwise pattern matching (red herring function)
def validate_signal_integrity(data):
    signature = 0
    for i, val in enumerate(data):
        signature ^= int(val) & 0xFF
        signature = (signature << 1) | (signature >> 7)
        signature &= 0xFF
    return signature == 0x5A  # Never actually checked

# Real processing begins here
processed_temp_data = preprocess_sensor_data(temperature_readings)

# Create composite index using humidity and dummy weight (distractor structure)
index_weights = {"morning": 0.4, "afternoon": 0.6}
weighted_index = sum(h * index_weights["afternoon"] for h in humidity_readings) / len(humidity_readings)

# Decoy statistical analysis
mean_pressure = sum(pressure_readings) / len(pressure_readings)
pressure_variance = sum((p - mean_pressure) ** 2 for p in pressure_readings) / len(pressure_readings)
stdev_pressure = math.sqrt(pressure_variance)

# Core diagnostic engine
status_codes = []
def analyze_readings(temps):
    total_score = 0.0
    trend_stability = 0
    
    # Analyze temperature trend
    for i in range(1, len(temps)):
        if abs(temps[i] - temps[i-1]) < 0.5:
            trend_stability += 1
    
    stability_ratio = trend_stability / (len(temps) - 1) if len(temps) > 1 else 1.0
    
    # Compute entropy-like complexity measure (real calculation)
    entropy_proxy = 0.0
    for t in temps:
        prob = (t - min(temps)) / (max(temps) - min(temps) + 1e-8)
        prob = max(prob, 1e-8)
        entropy_proxy -= prob * math.log(prob)
    
    # Apply hidden weighting formula
    raw_metric = stability_ratio * 100 + entropy_proxy * 15
    
    # Distractor: unused classification tree
    def classify_system_state(x):
        if x > 90: return 'OPTIMAL'
        elif x > 70: return 'STABLE'
        elif x > 50: return 'MONITOR'
        else: return 'CRITICAL'
    
    # Final computation path (answer depends only on this)
    adjustment_factor = 0.87
    if stability_ratio >= 0.6:
        adjustment_factor += 0.13
    final_diagnostic = int(raw_metric * adjustment_factor)  # This is the key result
    
    return final_diagnostic

# Execute main analysis
final_diagnostic = analyze_readings(processed_temp_data)

# Dead code path (misleading)
if legacy_mode_enabled:
    final_diagnostic = -999  # Never reached due to conditions above

# Print result as required
print(f"Result: {final_diagnostic}")