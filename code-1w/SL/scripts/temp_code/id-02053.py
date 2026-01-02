def compute_cyclic_shift_sum(sequence):
    base_offset = 7
    shift = sequence[-1] % 3
    segment = sequence[base_offset % len(sequence):]
    data_slice = segment if len(segment) > 0 else [0]
    
    # Irrelevant variable (minor distraction)
    temp_buffer = [x * 2 for x in sequence[:5]]
    
    offset = len(data_slice) + shift
    
    # Key computation
    result = (data_slice[1:] + data_slice[:-1])[offset % len(data_slice)]
    
    # Print final result as required
    print(f"Result: {result}")
    return result

# Input sequence with modular arithmetic properties
input_seq = [i**2 % 13 for i in range(10)]
compute_cyclic_shift_sum(input_seq)