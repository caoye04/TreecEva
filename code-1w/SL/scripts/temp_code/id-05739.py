import itertools

# Simulate dual-frequency signal interference in a phased array system
def generate_harmonic_sequence(base_freq, harmonics):
    return [base_freq * (i + 1) for i in range(harmonics)]

def apply_phase_modulation(signal_wave, depth=0.75):
    modulated = []
    for i, val in enumerate(signal_wave):
        modulated.append(val * (1 + depth * (i % 2)))
    return modulated

def calculate_constructive_peaks(waveform):
    # Irrelevant helper: counts peaks above mean (distractor)
    mean_val = sum(waveform) / len(waveform)
    count = 0
    for v in waveform:
        if v > mean_val:
            count += 1
    return count

def detect_coherence(sequence):
    # Misleading function: computes a red herring metric
    total = 0
    for a, b in zip(sequence, sequence[1:]):
        total += abs(a - b)
    return total / len(sequence) if sequence else 0

def calculate_interference(pat1, pat2):
    # Core logic: compute phase difference via cross-correlation peak
    max_corr = 0
    best_shift = 0
    
    # Extended logical chain with nested loops and conditions
    for shift in range(len(pat2)):
        correlation = 0
        for i in range(len(pat1)):
            j = (i + shift) % len(pat2)
            if pat1[i] > 0 and pat2[j] > 0:
                correlation += min(pat1[i], pat2[j])
            elif pat1[i] < 0 and pat2[j] < 0:
                correlation += max(pat1[i], pat2[j])
        if correlation > max_corr:
            max_corr = correlation
            best_shift = shift
    
    # Secondary transformation: map shift to phase angle
    phase_angle = 0
    for idx, val in enumerate(pat1):
        phase_angle += val * (best_shift - idx) ** 2
    
    # Final adjustment using combinatorics (relevant but obscured)
    combos = list(itertools.combinations([best_shift, len(pat1), len(pat2)], 2))
    combo_sum = sum(a * b for a, b in combos)
    
    # Actual answer derivation
    phase_angle = (phase_angle + combo_sum) % 360
    if phase_angle > 180:
        phase_angle -= 360
    
    return int(phase_angle)

# Irrelevant data structures (distractors)
data_log = {
    'timestamp': 1294875,
    'readings': [0.1, 0.3, 0.4],
    'status': 'nominal'
}

auxiliary_buffer = [0] * 10
for k in range(10):
    auxiliary_buffer[k] = k ** 3 - 2 * k

# Signal configuration (real inputs)
fundamental_a = 13
fundamental_b = 17
harmonics_count = 6

# Generate base patterns
pattern_a = generate_harmonic_sequence(fundamental_a, harmonics_count)
pattern_b = generate_harmonic_sequence(fundamental_b, harmonics_count)

# Apply real transformations
pattern_a = apply_phase_modulation(pattern_a, depth=0.6)
pattern_b = apply_phase_modulation(pattern_b, depth=0.6)

# Dead code path: never used (decoy)
if len(pattern_a) > 10:
    smoothed_a = [sum(pattern_a[i:i+3])/3 for i in range(len(pattern_a)-2)]
else:
    smoothed_a = None

# Compute coherence (irrelevant result)
coherence_score = detect_coherence(pattern_a)

# Trigger key computation
net_phase_shift = calculate_interference(pattern_a, pattern_b)

# Print final result as required
print(f"Result: {net_phase_shift}")