def analyze_system_metrics():
    base_frequency = 42.5
    calibration_offset = 1.73
    sample_data = [0.1, 0.3, 0.6, 0.9, 1.2]
    
    # Irrelevant signal processing chain (dead path)
    filtered_signals = []
    for s in sample_data:
        if s > 0.5:
            filtered_signals.append(s * 1.2)
    normalized = list(map(lambda x: x / sum(filtered_signals), filtered_signals))

    # Distractor: unused transformation
    transformed = [round(x ** 2 + calibration_offset, 3) for x in normalized]

    # Core quantum state simulation
    quantum_state = [0] * 8
    for i in range(len(quantum_state)):
        if i % 2 == 0:
            quantum_state[i] = (base_frequency + i) ** 0.5
        else:
            quantum_state[i] = -(base_frequency - i * 0.3)

    # Phase shift calculation with red herring intermediate
    temp_accum = 0
    for idx, val in enumerate(quantum_state):
        if val > 0:
            temp_accum += val * (idx + 1)
    phase_shift = temp_accum / 100.0
    dummy_shift = phase_shift * 0.1  # Unused

    # Stability index logic
    def calculate_stability_index(state, shift):
        magnitude = sum(abs(x) for x in state)
        peak = max(abs(x) for x in state)
        coherence = magnitude / len(state)
        adjustment_factor = 2.0 if peak > 7.0 else 1.0
        return round((coherence * adjustment_factor) - shift, 4)

    # Critical assignment
    energy_threshold = calculate_stability_index(quantum_state, phase_shift)
    
    # Additional misleading post-calculation
    if energy_threshold > 5:
        energy_threshold *= 0.8
    elif energy_threshold < 3:
        energy_threshold += 1.2
    else:
        energy_threshold = (energy_threshold + phase_shift) / 2
    
    # Final irrelevant container operation
    metadata_log = {'timestamp': 12345, 'readings': filtered_signals}
    metadata_log['status'] = 'processed' if len(transformed) > 3 else 'partial'

    print(f"Result: {energy_threshold}")

analyze_system_metrics()