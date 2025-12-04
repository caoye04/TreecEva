import itertools

def analyze_genetic_sequences(sequences, mutation_rate=0.05):
    """Analyze genetic sequences with a given mutation rate."""
    total_mutations = 0
    sequence_lengths = []
    
    for seq in sequences:
        # Count potential mutation sites
        mutation_sites = len([base for base in seq if base in 'ACGT'])
        expected_mutations = mutation_sites * mutation_rate
        total_mutations += expected_mutations
        sequence_lengths.append(len(seq))
    
    # This is a distraction - not used in main calculation
    if total_mutations > 50:
        mutation_severity = "HIGH"
    elif total_mutations > 20:
        mutation_severity = "MEDIUM"
    else:
        mutation_severity = "LOW"
    
    return sequence_lengths, mutation_severity

def calculate_complexity_score(sequence):
    """Calculate complexity score for a sequence."""
    # Count unique n-grams
    unique_bigrams = set()
    unique_trigrams = set()
    
    for i in range(len(sequence) - 1):
        unique_bigrams.add(sequence[i:i+2])
    
    for i in range(len(sequence) - 2):
        unique_trigrams.add(sequence[i:i+3])
    
    # This part is relevant
    complexity = len(unique_bigrams) * 2 + len(unique_trigrams) * 3
    
    # Misleading calculation - not used in final result
    entropy_factor = complexity / (len(sequence) if len(sequence) > 0 else 1)
    normalized_entropy = min(1.0, entropy_factor / 10)
    
    return complexity

def generate_test_combinations(elements, positions):
    """Generate test combinations using itertools."""
    # This function is a distraction
    all_combinations = list(itertools.combinations(elements, positions))
    filtered_combinations = [combo for combo in all_combinations if 'G' in combo]
    return filtered_combinations

def filter_sequences(sequences, min_length=10, max_gc_content=0.6):
    """Filter sequences based on length and GC content."""
    valid_sequences = []
    invalid_count = 0  # Distraction variable
    
    for seq in sequences:
        # Check length
        if len(seq) < min_length:
            invalid_count += 1
            continue
        
        # Calculate GC content
        gc_count = seq.count('G') + seq.count('C')
        gc_content = gc_count / len(seq) if len(seq) > 0 else 0
        
        # Misleading calculation - not used
        at_content = 1.0 - gc_content
        at_gc_ratio = at_content / gc_content if gc_content > 0 else float('inf')
        
        if gc_content <= max_gc_content:
            valid_sequences.append(seq)
        else:
            invalid_count += 1
    
    return valid_sequences

def calculate_optimal_length(sequences, threshold):
    """Calculate the optimal sequence length based on complexity scores."""
    if not sequences:
        return 0
    
    # Calculate complexity scores
    complexity_scores = [calculate_complexity_score(seq) for seq in sequences]
    
    # More distractions - not used in final calculation
    max_score = max(complexity_scores) if complexity_scores else 0
    min_score = min(complexity_scores) if complexity_scores else 0
    score_range = max_score - min_score if max_score != min_score else 1
    
    # Filter sequences by complexity threshold
    filtered_indices = [i for i, score in enumerate(complexity_scores) if score >= threshold]
    
    if not filtered_indices:
        return len(sequences[0])  # Default to first sequence length if none pass threshold
    
    # Calculate average length of sequences that pass the threshold
    filtered_lengths = [len(sequences[i]) for i in filtered_indices]
    optimal_length = sum(filtered_lengths) // len(filtered_lengths)
    
    # This is a distraction - the result is not used
    adjusted_length = optimal_length + (max_score // 100)
    
    return optimal_length

# Main execution
test_sequences = [
    "ACGTACGTACGTACGT",  # 16 bases
    "GGGGCCCCAAAATTTT",  # 16 bases
    "ATGCATGCATGC",      # 12 bases
    "GCGCGCGCGCGC",      # 12 bases
    "AATTCCGG"           # 8 bases - too short
]

# Generate some distraction data
mutations = ['A>T', 'C>G', 'G>C', 'T>A']
positions = [1, 2, 3, 4]
mutation_combinations = generate_test_combinations(mutations, 2)

# Process sequences
sequence_lengths, mutation_level = analyze_genetic_sequences(test_sequences)
average_length = sum(sequence_lengths) / len(sequence_lengths)

# This value is a distraction
weighted_length = average_length * (1 + 0.1 * (len(mutation_combinations) % 5))

# Filter sequences
filter_threshold = 30  # Complexity threshold
min_seq_length = 10
max_gc_percentage = 0.7

valid_sequences = filter_sequences(test_sequences, min_seq_length, max_gc_percentage)

# Calculate optimal length - this is what we're looking for
optimal_sequence_length = calculate_optimal_length(valid_sequences, filter_threshold)

# Distraction calculations
potential_optimization = optimal_sequence_length * 0.8
efficiency_score = 100 - (potential_optimization / 2)

print(f"Result: {optimal_sequence_length}")