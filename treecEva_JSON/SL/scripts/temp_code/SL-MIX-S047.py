import re
from collections import defaultdict

def calculate_palindrome_weights(sequence):
    palindromes = defaultdict(int)
    n = len(sequence)
    
    # Find all palindromic substrings using expanding window technique
    for i in range(n):
        # Odd length palindromes
        left, right = i, i
        while left >= 0 and right < n and sequence[left] == sequence[right]:
            if right - left + 1 >= 3:  # Only consider palindromes of length 3 or more
                palindromes[right - left + 1] += 1
            left -= 1
            right += 1
        
        # Even length palindromes
        left, right = i, i + 1
        while left >= 0 and right < n and sequence[left] == sequence[right]:
            if right - left + 1 >= 4:  # Only consider palindromes of length 4 or more
                palindromes[right - left + 1] += 1
            left -= 1
            right += 1
    
    return palindromes

def compute_genomic_score(palindrome_map):
    # Apply weighting formula: weight = length^2 * count
    total = sum(length**2 * count for length, count in palindrome_map.items())
    return total

# Main analysis pipeline
dna_sequence = "ATGCCGTAATCGGCTA"
pattern_match = re.search(r'([ATGC]{4,})', dna_sequence)
selected_segment = pattern_match.group(1) if pattern_match else dna_sequence[:8]

# Short-circuit evaluation for quality control
is_valid_sequence = len(selected_segment) >= 8 and all(base in 'ATGC' for base in selected_segment)
selected_segment = selected_segment if is_valid_sequence else dna_sequence[:8]

# Palindrome analysis
palindrome_data = calculate_palindrome_weights(selected_segment)
raw_score = compute_genomic_score(palindrome_data)

# Apply normalization using ternary operator
normalization_factor = 0.5 if raw_score > 100 else (0.75 if raw_score > 50 else 1.0)
final_score = int(raw_score * normalization_factor) if palindrome_data else 0

print(f"Result: {final_score}")