from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (distractor: not all fields are used)
sensor_readings = [
    {'node': 'A', 'temp': 23.5, 'status': 'active', 'priority': 1},
    {'node': 'B', 'temp': 25.1, 'status': 'idle',   'priority': 3},
    {'node': 'C', 'temp': 26.8, 'status': 'active', 'priority': 2},
    {'node': 'A', 'temp': 24.0, 'status': 'active', 'priority': 1},
    {'node': 'D', 'temp': 22.7, 'status': 'active', 'priority': 3},
    {'node': 'B', 'temp': 25.3, 'status': 'active', 'priority': 3}
]

# Irrelevant preprocessing: node status mapping (dead code path)
status_map = defaultdict(lambda: 'unknown')
for s in ['active', 'idle', 'standby', 'error']:
    status_map[s] = s + '_processed'

# Distractor function: unused but plausible
def analyze_health_legacy(logs):
    score = 0
    for entry in logs:
        if entry['temp'] > 25:
            score += entry['priority'] * 2
    return score * 0.1  # legacy weighting

# Real processing begins here
aggregated = defaultdict(list)
for reading in sensor_readings:
    aggregated[reading['node']].append(reading['temp'])

# Compute average temps per node
avg_temps = {k: sum(v)/len(v) for k, v in aggregated.items()}

# System state with irrelevant and relevant fields
system_state = {
    'nodes': ['A', 'B', 'C', 'D'],
    'threshold_critical': 26.0,
    'threshold_warning': 24.5,
    'last_reset_cycle': 142,
    'uptime_minutes': 8793,
    'config_flag': 0b1010,
    'debug_mode': False
}

# Data log with multiple red herrings
raw_events = [
    "ERR:101", "WARN:003", "INFO:221", "ERR:101", "WARN:005",
    "INFO:221", "INFO:221", "WARN:003"
]
event_counter = Counter(raw_events)

classification_scores = {}
for event, count in event_counter.items():
    code = event.split(':')[0]
    num = int(event.split(':')[1])
    if code == 'ERR':
        classification_scores[event] = count * 3.1
    elif code == 'WARN':
        classification_scores[event] = count * 1.7
    else:
        classification_scores[event] = count * 0.5  # info noise

# Misleading total score (not used in final result)
total_alert_score = sum(classification_scores.values()) * 0.9

# Critical diagnostic logic chain
flags_raised = 0
high_temp_nodes = 0

for node, avg_temp in avg_temps.items():
    if avg_temp > system_state['threshold_critical']:
        flags_raised += 2
        high_temp_nodes += 1
    elif avg_temp > system_state['threshold_warning']:
        flags_raised += 1

# Bit manipulation decoy (unused)
config_analysis = system_state['config_flag'] ^ 0b1111 & 0b0110

# Core data structure transformation
shift_register = [0] * 4
for i in range(len(sensor_readings)):
    shift_register[i % 4] ^= int(sensor_readings[i]['temp'])

# Unused checksum distraction
data_checksum = sum(shift_register) % 17

# Actual metric computation
stability_index = len(avg_temps) / (flags_raised + 1)
sensitivity_factor = math.log(1 + high_temp_nodes) * 10

# Simulated calibration offset (case conversion as red herring)
mode_str = system_state['debug_mode']
if mode_str:
    calib_offset = len('calibration'.upper())
else:
    calib_offset = len('calibration'.lower())  # always 11

# Primary data log for real processing
data_log = {
    'entries_count': len(sensor_readings),
    'unique_nodes': len(avg_temps),
    'critical_flags': flags_raised,
    'base_index': stability_index
}

# Main processing function with nested logic
def process_metrics(log_data, state):
    base = log_data['base_index']
    nodes = log_data['unique_nodes']
    flags = log_data['critical_flags']
    
    # Multi-step derived values
    modifier = 1.0
    if flags > 0:
        modifier += 0.5
    if nodes >= 4:
        modifier *= 1.2
    
    # Modular arithmetic with thresholding
    cycle_phase = state['last_reset_cycle'] % 8
    if cycle_phase in [2, 5, 7]:
        modifier *= 0.9
    elif cycle_phase in [0, 1, 3]:
        modifier *= 1.1
    else:
        modifier *= 1.05
    
    # Complex interaction
    intermediate = (base * modifier) + (nodes * 0.75)
    
    # Final adjustment using bit property (only uses debug_mode)
    if state['debug_mode']:
        adjustment = 5
    else:
        adjustment = -3
    
    result = intermediate + adjustment + calib_offset
    return int(result * 100) / 100  # round to 2 decimal places

# Execute key statement
final_diagnostic = process_metrics(data_log, system_state)

print(f"Target result: {final_diagnostic}")