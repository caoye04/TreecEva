from functools import reduce
from math import sqrt

def process_audio_signal():
    # Raw audio samples
    raw_samples = [12, -5, 8, -3, 15, -7, 9, 4, -11, 6]
    
    # Lambda for calculating energy of a sample (square of value)
    energy_func = lambda x: x * x
    
    # Apply energy calculation and noise filtering using ternary operator
    # If energy > 50, keep it; otherwise set to 0
    filtered_energies = [
        energy if (energy := energy_func(sample)) > 50 else 0 
        for sample in raw_samples
    ]
    
    # Sort energies in descending order
    sorted_energies = sorted(filtered_energies, reverse=True)
    
    # Apply normalization using list comprehension
    # Only process non-zero energies
    normalized = [
        round(energy / max(sorted_energies) * 100) 
        for energy in sorted_energies 
        if energy > 0
    ]
    
    # Calculate final signal energy as the geometric mean of top 3 normalized values
    top3 = normalized[:3] if len(normalized) >= 3 else normalized
    final_signal_energy = round(sqrt(reduce(lambda a, b: a * b, top3, 1))) if top3 else 0
    
    return final_signal_energy

final_signal_energy = process_audio_signal()
print(f"Result: {final_signal_energy}")