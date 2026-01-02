import math

def generate_wave_sequence(freq, phase, length):
    # Generates a sine wave sequence; used in signal processing simulation
    return [math.sin(2 * math.pi * (i * freq + phase)) for i in range(length)]

def apply_filter(signal, threshold):
    # Applies a basic high-pass filter (distraction: not used in final logic)
    return [x if abs(x) > threshold else 0 for x in signal]

def compute_coherence(seq1, seq2):
    # Computes coherence score between two sequences (semi-relevant distractor)
    if len(seq1) != len(seq2):
        return 0.0
    dot_product = sum(a * b for a, b in zip(seq1, seq2))
    norm_a = math.sqrt(sum(a ** 2 for a in seq1))
    norm_b = math.sqrt(sum(b ** 2 for b in seq2))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)

def calculate_interference(pat1, pat2):
    # Main logic: computes net phase shift based on combinatorial alignment
    n = len(pat1)
    shifts = []
    for i in range(n):
        # Find index of pat1[i] in pat2 (assume unique elements)
        try:
            idx = pat2.index(pat1[i])
            shift = (idx - i) % n
            shifts.append(shift)
        except ValueError:
            continue
    
    # Irrelevant filtering (distractor)
    filtered_shifts = [s for s in shifts if s > 0]
    temp_sum = sum(filtered_shifts) * 0.1  # unused distraction
    
    # Key computation: weighted average of shifts using combinatorics
    total_weight = 0
    weighted_sum = 0
    for j, shift in enumerate(shifts):
        weight = math.comb(len(shifts), j) if j < len(shifts) else 1  # combinatorial weight
        weighted_sum += shift * weight
        total_weight += weight
    
    avg_shift = weighted_sum / total_weight if total_weight != 0 else 0
    
    # Final transformation: map to phase angle
    phase_angle = avg_shift * (2 * math.pi / n) if n > 0 else 0
    return round(phase_angle, 5)

# Simulation parameters (some are distractions)
duration = 1024
sample_rate = 44100
freq_a = 0.1
freq_b = 0.15
phase_a = 0.25
phase_b = 0.75
buffer_size = 512
overlap = 256

# Generate symbolic patterns based on wave zero-crossings (abstraction)
signal_a = generate_wave_sequence(freq_a, phase_a, duration)
signal_b = generate_wave_sequence(freq_b, phase_b, duration)

# Extract rising zero-crossing indices as discrete pattern markers (key preprocessing)
def get_zero_crossings(sig):
    crossings = []
    for i in range(1, len(sig)):
        if sig[i-1] < 0 <= sig[i]:
            crossings.append(i)
    return crossings[:8]  # limit to first 8 for manageable size

marker_a = get_zero_crossings(signal_a)
marker_b = get_zero_crossings(signal_b)

# Transform into relative modulo pattern (core data)
pattern_a = [m % 13 for m in marker_a]
pattern_b = [m % 13 for m in marker_b]

# Apply dummy filter (irrelevant operation)
filtered_a = apply_filter(signal_a, 0.5)
filtered_b = apply_filter(signal_b, 0.5)

# Compute coherence (red herring variable)
coherence_score = compute_coherence(signal_a, signal_b)

# Critical statement: calculate interference phase shift
net_phase_shift = calculate_interference(pattern_a, pattern_b)

# Print result as required
print(f"Result: {net_phase_shift}")