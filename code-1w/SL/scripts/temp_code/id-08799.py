from collections import defaultdict, Counter

# Simulate signal processing with interference patterns
def analyze_harmonic_sequence(base_frequencies, harmonics):
    harmonic_power = defaultdict(float)
    total_energy = 0.0
    
    for f in base_frequencies:
        for i, h in enumerate(harmonics):
            harmonic_freq = f * h
            if harmonic_freq > 5000:
                continue
            harmonic_power[harmonic_freq] += (1 / (i + 1)) * (f / 100)
            total_energy += harmonic_power[harmonic_freq]
    
    # Misleading normalization
    normalized_power = {k: v / (total_energy + 1e-9) for k, v in harmonic_power.items()}
    return harmonic_power, normalized_power, total_energy

# Analyze phase coherence across modulated signals
def compute_coherence_metrics(signal_phases):
    phase_counts = Counter()
    coherence_score = 0
    
    for phase in signal_phases:
        rounded_phase = round(phase, 1)
        phase_counts[rounded_phase] += 1
        
        if 90.0 <= phase <= 270.0:
            coherence_score += 0.5
        else:
            coherence_score -= 0.1
    
    dominant_phase = phase_counts.most_common(1)[0][1] if phase_counts else 0
    return coherence_score, dominant_phase, len(phase_counts)

# Main interference phase calculator
def calculate_interference_phase(freqs, mods):
    shift_accumulator = 0
    temp_log = []
    
    for m in mods:
        if m % 3 == 0:
            shift_accumulator += m // 4
        elif m % 5 == 0:
            shift_accumulator -= m // 5
        
        # Dead computation - doesn't affect result
        binary_rep = bin(m).count('1')
        temp_log.append(binary_rep)
    
    # Real calculation path
    base_shift = sum(f ** 0.5 for f in freqs if f % 2 == 1)
    adjustment_factor = len([f for f in freqs if f > 100])
    
    # Distractor: complex-looking but unused structure
    freq_summary = {
        'max': max(freqs, default=0),
        'min': min(freqs, default=0),
        'range': max(freqs, default=0) - min(freqs, default=0),
        'entropy': sum((f / 100) ** 0.7 for f in freqs if f < 500)
    }
    
    # Actual key computation
    raw_phase = base_shift - adjustment_factor * 2.5 + shift_accumulator
    net_phase = raw_phase % 360
    
    # Additional red herring variables
    phantom_shift = 0
    for i in range(len(freqs)):
        if i % 2 == 0 and freqs[i] > 50:
            phantom_shift += (freqs[i] % 17) * 0.3
    
    return round(net_phase, 3)

# Simulation setup
frequency_profile = [44, 88, 132, 176, 220, 264, 308, 352]
modulation_sequence = [12, 15, 18, 25, 30, 33, 40]

# Execute analysis steps (distractors)
raw_harmonics, norm_powers, energy = analyze_harmonic_sequence(frequency_profile[:4], [1, 2, 3, 4, 5])
coherence, dominant, variety = compute_coherence_metrics([45, 90, 135, 180, 225, 270, 315])

# Key execution point
net_phase_shift = calculate_interference_phase(frequency_profile, modulation_sequence)

# Print final target result
print(f"Result: {net_phase_shift}")