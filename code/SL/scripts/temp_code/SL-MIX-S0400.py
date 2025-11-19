import hashlib

dna_sequences = ['ATCG', 'GGCT', 'AATT', 'CCGG', 'AAAT']

# Filter sequences containing at least one 'A'
valid_sequences = list(filter(lambda seq: 'A' in seq, dna_sequences))

# Compute hash values for valid sequences
hash_values = list(map(lambda seq: int(hashlib.md5(seq.encode()).hexdigest(), 16) % 10000, valid_sequences))

# Calculate privacy checksum
privacy_checksum = sum(hash_values)

print(f"Result: {privacy_checksum}")