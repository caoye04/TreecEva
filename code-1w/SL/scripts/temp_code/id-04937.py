import math

# System health monitoring simulation with layered diagnostics
def analyze_subsystem readings(readings):
    if not readings:
        return 0.0
    filtered = [r for r in readings if r > 25.0]  # Only high-threshold values
    if len(filtered) < 2:
        return sum(readings) / len(readings)
    return (sum(filtered) / len(filtered)) * 0.9

# Irrelevant helper - distractor
def calculate_efficiency(index, baseline=1.0):
    return (index ** 2) * baseline / 100

# Decoy function - never called
def legacy_diagnostic(data):
    acc = 0
    for x in data:
        acc += x % 7
    return acc * 0.5

# Core transformation pipeline
def transform_signal(raw_signal):
    processed = []
    for val in raw_signal:
        if val < 0:
            processed.append(abs(val) ** 0.5)
        elif val == 0:
            processed.append(0.1)
        else:
            processed.append(math.log(val + 1))
    return [round(p, 3) for p in processed]

# Secondary analysis with red herring variables
def evaluate_stability(measurements):
    avg = sum(measurements) / len(measurements)
    variance = sum((m - avg) ** 2 for m in measurements) / len(measurements)
    threshold = 5.7
    stability_score = 0
    
    # Distractor block: complex but unused logic
    if variance < threshold:
        for i in range(len(measurements)):
            if i % 3 == 0 and measurements[i] > avg:
                stability_score += 1
    else:
        temp_accum = 0
        for m in measurements:
            temp_accum += int(m) & 5  # Bitwise distraction
        stability_score = temp_accum % 10
    
    # Actual result (simple, buried in noise)
    return avg * 0.85

# Main aggregation logic
def aggregate_metrics(chain, state):
    # Irrelevant unpacking
    primary_path, secondary_path = chain['A'], chain['B']
    temp_debug = [x * 0.1 for x in primary_path if x > 50]  # Unused list comprehension
    
    # Real computation begins
    transformed_A = transform_signal(primary_path)
    diagnostic_A = analyze_subsystem_readings(transformed_A)
    
    transformed_B = [math.sin(x * 0.1) for x in secondary_path]  # List comprehension
    diagnostic_B = evaluate_stability(transformed_B)
    
    # Cross-check with system state flags
    override_flag = state.get('override_safety', False)
    calibration_mode = state.get('calibration_level', 0)
    
    intermediate_result = (diagnostic_A + diagnostic_B) * 1.2
    
    # Dead code path - misleading conditional
    if calibration_mode > 5 and override_flag:
        adjustment = 0
        for val in transformed_A:
            if val > 1.0:
                adjustment += int(val) ^ 3
        intermediate_result -= adjustment * 0.01
    
    # Final computation - this is the actual answer
    final_weight = 1.0 if not override_flag and calibration_mode < 3 else 0.7
    return round(intermediate_result * final_weight, 6)

# Simulated input data
processing_chain = {
    'A': [86, 42, 75, 0, 91, 15],
    'B': [120, 30, 60, 90, 150]
}
system_state = {
    'override_safety': False,
    'calibration_level': 2,
    'debug_mode': True,
    'power_cycle_count': 7,
    'last_reset_code': 203
}

# Key execution point
final_diagnostic = aggregate_metrics(processing_chain, system_state)
print(f"Target result: {final_diagnostic}")