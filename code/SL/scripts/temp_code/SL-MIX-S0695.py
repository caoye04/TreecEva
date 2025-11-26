def initialize_quantum_system():
    quantum_register = [0b1010, 0b1100, 0b0110, 0b1001]
    noise_suppression = 4
    calibration_offset = 7
    measurement_error = 2
    
    # Main quantum state initialization
    qubit_a = (quantum_register[0] & quantum_register[1]) | (quantum_register[2] ^ quantum_register[3])
    qubit_b = ((quantum_register[1] | quantum_register[2]) ^ quantum_register[0]) & 0b1111
    
    # Quantum dynamics calculations (relevant)
    phase_shift = (qubit_a << 2) + (qubit_b >> 1)
    entanglement_factor = (quantum_register[0] % 3) + 1
    coherence_level = (qubit_a | qubit_b) + noise_suppression
    decoherence_threshold = (quantum_register[1] & 0b0111) + measurement_error
    superposition_factor = (qubit_a ^ qubit_b) - calibration_offset
    
    # Distractor calculations (irrelevant)
    thermal_noise = (quantum_register[2] * 3) // 2
    gate_fidelity = (quantum_register[3] | 0b0101) ^ measurement_error
    quantum_fluctuation = thermal_noise + gate_fidelity
    
    # Critical quantum state computation
    final_quantum_state = (qubit_a ^ qubit_b) | (phase_shift // entanglement_factor) if coherence_level > decoherence_threshold else (qubit_a & qubit_b) ^ superposition_factor
    
    # More irrelevant operations
    optimal_coupling = quantum_fluctuation % entanglement_factor
    resonance_frequency = (gate_fidelity << 1) | (thermal_noise & 0b0011)
    
    print(f"Result: {final_quantum_state}")
    return final_quantum_state

# Execute the quantum simulation
quantum_result = initialize_quantum_system()