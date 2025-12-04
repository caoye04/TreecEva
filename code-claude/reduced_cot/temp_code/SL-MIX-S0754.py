# Gene sequence analyzer with scoring system
# This program analyzes DNA sequences and calculates quality scores

def calculate_gc_content(sequence):
    """Calculate GC content percentage in DNA sequence"""
    gc_count = sequence.count('G') + sequence.count('C')
    return gc_count / len(sequence) * 100 if sequence else 0

# Sample DNA sequences with quality scores
dna_samples = [
    "ATGCGCTAGCTA",
    "GCGCGCTATAGC",
    "AATTGGCCAATT",
    "GCATCGATCGAT"
]

quality_thresholds = [40, 60, 80, 95]
base_values = {'A': 2, 'T': 1, 'G': 3, 'C': 2}

# Tracking variables
processed = 0
discarded = 0
total_gc = 0
points = []
mutation_indices = []

# Initialize analysis parameters
min_length = 10
max_mutations = 3
weight_factor = 2.5
optimal_gc = 55.0
decay_rate = 0.15

# Process each DNA sequence
for i, sequence in enumerate(dna_samples):
    # Calculate sequence statistics
    gc_content = calculate_gc_content(sequence)
    sequence_score = 0
    mutations = 0
    
    # Track GC content for reporting
    total_gc += gc_content
    
    # Calculate sequence quality score
    for j, base in enumerate(sequence):
        if j % 3 == 0 and base in 'GC':
            mutations += 1
            mutation_indices.append(j)
        
        # Add base value to score
        if base in base_values:
            sequence_score += base_values[base]
    
    # Apply GC content adjustment
    gc_adjustment = abs(gc_content - optimal_gc) * decay_rate
    adjusted_score = sequence_score - gc_adjustment
    
    # Track sequence processing
    if len(sequence) >= min_length:
        processed += 1
        if mutations <= max_mutations:
            points.append(int(adjusted_score))
        else:
            discarded += 1
            # We still add these points but they won't count in final calculation
            points.append(int(adjusted_score / 3))

# Calculate average GC content (not used in final score)
avg_gc = total_gc / len(dna_samples) if dna_samples else 0

# Generate quality metrics (distractors)
quality_metrics = {}
for threshold in quality_thresholds:
    quality_metrics[threshold] = sum(1 for p in points if p > threshold)

# Determine if bonus applies based on slicing and zipping operations
sequence_pairs = list(zip(dna_samples[:-1], dna_samples[1:]))
common_chars = []

for seq1, seq2 in sequence_pairs:
    # Find common characters at same positions
    common = sum(1 for a, b in zip(seq1, seq2) if a == b)
    common_chars.append(common)

# Check if bonus applies based on sequence similarity
has_bonus = False
if len(common_chars) > 0:
    similarity_index = sum(common_chars) / len(common_chars)
    if similarity_index > 3 and processed > discarded:
        has_bonus = True

# Final score calculation - this is the key statement
valid_score = sum(points) // 2 if has_bonus else sum(points) // 4

# Alternative calculations that aren't used (distractors)
weighted_score = sum(p * weight_factor for p in points) / len(points) if points else 0
normalized_score = valid_score / (max(points) if points else 1)
mutation_impact = len(mutation_indices) * 2.5

# Print analysis results
print(f"Processed sequences: {processed}")
print(f"Discarded sequences: {discarded}")
print(f"Average GC content: {avg_gc:.2f}%")
print(f"Quality metrics: {quality_metrics}")
print(f"Bonus applied: {has_bonus}")
print(f"Result: {valid_score}")