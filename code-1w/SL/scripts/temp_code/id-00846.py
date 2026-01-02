def calculate_equilibrium(states):
    # Apply non-linear transformation using lambda
    transform = lambda x: (x ** 2 + 3 * x + 1) % 17
    transformed = [transform(state) for state in states]

    # Compute rolling checksum (distractor)
    checksum = 0
    for val in transformed:
        checksum = (checksum * 31 + val) % 997

    # Track frequency of high-energy states
    high_energy_count = sum(1 for t in transformed if t > 10)

    # Determine dominant parity (semi-relevant)
    even_count = sum(1 for t in transformed if t % 2 == 0)
    odd_count = len(transformed) - even_count
    dominant_parity = 1 if even_count >= odd_count else -1

    # Core logic: find equilibrium via weighted balance
    weighted_sum = sum(i * t for i, t in enumerate(transformed))
    total_energy = sum(transformed)
    
    # Simulate stabilization process (only last step matters)
    stabilized = False
    iteration = 0
    while not stabilized and iteration < 5:
        prev_weighted = weighted_sum
        weighted_sum = (weighted_sum + total_energy * dominant_parity) % 1000
        if abs(prev_weighted - weighted_sum) < 5:
            stabilized = True
        iteration += 1

    # Final adjustment based on symmetry
    mid_index = len(transformed) // 2
    left_half = transformed[:mid_index]
    right_half = transformed[-mid_index:]
    symmetry_delta = sum(abs(l - r) for l, r in zip(left_half, reversed(right_half)))

    # Irrelevant debug logging
    debug_info = {
        'states': states,
        'transformed_len': len(transformed),
        'max_value': max(transformed),
        'stabilization_iters': iteration
    }

    # Key computation
    base_score = weighted_sum * (1 + symmetry_delta % 4)
    adjustment_factor = len([x for x in states if x % 3 == 0])  # depends on original
    final_score = (base_score - adjustment_factor * 7) % 89

    # Answer variable
    equilibrium_score = final_score
    return equilibrium_score

# Initial energy states
energy_states = [5, 12, 3, 8, 1, 9, 4]

# Misleading pre-processing (dead-end path)
processed_states = [x * 2 + 1 for x in energy_states]
sorted_processed = sorted(processed_states, reverse=True)
duplicate_check = any(sorted_processed[i] == sorted_processed[i+1] 
                         for i in range(len(sorted_processed)-1))

# Actual execution point
equilibrium_score = calculate_equilibrium(energy_states)
print(f"Result: {equilibrium_score}")