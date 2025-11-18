from collections import defaultdict

def is_palindrome(segment):
    return segment == segment[::-1]

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def find_palindromes(dna_strand, length=5):
    found_palindromes = set()
    palindrome_count = 0
    
    def backtrack(start_idx, current_segment):
        nonlocal palindrome_count
        
        # Early return conditions
        if len(current_segment) > length:
            return
        
        if len(current_segment) == length:
            if is_palindrome(current_segment):
                if current_segment not in found_palindromes:
                    found_palindromes.add(current_segment)
                    palindrome_count += 1
            return
        
        # Explore further only if we can still form a segment of required length
        if start_idx >= len(dna_strand):
            return
            
        # Backtracking step - include current nucleotide
        backtrack(start_idx + 1, current_segment + dna_strand[start_idx])
        
        # Backtracking step - skip current nucleotide
        backtrack(start_idx + 1, current_segment)
    
    # Sort DNA strand for binary search optimization
    sorted_nucleotides = sorted(list(dna_strand))
    
    # Switch-case equivalent for processing different nucleotide patterns
    pattern_map = {
        'A': lambda x: x.startswith('A') and x.endswith('A'),
        'T': lambda x: x.startswith('T') and x.endswith('T'),
        'G': lambda x: x.startswith('G') and x.endswith('G'),
        'C': lambda x: x.startswith('C') and x.endswith('C')
    }
    
    # Generator expression to pre-filter candidates
    candidate_segments = (
        dna_strand[i:i+length] 
        for i in range(len(dna_strand) - length + 1)
        if binary_search(sorted_nucleotides, dna_strand[i])
    )
    
    # Process each candidate with backtracking
    for segment in candidate_segments:
        if len(segment) == length:
            first_nucleotide = segment[0]
            # Switch-case logic
            if first_nucleotide in pattern_map and pattern_map[first_nucleotide](segment):
                if is_palindrome(segment) and segment not in found_palindromes:
                    found_palindromes.add(segment)
                    palindrome_count += 1
    
    # Additional recursive exploration
    backtrack(0, "")
    
    return palindrome_count

# DNA sequence for analysis
lab_sample_dna = "ATGCCGTAATCGGCTAGCTAGCTAG"

# Execute analysis
palindrome_count = find_palindromes(lab_sample_dna)
print(f"Result: {palindrome_count}")