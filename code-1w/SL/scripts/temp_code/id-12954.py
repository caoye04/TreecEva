from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'sensor': 'temp', 'value': 45, 'status': 'ok', 'timestamp': 1001},
    {'sensor': 'pressure', 'value': 23, 'status': 'ok', 'timestamp': 1002},
    {'sensor': 'temp', 'value': 67, 'status': 'overheat', 'timestamp': 1003},
    {'sensor': 'flow', 'value': 15, 'status': 'ok', 'timestamp': 1004},
    {'sensor': 'temp', 'value': 34, 'status': 'ok', 'timestamp': 1005}
]

# Irrelevant historical stats (distractor)
historical_stats = {
    'avg_temp': 42.3,
    'peak_usage': 91,
    'maintenance_count': 3
}

# Misleading auxiliary function (dead path)
def analyze_efficiency(data):
    efficiency_score = 0
    for entry in data:
        if entry['sensor'] == 'flow':
            efficiency_score += entry['value'] * 1.5
    return efficiency_score  # Never used

# Decoy transformation (unused)
transformed = [x['value'] ** 0.5 for x in telemetry_stream if x['sensor'] == 'pressure']

# Real processing begins here
def extract_readings(logs, sensor_type):
    return [entry['value'] for entry in logs if entry['sensor'] == sensor_type]

# Bit manipulation simulation for hardware compatibility check (partially relevant)
def hardware_compatibility(code):
    shifted = (code << 3) & 0xFF
    toggled = shifted ^ 0b10101010
    return (toggled % 17) + 1

# System state with red herrings and actual signals
system_state = {
    'uptime': 12450,
    'mode': 'diagnostic',
    'version': '2.1.8',
    'flags': 0b1101,  # Use bits: 0=debug, 1=locked, 2=remote, 3=active
    'thresholds': {
        'temp_warn': 50,
        'pressure_min': 20
    }
}

# Log aggregation with distraction via unused counters
counters = defaultdict(int)
for log in telemetry_stream:
    counters[log['sensor']] += 1
    counters[f'{log["status"]}_total'] += 1  # Distractor counts

# Unused frequency analysis
status_freq = Counter([log['status'] for log in telemetry_stream])

# Core logic: detect anomalies in temperature readings
raw_temps = extract_readings(telemetry_stream, 'temp')
anomalies = 0
for temp in raw_temps:
    if temp > system_state['thresholds']['temp_warn']:
        anomalies += 1

# Conditional bit flag evaluation (relevant)
is_debug = system_state['flags'] & 0b0001
is_active = system_state['flags'] & 0b1000
activation_key = hardware_compatibility(system_state['flags']) if is_active else 7

# Fake error correction (irrelevant)
error_buffer = []
for i in range(3):
    error_buffer.append((anomalies * i) % 5)

# Actual metric computation chain
base_score = sum(raw_temps) // len(raw_temps)  # Integer average
adjusted_score = base_score + (activation_key if is_active else 0)
penalty = anomalies * 4
interim_result = adjusted_score - penalty

# Second decoy loop (no impact)
for _ in range(2):
    interim_result = int(math.sqrt(interim_result * 2))

# Final processing with list comprehension and meaningful logic
def process_metrics(log_data, state):
    temp_values = [x['value'] for x in log_data if x['sensor'] == 'temp' and x['status'] != 'ok']
    severity = sum(1 for t in temp_values if t > 60)
    
    # Complex conditional with short-circuiting
    if state['mode'] == 'diagnostic' and (state['flags'] & 0b1000) and not is_debug:
        multiplier = 3
    else:
        multiplier = 1
    
    # Final diagnostic calculation
    transient = (interim_result + severity * 10) * multiplier
    
    # Additional irrelevant transformation inside function
    debug_dump = {f'log_{i}': math.log(v['value'] + 1) for i, v in enumerate(log_data)}
    
    # Actual answer derivation
    final_value = transient ^ 0b1111  # Final XOR adjustment
    return final_value

# Execution point of interest
final_diagnostic = process_metrics(telemetry_stream, system_state)

# Output result as required
print(f"Target result: {final_diagnostic}")