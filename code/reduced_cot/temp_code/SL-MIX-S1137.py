def process_genomic_data():
    # Nucleotide to integer mapping
    encoding_map = {'A': 0, 'T': 1, 'G': 2, 'C': 3}
    
    # Initial DNA sequence
    dna_sequence = ['G', 'A', 'T', 'T', 'A', 'C', 'A']
    
    # Step 1: Encode the sequence
    encoded_values = [encoding_map[nucleotide] for nucleotide in dna_sequence]
    
    # Step 2: Reverse the sequence
    reversed_encoded = encoded_values[::-1]
    
    # Step 3: Create mask from sequence length
    seq_length = len(dna_sequence)
    mask = seq_length - 1 if seq_length % 2 == 0 else seq_length
    
    # Step 4: Apply bitwise XOR and filter
    masked_values = [value ^ mask for value in reversed_encoded]
    
    # Step 5: Sum values where masked > original
    masked_sum = sum(
        masked_val for orig_val, masked_val in zip(reversed_encoded, masked_values)
        if masked_val > orig_val
    )
    
    return masked_sum

# Execute the pipeline
masked_sum = process_genomic_data()
print(f"Result: {masked_sum}")