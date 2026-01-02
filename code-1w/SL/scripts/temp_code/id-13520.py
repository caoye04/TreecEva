def calculate_signal_phases():
    frequencies = [2, 4, 8, 16]
    base_offset = 3
    total_phase = 0
    phase_map = {}
    
    for index, freq in enumerate(frequencies):
        cycle = freq % 7
        if cycle > 4:
            phase_shift = cycle // 2
        else:
            phase_shift = cycle + 1
        
        # Key computation step
        total_phase += phase_shift * (index + 1)
        
        # Auxiliary mapping (minimal interference)
        phase_map[freq] = phase_shift
    
    # Irrelevant secondary calculation (slight distraction)
    avg_phase = sum(phase_map.values()) / len(phase_map) if phase_map else 0
    
    print(f"Result: {total_phase}")

calculate_signal_phases()