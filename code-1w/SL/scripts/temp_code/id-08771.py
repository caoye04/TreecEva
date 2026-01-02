import math

def analyze_spectral_efficiency(bandwidth, signal_modes):
    efficiency_map = {}
    for mode in signal_modes:
        if mode == 'QAM16':
            efficiency_map[mode] = 4.0
        elif mode == 'QPSK':
            efficiency_map[mode] = 2.0
        else:
            efficiency_map[mode] = 1.0
    return sum(efficiency_map.values()) * bandwidth

def generate_frequency_components(base_freq, harmonics):
    components = []
    for i in range(1, harmonics + 1):
        phase = (i * math.pi / 4) % (2 * math.pi)
        amplitude = 1.0 / (i ** 0.5)
        components.append((base_freq * i, amplitude, phase))
    return components

def validate_timing_sync(timing_buffer, threshold=0.05):
    drift = 0.0
    for i in range(1, len(timing_buffer)):
        drift += abs(timing_buffer[i] - timing_buffer[i-1])
    return drift < threshold

def calculate_interference_phase(profile, sequence):
    total_weight = 0.0
    net_phase = 0.0
    
    # Real computation path
    freq_components = generate_frequency_components(profile['base'], profile['harmonics'])
    mode_efficiency = analyze_spectral_efficiency(profile['bandwidth'], profile['modes'])
    
    temp_result_cache = {}  # Distractor: not used later
    redundant_counter = 0     # Distractor: dead accumulation
    
    for idx, (freq, amp, phase) in enumerate(freq_components):
        weight = amp * mode_efficiency
        total_weight += weight
        
        # Apply sequence-based modulation
        for j, bit in enumerate(sequence):
            if bit % 2 == 1:
                phase += math.sin(j * math.pi / 8)
            else:
                phase -= math.cos(j * math.pi / 8)
            redundant_counter += 1  # Irrelevant tracking
        
        adjusted_phase = phase % (2 * math.pi)
        net_phase += weight * adjusted_phase
    
    # Additional distractor block: unrelated set operations
    active_modes = set(profile['modes'])
    standard_modes = {'QAM16', 'QPSK', 'BPSK'}
    supported = active_modes & standard_modes
    deprecated = active_modes - standard_modes
    if 'BPSK' in supported:
        mode_efficiency *= 1.1  # Misleading adjustment (not used)
    
    # Final result
    if total_weight > 0:
        net_phase /= total_weight
    else:
        net_phase = 0.0
        
    return round(net_phase, 4)

# Setup inputs
frequency_profile = {
    'base': 120,
    'harmonics': 4,
    'bandwidth': 5,
    'modes': ['QAM16', 'QPSK']
}

alignment_sequence = [1, 0, 1, 1, 0]

# Key statement
net_phase_shift = calculate_interference_phase(frequency_profile, alignment_sequence)

# Print result
print(f"Result: {net_phase_shift}")