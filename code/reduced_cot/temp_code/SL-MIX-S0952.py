import re
from collections import defaultdict

def calculate_protein_markers(dna_sequence):
    # Initialize DP table
    dp = defaultdict(int)
    max_score = 0
    
    # Regex patterns for important codons
    marker_patterns = [
        r'ATG',  # Start codon
        r'TAA|TAG|TGA',  # Stop codons
        r'GG[ACGT]',  # Glycine codons
        r'GCG'  # Alanine codon
    ]
    
    # Score mapping
    scores = {'ATG': 10, 'TAA': 5, 'TAG': 5, 'TGA': 5, 'GG': 8, 'GCG': 7}
    
    # Process sequence in windows of 3 (codons)
    for i in range(0, len(dna_sequence) - 2):
        codon = dna_sequence[i:i+3]
        
        # Check all patterns
        for pattern in marker_patterns:
            if re.match(pattern, codon):
                base_pattern = codon[:2] if pattern == r'GG[ACGT]' else codon
                dp[i] = max(dp[i], dp.get(i-3, 0) + scores.get(base_pattern, 3))
                max_score = max(max_score, dp[i])
                break
    
    return max_score

# DNA sequence under analysis
sequence = "ATGGGCTAGGCCTAAGCGTAG"

# Calculate marker score
marker_analysis_result = calculate_protein_markers(sequence)
max_marker_score = marker_analysis_result + len(re.findall(r'GCG|ATG', sequence))

print(f"Result: {max_marker_score}")