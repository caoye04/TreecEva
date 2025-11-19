from collections import defaultdict
import re

def decode_nucleotides(encoded_seq):
    mapping = {1: 'A', 2: 'T', 3: 'G', 4: 'C'}
    return ''.join(mapping[n] for n in encoded_seq)

# Encoded DNA sequences
sequences = [
    [1, 3, 2, 4, 1],
    [4, 2, 3, 1, 2],
    [3, 1, 4, 2, 3],
    [2, 4, 1, 3, 4]
]

# Step 1: Decode sequences and filter those containing "AT"
pattern = re.compile(r'AT')
filtered_sequences = [
    seq for seq in sequences 
    if pattern.search(decode_nucleotides(seq))
]

# Step 2: Apply a custom scoring function using lambda
scoring_function = lambda seq: sum(x**2 for x in seq if x % 2 == 0)
scores = list(map(scoring_function, filtered_sequences))

# Step 3: Sort scores in descending order and take top 2
top_scores = sorted(scores, reverse=True)[:2]

# Step 4: Aggregate using a defaultdict to count score frequencies
score_frequency = defaultdict(int)
for score in top_scores:
    score_frequency[score] += 1

# Step 5: Compute final marker score as the product of unique scores
final_marker_score = 1
for score in score_frequency:
    final_marker_score *= score

print(f"Result: {final_marker_score}")