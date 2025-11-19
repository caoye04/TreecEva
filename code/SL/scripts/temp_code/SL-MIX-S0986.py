from itertools import combinations

def encode_nucleotides(seq):
    mapping = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    return [mapping[n] for n in seq]

def is_valid_subsequence(encoded_subseq):
    cum_sum = 0
    for val in encoded_subseq:
        cum_sum += val
        # Check if cumulative sum meets threshold using bitwise ops
        if (cum_sum & 3) == 0 and cum_sum >= 6:
            return True
    return False

def count_protein_markers(dna_sequence):
    encoded = encode_nucleotides(dna_sequence)
    n = len(encoded)
    dp = [0] * (n + 1)
    
    # Dynamic programming to count valid subsequences
    for i in range(1, n + 1):
        dp[i] = dp[i-1]
        for j in range(i):
            subseq = encoded[j:i]
            if is_valid_subsequence(subseq):
                dp[i] += 1
    
    return dp[n]

# Sample DNA sequence for analysis
sample_dna = "ATGCGATCG"
protein_marker_count = count_protein_markers(sample_dna)
print(f"Result: {protein_marker_count}")