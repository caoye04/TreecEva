import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_samples = [256, 192, 128, 64, 32, 16, 8, 4, 2, 1]
    scale_factor = 3.7
    adjusted = [int(x * scale_factor) for x in raw_samples]
    return adjusted

# Irrelevant helper - dead code path (red herring)
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    normalized = [(x - mean_val) / mean_val for x in data]
    return normalized

# Signal processing core
def preprocess_signal(raw_signal):
    filtered = []
    for val in raw_signal:
        if val & 1:  # Check oddness using bitwise
            val ^= 255  # XOR flip for noise reduction simulation
        val = abs(val - 100) + 50
        filtered.append(val)
    return filtered

# Misleading transformation chain (distractor)
def compute_legacy_metrics(signal):
    stats = {}
    stats['peak'] = max(signal)
    stats['trough'] = min(signal)
    stats['span'] = stats['peak'] - stats['trough']
    stats['entropy'] = 0.0
    for x in signal:
        if x > 0:
            stats['entropy'] += x * math.log(x, 2)
    return stats  # Not used later - red herring

# Key data transformation
config_profile = {
    'mode': 'diagnostic',
    'version': '3.4.1',
    'thresholds': {'low': 120, 'high': 200, 'critical': 250}
}

# String-based routing logic (uses string methods)
def route_by_profile(mode_str):
    mode_clean = mode_str.strip().lower()
    if 'diag' in mode_clean:
        return 'analysis'
    elif 'safe' in mode_clean:
        return 'bypass'
    else:
        return 'quarantine'

# Complex conditional processing
routing_key = route_by_profile(config_profile['mode'])
processed_data = []
if routing_key == 'analysis':
    raw_input = collect_sensor_readings()
    processed_data = preprocess_signal(raw_input)
    
    # Dead branch - unreachable due to above condition
    if routing_key == 'bypass':
        processed_data = [x // 2 for x in raw_input]

# Unused but plausible-looking aggregation (distractor)
avg_vals = [x for i, x in enumerate(processed_data) if i % 2 == 0]
temp_aggregate = sum(avg_vals) / len(avg_vals) if avg_vals else 0

# Dictionary mapping for dynamic thresholds (used later)
threshold_map = {
    level.upper(): int(val * 0.95) for level, val in config_profile['thresholds'].items()
}
threshold_map['ADJUSTED_CRITICAL'] = threshold_map['CRITICAL'] + 10

# Diagnostic engine with multiple logic steps
def analyze_signal(data, limits):
    count_high = 0
    count_critical = 0
    rolling_sum = 0
    history = []
    
    for idx, reading in enumerate(data):
        # Simulate time-series adjustment
        adjusted_reading = reading
        if idx % 3 == 0:
            adjusted_reading = (adjusted_reading >> 2) * 3  # Right shift and scale
        
        # Accumulate for average
        rolling_sum += adjusted_reading
        history.append(adjusted_reading)
        
        # Classification logic
        if adjusted_reading > limits['HIGH']:
            count_high += 1
        if adjusted_reading > limits['ADJUSTED_CRITICAL']:
            count_critical += 1
    
    # Compute derived metrics
    base_avg = rolling_sum / len(history)
    fluctuation = max(history) - min(history)
    
    # Final composite score (this is the answer)
    score_component_1 = base_avg * 1.5
    score_component_2 = fluctuation * 0.7
    penalty = count_critical * 50
    
    final_score = score_component_1 + score_component_2 - penalty
    
    # Additional irrelevant transformations (distractors)
    diagnostics_log = {
        'readings_processed': len(history),
        'high_exceedances': count_high,
        'critical_events': count_critical,
        'stability_index': fluctuation / (base_avg + 1e-8),
        'version_tag': f"V{config_profile['version']}"
    }
    
    # This function returns only the final_score; others are distractions
    return int(final_score)  # Truncate to integer

# Execution point of interest
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")