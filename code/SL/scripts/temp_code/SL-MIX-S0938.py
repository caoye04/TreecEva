from collections import defaultdict
from itertools import combinations

def encode_nucleotide(nucleotide_map, seq):
    return [nucleotide_map[nuc] for nuc in seq]

def transform_kmer(kmer):
    # Apply a bitwise transformation: shift left by 1 and XOR with 0b101
    transformed = []
    for val in kmer:
        transformed.append((val << 1) ^ 0b101)
    return tuple(transformed)

def analyze_motifs(encoded_seq, k):
    kmer_counts = defaultdict(int)
    n = len(encoded_seq)
    
    # Generate all k-mers
    for i in range(n - k + 1):
        kmer = tuple(encoded_seq[i:i+k])
        transformed_kmer = transform_kmer(kmer)
        kmer_counts[transformed_kmer] += 1
    
    # Count combinations of k-mers that sum to a specific target
    target_sum = 18
    target_count = 0
    
    # Short-circuit evaluation in condition check
    for kmer1, kmer2 in combinations(kmer_counts.keys(), 2):
        if kmer_counts[kmer1] > 0 and kmer_counts[kmer2] > 0 and sum(kmer1 + kmer2) == target_sum:
            target_count += kmer_counts[kmer1] * kmer_counts[kmer2]
    
    return target_count

# Main execution
if __name__ == "__main__":
    nucleotide_mapping = {'A': 1, 'T': 3, 'G': 2, 'C': 1}
    dna_fragment = "ATGATGA"
    encoded_sequence = encode_nucleotide(nucleotide_mapping, dna_fragment)
    k_value = 3
    
    target_count = analyze_motifs(encoded_sequence, k_value)
    print(f"Result: {target_count}")