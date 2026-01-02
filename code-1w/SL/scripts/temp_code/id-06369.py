def compute_sequence_similarity(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have equal length")
    
    matches = set()
    mismatch_count = 0
    
    for i, (a, b) in enumerate(zip(seq1, seq2)):
        if a == b:
            matches.add(i)
        else:
            mismatch_count += 1
    
    base_score = len(seq1) - mismatch_count
    penalty = 0.1 * mismatch_count
    adjusted_score = base_score - penalty
    
    similarity_scores = [adjusted_score / len(seq1)]
    
    normalization_factor = 1.0
    if len(seq1) > 5:
        normalization_factor = 2.0
    
    similarity_scores[0] *= normalization_factor
    
    total_similarity = sum(similarity_scores)
    return total_similarity

# Example sequences
seq_a = [1, 0, 1, 1, 0, 1]
seq_b = [1, 1, 1, 0, 0, 1]

result = compute_sequence_similarity(seq_a, seq_b)
print(f"Result: {result}")