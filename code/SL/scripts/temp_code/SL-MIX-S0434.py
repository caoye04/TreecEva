import math
from collections import defaultdict

def gaussian_window(N, sigma):
    return {n: math.exp(-0.5 * ((n - (N-1)/2) / sigma) ** 2) for n in range(N)}

def apply_gain(window_dict, gain_factor):
    return {k: v * gain_factor for k, v in window_dict.items()}

def compute_energy(window_dict):
    return sum(v**2 for v in window_dict.values())

# Signal processing pipeline
window_cache = {}
signal_segments = [128, 256, 512]
gain_schedule = [0.8, 1.2, 0.9]

processed_energies = []
for i, (segment_size, gain) in enumerate(zip(signal_segments, gain_schedule)):
    if segment_size not in window_cache:
        # Compute and cache window coefficients
        window_cache[segment_size] = gaussian_window(segment_size, segment_size/8)
    
    # Apply dynamic gain adjustment
    adjusted_window = apply_gain(window_cache[segment_size], gain)
    
    # Compute energy of processed segment
    segment_energy = compute_energy(adjusted_window)
    processed_energies.append(segment_energy)

# Calculate final energy metric
final_energy = round(sum(processed_energies) * 1000)
print(f"Result: {final_energy}")