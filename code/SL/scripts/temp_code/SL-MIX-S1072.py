from collections import defaultdict
import itertools

def calculate_structural_diversity(sequence):
    segment_map = defaultdict(int)
    window_size = 3
    
    for i in range(len(sequence) - window_size + 1):
        segment = sequence[i:i + window_size]
        if segment[0] != segment[-1] and segment[1] in 'aeiou':
            segment_permutations = set(itertools.permutations(segment))
            valid_perms = [p for p in segment_permutations if p[0] < p[-1]]
            for perm in valid_perms:
                segment_map[''.join(perm)] += 1
    
    diversity_score = sum(1 for count in segment_map.values() if count > 1)
    return diversity_score

with open('temp_molecule.txt', 'w') as f:
    f.write('abcdefghijk')

with open('temp_molecule.txt', 'r') as f:
    molecular_chain = f.read().strip()

filter_vowels = lambda s: ''.join(filter(lambda c: c in 'aeiou', s))
structural_diversity_score = calculate_structural_diversity(molecular_chain) * len(filter_vowels(molecular_chain))
print(f"Result: {structural_diversity_score}")