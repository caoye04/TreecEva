import math

def generate_wave_sequence(freq, phase, samples=8):
    """Generate a discrete wave sequence with given frequency and phase."""
    sequence = []
    for i in range(samples):
        value = math.sin(2 * math.pi * freq * i / samples + phase)
        sequence.append(round(value, 3))
    return sequence

def apply_mask(sequence, mask_type='hanning'):
    """Apply a windowing mask to reduce edge effects (distraction)."""
    masked = []
    n = len(sequence)
    for i in range(n):
        if mask_type == 'hanning':
            window = 0.5 * (1 - math.cos(2 * math.pi * i / (n - 1) if n > 1 else 1))
        else:
            window = 1.0
        masked.append(sequence[i] * window)
    return masked

def correlate_sequences(seq1, seq2):
    """Compute normalized correlation between two sequences."""
    if len(seq1) != len(seq2):
        return 0.0
    mean1 = sum(seq1) / len(seq1)
    mean2 = sum(seq2) / len(seq2)
    num = sum((seq1[i] - mean1) * (seq2[i] - mean2) for i in range(len(seq1)))
    den1 = math.sqrt(sum((x - mean1)**2 for x in seq1))
    den2 = math.sqrt(sum((y - mean2)**2 for y in seq2))
    if den1 == 0 or den2 == 0:
        return 0.0
    return round(num / (den1 * den2), 4)

def calculate_interference(pat1, pat2):
    """Calculate net phase shift based on interference pattern."""
    # Generate base patterns with different phases
    raw_a = generate_wave_sequence(freq=1, phase=math.pi/4, samples=8)
    raw_b = generate_wave_sequence(freq=1, phase=math.pi/3, samples=8)
    
    # Apply irrelevant masks (distractor computation)
    masked_a = apply_mask(raw_a, 'hanning')
    masked_b = apply_mask(raw_b, 'hanning')
    
    # Slice to use only central portion (relevant operation)
    core_a = masked_a[2:6]
    core_b = masked_b[2:6]
    
    # Compute correlation (semi-relevant)
    corr = correlate_sequences(core_a, core_b)
    
    # Simulate amplitude modulation (irrelevant)
    dummy_mod = []
    for i in range(len(core_a)):
        mod_val = abs(core_a[i]) * 1.5 + 0.1
        dummy_mod.append(mod_val)
    
    # Actual logic: count sign flips in difference (key reasoning step)
    diff_wave = [core_a[i] - core_b[i] for i in range(len(core_a))]
    sign_changes = 0
    for i in range(1, len(diff_wave)):
        if diff_wave[i-1] * diff_wave[i] < 0:
            sign_changes += 1
    
    # Integrate phase contributions (final answer logic)
    base_phase = math.pi / 6
    adjustment = 0
    if sign_changes >= 2:
        adjustment += math.pi / 4
    if corr > 0.6:
        adjustment -= math.pi / 8  # Partial cancellation
    
    # Net phase shift is the key output
    net_phase_shift = base_phase + adjustment
    
    # Dead code path (red herring)
    if False:
        backup = math.atan2(corr, sign_changes)
        net_phase_shift = backup
    
    return round(net_phase_shift, 4)

# Main execution
pattern_a = [0.1, 0.5, 0.8, 1.0, 0.8, 0.5, 0.1, -0.3]
pattern_b = [0.2, 0.6, 0.9, 1.1, 0.7, 0.4, 0.0, -0.4]

# Critical statement
net_phase_shift = calculate_interference(pattern_a, pattern_b)

print(f"Target result: {net_phase_shift}")