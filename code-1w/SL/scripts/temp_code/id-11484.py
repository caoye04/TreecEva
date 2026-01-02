import math

def analyze_phase_transition(energy_levels, threshold=256):
    """Irrelevant diagnostic function for phase analysis."""
    transitions = []
    for i, level in enumerate(energy_levels):
        if level > threshold and i > 0:
            transitions.append((i, math.log(level, 2)))
    return transitions

def transform_sequence(seq):
    """Misleading transformation with no impact on final result."""
    return [x ^ (x << 1) for x in seq][::-1]

def accumulate_diagnostic_metrics(data):
    """Dead code path — never called but looks important."""
    total = 0
    for item in data:
        if item % 3 == 0:
            total += item * 2
    return total

def calculate_thermal_output(stage_code):
    """Core function: computes thermal output based on stage."""
    base = sum([int(c) for c in str(stage_code) if c.isdigit()])
    modifier = 1.5 if 'X' in str(stage_code) else 0.8
    temp_offset = math.sin(math.pi / 4) * 100
    # Key computation
    return int((base * modifier) + temp_offset)

def main():
    # Initialize multiple variables, many irrelevant
    system_id = 'THRM-9X'
    energy_readings = [120, 204, 350, 512, 768]
    debug_trace = transform_sequence([7, 3, 9, 1])  # Distractor
    calibration_data = {'offset': 42, 'gain': 1.05}
    
    # Real data used in logic
    process_stages = ['INIT', 'HEAT_3A', 'COOL_2C', 'STAB_X7']
    fallback_value = len(system_id) * 12
    
    # Red herring: complex-looking but unused calculation
    entropy_score = sum([math.log(x) for x in energy_readings if x > 200])
    entropy_score = round(entropy_score, 2) if entropy_score > 10 else fallback_value / 2
    
    # Conditional expression with slicing — relevant to control flow
    active_stage = process_stages[1:][-1] if len(process_stages) > 2 else process_stages[0]
    
    # Core assignment with conditional logic
    thermal_capacity = calculate_thermal_output(process_stages[-1]) if process_stages else fallback_value
    
    # Additional decoy operations
    snapshot = energy_readings[:]
    snapshot.append(sum(debug_trace))  # Unused
    anomaly_detected = any([x > 1000 for x in energy_readings])  # False, irrelevant
    
    # Final override guard (not triggered)
    if not process_stages or not system_id.startswith('XYZ'):
        thermal_capacity = -999  # Dead branch
    
    # Output required variable
    print(f"Result: {thermal_capacity}")

if __name__ == '__main__':
    main()