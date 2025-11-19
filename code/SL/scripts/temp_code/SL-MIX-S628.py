import re
from functools import wraps

def validate_dna_sequence(func):
    @wraps(func)
    def wrapper(seq):
        if not re.match(r'^[ACGT]+$', seq):
            raise ValueError("Invalid DNA sequence")
        return func(seq)
    return wrapper

@validate_dna_sequence
def process_dna_sequence(dna_seq):
    codon_map = {}
    def count_valid_codons(sequence, index=0):
        if index >= len(sequence) - 2:
            return 0
        codon = sequence[index:index+3]
        if re.match(r'^[ACGT]{3}$', codon):
            codon_map[codon] = codon_map.get(codon, 0) + 1
            return 1 + count_valid_codons(sequence, index + 3)
        else:
            return count_valid_codons(sequence, index + 1)
    
    total_codons = count_valid_codons(dna_seq)
    # Filter codons appearing more than once
    frequent_codons = {k: v for k, v in codon_map.items() if v > 1}
    
    # Calculate sum of ASCII values of characters in frequent codons
    ascii_sum = sum(sum(ord(char) for char in codon) for codon in frequent_codons.keys())
    
    # Adjust total based on ASCII sum
    validated_codon_count = total_codons * len(frequent_codons) + ascii_sum
    return validated_codon_count

# Example DNA sequence
sequence = "ATGCGTATGCGTATG"
validated_codon_count = process_dna_sequence(sequence)
print(f"Result: {validated_codon_count}")