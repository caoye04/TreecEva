import math

# Simulated bioinformatics data processing pipeline with distractions
def analyze_sequence(sequence):
    base_composition = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in sequence:
        if base in base_composition:
            base_composition[base] += 1

    gc_content = (base_composition['G'] + base_composition['C']) / len(sequence)
    complexity_index = math.log(len(sequence)) * gc_content

    # Distractor: irrelevant transformation
    transformed_vals = [math.sin(i * complexity_index) for i in range(5)]
    normalized_seq = [x + 0.1 for x in transformed_vals if x > 0]

    return complexity_index, base_composition

# Secondary function - partially relevant
def generate_kmers(seq, k=3):
    kmers = set()
    for i in range(len(seq) - k + 1):
        kmers.add(seq[i:i+k])
    
    # Red herring: unused statistical calculation
    entropy = 0.0
    freq_dist = {}
    for kmer in kmers:
        freq_dist[kmer] = freq_dist.get(kmer, 0) + 1
    for count in freq_dist.values():
        p = count / len(kmers)
        if p > 0:
            entropy -= p * math.log2(p)
    
    return kmers

# Main analysis workflow
sequence_data = 'ATGCTAGCTAGCTAGCTTACGTAGCGCTAGCGCGCGATCGATCGATCGATCGTAGC'

# Step 1: Basic stats (some are red herrings)
seq_length = len(sequence_data)
duplicate_check = set(sequence_data)
unique_bases = len(duplicate_check)

# Step 2: Compute composition metrics
index, comp = analyze_sequence(sequence_data)

# Step 3: Generate feature sets
kmer_features = generate_kmers(sequence_data, k=4)
noise_filter = {kmer for kmer in kmer_features if 'N' not in kmer and len(kmer) == 4}

# Step 4: Masked pattern detection (irrelevant but looks important)
mask_patterns = []
for i in range(0, len(sequence_data) - 5):
    subseq = sequence_data[i:i+6]
    if subseq.count('G') >= 3:
        mask_patterns.append(i % 7)

pattern_modulo_sum = sum(mask_patterns) % 19 if mask_patterns else 0

# Step 5: Simulate quality filtering using multiple redundant checks
quality_flags = []
for kmer in kmer_features:
    if kmer.startswith('AT') or kmer.endswith('GC'):
        quality_flags.append(True)
    else:
        quality_flags.append(False)

# Step 6: Real logic begins - construct optimal set based on symmetry and composition
palindromic_kmers = {k for k in kmer_features if k == k[::-1]}
high_gc_kmers = {k for k in kmer_features if (k.count('G') + k.count('C')) >= 3}

# Core intersection - only this matters
optimal_set = palindromic_kmers & high_gc_kmers & noise_filter

# Misleading aggregation path (dead end)
temp_summary = []
for k in optimal_set:
    score = 0
    for char in k:
        if char == 'G':
            score += 2
        elif char == 'C':
            score += 2
        elif char == 'A':
            score += 1
    temp_summary.append(score * seq_length // 10)

aggregated_total = sum(temp_summary) + pattern_modulo_sum  # Distractor accumulation

# Critical statement - answer derived here
filtration_score = len(optimal_set)

# Irrelevant final transformation (looks important but unused)
scaled_result = aggregated_total / (filtration_score if filtration_score > 0 else 1)
adjusted_scores = [round(s * 1.5) for s in temp_summary]
final_report = {'count': filtration_score, 'scale': scaled_result, 'flags': sum(quality_flags)}

# Output target result
print(f"Result: {filtration_score}")