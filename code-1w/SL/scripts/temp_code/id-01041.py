def analyze_node_health(node_data, threshold=0.75):
    return sum(1 for x in node_data if x > threshold)

# Simulated sensor readings from distributed nodes (irrelevant to final result)
sensor_readings = [
    [0.6, 0.8, 0.9],
    [0.4, 0.5, 0.7],
    [0.9, 0.9, 0.8]
]
node_health_status = [analyze_node_health(row) for row in sensor_readings]

# Irrelevant auxiliary function for signal calibration
def calibrate_signal(strength, factor=1.1):
    return strength * factor if strength < 0.8 else strength

# Fake transformation chain with decoy data flow
raw_signals = [0.5, 0.7, 0.9]
calibrated = [calibrate_signal(s) for s in raw_signals]
smoothed = [x * 1.05 for x in calibrated]
adjusted = [max(x - 0.1, 0) for x in smoothed]

# Core system diagnostics (relevant data structures)
grid_diagnostics = {
    'voltage': [110, 120, 115, 130],
    'phase_shift': [0.1, 0.3, 0.2, 0.4],
    'harmonics': {2: 0.05, 3: 0.08, 5: 0.03}
}

system_load = [
    {'load': 80, 'temp': 45},
    {'load': 95, 'temp': 52},
    {'load': 70, 'temp': 40},
    {'load': 88, 'temp': 49}
]

# Dead code path - never called (distractor)
def deprecated_diagnostic(seq):
    return [x ** 2 for x in seq if x % 2 == 0]

# Unused intermediate transformations
baseline = [x['load'] * 0.95 for x in system_load]
overload_flags = [1 if x['temp'] > 48 else 0 for x in system_load]
temp_risk_score = sum(overload_flags)

# Bit manipulation red herring (no impact on final result)
status_flag = 0b10101010
mask = 0b11110000
masked_status = status_flag & mask
inverted = ~masked_status & 0b11111111

# Set operations - relevant to actual computation
voltage_set = set(grid_diagnostics['voltage'])
reference_voltages = {110, 115, 120}
common_levels = voltage_set & reference_voltages  # Intersection used later

# Enumerate and zip usage (required python features)
phase_values = grid_diagnostics['phase_shift']
indexed_phases = []
for i, phase in enumerate(phase_values):
    indexed_phases.append((i + 1, phase * 100))

load_sequence = [x['load'] for x in system_load]
dual_stream = list(zip(indexed_phases, load_sequence))

# Real computation begins here — multi-step reasoning required
base_metric = len(common_levels)
shift_penalty = sum(p[1] for p in indexed_phases if p[1] > 25)
efficiency_factor = 100 - shift_penalty

# Auxiliary calculation using set difference (distraction)
unused_diff = voltage_set - reference_voltages
phantom_correction = len(unused_diff) * 5

# Actual aggregation logic (critical path)
def aggregate_metrics(voltages, loads):
    base = len(common_levels)
    total_load = sum(item['load'] for item in loads)
    avg_voltage = sum(voltages['voltage']) / len(voltages['voltage'])
    
    # Hidden dependency: harmonic distortion weighting
    h = voltages['harmonics']
    weight = h[3] * 100  # Only 3rd harmonic used
    
    # Complex interaction across multiple variables
    intermediate = (base * avg_voltage) + (total_load / 10)
    penalty = 0
    for idx, val in enumerate(voltages['phase_shift']):
        if val > 0.25:
            penalty += (idx + 1) * 10
    
    # Final formula combines arithmetic, iteration, and conditional logic
    result = intermediate - penalty + weight
    
    # Decoy mutation (never affects output)
    result += phantom_correction - temp_risk_score
    
    return int(result)

# Execution point of interest
final_diagnostic = aggregate_metrics(grid_diagnostics, system_load)

# Print result as required
print(f"Result: {final_diagnostic}")