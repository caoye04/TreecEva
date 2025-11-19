from collections import defaultdict

def dna_rolling_hash(dna_str, window_size):
    base = 4
    mod = 1000000007
    hash_val = 0
    base_power = 1
    hash_map = defaultdict(int)
    
    # Precompute base^(window_size-1) % mod
    for _ in range(window_size - 1):
        base_power = (base_power * base) % mod
    
    # Compute hash for first window
    for i in range(window_size):
        nucleotide_val = {'A': 0, 'C': 1, 'G': 2, 'T': 3}[dna_str[i]]
        hash_val = (hash_val * base + nucleotide_val) % mod
    
    hash_map[hash_val] += 1
    collision_count = 0
    
    # Rolling hash computation
    for i in range(window_size, len(dna_str)):
        # Remove leftmost character
        left_char_val = {'A': 0, 'C': 1, 'G': 2, 'T': 3}[dna_str[i - window_size]]
        hash_val = (hash_val - left_char_val * base_power) % mod
        
        # Add rightmost character
        right_char_val = {'A': 0, 'C': 1, 'G': 2, 'T': 3}[dna_str[i]]
        hash_val = (hash_val * base + right_char_val) % mod
        
        # Check for collisions
        if hash_map[hash_val] > 0:
            collision_count += 1
        hash_map[hash_val] += 1
    
    return collision_count

dna_sequence = "ACGTACGTACGT"
window_length = 4
collision_count = dna_rolling_hash(dna_sequence, window_length)
print(f"Result: {collision_count}")