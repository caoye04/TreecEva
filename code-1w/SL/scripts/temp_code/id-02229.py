from itertools import cycle

# Signal processing simulation with modular arithmetic
def compute_phase_shift():
    frequency = 7
    wave_length = 12
    base_phase = 8
    shift = 0

    # Simulate signal samples using cycling indices
    indices = range(5)
    signals = [3, 1, 4, 1, 5]
    
    # Use enumerate and zip to align index with signal value
    for i, val in enumerate(zip(indices, signals)):
        idx, sig_val = val
        if sig_val % 2 == 1:
            shift += (i + 1) * frequency
    
    # Key computational step with modular arithmetic
    phase_offset = (base_phase + shift) % wave_length
    
    # Additional clean-up variable (minor interference)
    normalized = phase_offset / wave_length
    
    return phase_offset

result = compute_phase_shift()
print(f"Result: {result}")