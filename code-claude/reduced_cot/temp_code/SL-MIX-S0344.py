import itertools

# Analyzing genetic sequence patterns
base_pairs = ['A', 'T', 'G', 'C']
sequence_length = 2

# Generate all possible combinations of the base pairs
combinations = list(itertools.product(base_pairs, repeat=sequence_length))

# Some combinations may be equivalent in our analysis
processed_pairs = []
for pair in combinations:
    # Convert tuple to string for easier handling
    pair_str = ''.join(pair)
    processed_pairs.append(pair_str)

# Count unique combinations after processing
unique_count = len(set(combinations))

# For verification, also count the processed pairs
processed_count = len(set(processed_pairs))

# Output for debugging
print(f"Base pairs: {base_pairs}")
print(f"Sequence length: {sequence_length}")
print(f"Result: {unique_count}")