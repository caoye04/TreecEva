from collections import defaultdict, Counter

# Simulated system telemetry data with mixed signal types
telemetry_stream = [
    (100, 'temp', 72.5, True),
    (101, 'voltage', 3.3, False),
    (102, 'temp', 75.1, True),
    (103, 'current', 1.4, True),
    (104, 'temp', 73.8, True),
    (105, 'voltage', 3.2, False),
    (106, 'temp', 80.0, True),
    (107, 'current', 1.8, True),
    (108, 'voltage', 3.4, True),
    (109, 'temp', 77.3, True)
]

# Irrelevant auxiliary mapping (distractor)
unit_scale = {'temp': 1.0, 'voltage': 1000, 'current': 100}

# Misleading preprocessing - appears important but unused in final path
def legacy_normalize(entries):
    result = []
    for t, sensor, val, active in entries:
        if sensor in unit_scale:
            val *= unit_scale[sensor]
        result.append((t, sensor, round(val, 2), active))
    return result

legacy_data = legacy_normalize(telemetry_stream)  # Dead assignment

# Decoy statistical function (never called)
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    from math import log2
    return -sum((count / total) * log2(count / total) for count in counts.values())

# Signal filter that looks general but is actually bypassed
active_filters = {
    'noise_threshold': lambda x: x > 0.1,
    'stability_check': lambda x: abs(x - 75.0) < 10
}

# Core processing components
sensor_buffers = defaultdict(list)
status_registry = defaultdict(bool)

for timestamp, sensor_type, reading, is_active in telemetry_stream:
    if is_active:
        sensor_buffers[sensor_type].append(reading)
    status_registry[sensor_type] = status_registry[sensor_type] or is_active

# High-level diagnostic flags (some are red herrings)
system_flags = {
    'overheat_alert': False,
    'fluctuation_index': 0.0,
    'critical_sensors': [],
    'redundancy_loss': None,
    'phase_locked': True
}

# Populate actual used metrics
if 'temp' in sensor_buffers:
    temp_readings = sensor_buffers['temp']
    avg_temp = sum(temp_readings) / len(temp_readings)
    max_temp = max(temp_readings)
    
    # Real logic branch
    if max_temp > 79.0:
        system_flags['overheat_alert'] = True
        system_flags['critical_sensors'].append('temp')
    
    # This fluctuation index is overwritten later - misleading intermediate
    system_flags['fluctuation_index'] = round(max(temp_readings) - min(temp_readings), 2)

if 'voltage' in sensor_buffers:
    voltages = sensor_buffers['voltage']
    voltage_stable = all(abs(v - 3.3) < 0.2 for v in voltages)
    system_flags['phase_locked'] = voltage_stable

# Another decoy structure (unused)
calibration_matrix = [[1.0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    calibration_matrix[i][i] = 0.95

# Simulated log aggregation with metadata (partially relevant)
log_entries = []
for i, (t, s, r, a) in enumerate(telemetry_stream):
    entry = {
        'seq': i,
        'type': s,
        'val': r,
        'active': a,
        'weight': 1.0
    }
    
    # Conditional weighting that has no effect (dead logic)
    if s == 'temp' and r > 75.0:
        entry['weight'] = 1.1  # Never used downstream
    
    log_entries.append(entry)

# Key lambda transformation - used in final computation
weight_func = lambda x: x * 1.05 if x > 75 else x * 0.98

# Secondary buffer for derived values (only one element used)
derived_diagnostics = []
for entry in log_entries:
    if entry['type'] == 'temp' and entry['active']:
        adjusted = weight_func(entry['val'])
        derived_diagnostics.append(adjusted)

# Red herring counter (collected but unused)
reading_counter = Counter(entry['type'] for entry in log_entries)

# Central processing function with multiple inputs
def process_metrics(entries, flags):
    # Local shadowing of global name (distractor)
    status_registry = {'initialized': True, 'nodes': 5}
    
    # Unused nested function
    def validate_entry(e):
        return e['seq'] >= 0 and e['val'] > 0
    
    # Extract temperature values using enumerate to track position
    raw_temps = []
    for idx, entry in enumerate(entries):
        if entry['type'] == 'temp':
            raw_temps.append((idx, entry['val']))
    
    # Use zip to pair consecutive readings (creates distraction)
    paired_deltas = []
    for curr, next_val in zip(raw_temps, raw_temps[1:]):
        delta = next_val[1] - curr[1]
        paired_deltas.append((curr[0], delta))
    
    # Actual critical calculation
    high_temp_count = sum(1 for _, val in raw_temps if val > 75.0)
    base_score = 100 + high_temp_count * 25
    
    # Modify score based on system flags using logical conditions
    if flags['overheat_alert']:
        base_score += 50
    if not flags['phase_locked']:
        base_score -= 20
    
    # Final adjustment using tuple unpacking (real contribution)
    adjustments = [(1, 5), (2, -3), (3, 8)]
    total_adjust = 0
    for priority, mod in adjustments:
        total_adjust += mod
    
    # The real answer formation
    result = base_score + total_adjust
    
    # Dead code path with misleading print
    if result < 0:
        print("Critical system failure")  # Never reached
    
    return result

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_flags)
print(f"Target result: {final_diagnostic}")