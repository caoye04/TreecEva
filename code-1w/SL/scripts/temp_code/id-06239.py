import math

# Sensor calibration constants (irrelevant to final result)
CALIBRATION_FACTOR_A = 0.987
CALIBRATION_OFFSET_B = -0.013
REFERENCE_VOLTAGE = 3.3

# System state tracking (distractor variables)
current_mode = 'diagnostic'
activation_log = []
system_uptime = 12745
fault_history = [None, None, None]

# Input sensor data stream (simulated)
raw_readings = [
    'sensor1:1.2,voltage:3.1,temp:22.5,status:OK',
    'sensor2:0.9,voltage:3.0,temp:23.1,status:OK',
    'sensor3:1.5,voltage:3.2,temp:21.8,status:OK',
    'sensor4:2.1,voltage:2.8,temp:24.3,status:WARNING',
    'sensor5:0.7,voltage:3.1,temp:22.0,status:OK',
    'sensor6:1.8,voltage:2.9,temp:25.6,status:WARNING'
]

# Auxiliary mapping tables (some irrelevant entries)
threshold_map = {
    'low_power': 1.0,
    'high_sensitivity': 1.6,
    'baseline': 1.2,
    'calibration_pad': 0.05,
    'noise_floor': 0.3
}

status_priority = {'OK': 1, 'WARNING': 2, 'CRITICAL': 3}

# Decoy function - appears useful but unused in critical path
def validate_checksum(entry):
    return entry.count(',') == 3 and 'voltage' in entry

# Real processing function with distractions
def parse_entry(entry_str):
    if 'status:CRITICAL' in entry_str:
        return None  # Discard critical entries
    
    # Extract key-value pairs
    parts = entry_str.split(',')
    data = {}
    for part in parts:
        key, value = part.split(':')
        if value.replace('.', '').isdigit():
            data[key] = float(value) if '.' in value else int(value)
        else:
            data[key] = value
    
    # Distractor computation: voltage normalization (unused)
    if 'voltage' in data:
        normalized_v = (data['voltage'] - 2.5) * CALIBRATION_FACTOR_A
        data['norm_v'] = round(normalized_v, 3)
    
    return data

# Another decoy: system health monitor (never called)
def update_health_status(mode, timestamp=None):
    nonlocal system_uptime
    system_uptime += 60
    activation_log.append(f'{mode}_at_{timestamp or "unknown"}')
    return len(activation_log)

# Filter and transform readings
parsed_data = [parse_entry(entry) for entry in raw_readings if parse_entry(entry) is not None]

# Apply status filter (distractor: collects but doesn't use priority)
prioritized_entries = sorted(
    [d for d in parsed_data if d.get('status') != 'CRITICAL'],
    key=lambda x: status_priority.get(x.get('status'), 0)
)

# Extract sensor values using list comprehension with distraction
sensor_ids = [k for k in parsed_data[0].keys() if 'sensor' in k]
all_sensor_values = [d[sensor_ids[0]] for d in parsed_data if sensor_ids[0] in d]

# Real filtering logic buried in noise
filtered_data = []
for record in prioritized_entries:
    if 'temp' in record and record['temp'] > 23.0:
        continue  # Skip high temp readings
    if '1' in record.get(sensor_ids[0], ''):
        continue  # Artificial exclusion based on ID
    filtered_data.append(record)

# Decoy statistical analysis
mean_voltage = sum(d['voltage'] for d in parsed_data) / len(parsed_data) if parsed_data else 0
voltage_variance = sum((d['voltage'] - mean_voltage) ** 2 for d in parsed_data) / len(parsed_data) if parsed_data else 0

# Core diagnostic processing (the actual answer generator)
def process_readings(readings, thresholds):
    if not readings:
        return -999.0
    
    base_score = 0.0
    adjustment = thresholds['baseline']
    
    for reading in readings:
        value_key = [k for k in reading.keys() if k not in ['voltage', 'temp', 'status', 'norm_v'] and ':' not in k][0]
        raw_val = reading[value_key]
        
        # Actual computation logic
        if raw_val < thresholds['low_power']:
            base_score += 100 * raw_val
        elif raw_val > thresholds['high_sensitivity']:
            base_score += 150 * math.log(raw_val)
        else:
            base_score += 120 * raw_val
    
    # Final transformation
    final_score = base_score * (adjustment + 0.8) / (thresholds['noise_floor'] + 0.7)
    return round(final_score, 4)

# Execute main logic
final_diagnostic = process_readings(filtered_data, threshold_map)

# Irrelevant output formatting
result_str = f"Diagnostic Result: {final_diagnostic:.4f}"
result_str = result_str.upper().replace("RESULT", "OUTCOME")

# Critical output line - do not modify format
print(f"Target result: {final_diagnostic}")