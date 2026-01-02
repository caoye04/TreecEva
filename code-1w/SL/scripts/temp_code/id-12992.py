import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 24.7, 23.9, 25.8]
humidity_readings = [45, 47, 50, 44, 48, 52, 46, 49]
co2_levels = [410, 415, 420, 408, 430, 425, 412, 418]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.037
CALIBRATION_OFFSET_B = -0.012
REFERENCE_VOLTAGE = 3.3
MAX_RESOLUTION = 4096

# Preprocess function with red herring operations
def preprocess_sensor_data(raw_temps, raw_humid):
    normalized = []
    scaling_factor = REFERENCE_VOLTAGE / MAX_RESOLUTION  # Unused in logic
    adjustment = CALIBRATION_OFFSET_A * 1.5  # Distractor calculation
    
    for i in range(len(raw_temps)):
        temp_c = raw_temps[i]
        hum_p = raw_humid[i]
        # Real transformation: convert to heat index approximation
        hi = temp_c + 0.33 * hum_p - 0.7 * temp_c * (1 - hum_p / 100) - 4.0
        normalized.append(round(hi, 2))
    
    # Dead code path (never executed due to prior return structure)
    if len(normalized) > 100:
        fallback = sum([x * 0.9 for x in normalized])
        return [fallback] * len(normalized)
    
    return normalized

# Signal processing with multiple distractions
def filter_anomalies(data_stream):
    filtered = []
    anomaly_flags = []
    threshold = sum(data_stream) / len(data_stream) + 0.5  # Dynamic threshold
    
    for val in data_stream:
        is_anomalous = False
        if val > threshold * 1.1:
            is_anomalous = True
        elif val < 5:  # Impossible condition given data scale
            is_anomalous = True
            backup_reset = 0  # Dead variable
        
        anomaly_flags.append(is_anomalous)
        if not is_anomalous:
            filtered.append(val)
    
    # Unused statistical block (misleading intermediate result)
    if len(anomaly_flags) > 0:
        false_count = anomaly_flags.count(False)
        true_ratio = false_count / len(anomaly_flags)
        adjusted_ratio = math.log(max(true_ratio, 0.1)) * 100  # Not used
    
    return filtered

# Complex analysis combining multiple concepts
def compute_stability_index(readings):
    n = len(readings)
    if n == 0:
        return 0.0
    
    mean_val = sum(readings) / n
    variance = sum([(x - mean_val) ** 2 for x in readings]) / n
    std_dev = math.sqrt(variance)
    
    # Apply decay weighting (real contribution)
    weighted_sum = sum([readings[i] * math.exp(-0.1 * i) for i in range(n)])
    
    # Composite stability metric
    stability = (mean_val * 0.6) + (weighted_sum * 0.3) - (std_dev * 0.1)
    return round(stability, 3)

# Decoy function that looks important but is unused
def legacy_compatibility_mode(data):
    """Old algorithm - kept for backward compatibility checks"""
    result = 0
    for item in data:
        result ^= int(item * 10)  # Bitwise distraction
    return result % 1000

# Main diagnostic engine with list comprehension and nesting
def analyze_readings(heat_index_values):
    # Step 1: Identify critical thresholds
    critical_peaks = [x for x in heat_index_values if x > 25.0]
    peak_count = len(critical_peaks)
    
    # Step 2: Compute trend progression (real logic)
    trends = []
    for i in range(1, len(heat_index_values)):
        change = heat_index_values[i] - heat_index_values[i-1]
        trends.append(change)
    
    # Step 3: Accumulate directional bias
    positive_trend = sum([1 for t in trends if t > 0])
    negative_trend = sum([1 for t in trends if t < 0])
    neutral_trend = sum([1 for t in trends if t == 0])
    
    # Step 4: Calculate net movement score
    net_bias = positive_trend - negative_trend + (neutral_trend * 0.5)
    
    # Step 5: Combine with peak severity (actual answer formation)
    severity_weight = sum(critical_peaks) if critical_peaks else 0
    base_score = compute_stability_index(heat_index_values)
    
    # Final diagnostic formula (key statement)
    final_diagnostic = int(base_score * 2 + net_bias * 1.5 + severity_weight / 2)
    
    # Multiple decoy variables (irrelevant computations)
    diagnostic_hash = 0
    for c in "DGN-7X":
        diagnostic_hash += ord(c) ^ peak_count
    checksum_verify = (diagnostic_hash * 7) % 97
    
    # Another red herring: recursive dead end
    def validate_subsystem(level):
        if level <= 0:
            return 1
        return level + validate_subsystem(level - 2)
    
    return final_diagnostic

# Execution flow with distractors
processed_signals = preprocess_sensor_data(temperature_readings, humidity_readings)
cleaned_signals = filter_anomalies(processed_signals)

# Key statement where answer is determined
final_diagnostic = analyze_readings(processed_signals)

# Print target result
print(f"Result: {final_diagnostic}")