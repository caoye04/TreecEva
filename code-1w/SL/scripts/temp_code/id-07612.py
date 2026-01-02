import itertools

# Simulate wave interference patterns from two sources with harmonic frequencies

def generate_wave_sequence(base_freq, duration, damping=1.0):
    return [damping * (i ** 0.5) * (base_freq * i % 7) for i in range(1, duration + 1)]


def apply_filter(sequence, kernel_size=3):
    smoothed = []
    for i in range(len(sequence)):
        if i < kernel_size // 2 or i >= len(sequence) - kernel_size // 2:
            smoothed.append(sequence[i] // 2)
        else:
            window = sequence[i - kernel_size // 2:i + kernel_size // 2 + 1]
            smoothed.append(sum(window) // len(window))
    return smoothed

# Irrelevant helper: computes amplitude statistics (not used in final result)
def compute_amplitude_stats(seq):
    total = sum(seq)
    count = len(seq)
    avg = total / count if count else 0
    peak = max(seq, default=0)
    return {'total': total, 'average': avg, 'peak': peak}

# Core logic: determine phase coherence between two filtered sequences
def calculate_interference(seq1, seq2):
    truncated_len = min(len(seq1), len(seq2))
    seq1, seq2 = seq1[:truncated_len], seq2[:truncated_len]
    
    # Compute element-wise product and sum to detect constructive/destructive interference
    interference_signal = [a * b for a, b in zip(seq1, seq2)]
    raw_sum = sum(interference_signal)
    
    # Apply normalization based on combined energy
    energy1 = sum(x * x for x in seq1)
    energy2 = sum(y * y for y in seq2)
    combined_energy = (energy1 + energy2) or 1
    
    normalized_score = raw_sum / combined_energy
    
    # Final phase shift metric: scaled by harmonic offset factor
    harmonic_offset = abs(seq1[0] - seq2[0]) + 1
    return int(normalized_score * harmonic_offset * 10)

# Setup simulation parameters
freq_a, freq_b = 3, 5
duration = 12
damping_factor = 0.9

# Generate raw waveforms
raw_pattern_a = generate_wave_sequence(freq_a, duration)
raw_pattern_b = generate_wave_sequence(freq_b, duration)

# Apply noise filtering (relevant)
pattern_a = apply_filter(raw_pattern_a, kernel_size=3)
pattern_b = apply_filter(raw_pattern_b, kernel_size=3)

# Dead code path - misleading analysis branch (distraction)
if sum(pattern_a) > sum(pattern_b):
    significance_flag = True
    temp_analysis = [x * 1.5 for x in pattern_a]  # unused
    baseline_deviation = sum(temp_analysis) / len(temp_analysis)  # unused
else:
    significance_flag = False
    dummy_cache = {i: val for i, val in enumerate(pattern_b)}  # dead assignment

# Compute side metrics (irrelevant)
amplitude_info_a = compute_amplitude_stats(pattern_a)
amplitude_info_b = compute_amplitude_stats(pattern_b)

efficiency_ratio = (amplitude_info_a['average'] + 1) / (amplitude_info_b['average'] + 1)
scaling_hint = efficiency_ratio > 0.8

# Key statement: calculate net phase shift from interference
net_phase_shift = calculate_interference(pattern_a, pattern_b)

# Print result for evaluation
print(f"Result: {net_phase_shift}")