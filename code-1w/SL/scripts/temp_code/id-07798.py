def analyze_system_state(registers):
    # Irrelevant signal processing chain
    filtered_signals = [x * 0.95 for x in registers if x > 0]
    normalized = sum(filtered_signals) / len(filtered_signals) if filtered_signals else 0
    
    # Decoy quantum coherence calculation (unused)
    coherence_score = 0
    for i, val in enumerate(registers):
        if i % 3 == 0:
            coherence_score += abs(val) ** 0.5

    # Real logic starts: identify entangled states via bit patterns
    entanglement_flags = set()
    for val in registers:
        binary_rep = bin(val & 0xFFFF).count('1')  # Count set bits
        if binary_rep % 2 == 0 and val > 0:
            entanglement_flags.add(val)

    # Simulate decoherence filtering (distractor)
    decoherence_mask = {x for x in registers if bin(x).endswith('110')}
    masked_registers = [x for x in registers if x not in decoherence_mask]

    # Critical path: compute stability index from surviving entangled states
    stable_count = 0
    max_gap = 0
    sorted_flags = sorted(entanglement_flags)
    
    for i in range(1, len(sorted_flags)):
        gap = sorted_flags[i] - sorted_flags[i-1]
        if gap > max_gap:
            max_gap = gap
        if gap <= 32:
            stable_count += 1

    # Secondary diagnostic: harmonic resonance in register values
    resonance_peaks = 0
    for val in registers:
        if val > 100 and val % 17 == 0:
            resonance_peaks += 1

    # UNUSED intermediate result (red herring)
    phantom_metric = (resonance_peaks * normalized) / (coherence_score + 1e-5)

    # Final system state analysis: combine entanglement and stability
    base_score = len(entanglement_flags) * 1000
    penalty = max_gap // 10
    final_diagnostic = base_score - penalty - stable_count * 10

    # Dead code branch (never executed due to fixed input)
    if len(decoherence_mask) > 100:
        emergency_override = True
        final_diagnostic *= 0.5

    return final_diagnostic


def main():
    # Initialize quantum register states (simulated)
    quantum_registers = [
        0x1A2B, 0x3C4D, 0x5E6F, 0x7A8B, 0x9C0D,
        0x2B3C, 0x4D5E, 0x6F7A, 0x8B9C, 0x0D1E,
        0x1122, 0x3344, 0x5566, 0x7788, 0x99AA
    ]
    
    # Legacy calibration data (unused)
    calibration_map = {i: (i*1.05)**0.5 for i in range(1, 20)}
    baseline_offset = sum(calibration_map.values()) / 19
    
    # Trigger main analysis
    final_diagnostic = analyze_system_state(quantum_registers)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()