import itertools

# Analyzing DNA sequence overlaps between samples
def analyze_dna_sequences():
    sample_a = "ACGTACGT"
    sample_b = "TACGTACG"
    sample_c = "GTACGTAC"
    
    # Convert sequences to character sets
    chars_a = set(sample_a)
    chars_b = set(sample_b)
    chars_c = set(sample_c)
    
    # Find characters that appear in all sequences
    common_elements = itertools.filterfalse(
        lambda x: x not in chars_b or x not in chars_c, 
        chars_a
    )
    
    # Count the number of common elements
    overlap_count = len(list(common_elements))
    
    # Calculate a simple metric based on the overlap
    metric = overlap_count * 2
    
    return overlap_count

result = analyze_dna_sequences()
print(f"Result: {result}")