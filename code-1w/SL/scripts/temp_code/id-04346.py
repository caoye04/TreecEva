def analyze_pattern(seq1, seq2):
    match_indices = []
    for i, (a, b) in enumerate(zip(seq1, seq2)):
        if a == b:
            match_indices.append(i)
    return match_indices

seq_a = [1, 0, 1, 1, 0, 1]
seq_b = [1, 1, 1, 0, 0, 1]

# Compute positions where bits match
correspondences = analyze_pattern(seq_a, seq_b)

# Weight assigned to each matching position
weights = [2, 1, 3, 2, 4, 2]

# Irrelevant variable (minor distraction)
baseline_offset = sum(seq_a) - len(seq_b) // 2

# Final scoring function
def compute_final_score(indices, weight_list):
    score = 0
    for idx in indices:
        score += weight_list[idx]
    return score

# Key computation step
total_similarity = compute_final_score(correspondences, weights)

Result: total_similarity