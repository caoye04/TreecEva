import math

# Simulated sensor fusion module for aerospace telemetry
def analyze_phase_coherence(timestamps, readings):
    coherence_score = 0
    for i in range(1, len(readings)):
        delta_t = timestamps[i] - timestamps[i-1]
        phase_diff = abs(readings[i] - readings[i-1])
        if delta_t > 0:
            coherence_score += phase_diff / delta_t
    return int(coherence_score % 100)

# Irrelevant signal smoothing function (dead code path)
def smooth_signal(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window // 2)
        end = min(len(data), i + window // 2 + 1)
        smoothed.append(sum(data[start:end]) / (end - start))
    return smoothed

# Decoy calibration routine with misleading computations
def run_diagnostics(sensor_data):
    baseline = sum(sensor_data.get('baseline', [0])) * 0.01
    offset = len(sensor_data.get('errors', [])) ** 2
    fake_metric = math.sin(baseline) * offset
    threshold_adjustment = fake_metric * 0.75  # Never used later
    return {'calibration': 42, 'status': 'nominal'}

# Core logic for fault detection across subsystems
def detect_anomalies(log_entries, thresholds):
    anomalies = []
    for entry in log_entries:
        for key, value in entry.items():
            limit = thresholds.get(key, 100)
            if isinstance(value, (int, float)) and abs(value) > limit:
                anomalies.append((key, value))
    return anomalies

# Data transformation: map sensor IDs to normalized channels
def remap_sensors(raw_mapping):
    channel_map = {}
    for idx, sensor_id in enumerate(raw_mapping):
        channel_map[f'chan_{idx}'] = sensor_id.replace('SNS', 'CH')
    return channel_map

# Main aggregation function — the real answer depends on this
# But it's buried among red herrings
def aggregate_metrics(timing_log, system_state):
    # Real computation chain (hidden among distractions)
    base_value = len(timing_log) * 17
    
    # Extract execution phases
    phases = [t[1] for t in timing_log if t[1] in ['INIT', 'RUN', 'IDLE']]
    phase_counts = {phase: phases.count(phase) for phase in set(phases)}
    
    # Key calculation step: RUN phase dominance affects result
    run_weight = phase_counts.get('RUN', 0) * 3
    idle_penalty = phase_counts.get('IDLE', 0) * 2
    
    intermediate = base_value + run_weight - idle_penalty
    
    # Use dictionary and set operations meaningfully
    active_units = set(system_state.get('units', []))
    critical_units = {'U1', 'U3', 'U5', 'U7'}
    unit_overlap = len(critical_units & active_units)
    
    intermediate += unit_overlap * 5
    
    # Introduce enumerate and zip usage (required Python feature)
    history = system_state.get('history', [])
    cumulative_shift = 0
    for i, record in enumerate(history):
        for a, b in zip(record[::2], record[1::2]):
            cumulative_shift ^= (a + b + i) & 7
    
    final_value = intermediate + cumulative_shift
    
    # Final adjustment based on hidden pattern
    flags = system_state.get('flags', [])
    if 'OVERRIDE' not in flags and final_value > 100:
        final_value -= 45
    
    return final_value

# === START OF EXECUTION ===

# Irrelevant data structures (distractors)
timestamps = [100, 105, 112, 120, 125, 130]
readings = [20.1, 22.3, 25.8, 26.0, 29.4, 30.1]
signal_data = [1, 2, 1, 3, 2, 1]

# Unused configuration block (misleading)
config = {
    'timeout': 30,
    'retries': 3,
    'debug_mode': False,
    'buffer_size': 1024,
    'max_connections': 5
}

# Sensor mapping (partially relevant, but remap_sensors is unused)
sensor_layout = ['SNS01', 'SNS02', 'SNS03', 'SNS04']
remapped = remap_sensors(sensor_layout)  # Computed but not used

# Real input data
log_timing = [
    (1000, 'INIT'),
    (1050, 'RUN'),
    (1100, 'RUN'),
    (1150, 'IDLE'),
    (1200, 'RUN'),
    (1250, 'RUN'),
    (1300, 'IDLE')
]

state_snapshot = {
    'units': ['U1', 'U2', 'U3', 'U4'],
    'history': [
        [10, 20],
        [15, 25],
        [12, 22]
    ],
    'flags': ['STANDBY']
}

# Diagnostic call (irrelevant result)
diag_result = run_diagnostics({'baseline': [100, 200], 'errors': [1, 2]})

# Real anomaly detection (but result not directly used)
thresholds = {'temp': 90, 'pressure': 150}
entries = [
    {'temp': 85, 'pressure': 140},
    {'temp': 95, 'pressure': 130},
    {'temp': 88, 'pressure': 160}
]
anomaly_list = detect_anomalies(entries, thresholds)  # Only length indirectly affects nothing

# Coherence analysis (completely irrelevant)
coherence = analyze_phase_coherence(timestamps, readings)

# Critical assignment — this is where the answer is determined
final_diagnostic = aggregate_metrics(log_timing, state_snapshot)

# Output required format
print(f"Target result: {final_diagnostic}")