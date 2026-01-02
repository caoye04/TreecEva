def compute_system_dynamics(input_sequence):
    base_threshold = 42
    temporal_offset = 7
    accumulator = 0
    flow_registry = []
    
    for i in range(len(input_sequence)):
        if input_sequence[i] % 2 == 0:
            accumulator += input_sequence[i] // 2
        else:
            accumulator -= -(input_sequence[i] // 3)
        
        flow_registry.append(accumulator * (i + 1))

    # Irrelevant intermediate: energy mirroring (dead computation)
    mirrored_energy = [abs(x - base_threshold) for x in flow_registry if x > 50]
    normalized_set = set([x % 25 for x in mirrored_energy])
    
    # Distractor: unused transformation chain
    transformed = []
    for val in normalized_set:
        shifted = val + temporal_offset
        if shifted < 30:
            transformed.append(shifted ** 2)
    
    # Core logic resumes: slicing relevant segment
    recent_flows = flow_registry[-5:] if len(flow_registry) > 5 else flow_registry
    average_flow = sum(recent_flows) / len(recent_flows)
    
    # Adjustment based on system load
    system_load = sum(1 for x in input_sequence if x > 30)
    adjustment_factor = 1.5 if system_load > 3 else 0.8
    adjusted_flow = average_flow * adjustment_factor
    
    # Phase correction using index pattern
    indices = [i for i, x in enumerate(input_sequence) if x % 4 == 0]
    phase_shift = sum(indices[::2]) if len(indices) > 1 else len(indices)
    
    # Final computation point
    final_flux = adjusted_flow - phase_shift
    
    # Print required output
    print(f"Result: {final_flux}")

# Execute with deterministic input
input_data = [12, 45, 23, 67, 34, 29, 41, 18, 36]
compute_system_dynamics(input_data)