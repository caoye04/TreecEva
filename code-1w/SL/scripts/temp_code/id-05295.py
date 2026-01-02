def analyze_component_health(reading, baseline):
    return (reading / baseline) > 1.1

# System telemetry data
telemetry_logs = [
    {'time': 0, 'voltage': 3.3, 'current': 0.45, 'temp': 42},
    {'time': 1, 'voltage': 3.28, 'current': 0.47, 'temp': 43},
    {'time': 2, 'voltage': 3.31, 'current': 0.51, 'temp': 46},
    {'time': 3, 'voltage': 3.29, 'current': 0.53, 'temp': 49},
    {'time': 4, 'voltage': 3.32, 'current': 0.61, 'temp': 53}
]

# Irrelevant helper function (decoy)
def calculate_power_factor(v, i):
    return v * i * 0.8

# Unused transformation (dead code path)
transformed = [dict(d, efficiency=(d['voltage'] * d['current']) for d in telemetry_logs)]

# Extract voltage readings over time
voltage_series = [entry['voltage'] for entry in telemetry_logs]

# Calculate rolling average (distraction)
def rolling_avg(data, window=2):
    return [sum(data[i:i+window]) / window for i in range(len(data)-window+1)]
r_avg = rolling_avg(voltage_series)

# Simulate sensor calibration offset (irrelevant)
calibration_shift = sum([0.01 * i for i in range(len(telemetry_logs))])
adjusted_voltage = [v + 0.01*i for i, v in enumerate(voltage_series)]

# Core diagnostic logic masked by noise
baseline_current = 0.50
abnormal_count = 0
for log in telemetry_logs:
    if log['current'] > baseline_current:
        if analyze_component_health(log['temp'], 45):
            abnormal_count += 1

# Secondary metric: volatility detection (partial distractor)
voltages = [log['voltage'] for log in telemetry_logs]
volatility = max(voltages) - min(voltages)
stable_system = volatility < 0.05

# Character counting red herring
system_id = 'SYS-CTRL-V2'
checksum = sum(ord(c) for c in system_id) % 100  # unused

# Data structure manipulation with slicing distraction
diag_buffer = ['OK', 'OK', 'WARN', 'ALERT', 'CRITICAL']
recent_states = diag_buffer[-3:]  # slicing operation used

# Dictionary-based rule engine (key concept)
diagnostic_rules = {
    0: 100,
    1: 85,
    2: 60,
    3: 40,
    4: 20,
    5: 10
}

# Conditional expression with default fallback (python idiom)
def process_metrics(logs, threshold):
    high_load_periods = len([l for l in logs if l['current'] >= threshold])
    stress_factor = high_load_periods if high_load_periods <= 3 else 3
    base_score = diagnostic_rules.get(abnormal_count, 0)
    # Final adjustment using conditional expression
    penalty = 10 if not stable_system else 0
    adjusted_score = base_score - penalty
    # Additional noise
    debug_trace = f'Stress: {stress_factor}, Penalty: {penalty}'
    return adjusted_score

# Misleading intermediate calculation
projected_failure = (abnormal_count * 17) + (int(not stable_system) * 25)

# Key execution point
system_threshold = 0.50
final_diagnostic = process_metrics(telemetry_logs, system_threshold)

# Print result as required
print(f"Target result: {final_diagnostic}")