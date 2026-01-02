import itertools

# Simulate wave interference patterns from two sources
def generate_wave_pattern(frequency, duration, damping=1.0):
    return [damping * (i % frequency) for i in range(duration)]


def calculate_interference(seq1, seq2):
    # Compute element-wise phase difference and interference
    phase_diffs = [(a - b) % 8 for a, b in zip(seq1, seq2)]
    interference = [abs(diff - 4) for diff in phase_diffs]  # Distance from neutral phase
    
    # Distractor: analyze symmetry (not used in final result)
    mid = len(interference) // 2
    symmetric_pairs = sum(1 for i in range(mid) if interference[i] == interference[-(i+1)])
    
    # Real computation: weighted cumulative shift
    shift_accum = 0
    for i, val in enumerate(interference):
        if i % 3 == 0:
            shift_accum += val / (i + 1)
        elif i % 5 == 0:
            shift_accum -= val

    return shift_accum

# Generate complex signal patterns
pattern_a = generate_wave_pattern(frequency=7, duration=15, damping=0.9)
pattern_b = generate_wave_pattern(frequency=5, duration=15, damping=1.1)

# Misleading intermediate analysis
overlap_regions = [i for i in range(len(pattern_a)) if pattern_a[i] == pattern_b[i]]
unique_values_a = list(set(pattern_a))
max_peak_distance = max(pattern_a) - min(pattern_b)

# Key statement
net_phase_shift = calculate_interference(pattern_a, pattern_b)

# Additional distractor: unused transformation chain
data_stream = [x * 1.5 for x in pattern_a]
filtered_stream = [x for x in data_stream if x > 3]
aggregated = sum(filtered_stream) / len(filtered_stream) if filtered_stream else 0

# Print final answer
print(f"Result: {net_phase_shift}")