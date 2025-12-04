import itertools

DNA_BASES = ['A', 'C', 'G', 'T']
SAMPLE_SEQUENCES = ['ACGTAA', 'CCGTAG', 'TTAGCA', 'AGCTAA', 'CGGTAA']

# Extract subsequences based on specific criteria
def extract_subsequences(sequences, base_filter):
    return [seq[1:4] for seq in sequences if seq.startswith(base_filter)]

# Process DNA sequences to identify patterns
def analyze_dna_patterns(sequences):
    # Count occurrences of each base
    base_counts = {base: sum(seq.count(base) for seq in sequences) for base in DNA_BASES}
    
    # Identify most common base (not used in final calculation)
    most_common = max(base_counts, key=base_counts.get)
    
    # Generate all possible 2-base combinations
    combinations = list(itertools.combinations(DNA_BASES, 2))
    
    # Extract subsequences starting with 'A'
    a_subsequences = extract_subsequences(sequences, 'A')
    
    # Extract subsequences starting with 'C' (not used in final result)
    c_subsequences = extract_subsequences(sequences, 'C')
    
    # Calculate GC content percentage (distraction)
    gc_content = sum(seq.count('G') + seq.count('C') for seq in sequences) / sum(len(seq) for seq in sequences)
    gc_percentage = gc_content * 100
    
    # Filter sequences based on multiple criteria
    primary_filter = [seq for seq in sequences if 'AA' in seq]
    secondary_filter = [seq for seq in sequences if seq.endswith('A')]
    
    # Combine filters with slicing
    filtered_sequences = [seq[:-1] for seq in primary_filter if seq in secondary_filter]
    
    # Count valid sequences after filtering
    valid_count = len([s for s in filtered_sequences if len(s) > 0])
    
    # Calculate a complexity score (distraction)
    complexity_score = sum(len(set(seq)) for seq in filtered_sequences)
    
    return valid_count, complexity_score, gc_percentage

# Execute analysis
result, complexity, gc_percent = analyze_dna_patterns(SAMPLE_SEQUENCES)
print(f"Result: {result}")
