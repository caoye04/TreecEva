from collections import defaultdict

def rolling_hash(kmer):
    hash_value = 0
    for char in kmer:
        hash_value = (hash_value * 4 + ord(char)) % 100000007
    return hash_value

def find_collisions(sequences, k):
    hash_table = defaultdict(list)
    collision_count = 0
    
    for seq_id, sequence in enumerate(sequences):
        seen_in_current = set()
        for i in range(len(sequence) - k + 1):
            kmer = sequence[i:i+k]
            hash_val = rolling_hash(kmer)
            
            if hash_val in hash_table:
                # Check for actual collision (different k-mers with same hash)
                if kmer not in [entry[1] for entry in hash_table[hash_val]]:
                    collision_count += 1
            
            # Only add if not seen in current sequence
            if kmer not in seen_in_current:
                hash_table[hash_val].append((seq_id, kmer))
                seen_in_current.add(kmer)
    
    return collision_count

# Simulated DNA sequences
sequences = [
    "ATCGATCGATCG",
    "GCTAGCTAGCTA",
    "ATCGATCGATCG",  # Identical to first, will have same hashes
    "TTTTTTTTTTTT"
]
k = 4
collision_count = find_collisions(sequences, k)
print(f"Result: {collision_count}")