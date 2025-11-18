from collections import Counter
import math

def hex_to_traits(hex_code):
    # Convert hex string to integer, then to binary string
    binary_str = bin(int(hex_code, 16))[2:].zfill(16)
    # Return positions of '1' bits as trait indicators
    return [i for i, bit in enumerate(binary_str) if bit == '1']

def calculate_variance(values):
    if len(values) <= 1:
        return 0
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

def combination_count(n, r):
    if r > n or r < 0:
        return 0
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Species genetic data encoded as hex values
species_data = ['A3F1', 'B2C4', '8D1E', 'F0A5', '4C6B']

# Process each species to extract traits
all_traits = []
trait_frequencies = Counter()

for hex_code in species_data:
    traits = hex_to_traits(hex_code)
    all_traits.extend(traits)
    trait_frequencies.update(traits)

# Calculate frequency statistics
frequencies = list(trait_frequencies.values())
mean_frequency = sum(frequencies) / len(frequencies)
variance_frequency = calculate_variance(frequencies)

# Calculate combinatorial diversity score
unique_traits = len(trait_frequencies)
total_traits = len(all_traits)
combinations_score = combination_count(total_traits, unique_traits % 10)

# Compute final biodiversity index
biodiversity_index = int((mean_frequency * variance_frequency + combinations_score) / len(species_data))

print(f"Result: {biodiversity_index}")