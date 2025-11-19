import itertools

def decode_dna(encoded_seq):
    mapping = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(mapping[nuc] for nuc in encoded_seq[::-1])

def calculate_codon_scores(dna_seq):
    # Simplified amino acid property scores
    codon_map = {
        'ATG': 8, 'TTT': 2, 'TTC': 2, 'TTA': 3, 'TTG': 3,
        'CTT': 4, 'CTC': 4, 'CTA': 4, 'CTG': 4, 'ATT': 5,
        'ATC': 5, 'ATA': 5, 'GTT': 6, 'GTC': 6, 'GTA': 6,
        'GTG': 6, 'TCT': 1, 'TCC': 1, 'TCA': 1, 'TCG': 1
    }
    
    scores = []
    for i in range(0, len(dna_seq) - 2, 3):
        codon = dna_seq[i:i+3]
        scores.append(codon_map.get(codon, 0))
    
    return scores

def max_subarray_sum(scores):
    max_ending_here = max_so_far = scores[0]
    for score in scores[1:]:
        max_ending_here = max(score, max_ending_here + score)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# Encoded DNA sequence from lab data
encoded_dna_sequence = "TCGAGTCAATGGCT"

# Process the sequence
original_sequence = decode_dna(encoded_dna_sequence)
codon_scores = calculate_codon_scores(original_sequence)
max_score = max_subarray_sum(codon_scores)

print(f"Result: {max_score}")