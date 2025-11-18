import re
from collections import defaultdict

def tokenize_dna(sequence):
    pattern = r'[ACGT]{3}'
    return re.findall(pattern, sequence)

def count_valid_subsequences(tokens):
    dp = defaultdict(int)
    for token in tokens:
        dp[token] += 1
        for prev_token in dp:
            if prev_token != token and abs(len(prev_token) - len(token)) <= 1:
                dp[token] += dp[prev_token]
    return sum(dp.values())

def encode_result(count):
    return count ^ (count >> 1) if count > 0 else 0

dna_sequence = "ACGTCGTACGTACGTA"
tokens = tokenize_dna(dna_sequence)
subsequence_count = count_valid_subsequences(tokens)
encoded_mutations = encode_result(subsequence_count) if subsequence_count > 10 else subsequence_count + 5
print(f"Result: {encoded_mutations}")