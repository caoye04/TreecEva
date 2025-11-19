import re
from functools import reduce

def find_palindromes(seq, length):
    if length == 0:
        return ['']
    if length == 1:
        return ['A', 'T', 'C', 'G']
    
    smaller = find_palindromes(seq, length - 2)
    result = []
    for p in smaller:
        for nuc in ['A', 'T', 'C', 'G']:
            candidate = nuc + p + nuc
            if re.match(r'^[ACGT]+$', candidate):
                result.append(candidate)
    return result

def count_matches(sequence, patterns):
    counts = {}
    for pattern in patterns:
        counts[pattern] = len(re.findall(pattern, sequence))
    return counts

# Main processing
sample_dna = "ATCGCGATCG"
palindromic_seeds = find_palindromes(sample_dna, 4)
match_counts = count_matches(sample_dna, palindromic_seeds)
filtered_counts = {k: v for k, v in match_counts.items() if v > 0}

# Calculate density using bitwise operations and arithmetic
density_components = [len(k) << v for k, v in filtered_counts.items()]
palindromeDensity = reduce(lambda x, y: x ^ y, density_components, 0) if density_components else 0

print(f"Result: {palindromeDensity}")