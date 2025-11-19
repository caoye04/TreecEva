import re
from collections import defaultdict

def calculate_nucleotide_scores(sequences):
    score_map = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    position_scores = defaultdict(int)
    
    for seq in sequences:
        for idx, nucleotide in enumerate(seq):
            if nucleotide in score_map:
                position_scores[idx] += score_map[nucleotide]
    
    return position_scores

def compute_marker_weights(position_scores):
    weights = {}
    for pos, score in position_scores.items():
        # Apply a transformation using regex pattern matching
        if re.match(r'[2-9]', str(score)):
            weights[pos] = score * 2
        else:
            weights[pos] = score + 5
    return weights

# Main processing pipeline
sequences = [
    "ATGC",
    "GGCC",
    "TATA",
    "CGTA"
]

pos_scores = calculate_nucleotide_scores(sequences)
marker_weights = compute_marker_weights(pos_scores)

# Calculate final score using lambda and aggregation
weight_values = list(marker_weights.values())
aggregate_fn = lambda x, y: x + (y * 2) if y % 2 == 0 else x + y
final_score = 0
for val in weight_values:
    final_score = aggregate_fn(final_score, val)

print(f"Result: {final_score}")