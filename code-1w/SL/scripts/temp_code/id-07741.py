import math

def generate_wave_sequence(freq, phase, length):
    return [math.sin(2 * math.pi * (i * freq + phase)) for i in range(length)]

def calculate_peak_amplitude(wave):
    return max(wave) - min(wave)

def calculate_interference(seq1, seq2):
    interference = [abs(a - b) for a, b in zip(seq1, seq2)]
    total_shift = 0
    
    # Distractor: amplitude analysis (not used in final result)
    amp1 = calculate_peak_amplitude(seq1)
    amp2 = calculate_peak_amplitude(seq2)
    avg_amplitude = (amp1 + amp2) / 2
    
    # Real logic: count phase inversions
    crossings = 0
    net_displacement = 0
    for i in range(1, len(interference)):
        if interference[i] > 0.5 != interference[i-1] > 0.5:
            crossings += 1
        net_displacement += interference[i]
    
    # Secondary distractor: frequency estimation (unused)
    estimated_freq = len([x for x in interference if x > 0.5]) / len(interference)
    
    # Core calculation: weighted phase shift
    weight_factor = 0
    for idx, val in enumerate(interference):
        if idx % 3 == 0:
            weight_factor += val * (idx + 1)
    
    # Final computation with conditional adjustment
    base_shift = weight_factor / (crossings if crossings > 0 else 1)
    adjustment = 1.5 if net_displacement > 10 else 0.8
    
    # Key assignment point
    net_phase_shift = base_shift * adjustment
    
    # Irrelevant logging computations
    log_magnitude = math.log(abs(net_phase_shift) + 1)
    normalized_score = (log_magnitude * 100) // 1
    
    return net_phase_shift

# Main execution
pattern_a = generate_wave_sequence(0.3, 0.25, 24)
pattern_b = generate_wave_sequence(0.4, 0.15, 24)

# Trigger key computation
dummy_buffer = [x * 0.9 for x in pattern_a][::2]
dummy_stats = {"count": len(dummy_buffer), "sum": sum(dummy_buffer)}

net_phase_shift = calculate_interference(pattern_a, pattern_b)

print(f"Result: {net_phase_shift}")