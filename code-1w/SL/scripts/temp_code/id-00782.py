import math

def analyze_wave_packet(frequencies, amplitudes, phases):
    # Irrelevant preprocessing: normalize amplitudes (not used in final result)
    total_amplitude = sum(amplitudes)
    normalized = [a / total_amplitude for a in amplitudes]
    
    # Misleading frequency product (dead computation)
    freq_product = 1
    for f in frequencies:
        freq_product *= f if f > 0 else 1
    
    # Real work: compute weighted phase dispersion (unused but plausible)
    dispersion = 0
    for i, p in enumerate(phases):
        dispersion += math.sin(p) * math.cos(frequencies[i])
    
    return dispersion

def calculate_interference(phases, weights):
    cumulative = 0.0
    temp_buffer = []
    
    # Simulate wave superposition with weighted phase shifts
    for i in range(len(phases)):
        shifted = phases[i] + math.pi / 4
        wrapped = shifted % (2 * math.pi)
        temp_buffer.append(wrapped)
        
        # Actual contribution to result
        weighted_component = weights[i] * math.sin(wrapped)
        cumulative += weighted_component
    
    # Red herring: buffer analysis that doesn't affect output
    buffer_variance = 0
    if len(temp_buffer) > 1:
        mean_buf = sum(temp_buffer) / len(temp_buffer)
        buffer_variance = sum((x - mean_buf)**2 for x in temp_buffer) / len(temp_buffer)
    
    # Additional distraction: attempt to correct for harmonic distortion
    correction_factor = 0
    for i in range(len(temp_buffer)):
        if temp_buffer[i] > math.pi:
            correction_factor += 0.01
    
    # Final interference calculation (only this matters)
    final = cumulative * 1.5
    return final

# Main simulation setup
frequencies = [50, 60, 100, 120]
amplitudes = [2.0, 3.5, 1.8, 4.2]
phases = [0.0, math.pi/3, math.pi/6, math.pi/2]
weights = [0.8, 1.2, 0.9, 1.5]

# Dead code: FFT simulation placeholder
signal_snapshot = [amplitudes[i] * math.sin(frequencies[i]*0.1 + phases[i]) for i in range(4)]
spectrum = signal_snapshot[::2]  # slicing operation (irrelevant)

# Trigger secondary analysis (distraction)
dispersion_metric = analyze_wave_packet(frequencies, amplitudes, phases)

# Key computation with distractors around it
baseline_offset = sum(math.cos(p) for p in phases[:3])
adjustment = len(weights) * 0.05

net_phase_shift = calculate_interference(phases, weights)

# Print required result
print(f"Result: {net_phase_shift}")