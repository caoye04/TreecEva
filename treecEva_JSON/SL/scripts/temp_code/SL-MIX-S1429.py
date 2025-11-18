import re
from collections import defaultdict

def encode_genetic_marker(sequence):
    # Custom base-64 encoding for genetic markers
    encoding_map = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-'
    encoded = ''
    for i in range(0, len(sequence), 3):
        chunk = sequence[i:i+3].ljust(3, 'A')
        val = (ord(chunk[0]) << 16) + (ord(chunk[1]) << 8) + ord(chunk[2])
        for _ in range(4):
            encoded += encoding_map[val & 63]
            val >>= 6
    return encoded[::-1]

def decode_genetic_marker(encoded):
    # Decoding function
    decoding_map = {c: i for i, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-')}
    decoded = ''
    for i in range(0, len(encoded), 4):
        chunk = encoded[i:i+4][::-1]
        val = 0
        for c in chunk:
            val = (val << 6) + decoding_map[c]
        decoded += chr((val >> 16) & 255) + chr((val >> 8) & 255) + chr(val & 255)
    return decoded.rstrip('A')

def find_optimal_alignment(seq1, seq2):
    # Dynamic programming for sequence alignment
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = i + j
            elif seq1[i-1] == seq2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

def detect_mutation_signature(sequence):
    # Pattern matching for mutation signatures
    patterns = [r'G[AT]C', r'T[CG]A', r'A[TA]G']
    matches = []
    for pattern in patterns:
        matches.extend(re.findall(pattern, sequence))
    return len(matches)

# Process genetic samples
samples = [
    ('ATGCGTACGTAGCTAGCTAGC', 'CGTAGCTAGCTAGCTAGCTAG'),
    ('GCTAGCTAGCTAGCTAGCTAG', 'TAGCTAGCTAGCTAGCTAGCT'),
    ('ACGTAGCTAGCTAGCTAGCTA', 'GTAGCTAGCTAGCTAGCTAGCT')
]

# Encode samples
encoded_samples = [(encode_genetic_marker(s1), encode_genetic_marker(s2)) for s1, s2 in samples]

# Calculate alignment scores using dynamic programming
alignment_scores = [find_optimal_alignment(es1, es2) for es1, es2 in encoded_samples]

# Decode one sample to check for mutation signatures
decoded_sample = decode_genetic_marker(encoded_samples[1][0])
signature_count = detect_mutation_signature(decoded_sample)

# Combine results using set operations
score_set = frozenset(alignment_scores)
adjusted_scores = {score: score * 2 if score > 10 else score + 5 for score in score_set}

# Calculate final mutation score
final_mutation_score = sum(adjusted_scores.values()) + signature_count * 3

print(f"Result: {final_mutation_score}")