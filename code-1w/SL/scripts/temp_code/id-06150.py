import math

# Simulated telemetry data from distributed sensor array
telemetry_stream = [
    {'sensor': 'A', 'reading': 872, 'status': 'active', 'timestamp': 1648753200},
    {'sensor': 'B', 'reading': 431, 'status': 'active', 'timestamp': 1648753205},
    {'sensor': 'C', 'reading': 594, 'status': 'noisy', 'timestamp': 1648753210},
    {'sensor': 'D', 'reading': 723, 'status': 'active', 'timestamp': 1648753215}
]

# System configuration and thresholds
config = {
    'threshold_low': 400,
    'threshold_high': 700,
    'calibration_factor': 1.05,
    'decay_rate': 0.85,
    'history_window': 3
}

# Irrelevant auxiliary function (decoy)
def calculate_entropy(data):
    total = sum(d['reading'] for d in data)
    probs = [d['reading'] / total for d in data]
    return -sum(p * math.log2(p) for p in probs if p > 0)

# Misleading intermediate diagnostic (unused)
current_entropy = calculate_entropy(telemetry_stream)

# Data transformation pipeline
filtered_readings = [
    entry['reading'] * config['calibration_factor']
    for entry in telemetry_stream
    if entry['status'] == 'active'
]

# Dead code path: simulation of alternate processing (never called)
simulate_failure_mode = lambda x: [val * 0.1 for val in x if val > 500]

# Historical reference data (red herring)
historical_peaks = {
    'Q1': 902, 'Q2': 887, 'Q3': 903, 'Q4': 915
}

# Extract recent timestamps
recent_timestamps = list(map(lambda x: x['timestamp'], telemetry_stream))

# Compute time-based weight coefficients (distractor computation)
time_weights = [
    math.exp((recent_timestamps[i] - recent_timestamps[-1]) * 0.000001)
    for i in range(len(recent_timestamps))
]

# Core processing functions
def normalize(values, min_val=0, max_val=1000):
    span = max_val - min_val
    return [(v - min_val) / span for v in values]

# Complex conditional expression with nested logic
event_severity = 'high' if any(r > config['threshold_high'] for r in filtered_readings) else 'normal'

# Simulated system state with multiple attributes
system_state = {
    'mode': 'diagnostic',
    'version': '2.1.5',
    'uptime': 87432,
    'load_avg': [0.78, 0.82, 0.91],
    'event_severity': event_severity
}

# Log processing with tuple unpacking and destructuring
log_data = []
for item in telemetry_stream:
    sensor_id, reading, status = item['sensor'], item['reading'], item['status']
    adjusted = reading * config['calibration_factor']
    category = 'outlier' if adjusted > config['threshold_high'] else 'baseline'
    log_data.append((sensor_id, adjusted, category, status))

# Auxiliary map-reduce style transformation (partially relevant)
reading_stats = {
    'count': len(filtered_readings),
    'total': sum(filtered_readings),
    'max': max(filtered_readings),
    'min': min(filtered_readings)
}

# Secondary metrics with decoy aggregation
auxiliary_metrics = {
    'range': reading_stats['max'] - reading_stats['min'],
    'midpoint': (reading_stats['max'] + reading_stats['min']) / 2,
    'adjusted_avg': reading_stats['total'] / reading_stats['count'] * config['decay_rate']
}

# Higher-order function with closure (distractor)
def make_validator(threshold):
    return lambda x: x > threshold

is_critical = make_validator(900)

# Real-time anomaly detection (unused result)
anomalies_detected = [r for r in filtered_readings if is_critical(r)]

# Primary metric calculation with bit manipulation red herring
composite_key = 0
for i, val in enumerate(filtered_readings):
    composite_key ^= int(val) << (i % 3)  # Bit shifting distraction

# Final processing function combining multiple concepts
def process_metrics(log_entries, state):
    
    # Extract only valid entries using conditional expression
    valid_entries = [entry for entry in log_entries if entry[3] != 'noisy']
    
    # Unpack using tuple destructuring
    ids, readings, categories, _ = zip(*valid_entries)
    
    # Calculate weighted contribution based on severity
    weights = [1.2 if cat == 'outlier' else 1.0 for cat in categories]
    weighted_sum = sum(r * w for r, w in zip(readings, weights))
    
    # Apply decay based on system mode
    multiplier = 0.9 if state['mode'] == 'diagnostic' else 1.0
    
    # Incorporate version number as minor offset (misleading but deterministic)
    version_parts = list(map(int, state['version'].split('.')))
    version_offset = version_parts[0] * 0.1 + version_parts[1] * 0.01
    
    # Final diagnostic score
    diagnostic_score = (weighted_sum * multiplier) + version_offset
    
    # Additional adjustment based on uptime (irrelevant but consistent)
    uptime_influence = (state['uptime'] % 100) * 0.001
    
    return round(diagnostic_score + uptime_influence, 4)

# Execute critical statement
final_diagnostic = process_metrics(log_data, system_state)

print(f"Target result: {final_diagnostic}")