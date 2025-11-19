import re
from functools import reduce

def analyze_dna_sequence(seq):
    # Nucleotide scoring map
    scores = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    
    # Initial base score calculation using map and sum
    base_scores = list(map(lambda nuc: scores[nuc], seq))
    base_score = sum(base_scores)
    
    # Pattern correction: CG dinucleotides get +5 bonus
    cg_count = len(re.findall(r'CG', seq))
    cg_bonus = cg_count * 5
    
    # Length penalty: if sequence length > 10, subtract 3
    length_penalty = 3 if len(seq) > 10 else 0
    
    # GC content modifier: if GC content > 50%, add 7
    gc_count = seq.count('G') + seq.count('C')
    gc_content_percent = (gc_count / len(seq)) * 100 if len(seq) > 0 else 0
    gc_modifier = 7 if gc_content_percent > 50 else 0
    
    # Final score calculation with ternary operator for conditional adjustments
    adjustment = (cg_bonus - length_penalty) if cg_bonus > 0 else -length_penalty
    final_score = base_score + adjustment + gc_modifier
    
    return final_score

# Execute analysis
sequence = 'ATGCGTACGTAGCTAG'
final_score = analyze_dna_sequence(sequence)
print(f'Result: {final_score}')