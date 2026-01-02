import itertools

# Simulated quantum pulse calibration system
def generate_pulse_profile(duration, harmonics):
    profile = []
    for i in range(duration):
        val = 0
        for h in harmonics:
            val += (i % h) ** 2
        profile.append(val)
    return profile

# Irrelevant helper - decoy function
def analyze_coherence(data):
    total = 0
    for x in data:
        if x > 5:
            total += x * 0.1
    return round(total, 3)

# Real transformation core
def apply_phase_shift(seq, shift):
    shifted = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            shifted.append(val + shift)
        else:
            shifted.append(val - shift)
    return shifted

# Misleading normalization path - dead end
def normalize_signal(signal):
    max_val = max(signal)
    if max_val == 0:
        return signal
    return [s / max_val for s in signal]

# Key transformation logic
def aggregate_transform(sequence, mapping):
    mapped = [mapping.get(x % 7, x * 2) for x in sequence]
    filtered = [x for x in mapped if x % 3 != 0]
    
    # Apply phase shift with dynamic parameter
    dynamic_shift = len(filtered) % 11
    phased = apply_phase_shift(filtered, dynamic_shift)
    
    # Red herring: coherence analysis (not used in final result)
    _ = analyze_coherence(phased)
    
    # Actual reduction
    running_total = 0
    for idx, val in enumerate(phased):
        if idx % 3 == 0 and val > 0:
            running_total += val // 2
        elif idx % 4 == 0:
            running_total -= val % 5
    return running_total

# Unused but plausible-looking calibration routine
def calibrate_resonance(peaks):
    return [p * 1.05 for p in peaks if p < 50]

# Main execution block
if __name__ == "__main__":
    # Experimental parameters
    duration_ns = 17
    harmonic_modes = [3, 4, 6]
    
    # Generate primary data
    pulse_sequence = generate_pulse_profile(duration_ns, harmonic_modes)
    
    # Decoy data structure
    resonance_peaks = [12, 18, 23, 31, 44]
    calibrated_peaks = calibrate_resonance(resonance_peaks)  # Dead code path
    
    # Real mapping for transformation
    calibration_map = {0: 7, 1: 14, 2: 21, 3: 5, 4: 19, 5: 8, 6: 11}
    
    # Irrelevant statistical summary
    avg_pulse = sum(pulse_sequence) / len(pulse_sequence)
    pulse_variance = sum((x - avg_pulse) ** 2 for x in pulse_sequence) / len(pulse_sequence)
    
    # Core computation with distractors
    temp_buffer = []
    for p in pulse_sequence:
        temp_buffer.append(p * 2 + 1)
    
    # Normalization not actually used
    normalized_temp = normalize_signal(temp_buffer)
    
    # Critical statement
    final_flux = aggregate_transform(pulse_sequence, calibration_map)
    
    # Additional distraction: unused product calculation
    cartesian_pairs = list(itertools.product([1, 2], [3, 4]))
    pair_sum = sum(a + b for a, b in cartesian_pairs)
    
    # Lambda-based filter - looks important but unused
    high_pass = list(filter(lambda x: x > 15, pulse_sequence))
    
    print(f"Result: {final_flux}")