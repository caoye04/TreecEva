from math import log2

def calculate_entropy(freq_list):
    total = sum(freq_list)
    probabilities = [f / total for f in freq_list if f > 0]
    entropy = -sum(p * log2(p) for p in probabilities)
    return entropy

# Frequency counts of nucleotides in a DNA segment
frequencies = [120, 80, 105, 95]  # A, C, G, T counts

# Irrelevant auxiliary variable (minor distraction)
base_names = ['A', 'C', 'G', 'T']

# Key computation
total_entropy = calculate_entropy(frequencies)

Result: {total_entropy}