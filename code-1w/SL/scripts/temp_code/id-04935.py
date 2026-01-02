from collections import defaultdict, Counter
import itertools

# Simulated telemetry data from satellite subsystems
telemetry = [
    {'temp': 78, 'voltage': 12.4, 'status': 'active', 'checksum': 0x1A},
    {'temp': 85, 'voltage': 11.9, 'status': 'active', 'checksum': 0x2C},
    {'temp': 95, 'voltage': 11.2, 'status': 'degraded', 'checksum': 0x3F},
    {'temp': 105, 'voltage': 10.1, 'status': 'critical', 'checksum': 0x55},
    {'temp': 65, 'voltage': 13.0, 'status': 'active', 'checksum': 0x10}
]

# System thresholds for diagnostics
thresholds = {
    'overheat': 90,
    'low_voltage': 11.5,
    'critical_temp': 100
}

# Irrelevant mapping table for decoy logic
status_codes = defaultdict(lambda: 'unknown')
for i, code in enumerate(['OK', 'WARN', 'ERR', 'CRIT']):
    status_codes[i] = code

# Decoy transformation (never used)
def transform_readings(data):
    return [d['voltage'] * 100 for d in data if d['temp'] > 80]

# Misleading accumulator (looks important but unused in final result)
shadow_accumulator = 0
for entry in telemetry:
    shadow_accumulator += entry['temp'] ^ int(entry['voltage'])

# Auxiliary function with red herring parameters
def compute_stability_index(logs, weight_factor=1.3, debug_mode=False):
    indices = []
    for i, log in enumerate(logs):
        if log['status'] == 'critical':
            # This branch modifies a variable that gets discarded
            temp_spike = (log['temp'] - 80) * weight_factor
            indices.append(100)
        elif log['voltage'] < 11.0:
            indices.append(75)
        else:
            indices.append(90 - (log['temp'] - 70))
    return sum(indices) / len(indices) if indices else 0

# Unused but plausible-looking diagnostic matrix
status_matrix = list(itertools.product(['sensor', 'power', 'comms'], ['nominal', 'alert', 'fail']))

# Real processing begins here
working_set = [entry for entry in telemetry if entry['status'] != 'critical']

# Compute baseline trends using enumerate and zip
baseline_temps = [entry['temp'] for entry in working_set]
baseline_voltages = [entry['voltage'] for entry in working_set]
indexed_pairs = list(enumerate(zip(baseline_temps, baseline_voltages)))

# Calculate drift score (relevant to final result)
drift_score = 0
for i, (t, v) in indexed_pairs:
    if t > thresholds['overheat'] and v < thresholds['low_voltage']:
        drift_score += 3
    elif t > thresholds['overheat'] or v < thresholds['low_voltage']:
        drift_score += 1

# Hidden logic: count degraded entries that are excluded from working_set
degraded_count = len([e for e in telemetry if e['status'] == 'degraded'])

# Core diagnostic algorithm
def analyze_system_state(data, limits):
    critical_count = 0
    voltage_alerts = 0
    temp_sum = 0
    sample_count = 0

    # Primary evaluation loop
    for reading in data:
        temp_sum += reading['temp']
        sample_count += 1

        if reading['temp'] > limits['critical_temp']:
            critical_count += 1

        if reading['voltage'] < limits['low_voltage']:
            voltage_alerts += 1

        # Early termination red herring - never triggered due to data
        if reading['checksum'] == 0xFF:
            return -999  # Impossible condition (distraction)

    # Compute averages (some used, some not)
    avg_temp = temp_sum / sample_count
    avg_voltage = sum(r['voltage'] for r in data) / len(data)

    # Intermediate metric with partial relevance
    base_diagnostic = avg_temp - avg_voltage * 5

    # Key logic: only this line contributes to final answer
    # The drift_score and degraded_count were distractions
    final_component = (critical_count * 1000) + int(base_diagnostic)

    # Dead code path - unreachable due to logic
    if len(data) > 100:
        fallback = 0
        for _ in range(10):
            fallback ^= hash(str(_))
        return fallback

    return final_component

# Execute main analysis
stability = compute_stability_index(telemetry)  # Computed but not used
final_diagnostic = analyze_system_state(telemetry, thresholds)
print(f"Result: {final_diagnostic}")