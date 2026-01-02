import itertools

# System calibration constants (some irrelevant)
default_threshold = 0.75
scaling_factor = 1.618
calibration_mode = 'advanced'

# Sensor data simulation
diagnostic_codes = [101, 102, 103, 104]
sensor_readings = [
    {'id': 1, 'values': [1.2, 1.4, 1.3, 1.5]},
    {'id': 2, 'values': [0.9, 1.1, 1.0, 1.2]},
    {'id': 3, 'values': [1.8, 1.7, 1.9, 1.6]}
]

# Irrelevant diagnostic log initialization (red herring)
diagnostic_log = {}
for code in diagnostic_codes:
    diagnostic_log[code] = False

def process_signal(sequence, mode='normal'):
    if mode == 'normal':
        return sum(x ** 1.5 for x in sequence if x > 1.0)
    else:
        return sum(x ** 0.5 for x in sequence)

# Unused helper function (dead code path)
def legacy_compensate(value):
    return value * 0.87 if value > 1.5 else value * 1.03

# Primary signal processing chain
active_sensors = []
for sensor in sensor_readings:
    avg_val = sum(sensor['values']) / len(sensor['values'])
    if avg_val >= default_threshold:
        active_sensors.append(sensor['id'])

# Simulate multi-phase signal fusion
fusion_phases = []
for i, sensor in enumerate(sensor_readings):
    processed = process_signal(sensor['values'], mode=calibration_mode[:6])
    phase_entry = {
        'index': i,
        'raw': sensor['values'],
        'processed': processed,
        'flagged': processed > 2.5
    }
    fusion_phases.append(phase_entry)

# Irrelevant combinatorics on sensor IDs (distractor)
id_pairs = list(itertools.combinations(active_sensors, 2))
connection_matrix = {}
for a, b in id_pairs:
    connection_matrix[(a, b)] = (a + b) * 0.01  # Decoy metric

# Real computation buried among distractions
effective_signals = []
weights = [0.5, 1.0, 0.75]

for entry, weight in zip(fusion_phases, weights):
    if entry['flagged']:
        effective_signals.append(entry['processed'] * weight)

# More misdirection: unused enumeration pattern
diagnostic_trace = []
for idx, sig in enumerate(fusion_phases):
    temp_score = sig['processed'] * (idx + 1)
    diagnostic_trace.append(temp_score)  # Not used later

# Core logic hidden in apparent noise
aggregate = 0
for i, val in enumerate(effective_signals):
    if i % 2 == 0:
        aggregate += val * 1.1
    else:
        aggregate += val * 0.9

# Additional decoy transformation (never accessed)
final_array = [x * 2.1 for x in diagnostic_trace]
buffer_stack = list(itertools.accumulate(final_array[:2]))

# Key assignment point — answer derived here
phase_output = aggregate * scaling_factor

# Final red herring: complex but unused dictionary reduction
total_diagnostic = 0
status_map = {1: 'OK', 2: 'WARN', 3: 'OK'}
for sensor in sensor_readings:
    sid = sensor['id']
    if sid in status_map:
        total_diagnostic += len(status_map[sid])

print(f"Result: {phase_output}")