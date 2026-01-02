def sensor_validation(readings):
    """Irrelevant validation function (dead code path)."""
    return all(0 <= r <= 1000 for r in readings)


def legacy_calibrate(x):
    """Outdated calibration (decoy function)."""
    return (x * 0.97) + 3

# Irrelevant constants (distractors)
MAX_BUFFER_SIZE = 512
RETRY_LIMIT = 3
DEBUG_MODE = True
DEFAULT_TIMEOUT = 15.5

# Sensor metadata (partially relevant)
sensor_specs = {
    'temp': {'scale': 'C', 'range': (-40, 125)},
    'pressure': {'scale': 'kPa', 'range': (80, 105)},
    'humidity': {'scale': '%', 'range': (0, 100)}
}

# Simulated raw data from multiple sensors
raw_streams = [
    [23, 25, 24, 26, 28],
    [98, 99, 98, 100, 101],
    [60, 62, 61, 59, 63]
]

# Misleading transformation (not used in final path)
decoy_normalized = []
for stream in raw_streams:
    norm = [(val - min(stream)) / (max(stream) - min(stream)) for val in stream]
    decoy_normalized.append(norm)

# Key processing begins
offsets = [2, -1, 0]  # Adjustment per sensor channel
adjusted_streams = []
for i, stream in enumerate(raw_streams):
    adjusted = [val + offsets[i] for val in stream]
    adjusted_streams.append(adjusted)

# Transpose data: from channels x time to time x channels (using zip)
transposed_data = list(zip(*adjusted_streams))  # Now each entry is (temp, pressure, humidity)

# Apply thresholds based on environmental rules
threshold_map = {
    'high_temp': 25,
    'low_pressure': 99,
    'high_humidity': 60
}

status_flags = []
for t, row in enumerate(transposed_data):  # using enumerate
    temp, pressure, humidity = row
    
    # Complex conditional logic with short-circuiting and comparisons
    critical = False
    if temp > threshold_map['high_temp']:
        if pressure < threshold_map['low_pressure'] or humidity > threshold_map['high_humidity']:
            critical = True
    
    # Bitwise combination of status (bit manipulation red herring)
    status_code = (critical << 2) | (temp > 24) | ((pressure < 100) << 1)
    status_flags.append(status_code)

# Filter only high-severity events
alert_indices = [i for i, code in enumerate(status_flags) if (code & 4) != 0]  # Check bit 2

# Unused diagnostic path (dead code)
correlation_score = 0
if len(alert_indices) > 1:
    gaps = [alert_indices[i+1] - alert_indices[i] for i in range(len(alert_indices)-1)]
    correlation_score = sum(gaps) / len(gaps)

# Processed data structure used in final analysis
processed_data = []
for idx in alert_indices:
    original_vals = raw_streams[0][idx], raw_streams[1][idx], raw_streams[2][idx]
    adj_vals = adjusted_streams[0][idx], adjusted_streams[1][idx], adjusted_streams[2][idx]
    processed_data.append({
        'time': idx,
        'original': original_vals,
        'adjusted': adj_vals,
        'flag': status_flags[idx]
    })

# Auxiliary computation (distractor)
effective_gain = 1.0
for i in range(len(offsets)):
    effective_gain *= (1 + offsets[i] * 0.01)

# Core diagnostic algorithm (recursive)
def analyze_readings(data, limits, index=0, accumulator=0):
    if index >= len(data):
        return accumulator * 2  # Final amplification
    
    entry = data[index]
    orig_temp, orig_pres, orig_hum = entry['original']
    adj_temp, adj_pres, adj_hum = entry['adjusted']
    
    # Compound arithmetic and logic
    deviation = (adj_temp - orig_temp) + (orig_hum - adj_pres)
    
    # Conditional recursion with side-effect-like accumulation
    if adj_temp > limits['high_temp'] and adj_hum > limits['high_humidity']:
        contribution = abs(deviation) * (adj_pres / 100.0)
        accumulator += contribution
    
    return analyze_readings(data, limits, index + 1, accumulator)

# Trigger point: what is the value of final_diagnostic here?
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")