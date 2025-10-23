import re
import heapq
from collections import defaultdict

def manacher(s):
    # Transform string to handle even-length palindromes
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0
    
    for i in range(1, n-1):
        mirror = 2*C - i
        if i < R:
            P[i] = min(R - i, P[mirror])
        
        # Try to expand palindrome centered at i
        try:
            while T[i + (1 + P[i])] == T[i - (1 + P[i])]:
                P[i] += 1
        except IndexError:
            pass
        
        # If palindrome centered at i extends past R, adjust center and right boundary
        if i + P[i] > R:
            C, R = i, i + P[i]
    
    # Extract palindromes
    palindromes = []
    for i in range(1, n-1):
        if P[i] > 0:
            start = (i - P[i]) // 2
            length = P[i]
            palindromes.append((start, length))
    
    return palindromes

def calculate_stability(dna_sequence):
    # Find all palindromic substrings
    palindromes = manacher(dna_sequence)
    
    # Count frequency of each unique palindrome
    palindrome_freq = defaultdict(int)
    for start, length in palindromes:
        substring = dna_sequence[start:start+length]
        palindrome_freq[substring] += 1
    
    # Calculate base scores using dynamic programming
    # dp[i] represents max score for first i characters
    n = len(dna_sequence)
    dp = [0] * (n + 1)
    
    # For each position, check all possible palindromes ending there
    for i in range(1, n + 1):
        dp[i] = dp[i-1]  # Don't take any palindrome ending at i
        
        # Check all palindromes ending at position i
        for start, length in palindromes:
            if start + length == i:
                substring = dna_sequence[start:start+length]
                freq = palindrome_freq[substring]
                # Score formula: length^1.5 * log(freq+1)
                score = int(length ** 1.5 * (freq + 1) ** 0.5)
                dp[i] = max(dp[i], dp[start] + score)
    
    return dp[n]

# Main analysis
sequence = "ATGCCGTAATGCCGTAATGCCGTAATGCCGTA"

# Preprocessing: remove non-standard nucleotides
standard_nucleotides = re.sub(r'[^ATCG]', '', sequence)

# Calculate stability score
base_stability = calculate_stability(standard_nucleotides)

# Apply corrections based on GC content
gc_count = standard_nucleotides.count('G') + standard_nucleotides.count('C')
sequence_length = len(standard_nucleotides)
gc_content = gc_count / sequence_length if sequence_length > 0 else 0

correction_factor = 1 + (gc_content - 0.5) * 0.2
final_stability_score = int(base_stability * correction_factor)

print(f"Result: {final_stability_score}")