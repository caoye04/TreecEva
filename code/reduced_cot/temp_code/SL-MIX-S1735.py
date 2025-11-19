import itertools
from collections import Counter

def is_balanced(seq):
    counts = Counter(seq)
    return abs(counts['A'] - counts['T']) <= 1 and abs(counts['G'] - counts['C']) <= 1

def gc_content(seq):
    gc = seq.count('G') + seq.count('C')
    return gc / len(seq) if len(seq) > 0 else 0

def contains_forbidden_subseq(seq, forbidden):
    return any(sub in seq for sub in forbidden)

def mutate_strand(initial_strand, rulebook, forbidden_subsequences, target_gc_range):
    # Apply rulebook transformations
    transformed_pool = set()
    for nt in initial_strand:
        if nt in rulebook:
            transformed_pool.update(rulebook[nt])
        else:
            transformed_pool.add(nt)
    
    # Generate all possible 4-length combinations with repetition
    candidate_sequences = [''.join(p) for p in itertools.product(transformed_pool, repeat=4)]
    
    valid_mutations_count = 0
    for seq in candidate_sequences:
        if contains_forbidden_subseq(seq, forbidden_subsequences):
            continue
        if not is_balanced(seq):
            continue
        gc_ratio = gc_content(seq)
        if not (target_gc_range[0] <= gc_ratio <= target_gc_range[1]):
            continue
        valid_mutations_count += 1
    
    return valid_mutations_count

# Initial DNA strand
original_dna = "AGTC"

# Mutation rules: mapping of nucleotides to their potential substitutions
mutation_rules = {
    'A': {'A', 'G'},
    'T': {'T', 'C'},
    'G': {'G', 'A', 'T'},
    'C': {'C', 'G'}
}

# Forbidden subsequences that must not appear in any valid mutation
forbidden_patterns = ["AA", "TT"]

# Target GC-content range (inclusive)
gc_target_range = (0.4, 0.6)

# Execution point Y: Function call and result assignment
valid_mutations_count = mutate_strand(original_dna, mutation_rules, forbidden_patterns, gc_target_range)
print(f"Result: {valid_mutations_count}")