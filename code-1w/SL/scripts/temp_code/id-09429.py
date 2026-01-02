import math

# Simulated sensor array data (irrelevant initial setup)
sensor_offsets = [0.1, -0.3, 0.7, -0.8, 0.2]
baseline_calibration = sum([abs(x) for x in sensor_offsets]) / len(sensor_offsets)

# System state variables
temperature_profile = [22.5, 23.1, 24.0, 23.8, 25.2, 26.0, 25.8]
humidity_readings = [45, 47, 52, 58, 60, 59, 56]
pressure_log = [1013.25, 1012.8, 1011.9, 1010.5, 1009.7, 1008.9, 1008.4]

# Irrelevant transformation chain (dead path)
def legacy_transform(data):
    return [x * 1.02 + 0.5 for x in data if x > 0]

# Unused diagnostic function (decoy)
def compute_health_score(metrics):
    weight = 0.8 if len(metrics) > 5 else 0.6
    return sum(m ** 0.9 for m in metrics) * weight

# Core processing logic
def normalize_series(series):
    mean_val = sum(series) / len(series)
    return [(x - mean_val) / mean_val for x in series]

def detect_anomalies(series, sensitivity=0.05):
    return [i for i, x in enumerate(series) if abs(x) > sensitivity]

def rolling_window_average(series, window=3):
    if len(series) < window:
        return [sum(series)/len(series)]
    windows = [series[i:i+window] for i in range(len(series)-window+1)]
    return [sum(w)/len(w) for w in windows]

def calculate_entropy(values):
    total = sum(abs(v) for v in values)
    if total == 0:
        return 0.0
    probabilities = [abs(v) / total for v in values]
    return -sum(p * math.log(p) for p in probabilities if p > 0)

# Complex data transformation pipeline
preliminary_shift = [t * (1 + h/100) for t, h in zip(temperature_profile, humidity_readings)]
adjusted_series = normalize_series(preliminary_shift)
anomaly_indices = detect_anomalies(adjusted_series, sensitivity=0.08)

# Secondary irrelevant computation branch (misleading path)
predictive_model_bias = 0.0
for i in range(len(pressure_log)):
    if pressure_log[i] < 1010.0:
        predictive_model_bias += 0.01 * (1010.0 - pressure_log[i])
predictive_model_bias = round(predictive_model_bias, 3)

# Dummy container for red herring
system_flags = {
    'calibration_needed': False,
    'legacy_mode': True,
    'data_enriched': False,
    'bias_compensated': bool(predictive_model_bias > 0.05)
}

# Actual relevant processing begins here
entropy_measure = calculate_entropy(adjusted_series)
smoothed_signal = rolling_window_average([abs(x) for x in adjusted_series])

# Critical intermediate computation (part of logical chain)
event_marker = 0
for idx in anomaly_indices:
    if idx > 0:
        event_marker += int(abs(adjusted_series[idx]) * 100)

# Distractor: unused but plausible-looking aggregation
temporal_variance = sum(
    (adjusted_series[i+1] - adjusted_series[i])**2 
    for i in range(len(adjusted_series)-1)
)

# Key data structure used in final calculation
processing_chain = {
    'signal_entropy': entropy_measure,
    'event_count': len(anomaly_indices),
    'event_marker': event_marker,
    'smooth_trend': sum(smoothed_signal) / len(smoothed_signal),
    'raw_anomalies': anomaly_indices
}

# Threshold logic with conditional expression
base_threshold = 0.45
threshold_regulator = base_threshold if system_flags['calibration_needed'] else base_threshold * 1.2

# Final diagnostic computation (target statement)
def aggregate_metrics(chain, threshold):
    score = 0
    # Weighted contribution from entropy
    if chain['signal_entropy'] > threshold:
        score += 85
    # Contribution from event count
    if chain['event_count'] >= 2:
        score += chain['event_marker'] // 10
    else:
        score += chain['event_count'] * 15
    # Conditional trend bonus
    trend_bonus = 20 if chain['smooth_trend'] > 0.1 else 5
    score += trend_bonus
    
    # Red herring: this block appears important but is not triggered
    debug_weights = []
    for i in range(3):
        weight = (i + 1) * 0.3
        debug_weights.append(weight * chain['signal_entropy'])
    if sum(debug_weights) > 10:  # Never true given actual values
        score += 50
        
    return score

# Execute final statement
diagnostic_trace = []
for step in range(3):
    intermediate = processing_chain['signal_entropy'] * (step + 1)
    diagnostic_trace.append(intermediate)

final_diagnostic = aggregate_metrics(processing_chain, threshold_regulator)
print(f"Result: {final_diagnostic}")