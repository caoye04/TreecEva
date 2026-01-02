import math

# Simulated system telemetry data with mixed relevance
telemetry_stream = [
    {'id': 101, 'load': 0.85, 'temp': 70, 'errors': 2, 'timestamp': 1623456780},
    {'id': 102, 'load': 0.91, 'temp': 75, 'errors': 1, 'timestamp': 1623456785},
    {'id': 103, 'load': 0.88, 'temp': 72, 'errors': 3, 'timestamp': 1623456790},
    {'id': 104, 'load': 0.93, 'temp': 77, 'errors': 5, 'timestamp': 1623456795},
    {'id': 105, 'load': 0.87, 'temp': 71, 'errors': 2, 'timestamp': 1623456800}
]

# Irrelevant baseline reference (distractor)
baseline_performance = {
    'avg_load': 0.75,
    'max_temp': 65,
    'tolerance_window': 0.1,
    'calibration_factor': 1.05
}

# System thresholds for health check (relevant)
system_thresholds = {
    'critical_load': 0.90,
    'overheat_temp': 74,
    'error_burst': 4
}

# Red herring: unused transformation matrix (dead code path)
transformation_matrix = [[1.1, -0.1], [-0.05, 1.15]]
def apply_calibration(data, matrix):
    # This function is defined but never used
    return [matrix[0][0] * data['load'] + matrix[0][1] * data['temp']]

# Auxiliary diagnostic tool (partially relevant, partially misleading)
def compute_health_score(entry):
    score = 100
    if entry['load'] > 0.8:
        score -= 10
    if entry['temp'] > 70:
        score -= 5 * math.log(entry['temp'] - 69)
    if entry['errors'] > 0:
        score -= 3 * entry['errors'] ** 0.5
    return round(score, 2)

# Decoy aggregation function with unused logic
def aggregate_diagnostics(entries):
    cumulative = 0
    for e in entries:
        # This entire function is a red herring
        cumulative += compute_health_score(e) * 0.9
    return cumulative / len(entries) if entries else 0

# Real processing begins here — core logic buried under distractions
def parse_timestamp(t):
    return t - 1623456780  # seconds since base

def classify_event(entry):
    load_high = entry['load'] > system_thresholds['critical_load']
    temp_high = entry['temp'] > system_thresholds['overheat_temp']
    error_spike = entry['errors'] >= system_thresholds['error_burst']
    return load_high and (temp_high or error_spike)

# Main processing pipeline
log_entries = []
for raw in telemetry_stream:
    parsed_entry = {
        'time_offset': parse_timestamp(raw['timestamp']),
        'risk_flag': classify_event(raw),
        'raw_id': raw['id'],
        'metrics_snapshot': {
            'utilization': raw['load'],
            'thermal': raw['temp'],
            'fault_count': raw['errors']
        }
    }
    log_entries.append(parsed_entry)

# Secondary filter: detect sustained risk episodes
risk_sequence = []
current_streak = 0
for entry in log_entries:
    if entry['risk_flag']:
        current_streak += 1
    else:
        if current_streak > 0:
            risk_sequence.append(current_streak)
        current_streak = 0
if current_streak > 0:
    risk_sequence.append(current_streak)

# Compute burst severity using modular arithmetic on streak lengths
streak_code = 0
if risk_sequence:
    total_risk_periods = sum(1 for s in risk_sequence if s >= 2)
    max_risk_duration = max(risk_sequence)
    streak_code = (total_risk_periods * 17) % 13 + (max_risk_duration ** 2) % 11

# Real answer derivation hidden among distractors
status_map = {'stable': 0, 'caution': 1, 'warning': 2, 'critical': 3}

# Lambda-based dynamic classification (required python feature)
event_severity = lambda flag, code: status_map['warning'] if flag else status_map['caution']

# Conditional expression usage (required python feature)
initial_diagnostic = 10 if len(log_entries) == 5 else 0

# Dictionary-based state transformation
severity_lookup = {
    0: lambda x: x + 1,
    1: lambda x: x + 5,
    2: lambda x: x * 2 + 3,
    3: lambda x: int(math.sqrt(x)) + 10
}

# Final computation chain
intermediate_state = initial_diagnostic
for entry in log_entries:
    if entry['risk_flag']:
        intermediate_state = severity_lookup[event_severity(entry['risk_flag'], streak_code)](intermediate_state)

# Introduce more noise: irrelevant counters
idle_cycles = 0
phantom_mask = 0b101010
for i in range(len(telemetry_stream)):
    idle_cycles += (phantom_mask >> (i % 6)) & 1

# Final diagnostic computed from complex reasoning path
final_diagnostic = intermediate_state + streak_code - idle_cycles

# Output the target result as required
print(f"Target result: {final_diagnostic}")