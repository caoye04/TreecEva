import re
from itertools import combinations

def is_palindrome(s):
    return s == s[::-1]

def calculate_composition(dna_segment):
    comp = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for nuc in dna_segment:
        if nuc in comp:
            comp[nuc] += 1
    return comp

def score_segment(segment, pwm):
    score = 0
    for i, nucleotide in enumerate(segment):
        if nucleotide in pwm[i]:
            score += pwm[i][nucleotide]
    return score

def find_optimal_palindrome(dna_sequence, length, min_gc_content, pwm):
    max_score = -float('inf')
    optimal_segment = None
    
    # Generate all possible substrings of specified length
    for i in range(len(dna_sequence) - length + 1):
        substring = dna_sequence[i:i+length]
        
        # Check if it's a palindrome and meets GC content requirement
        if is_palindrome(substring) and len(re.findall(r'[GC]', substring))/length >= min_gc_content:
            composition = calculate_composition(substring)
            
            # Apply additional filtering using combinatorial checks
            valid_combinations = 0
            for combo in combinations(substring, 3):
                if combo[0] != combo[1] and combo[1] != combo[2]:
                    valid_combinations += 1
            
            # Only consider segments with sufficient diversity
            if valid_combinations > 2:
                segment_score = score_segment(substring, pwm)
                if segment_score > max_score:
                    max_score = segment_score
                    optimal_segment = substring
    
    return max_score if optimal_segment else 0

def main():
    # Position Weight Matrix for preferred nucleotides at each position
    pwm = [
        {'A': 2, 'T': -1, 'G': 1, 'C': 0},
        {'A': -2, 'T': -1, 'G': 3, 'C': 2},
        {'A': 0, 'T': 0, 'G': 2, 'C': 3},
        {'A': -1, 'T': -1, 'G': 1, 'C': 4},
        {'A': 3, 'T': -2, 'G': 0, 'C': 1},
        {'A': 4, 'T': -3, 'G': -1, 'C': 0}
    ]
    
    # DNA sequence under analysis
    genome_fragment = "ATGCCGTAATGCCGTACGTA"
    
    # Analysis parameters
    target_length = 6
    minimum_gc = 0.5
    
    # Perform the analysis
    max_score = find_optimal_palindrome(genome_fragment, target_length, minimum_gc, pwm)
    
    # Adjust score based on special conditions
    if max_score > 10 and 'CCG' in genome_fragment:
        max_score += 5
    elif max_score <= 10 or ('GCC' not in genome_fragment and len(genome_fragment) > 15):
        max_score -= 2
    
    print(f"Result: {max_score}")

if __name__ == "__main__":
    main()