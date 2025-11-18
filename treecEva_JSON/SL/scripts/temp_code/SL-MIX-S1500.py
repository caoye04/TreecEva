from functools import reduce

def mutation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2 if result > 0 else result
    return wrapper

class DNAMutationAnalyzer:
    def __init__(self, sequence):
        self.sequence = sequence
        self.nucleotide_map = {'A': 1, 'T': -1, 'C': 2, 'G': -2}
    
    @mutation_decorator
    def calculate_segment_score(self, segment):
        return sum(self.nucleotide_map[nuc] for nuc in segment)

# DNA sequence for analysis
sequence = "ATCGATCGATCG"
analyzer = DNAMutationAnalyzer(sequence)

# Split into overlapping segments of length 4
segments = [sequence[i:i+4] for i in range(len(sequence)-3)]

# Sort segments based on their lexicographical order
sorted_segments = sorted(segments)

# Dynamic programming table for cumulative scores
segment_scores = []
for seg in sorted_segments:
    raw_score = analyzer.calculate_segment_score(seg)
    # Ternary operator to adjust negative scores
    adjusted_score = raw_score if raw_score >= 0 else raw_score - 5
    segment_scores.append(adjusted_score)

# Calculate cumulative maximum score using dynamic programming
max_scores = [segment_scores[0]]
for i in range(1, len(segment_scores)):
    max_scores.append(max(segment_scores[i], max_scores[i-1] + segment_scores[i]))

# Final stability score is the maximum value in max_scores
final_stability_score = max(max_scores) if max_scores else 0

print(f"Result: {final_stability_score}")