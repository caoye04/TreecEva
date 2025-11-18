def analyze_dna_patterns(sequences):
    pattern_scores = {}
    nucleotide_pairs = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    
    for seq_id, sequence in enumerate(sequences):
        complement_seq = ''.join([nucleotide_pairs.get(nuc, 'N') for nuc in sequence])
        reverse_complement = complement_seq[::-1]
        
        palindromic_matches = 0
        for i in range(len(sequence) - 2):
            for j in range(i + 3, len(sequence) + 1):
                substring = sequence[i:j]
                if substring == reverse_complement[i:j]:
                    palindromic_matches += 1
        
        pattern_scores[seq_id] = palindromic_matches
    
    return pattern_scores

def calculate_regulatory_index(pattern_map, weight_factors):
    regulatory_index = 0
    for seq_id, matches in pattern_map.items():
        if matches > 0:
            weighted_value = matches * weight_factors.get(seq_id, 1)
            regulatory_index += weighted_value if weighted_value % 2 == 0 else -weighted_value
    return regulatory_index

# DNA sequences under analysis
chromosome_fragments = [
    "ATCGATCG",
    "GCATGCAT",
    "TTAACGTTAA",
    "CCGGCCGG"
]

# Weight factors for different sequence segments
segment_weights = {0: 2, 1: 3, 2: 1, 3: 4}

# Analysis pipeline
pattern_analysis = analyze_dna_patterns(chromosome_fragments)
regulatory_score = calculate_regulatory_index(pattern_analysis, segment_weights)
print(f"Result: {regulatory_score}")