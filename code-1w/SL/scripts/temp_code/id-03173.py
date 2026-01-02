def calculate_system_state(input_sequence):
    # Simulate sensor preprocessing with noise filtering
    filtered_data = [x for x in input_sequence if x > 0]
    
    # Irrelevant transformation: frequency harmonics (distractor)
    harmonic_sum = sum([i * val % 7 for i, val in enumerate(filtered_data)])
    normalization_offset = harmonic_sum / (len(filtered_data) + 1e-5)

    # Core state computation
    base_energy = sum(filtered_data) // len(filtered_data) if filtered_data else 0
    fluctuation_index = sum(1 for a, b in zip(filtered_data, filtered_data[1:]) if b > a)
    
    # State transition logic with conditional expression
    stability_flag = 'high' if fluctuation_index < 3 else 'low'
    adjustment_coeff = 0.1 if stability_flag == 'high' else 0.25

    # Secondary distractor: simulate dummy subsystem load
    subsystem_weights = [val ** 0.5 for val in filtered_data]
    weighted_average = sum(subsystem_weights) / len(subsystem_weights) if subsystem_weights else 0
    dummy_feedback = int(weighted_average * 1.5) & 15  # Bitwise masking (irrelevant)

    # Key computational chain
    raw_baseline = base_energy + fluctuation_index
    adjusted_base = raw_baseline * (1 - adjustment_coeff)
    
    # Correction mechanism based on pattern symmetry
    is_symmetric = filtered_data == filtered_data[::-1]
    symmetry_bonus = 1.1 if is_symmetric else 0.9
    
    # Additional red herring: time decay simulation (not used in final path)
    time_decay_chain = []
    temp = adjusted_base
    for _ in range(3):
        temp = temp * 0.95 + 0.1
        time_decay_chain.append(temp)
    
    # Final correction factor influenced by symmetry and fluctuation
    correction_factor = symmetry_bonus * (0.05 + fluctuation_index * 0.01)
    
    # Critical execution point
    final_flux = adjusted_base * (1 + correction_factor)
    
    # Output required result
    print(f"Result: {final_flux}")

# Execute with realistic input
sensor_readings = [4, 7, 2, 9, 2, 7, 4]  # Palindromic sequence to trigger symmetry
result = calculate_system_state(sensor_readings)