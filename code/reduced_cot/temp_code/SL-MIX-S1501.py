import math
import statistics
from itertools import combinations

# Signal processing parameters
frequency_bands = [2.4, 5.8, 3.6, 4.2, 6.1, 2.9]
attenuation_factors = [0.8, 0.9, 0.7, 0.85, 0.75, 0.95]
sampling_rates = [44.1, 48.0, 96.0, 192.0, 384.0, 768.0]  # kHz

# Calculate spectral coherence index
band_pairs = list(combinations(range(len(frequency_bands)), 2))
coherence_values = []

for i, j in band_pairs:
    # Compute exponential decay factor
    decay_factor = math.exp(-abs(frequency_bands[i] - frequency_bands[j]) * 0.5)
    
    # Apply attenuation correction
    corrected_decay = decay_factor * (attenuation_factors[i] + attenuation_factors[j]) / 2
    
    # Calculate log-scaled sampling ratio
    sampling_ratio = math.log(sampling_rates[j] / sampling_rates[i])
    
    # Compute pairwise coherence
    pair_coherence = corrected_decay * abs(sampling_ratio) * math.pow(frequency_bands[i], 1/3) * math.pow(frequency_bands[j], 1/3)
    coherence_values.append(pair_coherence)

# Statistical analysis of coherence values
mean_coherence = statistics.mean(coherence_values)
variance_coherence = statistics.variance(coherence_values)

# Final spectral coherence index calculation
spectral_coherence_index = math.log10(mean_coherence + 1) * math.sqrt(variance_coherence) * len(band_pairs)

print(f"Result: {spectral_coherence_index}")