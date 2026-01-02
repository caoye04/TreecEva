def preprocess_signal(data):
    # Irrelevant preprocessing with decoy math
    normalized = [x / max(data) for x in data]
    filtered = [x for x in normalized if x > 0.1]
    return [x * 128 for x in filtered]


def decoy_transformation(x):
    # Unused function - red herring
    return (x << 3) ^ 0xFF

# Simulated quantum register states (bit vectors)
quantum_registers = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0]
]

# Irrelevant calibration constants
calib_factor_a = 0.987
offset_matrix = [[0.1, 0.2], [0.3, 0.4]]
scaling_table = {i: i**2 for i in range(10)}  # Unused dict

# Signal artifact from unrelated subsystem
raw_analog_readings = [3.14, 2.71, 1.41, 0.57]
analyzed_noise = sum(preprocess_signal([10, 20, 30, 40]))  # Dead computation

# Real processing begins here
bit_weights = [8, 4, 2, 1]

# Convert each register to decimal using bit weights
register_values = []
for q in quantum_registers:
    weighted_sum = 0
    for bit, weight in zip(q, bit_weights):
        weighted_sum += bit * weight
    register_values.append(weighted_sum)

# Diagnostic thresholds
thresholds = {
    'low_power': 3,
    'optimal': 6,
    'overclocked': 10
}

# Misleading control flow with unused branches
status_flags = []
for val in register_values:
    if val < thresholds['low_power']:
        status_flags.append('ERROR')
    elif val >= thresholds['overclocked']:
        status_flags.append('WARNING')
    else:
        status_flags.append('OK')  # Only this branch is taken

# Auxiliary calculation with distraction
aggregate_entropy = 0.0
for i in range(len(register_values)):
    if i % 2 == 0:
        aggregate_entropy += register_values[i] * 0.5
    else:
        aggregate_entropy -= register_values[i] * 0.25

# Critical system health mapping (used)
health_map = {
    0: 100, 1: 90, 2: 80, 3: 70, 4: 60,
    5: 50, 6: 40, 7: 30, 8: 20, 9: 10, 10: 5
}

# Simulate fault detection
fault_counters = {'soft': 0, 'hard': 0}
for v in register_values:
    if v in health_map:
        fault_counters['soft'] += 1

# Core analysis function
def analyze_system_state(registers):
    # Bit manipulation and reduction
    totals = []
    for reg in registers:
        # Convert binary list to integer via bitwise logic
        acc = 0
        for bit in reg:
            acc = (acc << 1) | bit
        totals.append(acc)
    
    # Actual key computation
    base_score = sum(totals)
    
    # Conditional adjustment based on pattern
    adjustment = 0
    for reg in registers:
        # Check if first and last bits are both 1
        if reg[0] == 1 and reg[-1] == 1:
            adjustment += 5
    
    intermediate = base_score * 2 + adjustment
    
    # Final diagnostic computed from intermediate state
    if intermediate > 20:
        result = intermediate - 17
    else:
        result = intermediate + 13
    
    # Additional irrelevant transformation (not affecting result)
    _ = [x ** 2 for x in totals if x % 2 == 0]
    
    return result

# Execute main analysis
diagnostic_log = []
final_diagnostic = analyze_system_state(quantum_registers)
diagnostic_log.append(('FINAL', final_diagnostic))

# Print required output
print(f"Target result: {final_diagnostic}")