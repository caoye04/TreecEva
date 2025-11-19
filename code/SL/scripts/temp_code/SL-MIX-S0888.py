import re
from functools import reduce

def validate_dna_sequence(func):
    def wrapper(seq):
        if not re.match(r'^[ACGT]+$', seq):
            raise ValueError('Invalid DNA sequence')
        return func(seq)
    return wrapper

@validate_dna_sequence
def process_dna(dna_seq):
    nucleotide_scores = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    base_scores = list(map(lambda nuc: nucleotide_scores[nuc], dna_seq))
    
    # Apply a transformation: square odd scores, halve even scores
    transformed_scores = list(map(lambda x: x**2 if x % 2 != 0 else x//2, base_scores))
    
    # Compute cumulative product using reduce
    cumulative_product = reduce(lambda acc, val: acc * val, transformed_scores, 1)
    
    # Extract positions where original score was prime (2 or 3)
    prime_positions = [i for i, score in enumerate(base_scores) if score in [2, 3]]
    
    # Sum transformed values at prime positions
    prime_sum = sum(transformed_scores[i] for i in prime_positions)
    
    # Final score combines both metrics
    processed_score = cumulative_product + prime_sum
    return processed_score

# Execute the pipeline
sequence = "CGTAACGT"
processed_score = process_dna(sequence)
print(f"Result: {processed_score}")