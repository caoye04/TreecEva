import math

def generate_wave_sequence(freq, phase, samples=10):
    """Generate a sequence of wave values with given frequency and phase."""
    return [math.sin(2 * math.pi * freq * (i / samples) + phase) for i in range(samples)]

def calculate_peak_magnitude(wave):
    """Calculate peak magnitude of a wave (not used in final result)."""
    return max(wave) - min(wave)

def detect_dominant_frequency(signal):
    """Simulate frequency detection via simple heuristic (unused in logic)."""
    even_sum = sum(signal[i] for i in range(0, len(signal), 2))
    odd_sum = sum(signal[i] for i in range(1, len(signal), 2))
    return 'low' if abs(even_sum) > abs(odd_sum) else 'high'

def calculate_interference(seq1, seq2):
    """Compute net interference phase shift from two sequences."""
    total_offset = 0.0
    temp_accumulator = 0
    adjustment_factor = 0.5

    # Misleading initialization of irrelevant tracking variables
    coherence_score = 0.0
    instability_warning = False
    diagnostic_log = []

    # Real logic begins: compare element-wise phase differences
    for idx, (a, b) in enumerate(zip(seq1, seq2)):
        instantaneous_diff = a - b
        # Accumulate absolute difference for diagnostic purposes (semi-relevant)
        temp_accumulator += abs(instantaneous_diff)
        
        if abs(instantaneous_diff) > 0.5:
            coherence_score += 0.1
        else:
            coherence_score -= 0.05

        # Actual contribution to result: phase-like shift based on index parity
        if idx % 2 == 0:
            total_offset += math.copysign(1.0, instantaneous_diff) * adjustment_factor
        else:
            total_offset -= math.copysign(0.5, instantaneous_diff)

        # Dead code branch: never affects result
        if temp_accumulator > 100:
            instability_warning = True
            diagnostic_log.append(f'High accumulation at {idx}')

    # Final adjustment using only part of computed data
    net_shift = int(total_offset * 10)  # Scale and discretize

    # Irrelevant post-processing (distractor)
    normalized_coherence = round(coherence_score / len(seq1), 3)
    saturation_level = 'moderate' if normalized_coherence < 0.05 else 'high'

    return net_shift

# Main execution block
pattern_a = generate_wave_sequence(freq=1.5, phase=0.1)
pattern_b = generate_wave_sequence(freq=1.5, phase=0.4)

# Unused but plausible computations to increase cognitive load
baseline_rms = math.sqrt(sum(x**2 for x in pattern_a) / len(pattern_a))
signal_entropy = -sum(math.log(abs(x) + 1e-10) for x in pattern_a)

# Key computation
net_phase_shift = calculate_interference(pattern_a, pattern_b)

# Output result as required
print(f'Result: {net_phase_shift}')