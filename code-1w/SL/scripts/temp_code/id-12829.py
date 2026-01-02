def analyze_sequence(dna_strand):
    base_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in dna_strand:
        if base in base_counts:
            base_counts[base] += 1

    gc_content = base_counts['G'] + base_counts['C']
    at_content = base_counts['A'] + base_counts['T']

    segments = [dna_strand[i:i+3] for i in range(0, len(dna_strand)-2)]
    valid_triplets = [s for s in segments if 'N' not in s and len(s) == 3]
    
    # Extract triplets starting with 'G' or 'C' and convert to ASCII sum values
    ascii_values = []
    for triplet in valid_triplets:
        if triplet[0] in ['G', 'C']:
            ascii_sum = sum(ord(c) for c in triplet)
            ascii_values.append(ascii_sum)

    sorted_substrings = sorted(ascii_values, reverse=True)[:5]
    filtered_sum = sum(sorted_substrings)
    
    # Irrelevant distraction: counting stop codons (not used in final result)
    stop_codons = [triplet for triplet in valid_triplets if triplet in ['TAG', 'TAA', 'TGA']]
    dummy_count = len(stop_codons)

    print(f"Result: {filtered_sum}")

analyze_sequence("GGATGCATTGCAACGT")