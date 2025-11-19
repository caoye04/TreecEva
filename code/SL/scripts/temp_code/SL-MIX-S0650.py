from collections import defaultdict

def calculate_palindrome_score(dna_sequence):
    palindrome_freq = defaultdict(int)
    n = len(dna_sequence)
    
    # Find all palindromic substrings
    for i in range(n):
        for j in range(i+1, n+1):
            substring = dna_sequence[i:j]
            if substring == substring[::-1]:
                palindrome_freq[substring] += 1
    
    max_score = 0
    # Calculate score based on length and frequency
    for palindrome, freq in palindrome_freq.items():
        length = len(palindrome)
        if freq > 1 and length > 1:
            score = length * freq
            if score > max_score:
                max_score = score
    
    return max_score

# Research sequence
sequence = "ATGCCGTAATGGCAT"

# Process the sequence
max_score = calculate_palindrome_score(sequence)
print(f"Result: {max_score}")