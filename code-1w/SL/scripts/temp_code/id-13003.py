from itertools import combinations

# Simulate analysis of nucleotide sequence patterns in bioinformatics
dna_sequence = 'ATGCTAGCTAGCTAGCTTACGTAGCT'
subseq_length = 4
gc_threshold = 0.5
min_gc_content = 2
max_homopolymer_run = 2

# Extract all possible sub-sequences of given length
possible_subseqs = [dna_sequence[i:i+subseq_length] for i in range(len(dna_sequence) - subseq_length + 1)]

# Track redundant metrics for distraction
total_combinations = len(possible_subseqs)
unique_subseqs = set(possible_subseqs)
distinct_count = len(unique_subseqs)

# Helper: compute GC content
def gc_content(seq):
    return sum(1 for base in seq if base in 'GC') / len(seq)

# Helper: detect homopolymer runs (same nucleotide repeated)
def has_long_homopolymer(seq, max_run=3):
    for i in range(len(seq) - max_run + 1):
        if all(seq[i] == c for c in seq[i:i+max_run]):
            return True
    return False

# Misleading intermediate: count A/T rich sequences (not used in final logic)
at_rich_count = 0
for seq in possible_subseqs:
    if sum(1 for b in seq if b in 'AT') > 2:
        at_rich_count += 1

# Actual filtering criteria: sufficient GC content and no long homopolymers
filtered_for_gc = [s for s in possible_subseqs if gc_content(s) >= gc_threshold]
filtered_no_homopolymer = [s for s in filtered_for_gc if not has_long_homopolymer(s, max_homopolymer_run + 1)]

# Further filter out sequences with internal repeats (e.g., XYXY pattern)
def has_internal_repeat(seq):
    if len(seq) < 4:
        return False
    return seq[:2] == seq[2:]

no_internal_repeats = [s for s in filtered_no_homopolymer if not has_internal_repeat(s)]

# Construct valid sequences based on all filters
valid_sequences = []
for seq in no_internal_repeats:
    # Additional validation: must start with 'GC' or end with 'CG'
    if seq.startswith('GC') or seq.endswith('CG'):
        valid_sequences.append(seq)

# Dead code: unused permutation analysis (adds interference)
perm_analysis = []
for seq in unique_subseqs:
    perms = list(combinations(seq, 2))  # irrelevant usage
    perm_analysis.append(len(perms))

# Key assignment point
final_count = len(valid_sequences)
print(f"Result: {final_count}")