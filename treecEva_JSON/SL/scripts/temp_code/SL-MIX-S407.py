from functools import reduce
import hashlib

def tokenize_dna(sequence):
    return [sequence[i:i+3] for i in range(0, len(sequence), 3)]

def hash_substrings(tokens):
    return {token: hashlib.md5(token.encode()).hexdigest()[:8] for token in tokens}

def compute_frequency(tokens):
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def dynamic_score(freq_map):
    keys = sorted(freq_map.keys())
    dp = [0] * (len(keys) + 1)
    for i in range(1, len(keys) + 1):
        current = freq_map[keys[i-1]]
        dp[i] = max(dp[i-1], dp[i-2] + current if i >= 2 else current)
    return dp[len(keys)]

def process_genomic_data(dna_sequence):
    # Tokenization step
    codons = tokenize_dna(dna_sequence)
    
    # Hash all unique codons
    codon_hashes = hash_substrings(codons)
    
    # Compute frequency of each codon
    frequency_map = compute_frequency(codons)
    
    # Apply dynamic programming to maximize non-adjacent codon frequency score
    dp_score = dynamic_score(frequency_map)
    
    # Sort codons by frequency (descending) then by hash (ascending)
    sorted_codons = sorted(frequency_map.items(), key=lambda x: (-x[1], codon_hashes[x[0]]))
    
    # Calculate weighted sum based on position and frequency
    weighted_sum = sum((i + 1) * freq for i, (codon, freq) in enumerate(sorted_codons))
    
    # Final score combines dynamic programming result with weighted sum
    final_score = dp_score * 1000 + weighted_sum
    
    return final_score

# Experimental DNA sequence
experiment_sequence = "ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG......