def compute_efficiency():
    components = ['valve', 'pump', 'sensor', 'actuator']
    readings = [23, 45, 67, 89]
    statuses = [True, False, True, True]
    
    # Irrelevant tracking variables (distractors)
    debug_log = []
    cycle_counter = 0
    temp_buffer = []
    
    # Simulate preprocessing with zip and enumerate (some steps are misleading)
    processed = []
    for i, (comp, val) in enumerate(zip(components, readings)):
        if statuses[i]:
            adjusted = val * (i + 1)
            processed.append(adjusted)
            temp_buffer.append(f"{comp}:{adjusted}")  # unused later
        else:
            # This block runs but doesn't contribute to final answer
            debug_log.append(f"Skipped {comp} at index {i}")
    
    # Secondary computation with no impact (dead path)
    outlier_count = 0
    for val in readings:
        if val > 50:
            outlier_count += 1  # computed but unused
    
    # Core logic embedded among distractions
    base_threshold = 20
    total_output = sum(processed)  # depends on active components only
    
    # Multiple cycle simulations (only last one matters)
    for cycle in range(1, 4):
        cycle_time = 12 + (cycle * 0.5)
        if cycle == 3:  # Only third iteration affects final result
            efficiency_score = total_output / (cycle_time * 0.95)
    
    # Final red herring: conditional expression that doesn't alter anything
    status_flag = 'optimal' if efficiency_score > 100 else 'suboptimal'
    status_flag = 'verified' if len(components) == 4 else 'invalid'  # overrides previous

    print(f"Result: {efficiency_score}")

compute_efficiency()