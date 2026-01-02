import math

# Simulate quantum mode interactions in a constrained lattice system
def generate_modes(base_freq, harmonics):
    modes = []
    for i in range(1, harmonics + 1):
        phase = (base_freq * i * math.pi) / 4
        amplitude = math.sin(phase) if i % 3 != 0 else math.cos(phase)
        modes.append({'index': i, 'amplitude': amplitude, 'phase': phase})
    return modes

# Misleading helper: computes decoherence but not used in final result
def calculate_decoherence(modes):
    decoherence = 0.0
    for mode in modes:
        decoherence += abs(mode['amplitude'] - mode['phase'])
    temp_correction = sum([m['amplitude'] ** 2 for m in modes])
    fake_decay = temp_correction * 0.01  # Dead computation
    return decoherence

# Core integration function with relevant logic
def integrate_phase_shifts(modes):
    shift_sum = 0.0
    adjustment_factor = 1.0
    
    # Lambda-based filtering: only even-indexed modes contribute
    is_even_index = lambda m: m['index'] % 2 == 0
    filtered_modes = list(filter(is_even_index, modes))
    
    # Auxiliary tracking (semi-relevant)
    total_amplitude = sum([m['amplitude'] for m in modes])
    unused_metric = total_amplitude * len(filtered_modes)  # Distractor
    
    # Real computation: product of adjusted phase tangents
    for mode in filtered_modes:
        shifted_phase = mode['phase'] + adjustment_factor
        shift_contribution = math.tan(shifted_phase) if math.cos(shifted_phase) != 0 else 0
        shift_sum += shift_contribution
        adjustment_factor *= 0.9  # Stateful decay affecting later terms
    
    # Final nonlinear scaling
    flux = abs(shift_sum) ** 1.5
    
    # Red herring normalization (not applied)
    fake_normalization = flux / (len(modes) or 1)
    debug_value = math.log(abs(flux) + 1)  # Irrelevant but plausible
    
    return int(flux)  # Discretized output

# Secondary recursive combinatorics (distractor)
def count_microstates(n):
    if n <= 1:
        return 1
    return count_microstates(n - 1) + n

# Main execution flow
base_frequency = 3
harmonic_count = 6

modes_list = generate_modes(base_frequency, harmonic_count)

# Dead code path: unused analysis
decoherence_level = calculate_decoherence(modes_list)
microstate_count = count_microstates(harmonic_count)

# Key statement
final_flux = integrate_phase_shifts(modes_list)

print(f"Result: {final_flux}")