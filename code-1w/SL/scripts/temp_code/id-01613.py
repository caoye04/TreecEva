def compute_similarity_score(seq1, seq2):
    matches = 0
    for i, (a, b) in enumerate(zip(seq1, seq2)):
        if a == b:
            matches += 1
    return matches

# Pattern sequences representing user interaction behaviors
pattern_a = [1, 0, 1, 1, 0, 1]
pattern_b = [1, 1, 1, 0, 0, 1]

# Calculate similarity based on matching actions at same positions
total_similarity = compute_similarity_score(pattern_a, pattern_b)

Result: total_similarity