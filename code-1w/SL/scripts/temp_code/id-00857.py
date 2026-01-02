import math

# Simulated sensor fusion system for environmental monitoring
def collect_readings():
    raw_streams = {
        'temp': [23.5, 24.1, 22.9, 25.0, 23.8],
        'humidity': [45, 47, 50, 44, 46],
        'co2': [410, 415, 405, 420, 412]
    }
    return raw_streams

# Irrelevant preprocessing path (dead function)
def normalize_legacy(data):
    result = {}
    for key, values in data.items():
        mean = sum(values) / len(values)
        result[key] = [v - mean for v in values]
    return result

# Unused transformation function (distractor)
def transform_frequency(signal):
    return [math.sin(x * 0.1) for x in signal]

# Critical processing function with meaningful logic
def aggregate_window(readings, window_size=3):
    aggregated = {}
    for sensor, values in readings.items():
        windows = []
        for i in range(0, len(values) - window_size + 1):
            window_avg = sum(values[i:i+window_size]) / window_size
            windows.append(round(window_avg, 2))
        aggregated[sensor] = windows
    return aggregated

# Higher-order function with lambda (required feature)
def generate_filter(threshold):
    return lambda x: x > threshold

# Decoy diagnostic with misleading output
def preliminary_scan(dataset):
    spike_count = 0
    for stream in dataset.values():
        for val in stream:
            if isinstance(val, list):
                val = sum(val) / len(val)
            if val > 100:  # Irrelevant condition
                spike_count += 1
    score = spike_count * 10  # Red herring computation
    return score  # Never used

# Core analysis chain
readings = collect_readings()

# Apply real transformation
processed_data = aggregate_window(readings)

# Extract representative metrics
data_summary = {
    'temp_peak': max(processed_data['temp']),
    'humidity_stable': sum(1 for x in processed_data['humidity'] if x >= 45),
    'co2_trend': processed_data['co2'][-1] - processed_data['co2'][0]
}

# Define thresholds with some irrelevant ones
thresholds = {
    'temp_limit': 24.0,
    'safe_humidity_days': 2,
    'co2_rising': 5.0,
    'ignore_me': 999,
    'unused_flag': True
}

# Real evaluation logic
safety_checks = []
safety_checks.append(data_summary['temp_peak'] > thresholds['temp_limit'])
safety_checks.append(data_summary['humidity_stable'] >= thresholds['safe_humidity_days'])
safety_checks.append(abs(data_summary['co2_trend']) < thresholds['co2_rising'])

# Bit manipulation decoy (irrelevant)
status_word = 0b1101
masked = status_word & 0b0111
shifted = masked << 2
checksum_fake = bin(shifted ^ 0b1010)

# Unused dictionary operations (distractor)
diagnostic_log = {
    'initial': readings,
    'interim': processed_data,
    'flags': {f'chk{i}': v for i, v in enumerate(safety_checks)}
}
diagnostic_log['timestamp'] = '2023-11-05'
diagnostic_log.pop('flags', None)  # Misleading mutation

# Critical lambda usage (required feature)
evaluate_critical = generate_filter(thresholds['temp_limit'])
critical_temp_count = sum(1 for t in readings['temp'] if evaluate_critical(t))

# Final computation path
consensus = all(safety_checks)
weight_map = {'temp': 1.5, 'humidity': 1.2, 'co2': 1.3}
weighted_score = sum(
    data_summary[f'{key}_peak'] * weight_map[key]
    for key in ['temp']
) if critical_temp_count > 2 else 0

# Final diagnostic calculation (answer point)
baseline = 42
adjustment = math.floor(abs(data_summary['co2_trend']) * 10)
final_diagnostic = baseline + adjustment

# Print required output
print(f"Result: {final_diagnostic}")