import math
from itertools import combinations

def calculate_signal_metrics(pulse_sequence):
    base_freq = 137.5
    transformed_pulses = [math.log2(p + 1) for p in pulse_sequence if p > 0]
    energy_sum = sum(transformed_pulses)
    
    # Early return for weak signals
    if energy_sum < 10:
        return 0
    
    # Calculate symmetry metric
    symmetry_pairs = list(combinations(transformed_pulses, 2))
    symmetry_score = sum(1 for a, b in symmetry_pairs if abs(a - b) < 0.1)
    
    # Apply modular correction based on sequence length
    correction_factor = len(pulse_sequence) % 7
    adjusted_energy = energy_sum * (1 + correction_factor / 10)
    
    # Compute preliminary coherence
    preliminary_coherence = math.pow(adjusted_energy, 1/3) + math.sqrt(symmetry_score)
    
    # Final adjustments based on signal characteristics
    match len(pulse_sequence) % 4:
        case 0:
            final_coherence_score = preliminary_coherence * 1.2
        case 1:
            final_coherence_score = preliminary_coherence - math.log(preliminary_coherence)
        case 2:
            final_coherence_score = preliminary_coherence + math.sin(preliminary_coherence)
        case _:  # case 3
            final_coherence_score = preliminary_coherence if preliminary_coherence > 5 else 0
    
    return round(final_coherence_score, 4)

# Deep space observation data
observation_data = [32, 64, 15, 128, 256, 42, 512, 96, 1024]
final_coherence_score = calculate_signal_metrics(observation_data)
print(f"Result: {final_coherence_score}")