from itertools import combinations
from functools import reduce
from statistics import harmonic_mean

def calculate_motif_score(kmer):
    nucleotide_weights = {'A': 1.2, 'T': 1.5, 'G': 1.8, 'C': 2.0}
    position_factors = [1.1, 1.3, 1.0, 1.2, 1.4]
    score = 0
    for i, nucleotide in enumerate(kmer):
        if nucleotide in nucleotide_weights:
            score += nucleotide_weights[nucleotide] * position_factors[i]
    return score

def passes_statistical_filter(score):
    return score > 7.0 and score < 12.0

# DNA sequence database
sequence_database = [
    "ATGCG",
    "TGCAT",
    "CGTAC",
    "GACTG",
    "ACGTA",
    "GTACG",
    "TACGT",
    "CGTGA"
]

# Generate all possible 5-mers from the sequence database
all_kmers = []
for seq in sequence_database:
    if len(seq) >= 5:
        all_kmers.append(seq[:5])

# Calculate scores for all kmers
motif_scores = list(map(calculate_motif_score, all_kmers))

# Filter scores based on statistical thresholds
valid_scores = list(filter(passes_statistical_filter, motif_scores))

# Apply additional entropy correction only if we have enough valid scores
final_score = 0
if len(valid_scores) >= 3 and reduce(lambda x, y: x and y, [s > 8.0 for s in valid_scores[:3]], True):
    # Calculate harmonic mean of top valid scores
    top_scores = sorted(valid_scores, reverse=True)[:min(5, len(valid_scores))]
    harmonic_value = harmonic_mean(top_scores)
    
    # Apply entropy correction factor
    entropy_factor = len(set(all_kmers)) / len(all_kmers)
    final_score = round(harmonic_value * entropy_factor, 2)
else:
    final_score = -1

print(f"Result: {final_score}")