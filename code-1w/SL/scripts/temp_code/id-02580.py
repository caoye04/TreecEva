from collections import defaultdict
import math

def analyze_wave_interactions(wave_data):
    # Initialize structures
    frequency_count = defaultdict(int)
    phase_accumulator = []
    temp_magnitude_store = []

    # Process raw wave data
    for idx, (freq, phase, mag) in enumerate(wave_data):
        if freq > 0:
            frequency_count[freq] += 1
            adjusted_phase = (phase + idx * 0.1) % (2 * math.pi)
            phase_accumulator.append(adjusted_phase)
            
            # Distractor: magnitude processed but not used in final result
            normalized_mag = mag / (max(1, math.log(mag + 1)))
            temp_magnitude_store.append(normalized_mag * 0.9)

    # Compute dominant frequency (not directly used but looks important)
    dominant_freq = max(frequency_count, key=lambda k: frequency_count[k]) if frequency_count else 1

    # Simulate interference envelope (distractor computation)
    envelope = 0
    for i in range(len(phase_accumulator) - 1):
        envelope += abs(phase_accumulator[i+1] - phase_accumulator[i])
    envelope /= len(phase_accumulator) if phase_accumulator else 1

    # Core logic: calculate net phase shift from odd-indexed components
    relevant_phases = [p for i, p in enumerate(phase_accumulator) if i % 2 == 1]
    if not relevant_phases:
        net_phase_shift = 0.0
    else:
        net_phase_shift = sum(relevant_phases) / len(relevant_phases)

    # Additional red herring: transform envelope with unused function
    def decay_envelope(x, steps=10):
        for _ in range(steps):
            x = x * 0.95 + 0.01
        return x
    
    # Irrelevant recursive call that doesn't affect output
    _ = decay_envelope(envelope, len(temp_magnitude_store) if temp_magnitude_store else 5)

    return net_phase_shift


def calculate_interference_pattern(freqs, phasess):
    # Combine inputs into wave data format
    wave_entries = []
    for f, p in zip(freqs, phasess):
        entry = (f, p, f * 10)  # third element is dummy magnitude
        wave_entries.append(entry)
    
    result = analyze_wave_interactions(wave_entries)
    return result

# Input data
frequencies = [440, 880, 220, 660, 330]
phases = [math.pi/6, math.pi/3, math.pi/2, 2*math.pi/3, 5*math.pi/6]

# Execute main calculation
net_phase_shift = calculate_interference_pattern(frequencies, phases)

print(f"Result: {net_phase_shift}")