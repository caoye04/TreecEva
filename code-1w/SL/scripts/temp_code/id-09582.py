def analyze_system_stability(input_sequence):
    # Simulate multi-phase system analysis with noise filtering
    filtered_data = [x for x in input_sequence if x > 0]
    
    # Irrelevant transformation: character mapping (distractor)
    char_mapping = {i: chr(97 + (i % 26)) for i in range(len(filtered_data))}
    signature = ''.join(char_mapping.get(i, 'z') for i in range(min(len(char_mapping), 5)))
    
    # Primary computation path
    cumulative_power = 0
    activation_threshold = 7
    primary_phase = 0
    secondary_phase = 0
    temp_buffer = []
    
    for i, val in enumerate(filtered_data):
        if i % 2 == 0:
            # Even indices contribute to primary phase with exponential weighting
            contribution = (val ** 2) % 13
            primary_phase += contribution
            cumulative_power += contribution * 2
        else:
            # Odd indices affect secondary phase with bitwise modulation
            shifted = (val << 1) & 15
            secondary_phase += shifted ^ 3
            cumulative_power += shifted

        # Dead code path: never executed due to logic, but looks relevant
        if val < 0:
            temp_buffer.append(val * -1)

    # Red herring: unused statistical calculation
    avg_filtered = sum(filtered_data) / len(filtered_data) if filtered_data else 0
    variance_proxy = sum((x - avg_filtered) ** 2 for x in filtered_data) / len(filtered_data) if filtered_data else 0

    # Key statement: equilibrium score computation
    equilibrium_score = (primary_phase + secondary_phase) // activation_threshold
    
    # Unrelated string processing (uses string methods as required)
    status_tag = "stable" if equilibrium_score > 5 else "unstable"
    status_tag = status_tag.upper().replace("UN", "RE")  # String method usage

    # Output result as required
    print(f"Result: {equilibrium_score}")
    return equilibrium_score

# Execute with fixed input
result = analyze_system_stability([4, 5, 6, 7, 2, 8])