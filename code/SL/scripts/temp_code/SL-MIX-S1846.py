from functools import lru_cache
import sys
sys.setrecursionlimit(2000)

def is_palindrome(subseq):
    return subseq == subseq[::-1]

@lru_cache(maxsize=None)
def count_palindromes(dna_strand, target_length, position=0):
    # Base cases
    if position > len(dna_strand) - target_length:
        return 0
    
    # Extract substring of target length
    substring = dna_strand[position:position + target_length]
    
    # Check if it's a palindrome
    current_count = 1 if is_palindrome(substring) else 0
    
    # Recursive call for next position
    remaining_count = count_palindromes(dna_strand, target_length, position + 1)
    
    return current_count + remaining_count

dna_sample = "ATGCCGTAATCGGCTA"
target_len = 3

# Execute the analysis
result = count_palindromes(dna_sample, target_len, 0)

# Calculate cache size (number of entries)
cache_size = count_palindromes.cache_info().currsize

print(f"Result: {cache_size}")