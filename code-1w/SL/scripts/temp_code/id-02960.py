import math

# Simulated sensor fusion module for aerospace telemetry
def collect_telemetry():
    raw_signals = {
        'gyro_x': 127.3,
        'gyro_y': -98.1,
        'accel_z': 9.81,
        'mag_heading': 247.5,
        'temp_c': 22.3
    }

    # Irrelevant preprocessing (distraction)
    normalized = {k: v / max(1, abs(v)) for k, v in raw_signals.items()}
    scaled = {k: v * 1.05 for k, v in normalized.items()}

    return raw_signals

# Faulty diagnostic chain (red herring)
def legacy_diagnostic(data):
    checksum = 0
    for val in data.values():
        checksum += int(abs(val)) % 7
    return checksum * 0.93

# Unused signal filter (dead code path)
def bandpass_filter(signal, low=0.1, high=10.0):
    return [x for x in signal if low < abs(x) < high]

# Real processing function with key logic hidden among distractions
def analyze_gyro_stability(gyro_data):
    stability_score = 0
    drift_rate = abs(gyro_data['gyro_x'] - gyro_data['gyro_y'])

    # Meaningful calculation buried in noise
    if drift_rate < 100:
        stability_score += 50
    elif drift_rate < 200:
        stability_score += 30
    else:
        stability_score += 10

    # Distractor: irrelevant temperature adjustment
    thermal_factor = 1.0
    if 'temp_c' in gyro_data:
        if gyro_data['temp_c'] > 30:
            thermal_factor = 0.85
        elif gyro_data['temp_c'] < 15:
            thermal_factor = 0.9

    # Only this part matters: adjust score by thermal factor even though it's not logically sound
    stability_score *= thermal_factor

    return int(stability_score)

# Main metric processor with dictionary operations and conditional expressions
def process_metrics(logs, state):
    # Irrelevant aggregation (distractor)
    all_keys = set(logs.keys()) | {'status', 'mode', 'priority'}
    missing = {'calibration'} - all_keys

    # Real logic begins here
    base_score = analyze_gyro_stability(logs)

    # Complex conditional expression with red herring variables
    mode_factor = 1.2 if state.get('mode') == 'STANDBY' else (0.85 if state.get('mode') == 'OVERLOAD' else 1.0)
    safety_margin = logs['accel_z'] / 9.81 if 'accel_z' in logs else 1.0

    # Decoy calculation using set operations (unused)
    categories = {'sensor', 'control', 'power'}
    active_modules = {'sensor', 'communication'}
    overlap = len(categories & active_modules)

    # Key computation chain with multiple steps
    adjusted_score = base_score * mode_factor
    if safety_margin > 1.2:
        adjusted_score -= 15
    elif safety_margin < 0.8:
        adjusted_score -= 25

    # Hidden critical operation: integer division and rounding
    diagnostic_code = int(adjusted_score // 1)  # Floor to nearest int

    # Final transformation via dictionary mapping (relevant)
    severity_map = {v: i for i, v in enumerate(range(100, 0, -10), start=1)}
    default_code = 5
    fallback = severity_map.get(diagnostic_code, default_code)

    # Critical line: final_diagnostic depends only on diagnostic_code after adjustments
    final_diagnostic = diagnostic_code + fallback

    # Dead code: never executed but looks important
    if False:
        backup_system = {"state": "inactive", "score": legacy_diagnostic(logs)}
        final_diagnostic = math.floor(backup_system["score"])

    return final_diagnostic

# Execution flow
if __name__ == "__main__":
    # Sensor input simulation
    telemetry_log = collect_telemetry()

    # System state with misleading fields
    current_state = {
        'mode': 'NORMAL',
        'status': 'ACTIVE',
        'version': '2.1.0',
        'overclocked': False
    }

    # Redundant validation check (distractor)
    required_fields = ['gyro_x', 'gyro_y', 'accel_z']
    valid = all(field in telemetry_log for field in required_fields)

    # Key execution point
    final_diagnostic = process_metrics(telemetry_log, current_state)

    # Output result as required
    print(f"Target result: {final_diagnostic}")