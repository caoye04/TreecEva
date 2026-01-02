def analyze_signal_pattern():
    base_signal = 237
    mask = 48
    raw_sequence = [12, 19, 47, 61, 33]
    
    # Initialize derived sequence using enumerate and bitwise transformation
    sequence = []
    for i, val in enumerate(raw_sequence):
        transformed = (val ^ i) | 10
        sequence.append(transformed)
    
    temp_offset = 0
    for j in range(len(sequence)):
        if sequence[j] > 50:
            temp_offset += j
            break
    
    index = temp_offset
    phase_shift = (base_signal ^ mask) & sequence[index]
    
    # Irrelevant tracking variable (minimal distraction)
    debug_state = f"Signal processed at index {index}"
    
    print(f"Result: {phase_shift}")

analyze_signal_pattern()