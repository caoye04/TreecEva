import math

def analyze_spectral_peak(magnitude):
    return magnitude > 0.7

def generate_harmonic_series(base_freq, num_overtones):
    return [base_freq * (i + 1) for i in range(num_overtones)]

def calculate_interference_phase(frequencies, sequence):
    phase_accumulator = 0.0
    temp_buffer = []
    scaling_factor = 1.5
    offset_correction = 0.25
    
    # Irrelevant harmonic analysis (distractor)
    harmonics = generate_harmonic_series(220.0, 8)
    spectral_mask = [analyze_spectral_peak(abs(math.sin(h))) for h in harmonics]
    
    # Actual relevant computation begins
    filtered_sequence = [x for x in sequence if x % 2 == 1]  # Keep only odd values
    
    # Misleading normalization (not used later)
    normalized_seq = [(x - min(filtered_sequence)) / (max(filtered_sequence) - min(filtered_sequence) + 1e-8) for x in filtered_sequence]
    
    weighted_phases = []
    for i, freq in enumerate(frequencies):
        # Compute phase shift using modular arithmetic and trigonometric basis
        angle = (freq * 360 * 0.001) % 360
        radians = math.radians(angle)
        contribution = math.cos(radians) * math.sin(radians)
        weighted_phases.append(contribution * (i + 1))
    
    # Use lambda with zip to pair indices and weights
    index_weight_pairs = list(enumerate(zip(weighted_phases, filtered_sequence)))
    
    # Real accumulation happens here
    for idx, (wp, seq_val) in index_weight_pairs:
        if seq_val > 5:
            phase_accumulator += wp * 1.2
        else:
            phase_accumulator -= wp * 0.8

    # Redundant buffer operations (distractor)
    temp_buffer.extend(weighted_phases)
    temp_buffer = [x for x in temp_buffer if x != 0]
    temp_buffer.reverse()

    # Final adjustment using slicing of filtered_sequence
    if len(filtered_sequence) > 3:
        slice_sum = sum(filtered_sequence[1:4])
        phase_accumulator += (slice_sum % 7) * 0.1

    return round(phase_accumulator, 4)

# Main execution context
frequency_profile = [440.0, 880.0, 1320.0, 1760.0]
modulation_sequence = [3, 7, 2, 9, 4, 6]

# Dead code path (never called)
def unused_diagnostic_report():
    return {"status": "idle", "errors": []}

# Spurious variable assignments (irrelevant)
baseline_offset = 0.003
reference_table = {k: v for k, v in enumerate(['A','B','C'])}
redundant_calc = sum([x**2 for x in range(5)]) // 2

net_phase_shift = calculate_interference_phase(frequency_profile, modulation_sequence)
print(f"Result: {net_phase_shift}")