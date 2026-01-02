def simulate_sensor_readings(base_value, count):
    readings = []
    for i in range(count):
        temp = (base_value * (i + 1)) % 97
        if temp > 50:
            temp = temp ^ 45
        readings.append(temp)
    return readings

sensor_data = simulate_sensor_readings(37, 8)

# Irrelevant transformation chain (distractor)
encoded_tag = ''.join([chr((x + 12) % 26 + ord('a')) for x in sensor_data[:5]])
normalized_tag = encoded_tag.upper().replace('A', 'X').strip('X')
reversed_tag = normalized_tag[::-1] + "_CHK"

# Decoy function - never used but looks important
def compute_checksum(sequence):
    checksum = 0
    for val in sequence:
        checksum += val * 3
        checksum = checksum % 251
    return checksum

# Real processing begins here
filtered_diagnostics = [x for x in sensor_data if x % 4 == 0]
accumulated_offset = 0
for idx, value in enumerate(filtered_diagnostics):
    if idx % 2 == 0:
        accumulated_offset += value // 3
    else:
        accumulated_offset -= value % 7

# Simulate system state reconstruction (mixed operations)
state_vector = set()
for x in sensor_data:
    transformed = (x >> 2) + (x << 1) & 63
    state_vector.add(transformed)

# Add irrelevant set operation (distractor)
dummy_set = {x * 2 for x in state_vector if x < 30}
unused_intersection = state_vector & dummy_set

# Core logic disguised among red herrings
recovery_sequence = []
x = 1
while x < 200:
    if x % 17 == 0:
        recovery_sequence.append(x)
    x += 1

# This function actually uses multiple concepts: string, set, arithmetic, control flow
def analyze_system_fault(seq):
    fault_code = 0
    # String-based switch emulation (case conversion)
    mode_flag = 'AdJuSt'.swapcase()  # becomes 'aDjUsT'
    
    if 'Dj' in mode_flag:
        adjustment = len(mode_flag) * 2
    else:
        adjustment = -1
    
    # Bit manipulation and arithmetic mix
    for step in seq:
        if step < 50:
            fault_code += step ^ 7
        elif step < 100:
            fault_code -= step & 15
        else:
            fault_code += (step >> 3) + 2
    
    # Use of set to deduplicate intermediate values (critical path)
    intermediates = set()
    temp = abs(fault_code)
    while temp > 0:
        intermediates.add(temp % 11)
        temp = temp // 4
    
    # Final adjustment using set size and string length
    fault_code += len(intermediates) * adjustment
    
    # Dead code branch (never executed due to swapcase result)
    if mode_flag == 'ADJUST':
        fault_code = int(fault_code / 2)
    
    return fault_code

# Execution point of interest
final_diagnostic = analyze_system_fault(recovery_sequence)

# Print required output
print(f"Result: {final_diagnostic}")