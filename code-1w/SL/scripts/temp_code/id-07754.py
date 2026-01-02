def analyze_dna_sequence(sequence):
    k = 3
    frequency_map = {}
    
    # Extract k-mers and count frequencies
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer in frequency_map:
            frequency_map[kmer] += 1
        else:
            frequency_map[kmer] = 1
    
    # Irrelevant statistic (minor distraction)
    total_kmers = sum(frequency_map.values())
    avg_count = total_kmers / len(frequency_map)
    
    # Key computation step
    peak_frequency = max(frequency_map.values())
    
    return peak_frequency

# Simulate execution
dna_seq = "AGCTTGAACCGGTTAGCTAGCTTGAATGCA"
dummy_var = 42  # Irrelevant variable (intervention level 4: minimal distraction)
result = analyze_dna_sequence(dna_seq)
print(f"Target result: {result}")