import math

# Simulated telemetry data from satellite subsystems
telemetry_log = {
    'power': [12.4, 12.6, 12.5, 11.9, 12.0],
    'temp_cpu': [67, 72, 75, 78, 85],
    'temp_battery': [22, 23, 25, 28, 30],
    'signal_strength': [-74, -72, -75, -70, -68],
    'orientation': [(0.1, 0.05), (0.12, 0.08), (0.15, 0.1), (0.18, 0.14), (0.22, 0.19)]
}

# Fault detection flags from independent sensors
fault_flags = {
    'overvoltage': False,
    'thermal_throttle': True,
    'comms_jam': None,
    'attitude_drift': abs(0.22 - 0.1) > 0.1
}

# Irrelevant helper function (distractor)
def calculate_orbit_decay(age_years):
    return 100 * math.exp(-0.1 * age_years) + 45

# Unused signal processing chain (dead code path)
processed_signal = []
for db in telemetry_log['signal_strength']:
    if db < -70:
        processed_signal.append(db * 1.05)
    else:
        processed_signal.append(db * 0.98)

# Decoy state tracker (misleading intermediate)
current_mode = 'STANDBY'
if len(telemetry_log['power']) > 4:
    current_mode = 'ACTIVE'
if max(telemetry_log['temp_cpu']) > 80:
    current_mode = 'SAFE_MODE'

# Simulate phantom fault injection (red herring)
phantom_faults = set()
for i, t in enumerate(telemetry_log['temp_cpu']):
    if t > 70 and telemetry_log['power'][i] < 12.0:
        phantom_faults.add('spurious_thermal_alert')

# Auxiliary calculation with no impact (irrelevant computation)
avg_orientation = [
    sum(x[0] for x in telemetry_log['orientation']) / len(telemetry_log['orientation']),
    sum(x[1] for x in telemetry_log['orientation']) / len(telemetry_log['orientation'])
]

# Misdirection: complex-looking but unused bit manipulation
diagnostic_signature = 0
for val in telemetry_log['signal_strength'][-3:]:
    shifted = int(abs(val)) << 2
    diagnostic_signature ^= (shifted & 0xFF) | 0x10

# Real logic begins here — hidden among distractions
def evaluate_power_risk(log):
    recent = log['power'][-3:]
    return sum(1 for v in recent if v < 12.1) >= 2

def check_attitude_stability(log):
    roll_vals = [x[0] for x in log['orientation']]
    yaw_vals = [x[1] for x in log['orientation']]
    roll_trend = roll_vals[-1] - roll_vals[0]
    yaw_trend = yaw_vals[-1] - yaw_vals[0]
    return (roll_trend < 0.15) and (yaw_trend < 0.15)

def assess_thermal_load(log):
    cpu_avg = sum(log['temp_cpu']) / len(log['temp_cpu'])
    battery_peak = max(log['temp_battery'])
    return cpu_avg > 75 or battery_peak > 28

# Core analysis function
# Combines arithmetic, conditionals, dictionary lookups, and boolean logic
def analyze_system_state(log, flags):
    # Step 1: Power risk assessment
    power_risk = evaluate_power_risk(log)
    
    # Step 2: Attitude stability check
    stable_attitude = check_attitude_stability(log)
    
    # Step 3: Thermal evaluation
    high_thermal = assess_thermal_load(log)
    
    # Step 4: Resolve fault flag dependencies
    comms_issue = flags['comms_jam'] is not None and flags['comms_jam']
    critical_drift = flags['attitude_drift'] and not stable_attitude
    
    # Step 5: Aggregate conditions with conditional expressions
    severity_score = 0
    severity_score += 30 if power_risk else 0
    severity_score += 45 if high_thermal and flags['thermal_throttle'] else 0
    severity_score += 100 if critical_drift else 0
    severity_score += 20 if comms_issue else 0
    
    # Step 6: Apply nonlinear scaling based on safety mode
    if current_mode == 'SAFE_MODE':  # depends on global
        severity_score *= 1.25
    
    # Step 7: Final diagnostic as scaled integer (answer is deterministic)
    baseline = 17
    adjustment = int(round(severity_score / 5.0))
    final_diagnostic = baseline + adjustment
    
    # Step 8: Log dummy event (distraction)
    event_log = []
    if final_diagnostic > 50:
        event_log.append(('ALERT_RAISED', final_diagnostic))
    
    return final_diagnostic

# Execute key statement
final_diagnostic = analyze_system_state(telemetry_log, fault_flags)
print(f"Result: {final_diagnostic}")