from collections import defaultdict
import math

def process_genomic_data(sequence):
    codon_freq = defaultdict(int)
    tokens = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    
    # Quality filter using lambda
    quality_filter = lambda codon: 'N' not in codon and len(codon) == 3
    filtered_tokens = list(filter(quality_filter, tokens))
    
    # Frequency analysis
    for codon in filtered_tokens:
        codon_freq[codon] += 1
    
    # Positional confidence scoring
    position_weights = [math.exp(-i/10) for i in range(len(filtered_tokens))]
    cumulative_score = 0
    
    for idx, codon in enumerate(filtered_tokens):
        freq_score = codon_freq[codon] if codon_freq[codon] > 1 else 0.5
        cumulative_score += freq_score * position_weights[idx]
    
    # Final adjustment with ternary operator
    final_confidence_score = cumulative_score / len(filtered_tokens) if len(filtered_tokens) > 0 else 0
    return round(final_confidence_score, 4)

# Execution
dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
final_confidence_score = process_genomic_data(dna_sequence)
print(f"Result: {final_confidence_score}")