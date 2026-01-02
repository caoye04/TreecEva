import math

# Simulated quantum register diagnostics with extensive telemetry
def generate_telemetry_data(registers):
    telemetry = {}
    for i, r in enumerate(registers):
        noise_level = (r ** 2 + abs(r - 3)) / (i + 1.5)
        coherence = math.exp(-noise_level / 10)
        phase_drift = math.sin(r * 0.1) * coherence
        # Irrelevant telemetry fields (red herrings)
        telemetry[f'q{i}_temp'] = r * 1.2 + 5.1
        telemetry[f'q{i}_flux'] = r * 0.07 + 2.3
        telemetry[f'q{i}_coherence'] = coherence
        telemetry[f'q{i}_drift'] = phase_drift
        telemetry[f'q{i}_status'] = 'STABLE' if coherence > 0.7 else 'FLUCTUATING'
    return telemetry

# Misleading auxiliary function (dead path)
def validate_register_security(registers):
    checksum = 0
    for r in registers:
        if r % 2 == 0:
            checksum ^= (r * 3) % 256
        else:
            checksum ^= (r * 5) % 256
    security_flag = True if checksum % 7 == 0 else False
    return security_flag  # Never actually used in logic

# Decoy transformation chain
def transform_register_set(registers):
    transformed = [r * 2 + 1 for r in registers]
    shifted = [(t ^ 255) % 100 for t in transformed]  # Bit manipulation red herring
    normalized = [abs(s - 50) / 10.0 for s in shifted]
    return normalized  # Computed but not used

# Real analysis function with nested logic and dictionary operations
def analyze_system_state(registers):
    stats = {
        'amplitude_sum': 0,
        'phase_product': 1.0,
        'active_qubits': 0,
        'complexity_score': 0
    }

    # Nested conditional processing with multiple concepts
    for idx, val in enumerate(registers):
        if val > 0:
            amplitude = math.sqrt(val) if val >= 1 else val
            stats['amplitude_sum'] += amplitude

            if val % 2 == 1:
                stats['active_qubits'] += 1
                
                # Multi-level nesting with meaningful computation
                if idx > 0 and registers[idx - 1] > 2:
                    back_ref = registers[idx - 1]
                    adjustment_factor = math.log(back_ref + 1) / (idx + 1)
                    stats['complexity_score'] += adjustment_factor * val
                    
                    # Dictionary-based state tracking
                    intermediate_map = {i: math.floor(registers[i] * adjustment_factor) for i in range(len(registers))}
                    correction = sum(v for v in intermediate_map.values() if v % 3 == 0)
                    stats['phase_product'] *= (correction + 1) / 100.0

            # Conditional branch with distractor logic
            temp_accum = 0
            for j in range(3):
                temp_accum += (val + j) * (j + 1)
            # temp_accum is never used again — misleading intermediate

        elif val == 0:
            stats['phase_product'] *= 0.9

    # Secondary processing loop — appears important but only minor contribution
    decoy_sum = 0
    for k in range(len(registers)):
        if k % 2 == 0 and registers[k] != 0:
            decoy_sum += registers[k] * k
    # decoy_sum computed but not used in final result

    # Final diagnostic calculation using core accumulated values
    base_diagnostic = int(stats['amplitude_sum'] * 100)
    penalty = 10 if stats['active_qubits'] < 2 else 0
    bonus = 50 if stats['complexity_score'] > 3.0 else 0
    
    # Critical answer computation
    final_diagnostic = base_diagnostic + bonus - penalty

    # Dead code path — looks like validation but unused
    if final_diagnostic % 25 == 0:
        consistency_check = 'OPTIMAL'
    else:
        consistency_check = 'ACCEPTABLE'

    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Initialize quantum register states (simulated)
    quantum_registers = [4, 7, 0, 5, 3]

    # Generate telemetry (used to distract)
    telemetry_data = generate_telemetry_data(quantum_registers)

    # Call decoy functions — results ignored
    _ = validate_register_security(quantum_registers)
    _ = transform_register_set(quantum_registers)

    # Key statement that produces the target result
    final_diagnostic = analyze_system_state(quantum_registers)
    
    print(f"Result: {final_diagnostic}")