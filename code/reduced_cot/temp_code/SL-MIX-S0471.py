import math
from functools import reduce

def compute_gcd_list(numbers):
    return reduce(math.gcd, numbers)

# Audio channel harmonic frequencies (Hz) and energy levels
harmonic_frequencies = [110, 220, 330, 440, 550, 660, 770, 880]
energy_levels = [15, 32, 28, 45, 38, 50, 42, 55]

# Calculate minimum separation using GCD of frequencies
frequency_gcd = compute_gcd_list(harmonic_frequencies)
min_separation = frequency_gcd * 2

# Filter frequencies maintaining minimum separation
selected_indices = []
last_selected = -min_separation

for i, freq in enumerate(harmonic_frequencies):
    if freq >= last_selected + min_separation:
        selected_indices.append(i)
        last_selected = freq

# Apply greedy selection for maximum energy (non-adjacent constraint)
def max_energy_selection(energies):
    if not energies:
        return 0
    if len(energies) == 1:
        return energies[0]
    
    prev_max = energies[0]
    curr_max = max(energies[0], energies[1])
    
    for i in range(2, len(energies)):
        temp = max(curr_max, prev_max + energies[i])
        prev_max = curr_max
        curr_max = temp
    
    return curr_max

# Extract energies of separated frequencies
separated_energies = [energy_levels[i] for i in selected_indices]

# Compute maximum energy sum with non-adjacent constraint
max_energy_sum = max_energy_selection(separated_energies)

print(f"Result: {max_energy_sum}")