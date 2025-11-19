from itertools import combinations

def encode_dna(sequence):
    mapping = {'A': 0, 'T': 1, 'G': 2, 'C': 3}
    return [mapping[nucleotide] for nucleotide in sequence]

def decode_dna(encoded_seq):
    mapping = {0: 'A', 1: 'T', 2: 'G', 3: 'C'}
    return ''.join([mapping[num] for num in encoded_seq])

def transform_sequence(seq, operations):
    result = seq[:]
    for op in operations:
        if op == 'reverse':
            result = result[::-1]
        elif op == 'complement':
            result = [3 - x for x in result]
    return result

def longest_common_subsequence(seq1, seq2):
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i-1] == seq2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# Original DNA sequences
sequence_alpha = "ATGCGT"
sequence_beta = "TGCATC"

# Encode sequences
encoded_alpha = encode_dna(sequence_alpha)
encoded_beta = encode_dna(sequence_beta)

# Apply transformations
transform_ops_alpha = ['reverse', 'complement']
transform_ops_beta = ['complement', 'reverse']

transformed_alpha = transform_sequence(encoded_alpha, transform_ops_alpha)
transformed_beta = transform_sequence(encoded_beta, transform_ops_beta)

# Find longest common subsequence
lcs_length = longest_common_subsequence(transformed_alpha, transformed_beta)

print(f"Result: {lcs_length}")