import re
from functools import reduce

def is_genomic_palindrome(segment):
    return segment == segment[::-1] and len(segment) >= 3

def extract_valid_segments(dna_sequence):
    pattern = r'[ACGT]{3,}'
    return re.findall(pattern, dna_sequence)

def count_with_backtrack(segments):
    if not segments:
        return 0
    current_segment = segments[0]
    remaining_segments = segments[1:]
    
    palindrome_match = 1 if is_genomic_palindrome(current_segment) else 0
    
    if len(remaining_segments) > 0:
        return palindrome_match + count_with_backtrack(remaining_segments)
    else:
        return palindrome_match

gene_sequence = "ATGCCGTAATGCATCGATCGGCTAGCTAGCTTACGGCGGCGGCGCGATCGATCGATCG"

segment_pool = extract_valid_segments(gene_sequence)
filtered_pool = list(filter(lambda x: len(x) <= 8, segment_pool))
scored_pool = list(map(lambda seg: seg * 2 if 'GC' in seg else seg, filtered_pool))

validated_palindrome_count = count_with_backtrack(scored_pool)
print(f"Result: {validated_palindrome_count}")