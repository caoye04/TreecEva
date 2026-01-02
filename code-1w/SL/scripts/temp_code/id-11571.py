from itertools import cycle, islice

def analyze_sensor_drift(readings):
    # Irrelevant helper function: simulates sensor calibration (not used in final result)
    baseline = sum(readings[:3]) / 3
    drift = [abs(baseline - r) for r in readings]
    return sum(drift) / len(drift)

# Simulated IoT sensor data (temperature readings in Celsius)
sensor_readings = [23.5, 24.1, 23.9, 24.0, 25.2, 26.1, 25.8, 25.0]

drift_correction_factor = analyze_sensor_drift(sensor_readings)  # Dead code path — never used

# Process phase configuration
phases = ['heating', 'cooling', 'stabilization', 'compression']
durations = [15, 10, 20, 12]
temperature_setpoints = [75, 25, 50, 90]

# Create processing schedule using zip and enumerate
processing_schedule = []
for i, (phase, duration, temp) in enumerate(zip(phases, durations, temperature_setpoints)):
    efficiency_factor = (duration + temp) / (i + 1) if i > 0 else 1.0
    processing_schedule.append({
        'index': i,
        'phase': phase,
        'duration': duration,
        'setpoint': temp,
        'factor': efficiency_factor
    })

# Auxiliary computation: creates distraction with string manipulation
phase_names_upper = [p['phase'].upper() for p in processing_schedule]
status_flags = []
for name in phase_names_upper:
    if 'ING' in name:
        status_flags.append(name.replace('ING', '*'))
    else:
        status_flags.append(name)

# Misleading cumulative metric (unused)
total_load_score = 0
for entry in processing_schedule:
    total_load_score += entry['duration'] * entry['setpoint']

# Core logic: simulate yield calculation across phases
def calculate_phase_contribution(phase_data):
    contribution = 0
    for step in phase_data:
        if step['setpoint'] > 50:
            contribution += step['factor'] * 1.2
        else:
            contribution += step['factor'] * 0.8
    return round(contribution, 3)

# Use lambda to filter high-duration phases (semi-relevant)
long_phases_filter = lambda ph: ph['duration'] > 12
long_phases = list(filter(long_phases_filter, processing_schedule))

# Simulate resource allocation using itertools
cycle_phases = list(islice(cycle(['A', 'B']), len(sensor_readings))))
resource_map = {i: cycle_phases[i] for i in range(len(cycle_phases))}

# Actual yield calculation uses only factor and index logic
def calculate_optimal_yield(phases_list):
    base_yield = 0
    adjustment = 0
    for idx, p in enumerate(phases_list):
        if idx % 2 == 0:
            base_yield += p['factor'] * p['setpoint'] / 10
        else:
            adjustment += p['factor'] * 0.5
    return int(base_yield - adjustment)

# Key execution point
final_yield = calculate_optimal_yield(processing_phases)

# Correct variable reference: processing_phases was not yet defined; fix scope
processing_phases = processing_schedule

# Recompute final result with correct input
final_yield = calculate_optimal_yield(processing_phases)

print(f"Result: {final_yield}")