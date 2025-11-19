from collections import defaultdict
import math

def calculate_band_energy(samples, start, end):
    if start == end:
        return samples[start] * samples[start]
    mid = (start + end) // 2
    left_energy = calculate_band_energy(samples, start, mid)
    right_energy = calculate_band_energy(samples, mid + 1, end)
    return left_energy + right_energy

def find_peak_frequency(band_energies):
    peak_index = 0
    max_energy = band_energies[0]
    for i in range(1, len(band_energies)):
        if band_energies[i] > max_energy:
            max_energy = band_energies[i]
            peak_index = i
    return peak_index

# Audio samples represented as 16-bit integers
audio_samples = [1200, -800, 1500, -1200, 950, -600, 1800, -1500]
n_samples = len(audio_samples)

# Divide frequency spectrum into 4 bands
band_ranges = [(0, 1), (2, 3), (4, 5), (6, 7)]
band_energies = []

for start, end in band_ranges:
    energy = calculate_band_energy(audio_samples, start, end)
    band_energies.append(energy)

# Find peak frequency band using binary search approach
peak_band = find_peak_frequency(band_energies)

# Apply bitwise operations for noise reduction
noise_mask = 0b1111000000000000  # Mask to filter out lower bits
filtered_samples = [sample & noise_mask for sample in audio_samples]

# Calculate total signal strength with floating point operations
raw_signal_strength = sum(abs(sample) for sample in filtered_samples)
signal_scaling_factor = math.sqrt(2.0) / len(filtered_samples)
processed_signal_strength = int(raw_signal_strength * signal_scaling_factor)

# Apply final adjustment based on peak band location
processed_signal_strength = processed_signal_strength >> peak_band

print(f"Result: {processed_signal_strength}")