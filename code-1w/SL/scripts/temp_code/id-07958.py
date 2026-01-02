import math

def generate_wave_sequence(length, frequency, phase=0):
    # Creates a sinusoidal wave sequence; red herring for interference logic
    return [math.sin(2 * math.pi * frequency * (i / length) + phase) for i in range(length)]

def calculate_peak_magnitude(wave):
    # Computes max magnitude; not used in final answer but adds distraction
    return round(max(abs(val) for val in wave), 4)

def calculate_interference(seq1, seq2):
    # Core logic: counts overlapping positive peaks and computes phase difference
    overlap_count = 0
    total_offset = 0.0
    
    # Simulate signal alignment checks
    for i in range(min(len(seq1), len(seq2))):
        if seq1[i] > 0.5 and seq2[i] > 0.5:
            overlap_count += 1
            total_offset += abs(seq1[i] - seq2[i])
    
    # Distractor: irrelevant accumulation
    dummy_accumulator = 0
    for x in seq1[:10]:
        if x < 0:
            dummy_accumulator += x ** 2

    # Conditional expression with slicing - required python feature
    base_reference = seq1[len(seq1)//2:] if len(seq1) > 5 else seq1
    adjustment_factor = 1.5 if sum(base_reference) > 0 else 0.8

    # Real computation path
    avg_offset = total_offset / overlap_count if overlap_count > 0 else 0
    peak_similarity = overlap_count * adjustment_factor
    
    # Final deterministic calculation
    raw_shift = int((peak_similarity * 100) + avg_offset * 10)
    
    # Apply synthetic distortion (dead code path - never executed due to fixed input)
    if len(seq1) > 1000:
        raw_shift = int(math.sqrt(raw_shift))

    return raw_shift

# Main execution block
pattern_length = 16
freq_a, freq_b = 0.5, 0.75
phase_a, phase_b = math.pi / 4, math.pi / 3

# Generate two wave patterns (only lengths and values matter)
pattern_a = generate_wave_sequence(pattern_length, freq_a, phase_a)
pattern_b = generate_wave_sequence(pattern_length, freq_b, phase_b)

# Compute intermediate stats (distractors)
rms_a = sum(x**2 for x in pattern_a) / len(pattern_a)
peaks_b = calculate_peak_magnitude(pattern_b)

# Key statement: compute net phase shift from interference
dummy_flag = any(x < 0 for x in pattern_a[:8])
net_phase_shift = calculate_interference(pattern_a, pattern_b)

# Output result as required
print(f"Result: {net_phase_shift}")