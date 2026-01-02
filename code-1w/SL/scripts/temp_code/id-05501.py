import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4]
humidity_readings = [45, 47, 50, 44, 46, 48]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011]

# Auxiliary irrelevant sensor data (distractor)
sound_levels = [65, 70, 60, 80, 75, 68]  # Unused in final calculation
dust_particles = {1: 12, 2: 15, 3: 10}  # Decoy dictionary

# Mapping of thresholds for anomaly detection (some values are red herrings)
anomaly_thresholds = {
    'temp_high': 30.0,
    'temp_low': 15.0,
    'humidity_critical': 80,
    'pressure_spike': 1030
}

# Irrelevant transformation function (dead code path)
def transform_sound_data(data):
    return [x * 1.5 for x in data if x > 60]

# Misleading intermediate computation (distractor)
apparent_risk_score = sum(sound_levels) / len(sound_levels) * 0.3

# Core processing functions
def normalize(data):
    mean_val = sum(data) / len(data)
    return [round(x - mean_val, 2) for x in data]

def detect_spikes(data, threshold_multiplier=2.0):
    normalized = normalize(data)
    avg_abs_dev = sum(abs(x) for x in normalized) / len(normalized)
    spikes = [i for i, x in enumerate(normalized) if abs(x) > threshold_multiplier * avg_abs_dev]
    return set(spikes)

# Data fusion using set operations and arithmetic blending
def fuse_sensor_data(temp, hum, pres):
    norm_temp = normalize(temp)
    norm_hum = normalize(hum)
    norm_pres = normalize(pres)
    
    # Identify anomalous timestamps via set intersection
    temp_outliers = detect_spikes(temp, 1.8)
    hum_outliers = detect_spikes(hum, 2.2)
    pres_outliers = detect_spikes(pres, 2.0)
    
    # Critical fusion point: only timestamps with anomalies in at least two sensors matter
    dual_anomaly_window = (temp_outliers & hum_outliers) | (hum_outliers & pres_outliers) | (temp_outliers & pres_outliers)
    
    # Compute baseline-adjusted composite index over clean windows
    clean_windows = set(range(len(temp))) - dual_anomaly_window
    composite_index = 0.0
    for i in clean_windows:
        # Weighted contribution from normalized readings
        composite_index += (norm_temp[i] * 0.4 + 
                           (norm_hum[i] / 10) * 0.3 + 
                           (norm_pres[i] / 5) * 0.3)
    
    return round(composite_index, 4), dual_anomaly_window

# Higher-order diagnostic processor
def analyze_trend_pattern(values):
    # Simple trend scoring: +1 for increasing, -1 for decreasing triplets
    score = 0
    for i in range(2, len(values)):
        if values[i] > values[i-1] > values[i-2]:
            score += 1
        elif values[i] < values[i-1] < values[i-2]:
            score -= 1
    return score

# Wrapper to simulate system health inference
def process_readings(fusion_result):
    raw_index, anomalies = fusion_result
    
    # Simulated calibration offset (irrelevant in this context but looks important)
    calibration_jitter = sum([anomalies.pop() * 0.1 if anomalies else 0 for _ in range(3)])
    
    # Actual trend analysis on original temperature (subtle reuse of raw data)
    trend_significance = analyze_trend_pattern(temperature_readings)
    
    # Final diagnostic combines index, trend, and squared anomaly count (key formula)
    diagnostic_value = raw_index * 100 + trend_significance * 10 + len(anomalies) ** 2
    
    # Red herring: apparent complexity with unused branches
    if len(anomalies) > 10:
        diagnostic_value *= 0.9
    elif calibration_jitter > 5:
        diagnostic_value += 20
    else:
        pass  # Dead branch
    
    # Final adjustment based on set parity (trivial when anomalies is empty)
    if len(anomalies) % 2 == 1:
        diagnostic_value -= 5

    return int(round(diagnostic_value))

# Irrelevant auxiliary class (distractor)
class DataLogger:
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity
    
    def log(self, entry):
        if len(self.buffer) < self.capacity:
            self.buffer.append(entry)

logger = DataLogger(10)
logger.log("System boot")
logger.log("Sensor init")

# Decoy tuple unpacking with misleading naming
status_flags = ('active', 'calibrated', 'synced')
operation_mode, _, sync_status = status_flags

# Intermediate variables that seem important but aren't used in final result
aggregated_risk = apparent_risk_score + 10
system_stability_estimate = 98.7

# Key execution chain
normalized_temps = normalize(temperature_readings)
sensor_fusion = fuse_sensor_data(temperature_readings, humidity_readings, pressure_readings)
final_diagnostic = process_readings(sensor_fusion)

# Output the target result
print(f"Result: {final_diagnostic}")