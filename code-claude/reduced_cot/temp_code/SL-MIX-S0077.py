def calculate_mutation_viability(sequence, threshold=0.5):
    # Analyze DNA sequence mutations
    mutation_map = {}
    potential_sites = {i for i in range(len(sequence)) if sequence[i] in 'ACTG'}
    decoy_sites = {i for i in range(len(sequence)) if i % 7 == 0}
    
    # Calculate viability scores (misleading)
    viability_scores = []
    for i in potential_sites:
        base_score = (i * 3) % 10 / 10
        if i in decoy_sites:
            # Misleading calculation for decoy sites
            mutation_map[i] = base_score * 1.5
            if base_score > 0.7:
                viability_scores.append(base_score)
        else:
            mutation_map[i] = base_score
            if base_score > threshold:
                viability_scores.append(base_score)
    
    # Process mutations (more distraction)
    def apply_recursive_filter(scores, depth=0):
        if depth > 2 or not scores:
            return scores
        if sum(scores) / len(scores) < 0.6:
            return scores[1:]
        return apply_recursive_filter(scores, depth + 1)
    
    filtered_scores = apply_recursive_filter(viability_scores)
    
    # This is the critical part for the answer
    valid_mutation_sites = set()
    for site, score in mutation_map.items():
        # More distraction with complex conditions
        if site % 3 == 0 and score > 0.4:
            valid_mutation_sites.add(site)
        elif site % 5 == 0 and score < 0.8:
            valid_mutation_sites.add(site)
            
    # Unused calculations (red herring)
    average_score = sum(viability_scores) / len(viability_scores) if viability_scores else 0
    max_possible = len(potential_sites.intersection(decoy_sites))
    theoretical_limit = len(sequence) // 4
    
    # Create viable mutations
    viable_mutations = set()
    for site in valid_mutation_sites:
        # The actual determining logic
        if site < len(sequence) - 2:
            sub_seq = sequence[site:site+3]
            if 'A' in sub_seq or 'T' in sub_seq:
                viable_mutations.add(site)
    
    # More distraction: alternative calculation that's unused
    alt_viable = {s for s in valid_mutation_sites if s % 2 == 0}
    compensatory_sites = {s - 1 for s in alt_viable if s > 0}
    
    # This is the key statement
    active_mutations = len(viable_mutations)
    
    print(f"Result: {active_mutations}")
    return active_mutations

# DNA sequence for analysis
dna = "ACGTACGTACGTACGTACGT"
result = calculate_mutation_viability(dna, 0.3)