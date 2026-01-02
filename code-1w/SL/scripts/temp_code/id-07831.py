import math

def generate_wave_sequence(length, frequency, phase=0):
    """Generates a sine wave sequence (distractor function)"""
    return [math.sin(2 * math.pi * frequency * (i / length) + phase) for i in range(length)]

def analyze_symmetry(sequence):
    """Analyzes symmetry in a sequence (partially relevant but misleading)"""
    mid = len(sequence) // 2
    left, right = sequence[:mid], sequence[-mid:]
    return sum(1 for a, b in zip(left, reversed(right)) if abs(a - b) < 0.1)

def accumulate_magnitude(peaks, decay_factor=0.9):
    """Accumulates peak magnitudes with decay (red herring)"""
    total = 0.0
    for i, peak in enumerate(peaks):
        total += peak * (decay_factor ** i)
    return total

def bit_reversed_index(index, width):
    """Returns bit-reversed index for scrambling (distractor)"""
    return int(bin(index)[2:].zfill(width)[::-1], 2)

def scramble_sequence(seq):
    """Scrambles sequence using bit-reversal (dead code path)"""
    width = (len(seq) - 1).bit_length()
    scrambled = [0] * len(seq)
    for i in range(len(seq)):
        if i < len(scrambled):
            scrambled[bit_reversed_index(i, width)] = seq[i]
    return scrambled

def calculate_interference(signal_a, signal_b):
    """Calculates net phase shift from constructive/destructive interference"""
    # Key logic begins here — real computation path
    products = [a * b for a, b in zip(signal_a, signal_b)]
    cross_zero = sum(1 for i in range(1, len(products)) if products[i-1] > 0 >= products[i])
    
    # Construct phase change indicators
    phases = []
    for x in signal_a:
        if x > 0.5:
            phases.append(1)
        elif x < -0.5:
            phases.append(-1)
        else:
            phases.append(0)
    
    # Count transitions
    transitions = 0
    for i in range(1, len(phases)):
        if phases[i] != phases[i-1]:
            transitions += 1
    
    # Use enumerate to track odd-positioned transitions
    weighted_transitions = sum(idx for idx, t in enumerate(phases) if t == 1 and idx % 2 == 1)
    
    # Core answer derivation
    base_shift = sum(products) * 100
    adjustment = transitions - weighted_transitions
    final_shift = base_shift + adjustment
    
    # Introduce conditional expression (required feature)
    scaling = 2.5 if len(signal_a) > 10 else 1.0
    scaled_result = final_shift * scaling if cross_zero > 2 else final_shift / 2
    
    # Irrelevant normalization block (distractor)
    if scaled_result != 0:
        normalized = scaled_result / max(1, abs(scaled_result) // 10)
        temp_buf = [normalized * math.cos(i) for i in range(5)]
        accumulate_magnitude(temp_buf)  # Dead call
    
    return int(scaled_result)  # Actual answer returned

# Main execution
pattern_a = [math.sin(math.pi * i / 4) for i in range(16)]
pattern_b = [math.cos(math.pi * i / 5) for i in range(16)]

# Distractor data structures
stats_summary = {
    'max_a': max(pattern_a),
    'min_b': min(pattern_b),
    'len_a': len(pattern_a),
    'symmetry_score': analyze_symmetry(pattern_a)
}

# Unused transformation (red herring)
transformed_a = scramble_sequence([int(x * 10) for x in pattern_a])
transformed_b = [x for x in pattern_b if x > 0]

# Critical statement — point of interest
net_phase_shift = calculate_interference(pattern_a, pattern_b)

# Print result as required
print(f"Result: {net_phase_shift}")