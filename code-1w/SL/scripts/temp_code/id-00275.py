import itertools

def analyze_phase_shift(registers):
    # Irrelevant analysis function (dead weight)
    total = 0
    for r in registers:
        total += sum(r) % 7
    return total * 3

def detect_entanglement(registers):
    # Misleading computation - looks important but unused
    pairs = list(itertools.combinations(range(len(registers)), 2))
    score = 0
    for i, j in pairs:
        if len(registers[i]) == len(registers[j]):
            score += (registers[i][0] ^ registers[j][-1]) & 3
    return score + 11

def filter_noise(readings):
    # Distractor: processes data not used in final result
    filtered = [x for x in readings if x > 0]
    smoothed = list(map(lambda x: round(x * 0.9), filtered))
    return smoothed[:5]

def compute_coherence_score(sequence):
    # Unused helper with complex logic to distract
    if not sequence:
        return 0
    base = sequence[0]
    acc = 0
    for val in sequence[1:]:
        acc += abs(val - base) // max(1, base)
        base = (base + val) // 2
    return acc * len(sequence)

def monitor_system_state(registers, log_entries):
    # Core logic begins here
    activation_chain = []
    for reg in registers:
        # Extract diagnostic bits using slicing and bit operations
        pivot = len(reg) // 2
        left_slice = reg[:pivot]
        right_slice = reg[pivot:]
        
        # Key computation: XOR fold on right segment
        folded = 0
        for val in right_slice:
            folded ^= (val << 1) | (val & 1)
        
        # Conditional state accumulation
        if folded > 50:
            activation_chain.append(folded % 25)
        else:
            activation_chain.append(folded + 7)
    
    # Secondary processing: find first even index where value exceeds threshold
    trigger_index = -1
    for idx, val in enumerate(activation_chain):
        if val > 20 and idx % 2 == 0:
            trigger_index = idx
            break
    
    # Final decision logic
    if trigger_index >= 0:
        result = activation_chain[trigger_index] * 2
    else:
        result = sum(activation_chain) // max(1, len(activation_chain))
    
    # Irrelevant post-processing (distractor)
    checksum = 0
    for entry in log_entries:
        if 'ERROR' in entry:
            checksum += len(entry) % 13
    anomaly_mask = (checksum ^ 0xAA) & 0xFF
    
    # Dead code path - never executed due to structure
    if False and anomaly_mask > 100:
        backup_recovery = [anomaly_mask >> i for i in range(4)]
        result = sum(backup_recovery)
    
    # Final output
    return result

# System initialization (with red herrings)
quantum_registers = [
    [12, 18, 24, 30],
    [10, 15],
    [8, 16, 32, 64, 128],
    [5, 25]
]

sensor_readings = [101, -5, 203, 0, 155, 87]
error_log = [
    'ERR_INIT_7',
    'ERROR_CRITICAL_X9',
    'STATUS_OK',
    'ERROR_SYNC_FAIL'
]

# Noise filtering (irrelevant to final result)
denoised = filter_noise(sensor_readings)

# Unused coherence metrics
coherence = compute_coherence_score(sensor_readings)

# Phantom analysis calls (no side effects)
phase_total = analyze_phase_shift(quantum_registers)
entanglement_score = detect_entanglement(quantum_registers)

# Critical execution point
final_diagnostic = monitor_system_state(quantum_registers, error_log)

# Output result as required
print(f"Result: {final_diagnostic}")