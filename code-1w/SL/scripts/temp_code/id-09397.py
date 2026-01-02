import math

# Simulated telemetry data from a satellite subsystem
telemetry_log = {
    'voltage': [3.28, 3.31, 3.29, 3.30, 3.32, 3.27, 3.25, 3.45],
    'temperature': [22.5, 23.1, 22.8, 24.0, 25.6, 26.1, 27.3, 35.0],
    'radiation_count': [120, 125, 130, 132, 135, 140, 142, 150],
    'timestamp': [1678886400, 1678886460, 1678886520, 1678886580, 1678886640,
                  1678886700, 1678886760, 1678886820]
}

# System operational flags
system_flags = {
    'power_stable': True,
    'thermal_override': False,
    'comms_locked': True,
    'debug_mode': True
}

# Irrelevant calibration map (distractor)
calibration_map = {
    'sensor_a': lambda x: x * 1.02 + 0.05,
    'sensor_b': lambda x: x * 0.98 - 0.03,
    'sensor_c': lambda x: x * 1.05
}

# Decoy function that appears useful but is not used in main logic
def legacy_recalibrate(data):
    return [max(0, d * 0.97 - 0.1) for d in data if d > 0]

# Auxiliary function to compute moving average (used)
def moving_average(values, window_size=3):
    if len(values) < window_size:
        return [sum(values)/len(values)]
    return [sum(values[i:i+window_size]) / window_size 
            for i in range(len(values) - window_size + 1)]

# Complex bit manipulation for fault masking (used in limited way)
def detect_anomaly_burst(flags):
    code = 0
    for i, key in enumerate(['power_stable', 'thermal_override', 'comms_locked']):
        if not flags[key]:
            code |= (1 << i)
    return code ^ 0b101

# Unused recursive function (dead path)
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# String-based diagnostic generator - looks important but only partially used
def generate_diagnostics(code):
    messages = {
        0: "ALL_CLEAR",
        1: "POWER_FLUCTUATION",
        2: "THERMAL_ALERT",
        3: "COMMS_DEGRADED",
        4: "CRITICAL_OVERRIDE"
    }
    return messages.get(code, "UNKNOWN") + "_STATUS"

# Core analysis with multiple steps and red herrings
def analyze_system_state(log, flags):
    # Step 1: Extract last few voltage readings
    recent_voltage = log['voltage'][-4:]
    
    # Step 2: Compute moving average of voltage (relevant)
    avg_voltage = sum(moving_average(recent_voltage)[0]) / len(moving_average(recent_voltage))
    
    # Step 3: Check temperature trend (relevant)
    temp_trend = log['temperature'][-1] - log['temperature'][-4]
    overheat_risk = temp_trend > 2.0
    
    # Step 4: Radiation spike detection (distractor - not actually used in final decision)
    radiation_spikes = [r for r in log['radiation_count'] if r > 140]
    spike_rate = len(radiation_spikes) / len(log['radiation_count'])
    
    # Step 5: Apply fake calibration for distraction (result unused)
    calibrated_temp = [calibration_map['sensor_a'](t) for t in log['temperature']]
    
    # Step 6: Determine anomaly code from flags (partially relevant)
    anomaly_code = detect_anomaly_burst(flags)
    
    # Step 7: Generate misleading string diagnostic (only first char matters)
    diag_str = generate_diagnostics(anomaly_code)
    
    # Step 8: Extract ASCII value of first character as seed (clever distraction)
    seed_value = ord(diag_str[0])
    
    # Step 9: Real computation path begins here
    # Only care about thermal override status and voltage
    if not flags['thermal_override'] and avg_voltage < 3.3:
        base_score = 400
    elif flags['thermal_override'] and avg_voltage >= 3.3:
        base_score = 200
    else:
        base_score = 300
    
    # Step 10: Modify by temperature trend
    trend_factor = int(temp_trend * 10)
    adjusted_score = base_score + trend_factor
    
    # Step 11: Final adjustment using bit of diagnostic string (only 'A'=65 matters)
    ascii_offset = abs(seed_value - 65)  # 'A' is 65
    final_score = adjusted_score - ascii_offset
    
    # Step 12: Return final diagnostic value
    return final_score

# Execution point of interest
final_diagnostic = analyze_system_state(telemetry_log, system_flags)
print(f"Target result: {final_diagnostic}")