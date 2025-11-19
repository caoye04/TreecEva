from collections import defaultdict

def calculate_wave_sequence(n_terms):
    sequence = [1]  # First term is 1
    parity_tracker = defaultdict(int)
    
    for i in range(1, n_terms):
        next_term = sum(sequence) + (i + 1)
        sequence.append(next_term)
        
        # Track parity using bit manipulation
        parity_bit = next_term & 1
        parity_tracker[parity_bit] += 1
    
    return sequence, parity_tracker

def apply_correction(seq, parity_counts):
    even_count = parity_counts[0]
    # Correction factor calculation
    if even_count > 0:
        correction_factor = (len(seq) << 2) ^ even_count  # Left shift and XOR
    else:
        correction_factor = len(seq) * 3
    return correction_factor

# Main processing
wave_sequence, parity_map = calculate_wave_sequence(12)
correction_factor = apply_correction(wave_sequence, parity_map)

print(f"Result: {correction_factor}")