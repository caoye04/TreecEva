def analyze_system_load(load_series, threshold=75):
    peak = max(load_series)
    avg = sum(load_series) / len(load_series)
    above_threshold = [x for x in load_series if x > threshold]
    utilization_rate = len(above_threshold) / len(load_series)
    warning_flag = False
    if avg > 60 and utilization_rate > 0.4:
        warning_flag = True
    # Irrelevant transformation
    inverted = [100 - x for x in load_series]
    normalized = [x / 100 for x in load_series]
    return warning_flag, utilization_rate


def extract_diagnostic_codes(event_stream):
    codes = []
    for event in event_stream:
        if 'ERR' in event:
            codes.append(event.split('-')[1])
    severity_map = {'A': 3, 'B': 2, 'C': 1}
    total_severity = 0
    for code in codes:
        if code[0] in severity_map:
            total_severity += severity_map[code[0]]
    return total_severity

# Dead function - never called
def deprecated_calib_value(x):
    return (x * 0.95 + 4) ** 0.5

# Misleading initialization
baseline_config = {
    'version': '2.1',
    'active': True,
    'thresholds': {
        'cpu': 80,
        'memory': 70,
        'io': 60
    },
    'weights': [0.4, 0.3, 0.3],
    'debug_mode': False
}

metrics_log = [
    {'timestamp': '2023-05-01T10:00', 'cpu': 85, 'memory': 68, 'io': 55, 'status': 'OK'},
    {'timestamp': '2023-05-01T10:01', 'cpu': 92, 'memory': 72, 'io': 58, 'status': 'WARN'},
    {'timestamp': '2023-05-01T10:02', 'cpu': 67, 'memory': 75, 'io': 62, 'status': 'OK'},
    {'timestamp': '2023-05-01T10:03', 'cpu': 73, 'memory': 65, 'io': 59, 'status': 'OK'},
    {'timestamp': '2023-05-01T10:04', 'cpu': 88, 'memory': 78, 'io': 68, 'status': 'WARN'}
]

# Distractor list
maintenance_tasks = ['reindex', 'backup', 'cleanup', 'audit']
task_status = {task: 'completed' for task in maintenance_tasks}

# Auxiliary data
event_logs = [
    'EVNT-A12', 'ERR-B23', 'EVNT-C14', 'ERR-A19', 'DEBUG-X7', 'ERR-C31'
]

# Unused transformation
log_strings = [f"[{entry['timestamp']}] {entry['status']}" for entry in metrics_log]
slice_window = log_strings[1:4:1]

# Real processing begins
system_loads = [m['cpu'] for m in metrics_log]
flag, util_rate = analyze_system_load(system_loads, 70)

diag_severity = extract_diagnostic_codes(event_logs)

config_weights = baseline_config['weights']

# Simulate score components
cpu_component = sum(m['cpu'] for m in metrics_log) / len(metrics_log)
mem_violations = sum(1 for m in metrics_log if m['memory'] > baseline_config['thresholds']['memory'])
io_trend = metrics_log[-1]['io'] - metrics_log[0]['io']

# Dummy variables
placeholder_result = (cpu_component * 0.8) % 10
interim_key = ''.join([chr(97 + int(cpu_component) % 26), 'X', 'Y'])

# Core logic disguised among distractors
penalty_points = 0
if flag:
    penalty_points += 3
if mem_violations > 1:
    penalty_points += 2
if diag_severity >= 3:
    penalty_points += 4

base_score = 100
adjustment_factor = (util_rate * 10) ** 0.5

# Final calculation with string-based switch
mode_flag = 'high' if cpu_component > 80 else 'normal'

scaling_map = {'normal': 1.0, 'high': 0.85}

scaled_base = base_score * scaling_map[mode_flag]

# Critical statement
final_score = int(scaled_base - (penalty_points * adjustment_factor))

# Print required output
print(f"Result: {final_score}")