from itertools import cycle

def analyze_turbine_readings(readings):
    filtered = [r for r in readings if r > 0]
    avg = sum(filtered) / len(filtered) if filtered else 0
    normalized = [round(r / avg, 3) for r in filtered]
    return normalized

def generate_diagnostics(values, threshold=0.95):
    status_flags = {}
    for i, v in enumerate(values):
        status_flags[f'sensor_{i}'] = 'OK' if v >= threshold else 'CALIBRATE'
    # Irrelevant aggregation
    stats = {
        'count': len(values),
        'zeros': values.count(0),
        'peak': max(values, default=0)
    }
    return status_flags

def calculate_system_state(phase_log, diag):
    active_phases = []
    for idx, entry in enumerate(phase_log):
        if entry['power'] > 100 and entry['temp'] < 85:
            active_phases.append(idx)
    
    # Distractor: complex zip + enumerate that doesn't affect result
    timestamps = [1000 + i*5 for i in range(len(phase_log))]
    for ts, (i, log) in zip(timestamps, enumerate(phase_log)):
        log['timestamp'] = ts  # semi-relevant but unused later

    # Real logic: count valid transitions
    transitions = 0
    for i in range(1, len(active_phases)):
        if active_phases[i] - active_phases[i-1] == 1:
            transitions += 1

    # Misleading diagnostic analysis (not used in final answer)
    diag_result = generate_diagnostics([0.8, 0.96, 0.92, 0.98])
    compliance_count = sum(1 for s in diag_result.values() if s == 'OK')

    # Core calculation
    base_score = sum(p['efficiency'] for p in phase_log) * 10
    final_phase = int(base_score + transitions * 5 - 17)  # Key result

    return final_phase

# Main execution
phases = [
    {'power': 120, 'temp': 80, 'efficiency': 0.85},
    {'power': 95,  'temp': 78, 'efficiency': 0.76},
    {'power': 150, 'temp': 82, 'efficiency': 0.91},
    {'power': 160, 'temp': 84, 'efficiency': 0.89},
    {'power': 80,  'temp': 70, 'efficiency': 0.77},
    {'power': 110, 'temp': 83, 'efficiency': 0.93}
]

# Irrelevant data processing
readings = [-5, 0, 150, 200, -10, 180]
diagnostic_normalized = analyze_turbine_readings(readings)

# Sensor pattern cycling (dead code path)
cycle_pattern = list(zip(range(4), cycle(['A', 'B', 'C'])))

# Key execution point
diagnostics = {f'unit_{i}': 'active' for i in range(5)}
final_phase = calculate_system_state(phases, diagnostics)

print(f"Result: {final_phase}")