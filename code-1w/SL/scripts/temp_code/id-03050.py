import math

def simulate_quantum_decay(registers):
    # Irrelevant simulation function (dead path)
    for i in range(len(registers)):
        registers[i] = (registers[i] * 1.05) % 256
    return registers

def compute_entropy(data):
    # Distractor: computes something unused later
    total = sum(data)
    if total == 0:
        return 0
    entropy = 0
    for x in data:
        if x > 0:
            entropy -= (x / total) * math.log(x / total + 1e-9)
    return round(entropy, 4)

def detect_phase_inversion(pattern):
    # Another red herring function
    inverted = [255 - p for p in pattern]
    return [inv ^ 170 for inv in inverted]

def validate_coherence(state_vector, threshold=0.88):
    # Unused coherence check
    avg = sum(state_vector) / len(state_vector)
    coherent = all(abs(x - avg) < (avg * (1 - threshold)) for x in state_vector)
    return coherent

def extract_syndrome_bits(registers):
    # Extracts bit patterns from register values using bitwise analysis
    syndrome = []
    for val in registers:
        bit_count = bin(val).count('1')
        parity = bit_count % 2
        syndrome.append(parity)
    return syndrome

def apply_error_correction(syndrome, faults):
    # Corrects single-bit errors based on syndrome and fault map
    corrected = []
    for i, syn in enumerate(syndrome):
        if i < len(faults) and faults[i]:
            corrected.append(syn ^ 1)  # Flip due to detected fault
        else:
            corrected.append(syn)
    return corrected

def reconstruct_state_from_bits(bits):
    # Convert bit array back to byte-like integer representation
    value = 0
    for bit in bits:
        value = (value << 1) | bit
    return value & 255  # Clamp to 8 bits

def analyze_system_state(registers, fault_map):
    # Core logic chain embedded in distractions
    
    # Step 1: Extract syndrome bits from quantum register states
    syndrome_pattern = extract_syndrome_bits(registers)
    
    # Step 2: Apply error correction based on known fault matrix
    corrected_syndrome = apply_error_correction(syndrome_pattern, fault_map)
    
    # Step 3: Reconstruct compact state value from corrected bits
    raw_state = reconstruct_state_from_bits(corrected_syndrome)
    
    # Step 4: Transform using non-linear scaling (simulate calibration)
    calibrated = int((raw_state ** 1.5) / 10) % 1000
    
    # Step 5: Use dictionary to map calibrated value to diagnostic level
    level_map = {
        0: 100, 1: 105, 2: 110, 3: 115, 4: 120, 5: 125, 6: 130, 7: 135,
        8: 140, 9: 145, 10: 150, 11: 155, 12: 160, 13: 165, 14: 170, 15: 175,
        16: 180, 17: 185, 18: 190, 19: 195, 20: 200, 21: 205, 22: 210, 23: 215,
        24: 220, 25: 225, 26: 230, 27: 235, 28: 240, 29: 245, 30: 250, 31: 255
    }
    
    # Step 6: Map calibrated index (mod 32) to diagnostic output
    index = calibrated % 32
    base_diagnostic = level_map.get(index, 999)
    
    # Step 7: Add environmental interference factor (constant offset)
    interference_factor = 17
    enhanced_diagnostic = base_diagnostic + interference_factor
    
    # Step 8: Final adjustment using tuple unpacking and case-sensitive conversion
    flags = ('ENABLE_TRACE', 'INVERT_SIGNAL', 'CALIBRATE_OUTPUT')
    mode_flags = [f.lower().count('e') > 1 for f in flags]  # generates [True, False, True]
    
    adjustment = 0
    for idx, (flag_val, mode) in enumerate(zip(mode_flags, ['A','B','C'])):
        if flag_val:
            adjustment += idx * 3
    
    # Step 9: Final diagnostic computation
    final_diagnostic = enhanced_diagnostic - adjustment
    
    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    
    # Initialize quantum register states (simulated sensor readings)
    quantum_registers = [120, 88, 176, 44, 212]
    
    # Fault detection matrix from hardware sensors
    fault_matrix = [False, True, False, True, False]
    
    # Irrelevant pre-processing (distractor)
    processed = []
    for r in quantum_registers:
        shifted = (r >> 2) + (r << 1) & 255
        processed.append(shifted)
    
    # Compute entropy (unused result - red herring)
    entropy_metric = compute_entropy(processed)
    
    # Simulate decay (never called)
    # simulated = simulate_quantum_decay(quantum_registers[:])
    
    # Detect phase inversion (computed but not used)
    inverted_pattern = detect_phase_inversion(quantum_registers)
    
    # Validate coherence (called but result ignored)
    is_coherent = validate_coherence(inverted_pattern)
    
    # Key statement: Analyze system state to produce final diagnostic
    final_diagnostic = analyze_system_state(quantum_registers, fault_matrix)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")