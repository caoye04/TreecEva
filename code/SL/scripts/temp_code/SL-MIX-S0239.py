from itertools import combinations

def analyze_dna_palindromes(dna_sequence):
    n = len(dna_sequence)
    palindrome_count = 0
    
    # Dynamic programming table for palindrome checking
    is_palindrome = [[False] * n for _ in range(n)]
    
    # Every single character is a palindrome
    for i in range(n):
        is_palindrome[i][i] = True
    
    # Check for palindromes of length 2
    for i in range(n - 1):
        if dna_sequence[i] == dna_sequence[i + 1]:
            is_palindrome[i][i + 1] = True
    
    # Check for palindromes of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if dna_sequence[i] == dna_sequence[j] and is_palindrome[i + 1][j - 1]:
                is_palindrome[i][j] = True
    
    # Count valid palindromes with specific constraints
    for i in range(n):
        for j in range(i, n):
            if is_palindrome[i][j]:
                segment_length = j - i + 1
                segment = dna_sequence[i:j+1]
                
                # Constraint: length between 3 and 8
                # AND must contain at least one 'C' and one 'G'
                # AND must not have more than 2 'A's
                if (3 <= segment_length <= 8 and
                    'C' in segment and 'G' in segment and
                    segment.count('A') <= 2):
                    palindrome_count += 1
    
    return palindrome_count

def main():
    dna_seq = "ATCGATCGATCG"
    
    # Using a context manager for analysis tracking
    class AnalysisTracker:
        def __init__(self, name):
            self.name = name
            self.completed = False
        
        def __enter__(self):
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.completed = True
            return False
    
    with AnalysisTracker("DNA_Palindrome_Analysis") as tracker:
        if tracker.name == "DNA_Palindrome_Analysis":
            result = analyze_dna_palindromes(dna_seq)
            tracker.result = result
    
    # Additional filtering using set operations
    valid_nucleotides = frozenset(['A', 'T', 'C', 'G'])
    sequence_set = set(dna_seq)
    
    # Only proceed if sequence contains valid nucleotides
    if sequence_set.issubset(valid_nucleotides) and tracker.completed:
        palindrome_count = tracker.result
    else:
        palindrome_count = 0
    
    print(f"Result: {palindrome_count}")

if __name__ == "__main__":
    main()