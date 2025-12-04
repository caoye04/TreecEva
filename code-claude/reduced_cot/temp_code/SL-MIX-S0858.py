def analyze_genetic_sequences(sequences):
    # Track observed frequencies of nucleotide patterns
    observed_frequencies = {}
    potential_mutations = []
    decoy_patterns = ['AAGT', 'CTGA', 'GGCT']
    
    # Process each sequence
    for idx, sequence in enumerate(sequences):
        # Extract 3-nucleotide patterns
        for i in range(len(sequence) - 2):
            pattern = sequence[i:i+3]
            observed_frequencies[pattern] = observed_frequencies.get(pattern, 0) + 1
            
            # Track potential mutations (distracting computation)
            if 'G' in pattern and 'C' not in pattern:
                potential_mutations.append((idx, i, pattern))
    
    # Analyze decoy patterns (irrelevant computation)
    decoy_counts = {}
    for pattern in decoy_patterns:
        count = 0
        for seq in sequences:
            if pattern in seq:
                count += 1
        decoy_counts[pattern] = count * 2  # Misleading multiplication
    
    # Extract pattern products (key computation mixed with distractions)
    pattern_products = {}
    max_product = -1
    max_product_idx = ''
    
    # Process patterns with frequencies and calculate products
    sorted_patterns = sorted(observed_frequencies.keys())
    for pattern, freq in observed_frequencies.items():
        # Calculate nucleotide weights (distraction)
        weights = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        pattern_weight = sum(weights[n] for n in pattern)
        
        # Calculate product (key computation)
        if 'G' in pattern or 'C' in pattern:  # Relevant condition
            product = freq * len(pattern)
            if product > max_product:
                max_product = product
                max_product_idx = pattern
        
        # Store misleading products
        adjusted_freq = freq
        if pattern in ['ATG', 'CAT', 'GGG']:
            adjusted_freq = freq - 1  # Misleading adjustment
        pattern_products[pattern] = adjusted_freq * pattern_weight
    
    # More distracting computations
    highest_freq_pattern = max(observed_frequencies, key=observed_frequencies.get)
    highest_freq = observed_frequencies[highest_freq_pattern]
    
    # Dead code path
    if highest_freq > 100:
        target_frequency = highest_freq // 2
    else:
        # This is the actual computation we care about
        target_frequency = observed_frequencies[max_product_idx]
    
    # Distraction: calculate average frequency
    avg_freq = sum(observed_frequencies.values()) / len(observed_frequencies)
    
    # Misleading final calculations
    final_score = highest_freq * 2
    mutation_risk = len(potential_mutations) / len(sequences) if sequences else 0
    
    print(f"Target result: {target_frequency}")
    return target_frequency

# Sample data
sequences = [
    "ATGCGTACGATCG",
    "ACGTACGTACGTA",
    "GCTACGATCGTAG",
    "CGATCGTACGAAC"
]

result = analyze_genetic_sequences(sequences)