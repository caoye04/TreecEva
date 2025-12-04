# Calculate weighted frequency of characters in DNA sequences
sequences = ['ACGTACGT', 'TTAGCTA', 'CGCGAATT']

# Base weights (A=1, C=2, G=3, T=4)
base_weights = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

# Process each sequence
processed_data = []
decay_factor = 0.8  # Decay factor for position weighting (not used in final calculation)

for idx, seq in enumerate(sequences):
    # Count occurrences of each base
    base_counts = {base: 0 for base in 'ACGT'}
    
    # Track position information (not used in final result)
    positions = {base: [] for base in 'ACGT'}
    
    for pos, base in enumerate(seq):
        base_counts[base] += 1
        positions[base].append(pos)
    
    # Calculate sequence metrics
    gc_content = (base_counts['G'] + base_counts['C']) / len(seq)
    at_content = (base_counts['A'] + base_counts['T']) / len(seq)
    
    # Store processed data
    processed_data.append({
        'sequence': seq,
        'counts': base_counts,
        'positions': positions,
        'gc_content': gc_content,
        'at_content': at_content
    })

# Generate weighted values for each sequence
weighted_values = []

for data in processed_data:
    # Calculate weighted value based on base weights
    weighted_sum = sum(data['counts'][base] * base_weights[base] for base in 'ACGT')
    weighted_values.append(weighted_sum)

# Apply lambda function to adjust values (but ultimately unused)
adjusted_values = list(map(lambda x: x * 1.0, weighted_values))

# Zip sequence indices with their weighted values
zipped_data = list(zip(range(len(sequences)), weighted_values))

# Extract only the weights
weights = [w for _, w in zipped_data]

# Calculate total weight
total_weight = sum(weights)

# Alternative calculation that gives different result (not used)
alternative_total = sum(len(seq) for seq in sequences)

print(f"Result: {total_weight}")