def analyze_signal_sequence(signal):
    total_cycles = 0
    phase_shift = 0
    temp_buffer = []

    for i, point in enumerate(signal):
        if point < 0:
            continue
        
        amplitude = abs(point)
        if amplitude > 3:
            phase_shift += 1
            temp_buffer.append(amplitude * 2)
        else:
            temp_buffer.append(amplitude)
        
        total_cycles += len(temp_buffer) // (i + 1)
        
        if sum(temp_buffer) > 10:
            break
            
    # Irrelevant post-processing (distractor)
    final_data = [x for x in temp_buffer if x > 1]
    scaling_factor = 1.5

    print(f"Result: {total_cycles}")

signal_input = [1, -2, 3, 4, -1, 2]
analyze_signal_sequence(signal_input)