def analyze_system_performance():
    components = ['sensor', 'actuator', 'controller', 'transmitter']
    status_codes = [1, 1, 0, 1]
    readings = [23.5, 45.1, 19.8, 30.2]
    
    # Irrelevant transformation
    processed_readings = [round(r ** 0.5, 2) for r in readings]
    
    # Tracking active subsystems
    active_subsystems = 0
    subsystem_outputs = []
    for i, code in enumerate(status_codes):
        if code == 1:
            active_subsystems += 1
            subsystem_outputs.append(readings[i] * 1.2)

    # Distractor: unused computation on names
    name_lengths = [len(name) for name in components]
    avg_length = sum(name_lengths) / len(name_lengths)

    # Real data path
    total_output = sum(subsystem_outputs)
    cycle_time = 12.5
    processor_count = 3
    
    # Key state tracking
    system_states = list(zip(components, status_codes, readings))
    stable_systems = 0
    for comp, st, val in system_states:
        if st == 1 and val > 20:
            stable_systems += 1

    # Secondary distractor: case conversion chain
    upper_names = [c.upper() for c in components]
    flipped = [name.lower().swapcase() for name in upper_names]
    
    # Critical calculation
    efficiency_score = total_output / (cycle_time * processor_count)
    
    # Additional red herring
    derived_metrics = []
    for idx, (comp, out) in enumerate(zip(components, subsystem_outputs)):
        if idx % 2 == 0:
            derived_metrics.append(out * idx)

    return efficiency_score

result = analyze_system_performance()
print(f"Result: {result}")