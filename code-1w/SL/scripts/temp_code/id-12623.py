import math

# Simulated sensor array data (some relevant, some red herrings)
sensor_a = 145
sensor_b = 89
sensor_c = 23  # Unused in final calculation but looks important
sensor_d = 0   # Deliberately misleading: used in dead branch

# Auxiliary constants with plausible but irrelevant meanings
calibration_factor = 0.987
noise_threshold = 12.5
baseline_offset = -7

# Complex preprocessing chain with mixed relevance
def preprocess_sensor(x, y):
    return (x ^ y) + (x >> 2)

# Dead function - appears useful but never called
def legacy_normalization(val):
    return val // 2 if val > 0 else val * 2

# Bit manipulation lookup via dictionary - actual relevant logic
bit_flags = {
    0: lambda x: x & 1,
    1: lambda x: x & 3,
    2: lambda x: x >> 1,
    3: lambda x: x ^ 15
}

# Set-based interference: collects unused diagnostics
diagnostic_log = set()
diagnostic_log.add(sensor_a)
diagnostic_log.add(sensor_b)
diagnostic_log.add('ERROR_404')  # Misleading string entry

def generate_health_signature(n):
    # Irrelevant transformation with side effects on global set
    signature = 0
    for i in range(n % 7):
        signature ^= i * 13
        diagnostic_log.add(f'trace_{i}')  # Distractor: pollutes log
    return signature

# Conditional branch with early exit red herring
def safety_check(level):
    if level > 100:
        return False  # Looks critical but not triggered
    elif level == 89:
        return True   # This will trigger but result unused
    return level % 2 == 0

# Main evaluation logic buried in abstraction
health_metrics = []
for i in range(3):
    transformed = preprocess_sensor(sensor_a, sensor_b) + i * 5
    health_metrics.append(transformed // (i + 1) if i != 0 else transformed)

# Real computation begins here — hidden among noise
aggregate = sum(health_metrics[:2])  # Only first two matter

# Apply bit flag logic using dictionary dispatch
filtered_result = bit_flags[2](aggregate)  # Right shift by 1

# More decoy variables
system_warm = safety_check(sensor_b)
dummy_diagnostic = generate_health_signature(sensor_a)

# Core state matrix with cross-references
operational_matrix = [
    [filtered_result, sensor_b, 0],
    [sensor_a, baseline_offset, 42],  # 42 is magic number distraction
    [calibration_factor * 100, 0, 0]
]

# Critical function containing short-circuit logic and lambda use
def system_status_eval(matrix):
    row_sums = []
    for row in matrix:
        s = sum(x for x in row if isinstance(x, int) and x >= 0)  # Ignore float, negative
        row_sums.append(s)
    
    # Actual answer derived from non-obvious combination
    primary = row_sums[0]  # Depends on filtered_result and sensor_b
    secondary = row_sums[1]  # Includes sensor_a (145) and ignores offset
    
    # Final logic step: combine using bitwise and arithmetic mix
    intermediate = (primary << 1) | secondary  # Shift and OR
    if intermediate > 500:
        intermediate = int(math.sqrt(intermediate))  # Adjustment path taken
    
    # Lambda-based final modulation — only executes if condition met
    modulator = (lambda x: x + 17) if intermediate % 2 == 0 else (lambda x: x - 3)
    return modulator(intermediate)

# Execution point of interest
final_diagnostic = system_status_eval(operational_matrix)

# Output required format
print(f"Target result: {final_diagnostic}")