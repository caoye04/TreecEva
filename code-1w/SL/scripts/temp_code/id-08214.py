from collections import defaultdict
import math

def generate_harmonic_profile(fundamental_freq, overtones):
    profile = defaultdict(float)
    total_energy = 0.0
    
    for i in range(1, overtones + 1):
        harmonic_freq = fundamental_freq * i
        amplitude = 1 / (i ** 1.5)
        phase = math.pi / (2 * i) if i % 2 == 0 else 0
        profile[harmonic_freq] = amplitude
        total_energy += amplitude ** 2
    
    # Irrelevant energy normalization (distractor)
    for freq in profile:
        profile[freq] /= math.sqrt(total_energy) if total_energy > 0 else 1
    
    return profile

def build_composite_wave(phases, amplitudes):
    # Simulate wave superposition with phase alignment
    cumulative_shift = 0.0
    peak_displacement = 0.0
    temp_buffer = []
    
    for i, (p, a) in enumerate(zip(phases, amplitudes)):
        shifted = a * math.sin(p + math.pi / 4)
        cumulative_shift += shifted
        peak_displacement = max(peak_displacement, abs(shifted))
        if i % 3 == 0:
            temp_buffer.append(cumulative_shift)
    
    # Dead computation: buffer not used later
    normalized_disp = peak_displacement / (len(phases) + 1e-8)
    
    return {'shift': cumulative_shift, 'peaks': peak_displacement}

def calculate_interference_phase(wave_data, harmonic_dict):
    base = wave_data['shift']
    correction_factor = 0.0
    phase_offset = 0.0
    dummy_counter = 0
    
    # Simulate interference from harmonic spectrum
    for freq, amp in harmonic_dict.items():
        if freq > 100:  # arbitrary filter
            correction_factor += amp * math.cos(freq * 0.01)
        if freq < 50:
            dummy_counter += 1  # red herring
    
    # Actual key computation
    phase_offset = base + 2 * correction_factor
    
    # Distractor: irrelevant conditional update
    if dummy_counter > 10:
        phase_offset *= 0.9
    
    return phase_offset

# Main execution
fundamental = 20
overtones_count = 8

# Generate harmonic content
harmonics = generate_harmonic_profile(fundamental, overtones_count)

# Create phase and amplitude arrays (semi-relevant)
phases = [math.pi / n if n > 0 else 0 for n in range(overtones_count, 0, -1)]
amplitudes = [1/(n**0.5) for n in range(1, overtones_count + 1)]

# Build composite waveform (intermediate result)
composite_wave = build_composite_wave(phases, amplitudes)

# Introduce temporary diagnostic
energy_diagnostic = sum(amplitudes) * math.log(fundamental + 1)

# Key statement
net_phase_shift = calculate_interference_phase(composite_wave, harmonics)

# Print final result
print(f"Result: {net_phase_shift}")