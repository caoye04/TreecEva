def parse_system_events(raw_data):
    events = raw_data.split(',')
    parsed = []
    for event in events:
        code, timestamp, severity = event.strip().split('|')
        parsed.append({'code': code, 'time': int(timestamp), 'level': int(severity)})
    return parsed

# Irrelevant sensor calibration data (distractor)
sensor_offsets = [0.12, -0.05, 0.33, 0.0, 0.18]
calibration_matrix = [[1, 0], [0, 1]]
active_sensors = {1, 3, 4, 7}

# System fault dictionary with real and decoy codes
fault_library = {
    'E101': 'Memory overflow',
    'E205': 'Bus timeout',
    'W302': 'Thermal drift',
    'I401': 'Idle cycle',  # Not an error
    'E506': 'Register corruption',
    'E607': 'Clock desync'
}

# Simulated raw input (mixture of relevant and irrelevant entries)
raw_input = "E101|1678000000|3|, W302|1678000120|2|, I401|1678000150|1|, E205|1678000300|4|, X999|1678000400|0|"

event_log = parse_system_events(raw_input)

# Extract only error-level events (severity >= 3) and known fault codes
filtered_events = [e for e in event_log if e['level'] >= 3 and e['code'] in fault_library]

# Decoy statistical analysis on timestamps (red herring)
timestamps = [e['time'] for e in event_log]
avg_time = sum(timestamps) / len(timestamps)
time_variance = sum((t - avg_time)**2 for t in timestamps) / len(timestamps)

# Real processing: collect unique error codes that are critical
recent_errors = {e['code'] for e in filtered_events if e['code'].startswith('E')}

# Legacy compatibility mapping (unused path - dead code)
legacy_mapping = {'E101': 'MEM_ERR', 'E205': 'BUS_ERR'}
translated = [legacy_mapping.get(code, 'UNKNOWN') for code in recent_errors]

# Auxiliary diagnostic chain (partially relevant)
def compute_stability_index(errors, base=100):
    penalty = 0
    for err in errors:
        if err == 'E101':
            penalty += 15
        elif err == 'E205':
            penalty += 25
        elif err == 'E506':
            penalty += 40  # Not present
    return base - penalty

stability_score = compute_stability_index(recent_errors)

# Core analysis function with set operations and logic
redundant_codes = {'E101', 'E205', 'E506', 'E607'}
known_warnings = {'W302', 'W405'}

system_health_flags = set()
if stability_score < 80:
    system_health_flags.add('CRITICAL')
if len(recent_errors) >= 3:
    system_health_flags.add('OVERLOADED')

# Determine relevance using set difference (key step)
relevant_codes = redundant_codes.intersection(recent_errors)

# Simulated log with decoy entries
system_log = {
    'entries': 127,
    'warnings_ignored': 3,
    'last_reset': '2023-01-01',
    'debug_mode': False
}

# Critical computation path
intermediate_weight = len(relevant_codes) * 17

# Misleading floating point accumulation (distraction)
accumulated_drift = 0.0
for i in range(5):
    accumulated_drift += 0.1  # Floating point quirk not used later

# Final analysis using multiple concepts
def analyze_fault_codes(codes, log_context):
    base_value = 1000
    modifier = 0
    
    if 'E101' in codes:
        modifier += 50
    if 'E205' in codes:
        modifier += 70
    
    # Use of min/max/average pattern (partially relevant)
    all_penalties = [modifier]
    if log_context['debug_mode']:
        all_penalties.append(-20)
    
    total_penalty = sum(all_penalties)
    result = base_value - total_penalty
    
    # Final adjustment based on set size
    if len(codes) == 1:
        result -= 10
    elif len(codes) == 2:
        result += 5
    
    return result

# Key execution point
final_diagnostic = analyze_fault_codes(relevant_codes, system_log)

print(f"Result: {final_diagnostic}")