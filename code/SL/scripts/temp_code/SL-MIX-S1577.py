from collections import defaultdict
import statistics

# Nucleotide instability weights
weights = {'A': 1.2, 'T': 0.8, 'G': 1.5, 'C': 1.0}
sequences = ['ATGGCT', 'TGCATG', 'CGTACG', 'AAATTT']

# Compute instability scores for each sequence
instability_scores = []
for seq in sequences:
    score = sum(weights[nuc] for nuc in seq)
    instability_scores.append(score)

# Calculate mean and standard deviation of scores
mean_score = statistics.mean(instability_scores)
stdev_score = statistics.stdev(instability_scores) if len(instability_scores) > 1 else 0

# Identify outlier sequences (scores beyond 1 stdev from mean)
outliers = [s for s, score in zip(sequences, instability_scores) if abs(score - mean_score) > stdev_score]

# Build nucleotide frequency map for outliers only
nuc_freq = defaultdict(int)
for seq in outliers:
    for nuc in seq:
        nuc_freq[nuc] += 1

# Compute weighted frequency score for outlier nucleotides
weighted_freq_sum = sum(freq * weights[nuc] for nuc, freq in nuc_freq.items())

# Final score combines statistical measures with frequency analysis
final_score = round((mean_score + stdev_score) * weighted_freq_sum)
print(f"Result: {final_score}")