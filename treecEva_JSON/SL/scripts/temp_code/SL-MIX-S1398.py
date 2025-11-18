from functools import reduce

def calculate_nucleotide_score(nucleotide):
    scores = {'A': 2, 'T': -1, 'G': 3, 'C': -2}
    return scores.get(nucleotide, 0)

def max_subarray_sum(arr):
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_max = max_subarray_sum(left_half)
    right_max = max_subarray_sum(right_half)
    
    # Calculate crossing sum
    left_sum = float('-inf')
    temp_sum = 0
    for i in range(mid-1, -1, -1):
        temp_sum += arr[i]
        left_sum = max(left_sum, temp_sum)
    
    right_sum = float('-inf')
    temp_sum = 0
    for i in range(mid, len(arr)):
        temp_sum += arr[i]
        right_sum = max(right_sum, temp_sum)
    
    cross_sum = left_sum + right_sum
    
    return max(left_max, right_max, cross_sum)

dna_strand = "ATGCGATCGATCGATCGATCGATCGATCGATCGATCGATCG"
nucleotide_scores = list(map(calculate_nucleotide_score, dna_strand))

# Using dynamic programming to track local maximums
local_max = nucleotide_scores[0]
global_max = nucleotide_scores[0]
for i in range(1, len(nucleotide_scores)):
    local_max = max(nucleotide_scores[i], local_max + nucleotide_scores[i])
    global_max = max(global_max, local_max)

dp_score = global_max

# Divide and conquer approach
conquer_score = max_subarray_sum(nucleotide_scores)

# Combinatorics part - calculating possible combinations of high-scoring segments
high_scoring_positions = [i for i, score in enumerate(nucleotide_scores) if score > 0]
combination_count = 0
for i in range(1, min(4, len(high_scoring_positions)+1)):
    combination_count += len([1 for j in range(len(high_scoring_positions)-i+1)])

# Final score calculation using ternary operator
max_score = dp_score if dp_score > conquer_score else conquer_score
max_score = max_score + (combination_count if combination_count > 10 else 0)

print(f"Result: {max_score}")