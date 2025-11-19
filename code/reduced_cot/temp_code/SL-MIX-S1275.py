import math
from itertools import permutations
from functools import reduce

def compute_spectral_features(band_powers):
    # Normalize band powers to probabilities
    total_power = sum(band_powers)
    probabilities = [p / total_power for p in band_powers]
    
    # Compute Shannon entropy with logarithm base 2
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return entropy

# Frequency band power measurements (in microvolts^2)
frequency_bands = [2.3, 5.1, 3.7, 8.2, 1.9]

# Generate all possible 3-band combinations from the 5 bands
band_combinations = list(permutations(frequency_bands, 3))

# Apply spectral feature computation to each combination
entropy_values = list(map(compute_spectral_features, band_combinations))

# Calculate exponential weighting factor
weighting_factor = math.exp(0.1 * len(entropy_values))

# Apply weighted aggregation using reduce
weighted_entropy_sum = reduce(lambda acc, e: acc + e * weighting_factor, entropy_values, 0)

# Compute final spectral complexity index
spectral_complexity_index = round(weighted_entropy_sum / math.log(len(band_combinations) + 1), 2)

print(f"Result: {spectral_complexity_index}")