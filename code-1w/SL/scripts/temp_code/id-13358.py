import itertools

# Simulated sensor array data from a distributed monitoring system
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8, 24.4, 26.2, 23.7]
pressure_readings = [101.3, 102.1, 100.9, 103.5, 99.8, 101.0, 102.8, 100.5]
humidity_readings = [45, 47, 50, 44, 52, 48, 46, 51]

# Irrelevant preprocessing: rolling average (not used in final calculation)
def rolling_average(data, window=3):
    return [sum(data[i:i+window]) / window for i in range(len(data)-window+1)]

smoothed_temp = rolling_average(temperature_readings)
smoothed_pressure = rolling_average(pressure_readings)

# Distractor function: entropy calculation (unused)
def calculate_entropy(values):
    total = sum(values)
    probs = [v/total for v in values if v > 0]
    from math import log
    return -sum(p * log(p) for p in probs)

entropy_humidity = calculate_entropy(humidity_readings[:4])

# Core signal extraction using list comprehension and slicing
strong_signals = [
    temp * 1.2 + hum * 0.3 for temp, hum in 
    zip(temperature_readings[::2], humidity_readings[1::2])
]

# Misleading intermediate transformation (dead end)
signal_magnitude = sum([x**2 for x in strong_signals]) ** 0.5
normalization_factor = max(strong_signals) if strong_signals else 1
scaled_signals = [s / normalization_factor for s in strong_signals]

# Real computation path begins: pattern detection with itertools
paired_offsets = list(itertools.pairwise([int(t) for t in temperature_readings]))
drift_patterns = [abs(b - a) for a, b in paired_offsets if a < b]

# Key derived metric (used later)
instability_score = sum(drift_patterns)

# Simulated system state with red herring fields
system_state = {
    'status': 'nominal',
    'uptime_hours': 8765,
    'version': '3.7.1-alpha',
    'health_factor': 0.87,
    'diagnostics': {
        'latency_ms': [12, 15, 11, 14],
        'retry_count': 3
    }
}

# Decoy data structure
historical_baselines = {
    'temp_avg': 24.0,
    'pressure_avg': 101.5,
    'drift_tolerance': 1.5
}

# Composite metric array built with list comprehension and slicing
aggregate_metrics = [
    len(temperature_readings),
    sum(pressure_readings) // len(pressure_readings),
    instability_score * 2,
    entropy_humidity * 10,
    signal_magnitude // 10
]

# Unused control flow (distractor)
if system_state['uptime_hours'] > 5000:
    adjustment = 1.05
    # This block appears important but is not connected to final result
    enhanced_diagnostics = [val * adjustment for val in aggregate_metrics]

# Critical assignment point
final_diagnostic = aggregate_metrics[2] * system_state['health_factor']

# Output required format
print(f"Result: {final_diagnostic}")