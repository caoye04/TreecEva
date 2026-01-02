def compute_efficiency():
    base_units = 48
    expansion_factor = 3
    cycle_time = 12.5
    overhead_penalty = 0.15
    degradation_rate = 0.02
    
    # Simulate production phases
    phase_outputs = []
    temp_buffer = 0
    for i in range(1, 6):
        if i % 2 == 0:
            temp_buffer += base_units * expansion_factor // i
        else:
            temp_buffer += base_units * (i + 1)
        
        # Apply degradation over cycles (irrelevant to final result)
        adjusted_buffer = temp_buffer * ((1 - degradation_rate) ** i)
        phase_outputs.append(int(adjusted_buffer))
    
    # Red herring: unused diagnostics
    diagnostic_codes = [f'ERR{i}{phase_outputs[i-1] % 10}' for i in range(1, len(phase_outputs)+1)]
    last_diagnostic = diagnostic_codes[-1]
    
    # Core calculation path
    total_output = sum(phase_outputs)
    peak_capacity = max(phase_outputs)
    avg_output = total_output / len(phase_outputs)
    
    # Key statement
    efficiency_score = total_output / (cycle_time * 0.95)
    
    # Dead code - never used
    if efficiency_score > 100:
        efficiency_score *= 0.9
    
    # Misleading normalization
    normalized_score = efficiency_score / (expansion_factor + 1)
    
    # Output the target variable
    print(f"Result: {efficiency_score}")
    
compute_efficiency()