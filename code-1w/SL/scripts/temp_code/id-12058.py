import math

# Simulated system telemetry data
current_voltage = 230.5
phase_angle = 45
frequency_drift = 0.07
baseline_threshold = 220

# Health metric components
voltage_ratio = current_voltage / baseline_threshold
power_factor = math.cos(math.radians(phase_angle))
adjusted_drift = frequency_drift * 100

# System status flags
device_status_codes = {1: 'active', 2: 'standby', 3: 'maintenance', 4: 'fault'}
active_devices = [1, 2, 1, 4, 2, 1]
status_count = {}
for code in active_devices:
    status_count[code] = status_count.get(code, 0) + 1

# Flag anomalies
anomaly_flags = set()
if status_count.get(4, 0) > 0:
    anomaly_flags.add('FAULT_DEVICE')
if voltage_ratio > 1.05:
    anomaly_flags.add('OVER_VOLTAGE')
if voltage_ratio < 0.95:
    anomaly_flags.add('UNDER_VOLTAGE')
if adjusted_drift > 5:
    anomaly_flags.add('FREQUENCY_INSTABILITY')

# Irrelevant signal processing (distractor)
def process_signal(noise_floor, samples):
    result = 0
    for i in range(samples):
        result += math.sin(i * noise_floor)
    return result  # Unused return

signal_trace = process_signal(0.03, 500)  # Dead computation

# Data normalization (partially relevant)
metrics = [voltage_ratio, power_factor, adjusted_drift]
normalized = [(x - min(metrics)) / (max(metrics) - min(metrics) + 1e-8) for x in metrics]

# Construct health vector
health_metrics = {
    'vitality': normalized[0],
    'efficiency': normalized[1],
    'stability': normalized[2]
}

# System-level diagnostic flags
system_flags = set()
system_flags.add('POWER_PHASE_OK')
if phase_angle > 60:
    system_flags.add('HIGH_PHASE_WARNING')
if frequency_drift > 0.05:
    system_flags.add('DRIFT_ALERT')

# Decoy analysis function (never called)
def legacy_diagnostic(data):
    score = 0
    for k, v in data.items():
        score += hash(k) % 10 * v
    return score * 0.7

# Unused combinatorics (red herring)
def count_subsequences(arr):
    n = len(arr)
    return (2 ** n) - n - 1

combo_count = count_subsequences(active_devices)  # Computed but unused

# Core diagnostic logic
threshold_map = {
    'vitality': 0.7,
    'efficiency': 0.65,
    'stability': 0.8
}

def evaluate_metric(value, threshold):
    return 1 if value >= threshold else 0

def analyze_system_state(metrics, flags):
    # Bitmask-style evaluation
    diagnostic_code = 0
    
    # Evaluate each metric against threshold
    for key, val in metrics.items():
        if evaluate_metric(val, threshold_map[key]):
            diagnostic_code |= (1 << list(threshold_map.keys()).index(key))
    
    # Additional weighting based on flags
    if 'DRIFT_ALERT' in flags:
        diagnostic_code += 10
    if 'FAULT_DEVICE' in anomaly_flags:  # Cross-reference from outer scope
        diagnostic_code *= 2
    
    # Secondary adjustment using set operations
    critical_issues = anomaly_flags & {'OVER_VOLTAGE', 'FREQUENCY_INSTABILITY', 'FAULT_DEVICE'}
    if len(critical_issues) >= 2:
        diagnostic_code = int(diagnostic_code * 1.5)
    
    # Final adjustment based on modular condition
    if diagnostic_code % 7 == 0:
        diagnostic_code -= 5
    
    return diagnostic_code

# Execution point of interest
final_diagnostic = analyze_system_state(health_metrics, system_flags)

# Output result
print(f"Result: {final_diagnostic}")