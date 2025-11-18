def process_genomic_sequence(seq):
    # Nucleotide to score mapping
    scores = {'A': 2, 'T': 3, 'G': 5, 'C': 7}
    
    # Complement mapping using dictionary comprehension
    complements = {k: v for k, v in zip('ATGC', 'TACG')}
    
    # Transform sequence to its complement
    complement_seq = ''.join(complements[nuc] for nuc in seq)
    
    # Calculate raw scores for original and complement sequences
    original_scores = [scores[nuc] for nuc in seq]
    complement_scores = [scores[nuc] for nuc in complement_seq]
    
    # Pairwise product of scores
    paired_scores = [o * c for o, c in zip(original_scores, complement_scores)]
    
    # Lambda to compute cumulative sum
    cumsum = lambda lst: [sum(lst[:i+1]) for i in range(len(lst))]
    
    # Compute cumulative scores
    cumulative_paired = cumsum(paired_scores)
    
    # Binary search helper to find insertion point for median adjustment
    def binary_search_insert_point(arr, target):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low
    
    # Median adjustment factor
    sorted_cumulative = sorted(cumulative_paired)
    median_val = sorted_cumulative[len(sorted_cumulative)//2]
    insert_pos = binary_search_insert_point(sorted_cumulative, median_val)
    
    # Final score computation
    adjusted_scores = [score + insert_pos for score in cumulative_paired]
    final_score = sum(adjusted_scores)
    
    return final_score

# Execute pipeline
sequence = 'ATGCGTA'
final_score = process_genomic_sequence(sequence)
print(f'Result: {final_score}')