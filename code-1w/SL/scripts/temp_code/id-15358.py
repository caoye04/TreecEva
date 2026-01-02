from collections import defaultdict

# Simulate alignment of two biological sequences
def compute_sequence_similarity(seq1, seq2):
    length = min(len(seq1), len(seq2))
    total_similarity = 0
    gap_count = 0  # distractor: not used in final calculation

    for i, (a, b) in enumerate(zip(seq1[:length], seq2[:length])):
        if a == b:
            similarity_score = 1.5
        elif a in 'CG' and b in 'AT':
            similarity_score = 0.5
        else:
            similarity_score = -0.5
        
        total_similarity += similarity_score
        
        # Irrelevant conditional (distractor)
        if a == '-' or b == '-':
            gap_count += 1

    return total_similarity

seq_a = 'ATGCGATAG'
seq_b = 'ATCACATCG'
result = compute_sequence_similarity(seq_a, seq_b)
print(f"Result: {result}")