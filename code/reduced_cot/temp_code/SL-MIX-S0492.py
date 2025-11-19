import math

def compute_entropy_distribution(freq_bands, weights):
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]
    entropy_sum = 0
    for i in range(len(freq_bands)):
        if freq_bands[i] > 0:
            entropy_sum += normalized_weights[i] * math.log(freq_bands[i])
    return -entropy_sum

def process_audio_segments(segment_data):
    spectral_products = []
    energy_totals = []
    for segment in segment_data:
        band_energies = segment['bands']
        band_weights = segment['weights']
        product = 1
        total_energy = 0
        for j in range(len(band_energies)):
            energy = band_energies[j]
            weight = band_weights[j]
            product *= energy ** weight
            total_energy += energy
        spectral_products.append(product)
        energy_totals.append(total_energy)
    return spectral_products, energy_totals

# Audio segment data representing frequency bands and their weights
audio_segments = [
    {'bands': [2, 4, 8], 'weights': [0.2, 0.3, 0.5]},
    {'bands': [3, 9, 27], 'weights': [0.1, 0.4, 0.5]},
    {'bands': [5, 25, 125], 'weights': [0.3, 0.3, 0.4]}
]

# Process segments to get spectral products and energy totals
products, energies = process_audio_segments(audio_segments)

# Compute entropy distribution for each segment's energy profile
entropies = []
for k in range(len(energies)):
    segment_bands = audio_segments[k]['bands']
    segment_weights = audio_segments[k]['weights']
    entropy_val = compute_entropy_distribution(segment_bands, segment_weights)
    entropies.append(entropy_val)

# Calculate the spectral flatness index using exponential weighting
spectral_flatness_index = 0
for idx in range(len(products)):
    weighted_entropy = entropies[idx] * math.exp(-idx)
    spectral_flatness_index += weighted_entropy * math.log(products[idx] + 1)

print(f"Result: {round(spectral_flatness_index, 6)}")