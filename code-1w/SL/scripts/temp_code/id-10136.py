from math import log2

def calculate_entropy(frequency, total):
    if frequency == 0:
        return 0
    probability = frequency / total
    return -probability * log2(probability)

# Simulate base composition frequencies in a DNA segment
dna_frequencies = {'A': 30, 'C': 20, 'G': 25, 'T': 25}
total_bases = sum(dna_frequencies.values())

# Calculate entropy for each nucleotide
entropies = [calculate_entropy(freq, total_bases) for freq in dna_frequencies.values()]

# Compute total information entropy
total_entropy = sum(entropies)

# Irrelevant auxiliary variable (minimal distraction)
max_frequency = max(dna_frequencies.values())

print(f"Result: {total_entropy}")