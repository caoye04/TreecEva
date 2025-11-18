import itertools

def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))

def tokenize_dna(dna_seq, k):
    return [dna_seq[i:i+k] for i in range(len(dna_seq) - k + 1)]

def compute_binding_scores(kmers):
    dp = {}
    for kmer in kmers:
        rc_kmer = reverse_complement(kmer)
        if kmer in dp:
            dp[kmer] += 1
        elif rc_kmer in dp:
            dp[rc_kmer] += 1
        else:
            dp[kmer] = 1
    return dp

def calculate_motif_score(binding_scores_dict):
    total_score = 0
    for kmer, count in binding_scores_dict.items():
        # Apply a transformation: score = count * (sum of ASCII values of kmer)
        ascii_sum = sum(ord(c) for c in kmer)
        total_score += count * ascii_sum
    return total_score

# Main processing pipeline
dna_sequence = "ATCGATCGATCG"
kmer_length = 4

# Step 1: Tokenize
kmer_list = tokenize_dna(dna_sequence, kmer_length)

# Step 2: Compute binding scores using dynamic programming approach
binding_scores = compute_binding_scores(kmer_list)

# Step 3: Calculate motif score
intermediate_score = calculate_motif_score(binding_scores)

# Step 4: Apply final transformation using lambda
transform = lambda x: (x // 10) * 7 - (x % 10)
final_motif_score = transform(intermediate_score)

print(f"Result: {final_motif_score}")