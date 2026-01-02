def simulate_quantum_flux(input_sequence):
    temp_buffer = [x ** 2 + 3 * x + 1 for x in input_sequence if x % 2 == 0]
    checksum = sum(temp_buffer) % 107

    # Irrelevant quantum state mockups
    qubit_state = {i: (i ** 3) % 5 for i in range(8)}
    coherence_map = dict(zip(qubit_state.keys(), [v * 0.99 for v in qubit_state.values()]))
    decoherence_events = 0
    for k, v in coherence_map.items():
        if v < 3:
            decoherence_events += 1

    # Distractor: unused transformation
    transformed = list(map(lambda x: (x << 2) ^ 5, temp_buffer))

    # Real path begins here — subtle signal in noise
    filtered = [x for x in temp_buffer if x > 50]
    normalized = [x / checksum for x in filtered]
    return normalized


def evaluate_entanglement_metrics(data_stream):
    segments = [data_stream[i:i+3] for i in range(0, len(data_stream), 3)]
    entangled_pairs = []

    for seg in segments:
        if len(seg) == 3:
            entangled_pairs.append(sum(seg) * seg[0])

    # Dead code path — looks important but unused
    if len(entangled_pairs) > 10:
        backup = [x - 1 for x in entangled_pairs]
        return backup

    # Actual logic buried here
    scaling_factor = 0.87
    adjusted = [val * scaling_factor for val in entangled_pairs]
    return sum(adjusted) if adjusted else 0


def calculate_thermal_properties(state_vector):
    # Misleading initialization
    baseline = 1024
    offset_grid = [[i + j for j in range(4)] for i in range(4)]
    total_offset = sum(sum(row) for row in offset_grid)

    # Decoy physics calculations
    hypothetical_mass = 7.2e-5
    energy_states = [hypothetical_mass * (k ** 2) for k in range(1, 6)]
    partition_function = sum(energy_states)

    # Core logic — obscured by context
    raw_values = [state_vector[i] * (i + 1) for i in range(len(state_vector))]
    accumulated = sum(raw_values)
    correction_term = len(state_vector) ** 2

    # Final computation
    thermal_capacity = int(accumulated - correction_term + 42)
    
    # Red herring output
    diagnostics = {'capacity': thermal_capacity, 'baseline': baseline, 'total_offset': total_offset}
    
    return thermal_capacity

# Main execution flow
if __name__ == '__main__':
    # Initial data with mixed relevance
    signal_input = list(range(1, 18))
    signal_input = [x for x in signal_input if x not in {4, 8, 12, 16}]  # Filter evens

    # Step 1: Simulate quantum flux (produces normalized values)
    flux_output = simulate_quantum_flux(signal_input)

    # Step 2: Evaluate entanglement (uses flux output)
    entanglement_score = evaluate_entanglement_metrics(flux_output)

    # Step 3: Prepare equilibrium state — key input to target function
    equilibrium_state = [int(x * 100) for x in flux_output]
    equilibrium_state.append(int(entanglement_score))

    # Step 4: Critical statement — compute thermal capacity
    thermal_capacity = calculate_thermal_properties(equilibrium_state)

    # Output result as required
    print(f"Result: {thermal_capacity}")