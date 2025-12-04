def process_genetic_sequence(sequence, markers):
    # Extract primary segments from the sequence
    primary_segments = sequence[3:15] + sequence[20:28]
    
    # Calculate segment properties
    segment_weights = [len(s) for s in primary_segments if s.isalpha()]
    avg_weight = sum(segment_weights) / len(segment_weights) if segment_weights else 0
    
    # Define nucleotide values
    nucleotide_values = {'A': 1, 'C': -1, 'G': 2, 'T': -2}
    
    # Process markers (some are relevant, some aren't)
    active_markers = set([m for m in markers if m.startswith('M')])
    inactive_markers = set(markers) - active_markers
    marker_strength = len(active_markers) * 2
    
    # Analyze sequence with lambda function
    analyzer = lambda x: nucleotide_values.get(x, 0) * (1 if x in 'AG' else -1 if x in 'CT' else 0)
    
    # Generate numerical representation of sequence
    numerical_sequence = [analyzer(nucleotide) for nucleotide in sequence]
    
    # Apply marker effects (distraction)
    if 'M3' in active_markers:
        numerical_sequence = [n + 1 for n in numerical_sequence]
    if 'M7' in inactive_markers:
        marker_strength += 3
    
    # Extract relevant positions based on a pattern
    position_selector = [i for i in range(len(numerical_sequence)) if i % 3 == 1]
    
    # Filter sequence based on position and value
    filtered_sequence = [numerical_sequence[i] for i in position_selector if i < len(numerical_sequence)]
    
    # Calculate final result
    filtered_sequence_sum = sum(filtered_sequence)
    
    # Apply additional processing (distraction)
    normalized_sum = filtered_sequence_sum / len(filtered_sequence) if filtered_sequence else 0
    weighted_sum = filtered_sequence_sum * (marker_strength / 10) if marker_strength else filtered_sequence_sum
    
    print(f"Result: {filtered_sequence_sum}")
    return filtered_sequence_sum

# Test data
dna_sequence = "ACGTACGTACGTACGTACGT"
marker_set = ["M1", "M3", "R5", "T7"]

# Process the sequence
result = process_genetic_sequence(dna_sequence, marker_set)