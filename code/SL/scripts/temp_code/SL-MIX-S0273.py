import statistics
from collections import namedtuple

# Define a nucleotide mapping
Nucleotide = namedtuple('Nucleotide', ['symbol', 'value'])

code_map = {
    'A': Nucleotide('Adenine', 0),
    'T': Nucleotide('Thymine', 1),
    'G': Nucleotide('Guanine', 2),
    'C': Nucleotide('Cytosine', 3)
}

# Encoded DNA sequence values
dna_values = [2, 1, 3, 0, 2, 3, 1]

# Calculate variance of the encoded sequence
encoded_variance = statistics.variance(dna_values)

print(f"Result: {encoded_variance}")