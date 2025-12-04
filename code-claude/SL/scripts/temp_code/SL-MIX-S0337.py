import itertools

# DNA sequence analysis function
def analyze_dna_segment(sequence):
    # Initial processing
    valid_chars = {'A', 'C', 'G', 'T'}
    
    # Filter out any non-DNA characters
    filtered_sequence = [char for char in sequence if char in valid_chars]
    
    # Find unique nucleotides in the filtered sequence
    unique_count = len(set(filtered_sequence))
    
    # Count occurrences of each nucleotide
    nucleotide_counts = {}
    for key, group in itertools.groupby(sorted(filtered_sequence)):
        nucleotide_counts[key] = len(list(group))
    
    # Calculate GC content percentage (just for info)
    gc_content = ((nucleotide_counts.get('G', 0) + nucleotide_counts.get('C', 0)) / 
                 len(filtered_sequence) * 100) if filtered_sequence else 0
    
    return unique_count

# Test with a sample DNA segment with some invalid characters
dna_sample = "ACGTX123ACCGTN-TGCA"
result = analyze_dna_segment(dna_sample)
print(f"Result: {result}")