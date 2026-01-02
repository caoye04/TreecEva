def analyze_spectral_components(raw_frequencies, sample_rate=44100):
    normalized = [f / sample_rate for f in raw_frequencies]
    amplitudes = [abs(f * 0.5) for f in normalized]
    weighted_sum = sum(amplitudes)
    
    # Distractor: irrelevant spectral smoothing
    smoothed = []
    for i in range(len(normalized)):
        left = normalized[i-1] if i > 0 else normalized[-1]
        right = normalized[i+1] if i < len(normalized)-1 else normalized[0]
        smoothed.append((left + normalized[i] + right) / 3)
    
    return weighted_sum


def calculate_harmonic_energy(levels):
    total_energy = 0
    for idx, level in enumerate(levels):
        if idx % 2 == 0:
            total_energy += level ** 2
        else:
            total_energy -= level ** 0.5
    return total_energy


def calculate_interference_phase(signals, overtones):
    phase_accumulator = 0.0
    temp_buffer = []
    
    for i, (base, overtone) in enumerate(zip(signals, overtones)):
        harmonic_ratio = overtone / (base + 1e-8)
        if harmonic_ratio > 1.5:
            phase_step = harmonic_ratio * 0.75
        else:
            phase_step = base * 0.1
        
        # Real computation step
        phase_accumulator += phase_step * (i + 1)
        
        # Distractor: filling buffer with intermediate values not used later
        temp_buffer.append(harmonic_ratio ** 2)
        
        # Additional distraction: nested conditional with dead logic
        if i > 10:
            reset_flag = True
            temp_buffer.clear()
    
    # Another distractor: unused transformation
    inverted_phases = [1.0 / (p + 1e-5) for p in temp_buffer]
    
    return phase_accumulator

# Main execution block
if __name__ == "__main__":
    base_signals = [120, 240, 360, 480, 600]
    harmonics = [180, 250, 500, 490, 620]
    noise_floor = [0.01, 0.03, 0.02, 0.05, 0.04]
    
    # Irrelevant preprocessing chain
    adjusted_signals = []
    for s in base_signals:
        adjusted = s * 1.05
        if adjusted > 200:
            adjusted *= 0.9
        adjusted_signals.append(adjusted)
    
    # Unused helper calculation
    signal_entropy = 0
    for a in adjusted_signals:
        if a > 0:
            signal_entropy -= a * __import__('math').log(a)
    
    # Core computation
    net_phase_shift = calculate_interference_phase(base_signals, harmonics)
    
    # Secondary unrelated metric (distractor)
    avg_harmonic_deviation = sum(abs(h - b) for h, b in zip(harmonics, base_signals)) / len(base_signals)
    
    # Final output
    print(f"Result: {net_phase_shift}")