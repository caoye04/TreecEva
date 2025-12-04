import itertools

def analyze_dna_sequences(sequences):
    # Extract unique DNA bases from all sequences
    all_bases = set()
    for seq in sequences:
        all_bases.update(seq)
    
    # Count occurrences of each base
    base_counts = {base: 0 for base in all_bases}
    for seq in sequences:
        for base in seq:
            base_counts[base] += 1
    
    # Sort sequences by length (not used in final calculation)
    sorted_sequences = sorted(sequences, key=len, reverse=True)
    
    # Find potential mutation patterns
    mutation_patterns = []
    for i in range(1, 4):
        mutation_patterns.extend(list(itertools.combinations(all_bases, i)))
    
    # Calculate sequence compatibility scores (distractor calculation)
    compatibility_scores = []
    for seq in sequences:
        score = sum(base_counts[base] for base in set(seq))
        compatibility_scores.append(score)
    
    # Process each sequence with mutation patterns
    valid_results = []
    for seq in sequences:
        # Generate potential variations
        seq_bases = set(seq)
        
        # This is the key calculation
        if len(seq) > 3 and len(seq_bases) >= 2:
            # Find all possible pairs from the sequence
            pairs = list(itertools.combinations(seq, 2))
            
            # Extract only pairs with different bases
            distinct_pairs = [p for p in pairs if p[0] != p[1]]
            
            # Calculate a hash value for each distinct pair
            for pair in distinct_pairs:
                hash_val = (ord(pair[0]) - ord('A')) * 10 + (ord(pair[1]) - ord('A'))
                valid_results.append(hash_val)
    
    # Calculate metrics based on mutation analysis
    avg_score = sum(compatibility_scores) / len(compatibility_scores) if compatibility_scores else 0
    max_pattern_length = max(len(p) for p in mutation_patterns)
    
    # Calculate the number of unique combinations from valid results
    unique_combinations = len(set(valid_results))
    
    return unique_combinations

# Sample DNA sequences
dna_sequences = ['ACGT', 'AACC', 'TGCA', 'GGTA']

# Process sequences and get result
result = analyze_dna_sequences(dna_sequences)
print(f"Result: {result}")