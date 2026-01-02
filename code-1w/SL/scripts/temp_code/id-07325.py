def analyze_system_throughput():
    base_levels = [12, 15, 8, 23, 7]
    thresholds = {5, 10, 15, 20}
    adjustment_factor = 3
    temporal_weights = [0.8, 1.2, 0.9, 1.1, 1.0]
    
    cumulative_impact = 0
    transient_buffer = []
    
    for i, (idx, level) in enumerate(zip(range(len(base_levels)), base_levels)):
        weighted_value = int(level * temporal_weights[i])
        if weighted_value > 10:
            weighted_value -= adjustment_factor
        
        # Irrelevant tracking (distractor)
        if idx % 2 == 0:
            transient_buffer.append(weighted_value * 0.5)
        
        is_critical = weighted_value in thresholds
        safety_margin = 2 if is_critical else 1
        
        # Core computation branch
        if level < 10:
            level = level ** 2 + adjustment_factor
        else:
            level += adjustment_factor

        cumulative_impact += level * safety_margin
    
    # Secondary processing with set operations
    unique_contributions = set()
    for val in base_levels:
        transformed = val ^ adjustment_factor
        unique_contributions.add(transformed)
    
    # Dummy loop with no effect on final result
    temp_sum = 0
    for _ in range(3):
        temp_sum += len(transient_buffer)  # Dead-end computation

    # Key computational chain
    adjusted_flow = cumulative_impact % 256
    phase_shift = len(unique_contributions) << 2
    normalization_offset = sum(temporal_weights) // len(temporal_weights)
    
    # Final assignment with bitwise XOR
    final_flux = adjusted_flow ^ phase_shift
    
    # Extraneous variable (distraction)
    diagnostic_trace = [cumulative_impact, adjusted_flow, phase_shift, normalization_offset]
    
    print(f"Result: {final_flux}")

analyze_system_throughput()