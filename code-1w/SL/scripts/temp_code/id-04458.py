import math

# Simulated telemetry data from satellite subsystems
telemetry_packets = [
    {'id': 101, 'temp': 48.2, 'voltage': 3.31, 'status': 'ACTIVE'},
    {'id': 102, 'temp': -23.5, 'voltage': 3.29, 'status': 'STANDBY'},
    {'id': 103, 'temp': 77.8, 'voltage': 3.33, 'status': 'ACTIVE'},
    {'id': 104, 'temp': 0.0, 'voltage': 3.20, 'status': 'ERROR'},
    {'id': 105, 'temp': 55.1, 'voltage': 3.35, 'status': 'ACTIVE'}
]

# Irrelevant signal processing functions (distractor)
def apply_fourier_transform(data):
    return [math.sin(x / 10) for x in range(len(data))]

def analyze_spectral_power(signal):
    return sum(x**2 for x in signal) / len(signal)

# Unused diagnostic thresholds (red herring)
threshold_map = {
    'temp_critical': 85.0,
    'temp_warning': 70.0,
    'voltage_high': 3.45,
    'voltage_low': 3.15
}

# Fake anomaly detection with dead logic path
def detect_anomaly(packet):
    if packet['temp'] > 100:
        return True
    elif packet['voltage'] < 2.0:
        return True
    else:
        return False  # Never triggers in actual data

# Unused list of historical faults (irrelevant data)
historical_faults = [
    {'timestamp': '2023-01-05', 'code': 'E101', 'resolved': True},
    {'timestamp': '2023-02-17', 'code': 'E205', 'resolved': False}
]

# Simulated log entries with mixed types (relevant and irrelevant)
log_entries = [
    {'level': 'INFO', 'msg': 'System boot', 'code': 0},
    {'level': 'WARN', 'msg': 'Minor sync drift', 'code': 102},
    {'level': 'ERROR', 'msg': 'Checksum fail', 'code': 201},
    {'level': 'DEBUG', 'msg': 'Cache cleared', 'code': 999},
    {'level': 'INFO', 'msg': 'Handshake complete', 'code': 0}
]

# System flags with bitfield encoding (some relevant, some not)
system_flags = {
    'power_ok': True,
    'comms_locked': False,
    'sensor_array_ready': True,
    'calibration_pending': True,
    'legacy_mode': False,
    'debug_override': False
}

# Decoy function that looks important but isn't used in final calculation
def compute_signal_latency(packets):
    total = 0
    for p in packets:
        if p['status'] == 'ACTIVE':
            total += p['voltage'] * 100
    return int(total)

# Auxiliary transformation with set operations (partially relevant)
active_ids = {p['id'] for p in telemetry_packets if p['status'] == 'ACTIVE'}
stale_ids = {102, 104}
purge_candidates = active_ids & stale_ids  # Empty set, but included to distract

# Dictionary aggregation of temperature stats (used later)
temp_stats = {}
for packet in telemetry_packets:
    status = packet['status']
    temp = packet['temp']
    if status not in temp_stats:
        temp_stats[status] = []
    temp_stats[status].append(temp)

# Compute median function (used once)
def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2] + s[-(n//2 + 1)]) / 2

# Extract median temperature of active systems
if 'ACTIVE' in temp_stats:
    median_active_temp = median(temp_stats['ACTIVE'])  # 55.1
else:
    median_active_temp = 0.0

# Bit manipulation red herring
flag_value = 0
for i, (k, v) in enumerate(system_flags.items()):
    if v:
        flag_value |= (1 << i)  # Computes a bitmask, not used directly

# Dummy transformation on logs
error_count = sum(1 for log in log_entries if log['level'] == 'ERROR')
debug_count = sum(1 for log in log_entries if log['level'] == 'DEBUG')
info_count = sum(1 for log in log_entries if log['level'] == 'INFO')

code_frequencies = {}
for log in log_entries:
    c = log['code']
    code_frequencies[c] = code_frequencies.get(c, 0) + 1

# Complex conditional evaluation chain (core logic)
def evaluate_health_score(temp, base=1.0):
    if temp < -20:
        return base * 0.6
    elif temp < 0:
        return base * 0.8
    elif temp < 60:
        return base * 1.0
    elif temp < 80:
        return base * 0.9
    else:
        return base * 0.7

# Nested dictionary construction (distractor)
nested_diagnostics = {
    'version': '2.1',
    'modules': {
        'comm': {'status': 1, 'errors': 0},
        'power': {'status': 0, 'errors': 1},
        'sensor': {'status': 1, 'errors': 0}
    }
}

# Main integrity evaluation function
# Combines boolean logic, arithmetic, and dictionary lookups
def evaluate_system_integrity(logs, flags):
    # Step 1: Base score from log structure
    base_score = len(logs) * 10  # 50
    
    # Step 2: Apply error penalty
    error_penalty = error_count * 15  # 15
    debug_bonus = debug_count * 5    # 5
    net_adjustment = debug_bonus - error_penalty  # -10
    
    # Step 3: Flag-based multiplier
    multiplier = 1.0
    if flags['power_ok'] and flags['sensor_array_ready']:
        multiplier *= 1.2
    if not flags['comms_locked']:
        multiplier *= 1.1
    if flags['calibration_pending']:
        multiplier *= 0.9
    
    # Step 4: Temperature influence via health scoring
    temp_influence = evaluate_health_score(median_active_temp)  # 0.9 (55.1 → 60 threshold)
    
    # Step 5: Code frequency bonus
    zero_code_bonus = code_frequencies.get(0, 0) * 8  # 2 * 8 = 16
    
    # Step 6: Set cardinality check (purge_candidates is empty → 0)
    purge_penalty = len(purge_candidates) * 20  # 0
    
    # Step 7: Combine all factors
    raw_score = (base_score + net_adjustment + zero_code_bonus - purge_penalty)
    
    # Step 8: Apply multipliers in sequence
    intermediate = raw_score * multiplier        # 66 * 1.2*1.1*0.9 = 66 * 1.188 = 78.408
    final_score = intermediate * temp_influence  # 78.408 * 0.9 = 70.5672
    
    # Step 9: Round to nearest integer
    return int(round(final_score))

# Execute main evaluation
final_diagnostic = evaluate_system_integrity(log_entries, system_flags)

# Print result as required
print(f"Result: {final_diagnostic}")