import itertools

# Simulated quantum register diagnostics with decoy metrics
def initialize_quantum_registers():
    registers = {}
    for q in range(8):
        registers[f'q{q}'] = {
            'state': (0.707 + 0.707j) if q % 2 == 0 else (0.5 + 0.866j),
            'coherence': 95 + q * 1.5,
            'error_rate': round(0.001 / (q + 1), 6),
            'timestamp': 1623456789 + q * 100
        }
    return registers

# Irrelevant transformation: Fourier-like but unused later
def compute_fourier_snapshot(regs):
    magnitude_sum = 0.0
    for k, v in regs.items():
        mag = abs(v['state']) ** 2
        if 'q3' in k:
            mag *= 1.5
        magnitude_sum += mag * v['coherence']
    return round(magnitude_sum / len(regs), 4)

# Decoy function – looks important but not part of final path
def evaluate_error_syndrome(regs):
    syndrome_score = 0
    for reg in regs.values():
        if reg['error_rate'] < 0.0005:
            syndrome_score += 1
    return syndrome_score * 100

# Real data processing with distractors embedded
def extract_phase_signatures(regs):
    phases = []
    decoy_accumulator = 0  # Unused red herring
    for reg in regs.values():
        phase = round(reg['state'].imag / reg['state'].real, 6)
        if phase > 0.5:
            phases.append(phase * reg['coherence'])
        else:
            decoy_accumulator += phase  # Dead computation
    sorted_phases = sorted(phases, reverse=True)
    return sorted_phases[:4]  # Top 4 phase contributions

# Conditional logic chain with misleading early exit clues
def validate_calibration_sequence(regs):
    valid_count = 0
    total_coherence = 0
    for k, v in regs.items():
        if 'q6' in k or 'q7' in k:
            continue  # Skip high-noise registers
        if v['coherence'] > 96.0 and abs(v['state']) > 0.99:
            valid_count += 1
        total_coherence += v['coherence']
    avg_coh = total_coherence / len(regs)
    # Return tuple with plausible but unused second element
    return valid_count >= 4, avg_coh > 97.0

# Main analysis using itertools and dictionary reductions
def analyze_system_state(regs):
    # Extract amplitude magnitudes above threshold
    amplitudes = [abs(v['state']) for v in regs.values()]
    filtered_amps = list(filter(lambda x: x > 0.6, amplitudes))
    
    # Use itertools to generate paired coherence interactions (distractor)
    coherence_vals = [v['coherence'] for v in regs.values()]
    pair_combinations = list(itertools.combinations(coherence_vals, 2))
    interaction_total = sum(abs(a - b) for a, b in pair_combinations)  # Heavy but irrelevant
    
    # Real signal: count how many have dominant imaginary component
    imag_dominant = sum(1 for v in regs.values() if abs(v['state'].imag) > abs(v['state'].real))
    
    # Combine with phase signature from earlier
    top_phases = extract_phase_signatures(regs)
    phase_influence = sum(top_phases) / len(top_phases) if top_phases else 0
    
    # Final logic gate simulation: XOR-like behavior on binary flags
    calib_flag, stability_flag = validate_calibration_sequence(regs)
    logic_fusion = (1 if calib_flag else 0) ^ (1 if stability_flag else 0)
    
    # Actual answer derivation (non-obvious through distractions)
    diagnostic_base = imag_dominant * 1000
    diagnostic_refinement = int(phase_influence)
    final_diagnostic = diagnostic_base + diagnostic_refinement
    
    # Red herring print (not captured)
    debug_code = (interaction_total * 0.001) % 100
    
    return final_diagnostic

# Execution flow with multiple side computations
quantum_registers = initialize_quantum_registers()
current_snapshot = compute_fourier_snapshot(quantum_registers)  # Unused
syndrome_result = evaluate_error_syndrome(quantum_registers)  # Unused
system_flags = validate_calibration_sequence(quantum_registers)  # Partially used via internal logic
final_diagnostic = analyze_system_state(quantum_registers)
print(f"Result: {final_diagnostic}")