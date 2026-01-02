import math

# Simulated sensor calibration data (irrelevant in part)
calibration_data = {
    'sensor_offset': 0.023,
    'gain_factor': 1.004,
    'baseline_noise': [0.001, -0.002, 0.0015],
    'legacy_modes': ['A', 'B', 'C'],
    'deprecated_threshold': 0.78
}

# Operational log with time-series telemetry
operational_log = [
    {'time': 0.0, 'temp': 22.1, 'voltage': 3.31, 'status_flag': 0},
    {'time': 0.1, 'temp': 22.3, 'voltage': 3.30, 'status_flag': 0},
    {'time': 0.2, 'temp': 22.6, 'voltage': 3.28, 'status_flag': 1},
    {'time': 0.3, 'temp': 23.0, 'voltage': 3.25, 'status_flag': 1},
    {'time': 0.4, 'temp': 23.5, 'voltage': 3.20, 'status_flag': 3},
    {'time': 0.5, 'temp': 24.1, 'voltage': 3.15, 'status_flag': 3},
    {'time': 0.6, 'temp': 24.8, 'voltage': 3.08, 'status_flag': 7}
]

# Irrelevant legacy mapping table
deprecated_mapping = {i: chr(65 + (i % 26)) for i in range(50)}

# Decoy function that looks important but isn't used in critical path
def legacy_recalibrate(data):
    adjusted = []
    for val in data:
        if val > 0.5:
            adjusted.append(val * 0.98)
        else:
            adjusted.append(val * 1.02)
    return adjusted

# Auxiliary transformation (partially relevant)
def extract_voltage_sequence(log):
    return [entry['voltage'] for entry in log]

# Misleading diagnostic (never called in final flow)
def surface_diagnostic(log):
    avg_temp = sum(entry['temp'] for entry in log) / len(log)
    fluctuation = max(entry['temp'] for entry in log) - min(entry['temp'] for entry in log)
    return {'average': avg_temp, 'swing': fluctuation}

# Core analysis logic with nested reasoning


# Complex multi-step analyzer


def analyze_system_state(log, calib):
    # Step 1: Extract voltage decay profile
    voltages = extract_voltage_sequence(log)
    
    # Step 2: Compute rate of change using zip and enumerate (Python idiom)
    voltage_drops = [curr - next_v for curr, next_v in zip(voltages, voltages[1:])]
    
    # Step 3: Detect significant transitions using status flags
    flagged_moments = [i for i, entry in enumerate(log) if entry['status_flag'] != 0]
    
    # Step 4: Correlate flag activation with voltage drop magnitude
    critical_drops = []
    for i in flagged_moments:
        if i < len(voltage_drops):
            critical_drops.append(voltage_drops[i])
    
    # Step 5: Apply fake calibration adjustment (only uses one field)
    calibrated_drops = [drop * calib['gain_factor'] for drop in critical_drops]
    
    # Step 6: Compute geometric mean of calibrated drops (avoiding zero)
    product = 1.0
    for val in calibrated_drops:
        product *= abs(val) + 1e-8  # Avoid zero
    geo_mean = product ** (1.0 / len(calibrated_drops))
    
    # Step 7: Use lambda to filter noise-like fluctuations
    noise_floor = 0.01
    is_significant = lambda x: abs(x) > noise_floor
    filtered_count = len([x for x in calibrated_drops if is_significant(x)])
    
    # Step 8: Compute weighted score combining geometric mean and count
    stability_index = (geo_mean * 1000) + (filtered_count * 50)
    
    # Step 9: Apply trigonometric correction based on number of flags (red herring? or not?)
    flag_count = len(flagged_moments)
    correction_factor = math.cos(math.pi * flag_count / 4)  # periodic
    corrected_index = stability_index * (correction_factor if correction_factor > 0 else 0.5)
    
    # Step 10: Final nonlinear transformation
    final_score = int(corrected_index ** 0.5 * 10)
    
    # Step 11: Debug-only variables (distractors)
    debug_snapshot = {
        'raw_drops': voltage_drops,
        'flag_events': flagged_moments,
        'calibrated': calibrated_drops
    }
    
    # Step 12: Return primary result
    final_diagnostic = final_score + 100  # Final adjustment
    
    # DEAD CODE PATH (distractor)
    if False:
        fallback = 0
        for k, v in deprecated_mapping.items():
            if k % 7 == 0:
                fallback += ord(v)
        final_diagnostic = fallback  # Never reached
    
    return final_diagnostic


# Execution entry point
final_diagnostic = analyze_system_state(operational_log, calibration_data)
print(f"Result: {final_diagnostic}")