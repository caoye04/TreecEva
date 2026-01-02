import itertools

def generate_phase_shift(sequence):
    """Irrelevant function: simulates phase shifting in signal processing (dead code)"""
    return [seq * (1 + i * 0.1) for i, seq in enumerate(sequence)]

def decoy_aggregator(data):
    """Misleading function: computes a checksum that is never used"""
    return sum(d ** 2 for d in data if d % 3 == 0)

def evaluate_enthalpy(flow_rate, pressure):
    """Distraction logic: calculates enthalpy but returns a constant to mislead reasoning"""
    temp_offset = 273.15
    adjusted = flow_rate * pressure / 100
    return temp_offset + 50 if adjusted > 10 else temp_offset - 10

def calculate_thermal_response(pattern, efficiency):
    """Core function: computes thermal capacity through bit manipulation and conditional logic"""
    base_value = 0
    for i, val in enumerate(pattern):
        if i % 2 == 0:
            base_value += (val ^ i) & 7  # Bitwise XOR and mask
        else:
            base_value -= (val | (i // 2)) >> 1  # OR and right shift
    
    # Conditional expression based on efficiency thresholds
    adjustment = 150 if efficiency > 0.85 else (75 if efficiency == 0.75 else 30)
    
    # Lambda for dynamic scaling (used once)
    scale_fn = lambda x, f: round(x * f, 4)
    scaled = scale_fn(base_value + adjustment, efficiency)
    
    # Simulate sensor drift (irrelevant offset)
    drift_compensation = sum(itertools.repeat(0.001, 50))  # Adds 0.05, but not applied
    
    return int(scaled)  # Final deterministic integer result

# Main execution block with red herrings
if __name__ == "__main__":
    # Irrelevant data structures
    signal_readings = [0.1, 0.3, 0.5, 0.9, 1.2]
    fault_codes = {101: 'overheat', 205: 'flow_low', 303: 'pressure_drop'}
    calibration_matrix = [[1, 0], [0, 1]]

    # Distractor variables
    ambient_temperature = 22.5
    humidity_level = 65
    max_flow_rate = 120
    safety_margin = 0.15

    # Core input data (obscured among noise)
    logic_sequence = [5, 3, 8, 12, 7, 4, 9]
    efficiency_factor = 0.88  # Triggers +150 adjustment

    # Dead code path (never executed)
    debug_mode = False
    if debug_mode:
        print(generate_phase_shift(signal_readings))
        print(decoy_aggregator(logic_sequence))

    # Critical computation
    thermal_capacity = calculate_thermal_response(logic_sequence, efficiency_factor)

    # More distractions
    expected_load = max_flow_rate * (1 - safety_margin)
    system_status = 'nominal' if expected_load > 100 else 'degraded'

    # Output the required result
    print(f"Result: {thermal_capacity}")