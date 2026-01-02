import math

# Simulate signal processing with phase corrections and noise filtering
def process_frequency_bands(base_freq, harmonics):
    total_energy = 0.0
    phase_contributions = []
    temp_buffer = []

    for i, harmonic in enumerate(harmonics):
        # Compute energy contribution (irrelevant to final phase but part of distraction)
        energy = (base_freq * harmonic) ** 2 / (i + 1)
        total_energy += energy

        # Actual phase logic
        raw_phase = (base_freq * harmonic * 7) % 360
        if raw_phase > 180:
            adjusted_phase = raw_phase - 360
        else:
            adjusted_phase = raw_phase
        
        phase_contributions.append(adjusted_phase)

        # Distractor: buffer accumulation that goes unused
        temp_buffer.append((energy, raw_phase, adjusted_phase))

    # Sum relevant phases
    final_sum = sum(phase_contributions)

    # Key computation point
    net_phase_shift = final_sum % 360

    # More distractions: unrelated scaling and slicing
    scaled_buffer = temp_buffer[::2]  # Use slicing but don't affect result
    cumulative_scale = 0
    for entry in scaled_buffer:
        cumulative_scale += entry[0] * 0.01  # Irrelevant accumulation

    # Additional red herring: conditional that never triggers in practice
    if len(scaled_buffer) > 100:
        net_phase_shift -= 180

    return net_phase_shift

# Input setup
base_frequency = 13
harmonic_multiples = [1, 3, 5, 7, 9]

# Execute
result = process_frequency_bands(base_frequency, harmonic_multiples)
Target result: {result}