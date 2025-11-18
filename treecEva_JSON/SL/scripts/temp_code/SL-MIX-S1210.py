import itertools
import math

genetic_markers = ['A', 'C', 'G', 'T', 'X', 'Y']
valid_combinations = [
    ('A', 'C', 'G'), 
    ('T', 'X', 'Y'), 
    ('A', 'T', 'X'), 
    ('C', 'G', 'Y')
]

scoring_weights = {('A', 'C', 'G'): 15, ('T', 'X', 'Y'): 22, ('A', 'T', 'X'): 18, ('C', 'G', 'Y'): 25}
base_values = {'A': 1, 'C': 2, 'G': 4, 'T': 8, 'X': 16, 'Y': 32}

cumulative_score = 0

for combo in valid_combinations:
    combo_permutations = list(itertools.permutations(combo))
    combo_weight = scoring_weights[combo]
    
    for perm in combo_permutations:
        bit_mask = 0
        for marker in perm:
            bit_mask |= base_values[marker]
        
        # Apply scoring formula: (bit_mask XOR combo_weight) * factorial(length)
        score_contribution = (bit_mask ^ combo_weight) * math.factorial(len(perm))
        cumulative_score += score_contribution
        
        # Nested condition to add complexity
        if len(perm) > 2 and (bit_mask & combo_weight) > 0:
            cumulative_score += (bit_mask & combo_weight) << 1

print(f"Result: {cumulative_score}")