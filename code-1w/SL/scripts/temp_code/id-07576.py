def analyze_system_stability(input_sequence):
    raw_magnitude = sum(x ** 2 for x in input_sequence)
    normalized_power = raw_magnitude ** 0.5
    
    # Distraction: irrelevant frequency analysis
    frequency_map = {}
    for x in input_sequence:
        frequency_map[x] = frequency_map.get(x, 0) + 1
    dominant_frequency = max(frequency_map.values(), default=0)
    
    threshold_ref = 10.0
    stability_flag = normalized_power < threshold_ref
    
    # Secondary distraction: phase shift simulation (unused)
    phase_shifts = [abs(input_sequence[i] - input_sequence[i-1]) for i in range(1, len(input_sequence))]
    coherence_index = sum(1 for p in phase_shifts if p < 3) / len(phase_shifts) if phase_shifts else 0
    
    baseline_reference = 42
    adjustment_factor = 1.5 if len(input_sequence) % 2 == 0 else 2.0
    
    temp_offset = 0
    for val in input_sequence:
        if val > 5:
            temp_offset += val // 3
    
    # Core logic with conditional expression
    preliminary_score = (normalized_power * adjustment_factor) - temp_offset
    final_tally = int(preliminary_score % 17)
    
    checksum_valid = sum(input_sequence) % 8 == 0
    system_rank = len([x for x in input_sequence if x % 4 == 0])
    valid_state = stability_flag and checksum_valid and (system_rank >= 2)
    
    backup_offset = (baseline_reference - len(input_sequence)) * 3
    
    equilibrium_score = final_tally if valid_state else backup_offset
    
    # Irrelevant post-processing
    decay_rate = 0.95
    projected_decay = equilibrium_score
    for _ in range(5):
        projected_decay *= decay_rate
    
    return equilibrium_score

# Execute with fixed input
data_stream = [3, 6, 2, 8, 4]
result = analyze_system_stability(data_stream)
print(f"Result: {result}")