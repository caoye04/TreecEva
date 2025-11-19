from collections import defaultdict
import hashlib

def hash_sequence(seq):
    return int(hashlib.md5(seq.encode()).hexdigest(), 16) % 1000000

dna_sequences = ['ATGCGTACGT', 'CGTATGCGTA', 'TACGTATGCG']

# Step 1: Generate all rotations of each sequence
rotation_map = defaultdict(list)
for seq in dna_sequences:
    for i in range(len(seq)):
        rotation = seq[i:] + seq[:i]
        rotation_map[seq].append(rotation)

# Step 2: Hash all rotations and store in a matrix
hash_matrix = []
for seq in dna_sequences:
    row = [hash_sequence(rot) for rot in rotation_map[seq]]
    hash_matrix.append(row)

# Step 3: Compute combination scores using lambda
combination_scores = []
combine_func = lambda x, y: (x + y) * (x ^ y)
for i in range(len(hash_matrix)):
    score = 0
    for j in range(len(hash_matrix[i])):
        if j < len(hash_matrix[i]) - 1:
            score += combine_func(hash_matrix[i][j], hash_matrix[i][j+1])
    combination_scores.append(score)

# Step 4: Calculate final score
final_score = sum(combination_scores) % 1000
print(f'Result: {final_score}')