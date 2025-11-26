def analyze_dna_sequences(sequences):
    base_counts = {}
    pattern_multiplier = 3
    redundant_count = 7
    
    # Irrelevant sequence processing (distractor)
    temp_storage = []
    for i, seq in enumerate(sequences):
        if len(seq) > 5:
            temp_storage.append(seq[::-1])  # Reverse strings
    
    # Main logic for valid sequence counting
    valid_sequences_count = 0
    invalid_patterns = 0
    
    for seq in sequences:
        # Count base occurrences (relevant)
        for base in seq:
            base_counts[base] = base_counts.get(base, 0) + 1
        
        # Check for valid patterns
        has_ATG = 'ATG' in seq
        has_TAA = 'TAA' in seq
        
        # Misleading intermediate calculation (distractor)
        invalid_patterns += len(seq) % 4
        
        if has_ATG and not has_TAA:
            valid_sequences_count += 2
        elif has_TAA and not has_ATG:
            valid_sequences_count += 1
        else:
            # Dead code path (distractor)
            invalid_patterns -= 1
    
    # More irrelevant computations
    total_bases = sum(base_counts.values())
    avg_length = total_bases / len(sequences) if sequences else 0
    
    # Unused variable (distractor)
    complexity_score = valid_sequences_count * avg_length + invalid_patterns
    
    # Final calculation (critical path)
    final_sequence_count = valid_sequences_count * pattern_multiplier - redundant_count
    
    # Print the result
    print(f"Result: {final_sequence_count}")
    return final_sequence_count

# Test data
dna_sequences = ['ATGCTAGCT', 'CTAGCTAA', 'GGATGCAT', 'TTTAAAGGG', 'ATGTTTCCC', 'CCCTAA']
result = analyze_dna_sequences(dna_sequences)