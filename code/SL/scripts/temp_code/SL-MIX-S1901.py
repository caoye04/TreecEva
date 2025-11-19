import re
from functools import reduce

def hash_kmer(kmer):
    return reduce(lambda acc, c: (acc * 4 + {'A': 0, 'C': 1, 'G': 2, 'T': 3}[c]) % 1000003, kmer, 0)

def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))

sequences = ["ACGTACGT", "CGTACGTA", "GTACGTAC"]
k = 4
collision_count = 0
hash_table = {}

for seq in sequences:
    kmers = [seq[i:i+k] for i in range(len(seq) - k + 1)]
    rc_kmers = list(map(reverse_complement, kmers))
    all_kmers = kmers + rc_kmers
    
    for kmer in all_kmers:
        h = hash_kmer(kmer)
        if h in hash_table:
            if hash_table[h] != kmer:
                collision_count += 1
        else:
            hash_table[h] = kmer

print(f"Result: {collision_count}")