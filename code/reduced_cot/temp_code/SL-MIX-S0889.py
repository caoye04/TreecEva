import re
from collections import defaultdict
import numpy as np

def process_genomic_data(dna_sequence):
    # Step 1: Initialize codon counter
    codon_counter = defaultdict(int)
    
    # Step 2: Find all codons (3-letter sequences) using regex
    codons = re.findall(r'[ATCG]{3}', dna_sequence)
    
    # Step 3: Count each codon
    for codon in codons:
        codon_counter[codon] += 1
    
    # Step 4: Apply transformation matrix to codon counts
    # Create a list of counts for transformation
    count_vector = [codon_counter['ATG'], codon_counter['TGA'], codon_counter['TAG'], codon_counter['TAA']]
    
    # Transformation matrix
    transform_matrix = np.array([
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 0, 1, 1]
    ])
    
    # Apply transformation
    transformed_counts = np.dot(transform_matrix, count_vector)
    
    # Step 5: Aggregate transformed results
    final_codon_count = int(sum(transformed_counts))
    
    return final_codon_count

# Simulated DNA sequence input
input_dna = "ATGTGATAGTAATGATGATGTGA" * 10

# Execute the pipeline
final_codon_count = process_genomic_data(input_dna)
print(f'Result: {final_codon_count}')