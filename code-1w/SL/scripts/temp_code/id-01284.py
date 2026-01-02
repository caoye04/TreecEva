def calculate_efficiency(sequence):
    base_modifier = 0.87
    adjustment_factor = 1.03
    temp_buffer = [x * base_modifier for x in sequence if x > 5]
    
    # Irrelevant transformation (distractor)
    transformed = list(map(lambda y: y ** 0.5 + 2, temp_buffer))
    avg_transformed = sum(transformed) / len(transformed) if transformed else 0
    
    # Core logic begins
    filtered = [x for x in sequence if x % 2 == 1]  # Only odd values
    shifted_values = filtered[1:] + [filtered[0]]   # Left circular shift
    pairwise_diffs = [abs(a - b) for a, b in zip(filtered, shifted_values)]
    
    # Secondary distractor: unused computation chain
    noise_accumulator = 0
    for i in range(len(temp_buffer)):
        noise_accumulator += temp_buffer[i] * (i + 1)
    noise_accumulator = round(noise_accumulator / 100, 4)
    
    # Actual efficiency calculation
    raw_score = sum(pairwise_diffs) * adjustment_factor
    scaling_offset = len(sequence) // 2
    final_score = raw_score - scaling_offset
    
    return int(final_score)

# Simulation data for thermal process steps
process_sequence = [3, 8, 5, 12, 7, 9, 4]

# Misleading pre-computations (dead code path)
dummy_analysis = {"peak": max(process_sequence), "range": min(process_sequence)}
baseline_metric = dummy_analysis["peak"] * 0.5

# Key assignment point
thermal_capacity = calculate_efficiency(process_sequence)

Result: {thermal_capacity}