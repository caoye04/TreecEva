def simulate_quantum_transitions():
    # Initial energy states
    energy_levels = {0: 10, 1: 15, 2: 20, 3: 25}
    valid_transitions = {(0, 1), (1, 2), (2, 3), (3, 0)}
    transition_modulus = 4
    
    # State tracking
    current_state = 0
    total_energy_change = 0
    
    # Process transitions
    for step in range(7):
        next_state = (current_state + 1) % transition_modulus
        if (current_state, next_state) in valid_transitions:
            delta_energy = energy_levels[next_state] - energy_levels[current_state]
            total_energy_change += delta_energy
            current_state = next_state
        else:
            # Invalid transition resets to initial state
            current_state = 0
    
    # Calculate final balance using set operations
    stable_states = frozenset([state for state in energy_levels if energy_levels[state] % 5 == 0])
    active_states = {0, 1, 2}
    intersection_count = len(stable_states & active_states)
    
    final_energy_balance = total_energy_change * intersection_count
    return final_energy_balance

final_energy_balance = simulate_quantum_transitions()
print(f"Result: {final_energy_balance}")