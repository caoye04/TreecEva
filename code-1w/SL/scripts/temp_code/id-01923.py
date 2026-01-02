import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8]
humidity_readings = [55.2, 57.8, 53.1, 60.5, 62.0, 58.7, 56.3]
pressure_readings = [1013.25, 1012.10, 1014.30, 1011.80, 1009.45, 1010.00, 1013.90]

# Irrelevant backup dataset (distractor)
backup_temperatures = [18.3, 19.0, 17.9, 20.1]  # Unused in computation

# Noise filter using moving average (relevant preprocessing)
def smooth_signal(signal):
    smoothed = []
    for i in range(len(signal)):
        if i < 2 or i >= len(signal) - 2:
            smoothed.append(signal[i])
        else:
            window_avg = sum(signal[i-2:i+3]) / 5
            smoothed.append(round(window_avg, 2))
    return smoothed

# Apply smoothing to primary signals
temp_smoothed = smooth_signal(temperature_readings)
humid_smoothed = smooth_signal(humidity_readings)
press_smoothed = smooth_signal(pressure_readings)

# Compute derived indices (some relevant, some red herrings)
heat_index = []
for t, h in zip(temp_smoothed, humid_smoothed):
    hi = t + 0.53 * h  # Simplified approximation
    heat_index.append(round(hi, 2))

# Dew point calculation - actually unused later (dead path)
dew_points = []
for t, h in zip(temp_smoothed, humid_smoothed):
    dew = t - ((100 - h) / 5.0)
    dew_points.append(round(dew, 2))

# Atmospheric stability index (unused distractor)
stability_index = []
for p in press_smoothed:
    stab = (p - 1010.0) * 0.75
    stability_index.append(round(stab, 2))

# Signal coherence metric between temperature and pressure (red herring)
coherence_score = 0
for i in range(len(temp_smoothed)):
    coherence_score += abs(temp_smoothed[i] - press_smoothed[i] / 40.0)
coherence_score = round(coherence_score / len(temp_smoothed), 2)

# Critical processing chain: multi-stage transformation pipeline
processing_stages = {
    'stage_1': lambda x: [val * 1.02 for val in x],
    'stage_2': lambda x: [val + 0.5 for val in x],
    'stage_3': lambda x: [math.log(val) if val > 0 else 0 for val in x],
    'stage_4': lambda x: [val ** 0.95 for val in x]
}

# Apply transformation chain to smoothed temperature
processing_chain = temp_smoothed.copy()
for stage in ['stage_1', 'stage_2', 'stage_3', 'stage_4']:
    processing_chain = processing_stages[stage](processing_chain)

# Diagnostic flags from system health monitor (mix of relevant and irrelevant)
diagnostic_flags = {
    'sensor_a_ok': True,
    'calibration_recent': False,
    'outlier_threshold_met': True,
    'data_fully_synced': False,
    'redundancy_active': True
}

# Real-time anomaly detection (misleading intermediate result)
anomaly_vector = []
for val in temperature_readings:
    if val > 25.0:
        anomaly_vector.append(1)
    else:
        anomaly_vector.append(0)
rolling_anomaly_rate = sum(anomaly_vector) / len(anomaly_vector)

# Actual aggregation logic (well-hidden among distractions)
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probs)
    return round(entropy, 4)

# Auxiliary weight calculation based on humidity variance (irrelevant)
humidity_variance = (max(humid_smoothed) - min(humid_smoothed)) / 2
weight_factor = math.sin(humidity_variance) if humidity_variance > 0 else 0

# Core diagnostic metric: entropy of final processed signal
main_diagnostic_value = compute_entropy(processing_chain)

# Secondary metrics (distractors)
secondary_diagnostic = sum(press_smoothed) / len(press_smoothed)
tertiary_diagnostic = max(heat_index) - min(heat_index)

# Final aggregation function combining multiple sources
# BUT only main_diagnostic_value actually affects the result
# All other parameters are ignored in this function (decoy structure)
def aggregate_metrics(processed_signal, flags):
    _ = flags.get('calibration_recent')  # Unused
    _ = flags.get('data_fully_synced')   # Unused
    
    # Hidden critical operation: find position of maximum in original temp
    peak_idx = temperature_readings.index(max(temperature_readings))
    
    # Extract corresponding value from processed chain at same index
    extracted_value = processed_signal[peak_idx]
    
    # Apply final transformation using seemingly random constant
    magic_constant = 17.39
    result = (extracted_value * magic_constant) + 0.5
    
    # Additional decoy operations below (no effect)
    if flags.get('outlier_threshold_met'):
        dummy = sum([math.sqrt(x) for x in processed_signal[-3:]])
    if flags.get('redundancy_active'):
        dummy2 = math.exp(-min(processed_signal))
        
    return int(round(result))

# Execute final computation
temp_copy_for_debug = temp_smoothed  # Dead storage
final_diagnostic = aggregate_metrics(processing_chain, diagnostic_flags)

# Output the target result
print(f"Result: {final_diagnostic}")