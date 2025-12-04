import itertools

def calculate_dna_compatibility(seq1, seq2):
    # Calculate compatibility score between two DNA sequences
    match_score = 0
    mismatch_penalty = 0
    
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            match_score += 2
        else:
            # Different nucleotides have different mismatch penalties
            if (seq1[i], seq2[i]) in [('A', 'T'), ('T', 'A'), ('G', 'C'), ('C', 'G')]:
                mismatch_penalty += 1  # Complementary bases have lower penalty
            else:
                mismatch_penalty += 2
    
    # This calculation is actually irrelevant for the final result
    gc_content1 = (seq1.count('G') + seq1.count('C')) / len(seq1)
    gc_content2 = (seq2.count('G') + seq2.count('C')) / len(seq2)
    gc_diff = abs(gc_content1 - gc_content2) * 10
    
    return match_score - mismatch_penalty

# Define DNA sequences for analysis
dna_fragments = ['ACGT', 'TGCA', 'GGCC', 'AATT', 'CGTA']

# Generate all possible combinations of 3 fragments
all_combinations = list(itertools.combinations(dna_fragments, 3))

# Filter combinations based on certain criteria
temperature_values = [72, 68, 65, 70, 69]  # PCR temperatures for each fragment
filtered_combinations = []

for combo in all_combinations:
    # Calculate average temperature (not used in final calculation)
    indices = [dna_fragments.index(fragment) for fragment in combo]
    avg_temp = sum(temperature_values[i] for i in indices) / len(indices)
    
    # Only keep combinations with specific nucleotide patterns
    if 'ACGT' in combo or 'CGTA' in combo:
        filtered_combinations.append(combo)

def calculate_sequence_score(combinations):
    if not combinations:
        return -1
    
    best_score = -float('inf')
    best_combo = None
    
    for combo in combinations:
        # Calculate compatibility between fragments
        score = calculate_dna_compatibility(combo[0], combo[1])
        score += calculate_dna_compatibility(combo[1], combo[2])
        
        # Track highest score
        if score > best_score:
            best_score = score
            best_combo = combo
    
    # This additional calculation doesn't affect the result
    total_length = sum(len(fragment) for fragment in best_combo)
    complexity_factor = len(set(''.join(best_combo))) / 4  # Nucleotide diversity
    
    return best_score

# Process the filtered combinations
optimal_sequence_score = calculate_sequence_score(filtered_combinations)
print(f"Result: {optimal_sequence_score}")