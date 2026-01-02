from collections import defaultdict
import math

# Simulated telemetry data from a distributed sensor network
telemetry_streams = {
    'sensor_a': [12, 15, 14, 18, 22, 25, 24, 20],
    'sensor_b': [8, 10, 13, 17, 20, 23, 25, 26],
    'sensor_c': [5, 7, 9, 12, 14, 16, 18, 19]
}

# Irrelevant baseline calibration (distractor)
calibration_offsets = {'x': 0.98, 'y': 1.02, 'z': 0.99}
baseline_adjustment = sum(calibration_offsets.values()) / len(calibration_offsets)

# Simulate packet loss and recovery log (mixed relevance)
packet_log = [
    {'seq': 1, 'status': 'received', 'retry': 0},
    {'seq': 2, 'status': 'lost', 'retry': 1},
    {'seq': 3, 'status': 'received', 'retry': 0},
    {'seq': 4, 'status': 'lost', 'retry': 2},
    {'seq': 5, 'status': 'received', 'retry': 0}
]

# Dead code path: unused error simulation (red herring)
def simulate_failure_mode(mode):
    if mode == 'critical':
        return [i ** 3 for i in range(5)]
    else:
        return [i ** 2 for i in range(3)]

# Unused transformation chain (decoy)
transform_chain = lambda x: x >> 2
shifted_values = [transform_chain(v) for v in range(100, 110, 2)]

# Real processing begins here — compute rolling averages per sensor
rolling_averages = defaultdict(list)
window_size = 3

for sensor, readings in telemetry_streams.items():
    for i in range(len(readings) - window_size + 1):
        window_avg = sum(readings[i:i+window_size]) / window_size
        rolling_averages[sensor].append(round(window_avg, 2))

# Compute variance for each sensor's rolling average (intermediate diagnostic)
sensor_variances = {}
for sensor, avgs in rolling_averages.items():
    mean_avg = sum(avgs) / len(avgs)
    variance = sum((x - mean_avg) ** 2 for x in avgs) / len(avgs)
    sensor_variances[sensor] = round(variance, 3)

# System state with multiple flags (some irrelevant)
system_state = {
    'node_health': 'stable',
    'power_status': 'nominal',
    'last_sync_cycle': 42,
    'sync_interval': 5,
    'overload_threshold': 22,
    'current_load': 19
}

# Log data with mixed content (contains relevant and irrelevant entries)
log_data = [
    {'level': 'INFO', 'event': 'startup', 'ts': 0},
    {'level': 'WARN', 'event': 'temp_fluctuation', 'ts': 3},
    {'level': 'INFO', 'event': 'heartbeat', 'ts': 5},
    {'level': 'ERROR', 'event': 'buffer_overflow', 'ts': 7},
    {'level': 'INFO', 'event': 'recovery_initiated', 'ts': 8}
]

# Misleading aggregation (looks important but unused)
total_warnings = len([e for e in log_data if e['level'] == 'WARN'])
error_timestamps = [e['ts'] for e in log_data if 'ERROR' in e['level']]

# Auxiliary function to extract sync anomalies (not actually called)
def detect_sync_anomalies(logs, interval):
    timestamps = [entry['ts'] for entry in logs if entry['event'] == 'heartbeat']
    gaps = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
    return [gap for gap in gaps if gap > interval + 1]

# Core metric processor — this is where real logic happens
def analyze_variance_trend(variances):
    # Normalize variances using logarithmic scaling
    total_norm = 0.0
    for s, v in variances.items():
        if v > 0:
            total_norm += math.log(v * 10)  # Amplify small differences
    return round(total_norm, 4)

# Secondary filter based on system load condition (used later)
def is_stress_condition(state):
    threshold = state['overload_threshold']
    margin = abs(threshold - state['current_load'])
    return margin <= 3

# UNUSED: complex bit manipulation routine (distractor)
def compute_checksum(data_list):
    checksum = 0
    for val in data_list:
        checksum ^= (val << 1)
        checksum &= 0xFF
        checksum += (val >> 2)
    return checksum % 100

# Another decoy — set operation that looks meaningful
active_sensors = set(telemetry_streams.keys())
failed_sensors = set(['sensor_d'])  # Not in system
recovered_sensors = active_sensors - failed_sensors

# Main processing function combining multiple concepts
def process_metrics(log_entries, sys_state):
    # Extract event counts (only INFO used later)
    event_count = defaultdict(int)
    for entry in log_entries:
        event_count[entry['level']] += 1

    # Only 'INFO' count is used; others are distractions
    info_events = event_count['INFO']

    # Determine stress multiplier
    stress_multiplier = 2.5 if is_stress_condition(sys_state) else 1.0

    # Use the normalized variance from earlier analysis
    trend_score = analyze_variance_trend(sensor_variances)

    # Core calculation: blend trend score with log frequency under stress factor
    raw_diagnostic = (trend_score * info_events) * stress_multiplier

    # Apply artificial rounding policy (simulates reporting constraints)
    if raw_diagnostic.is_integer():
        final = int(raw_diagnostic)
    else:
        final = round(raw_diagnostic, 3)

    # Inject dependency on last sync cycle (irrelevant but plausible)
    cycle_mod = sys_state['last_sync_cycle'] % 7
    final += cycle_mod * 0.1  # Tiny adjustment, looks intentional

    return round(final, 3)

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_state)

# Print result as required
print(f"Target result: {final_diagnostic}")