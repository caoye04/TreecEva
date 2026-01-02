def compute_sequence_alignment(seq1, seq2):
    length = min(len(seq1), len(seq2))
    similarity_values = []
    
    for i, (a, b) in enumerate(zip(seq1[:length], seq2[:length])):
        if a == b:
            similarity_values.append(1)
        else:
            similarity_values.append(-0.5)
    
    adjustment_factor = 0.1 * len(similarity_values)
    alignment_score = sum(similarity_values)
    normalized_score = alignment_score + adjustment_factor
    
    return alignment_score

# Input sequences
dna_seq_a = "ATGCGTAC"
dna_seq_b = "ATGAATAC"

result = compute_sequence_alignment(dna_seq_a, dna_seq_b)
print(f"Result: {result}")